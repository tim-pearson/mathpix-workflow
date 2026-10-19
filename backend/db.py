"""SQLite persistence + rollups for question progress.

Deliberately tiny and stdlib-only (sqlite3): a single table of question
statuses, and a per-chapter rollup derived from the question id prefix
(ch<NN>-<block>-<qid>).  Every function opens its own connection to `path`,
so it is safe under FastAPI's thread pool and trivially testable against a
temporary database file.  The data lives in the SQLite *file*, so restarting
the process (or rebuilding the container while the file/volume persists)
never loses progress.
"""
import re
import sqlite3
from datetime import datetime, timezone

VALID_STATUS = {"green", "yellow", "red"}
QID_RE = re.compile(r"^ch\d\d-[\w-]+-(?:q|ps|p|m)\d+$")
CHAPTER_RE = re.compile(r"^(ch\d\d)-")


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def connect(path):
    return sqlite3.connect(path, check_same_thread=False)


def init(path):
    """Create the schema if needed; returns the connection (open)."""
    conn = connect(path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS progress ("
        " question_id TEXT PRIMARY KEY,"
        " status TEXT NOT NULL CHECK (status IN ('green','yellow','red')),"
        " updated_at TEXT NOT NULL)")
    conn.commit()
    return conn


def valid_question_id(qid):
    return bool(QID_RE.match(qid))


def set_status(path, qid, status):
    """Record/refresh a question's status (green/yellow/red)."""
    if status not in VALID_STATUS:
        raise ValueError(f"status must be one of {sorted(VALID_STATUS)}")
    if not valid_question_id(qid):
        raise ValueError(f"invalid question id: {qid!r}")
    conn = init(path)
    try:
        conn.execute(
            "INSERT INTO progress (question_id, status, updated_at)"
            " VALUES (?, ?, ?)"
            " ON CONFLICT(question_id) DO UPDATE SET"
            "  status = excluded.status, updated_at = excluded.updated_at",
            (qid, status, now_iso()))
        conn.commit()
    finally:
        conn.close()


def clear_status(path, qid):
    """Remove a record so the question is unattempted again."""
    conn = init(path)
    try:
        conn.execute("DELETE FROM progress WHERE question_id = ?", (qid,))
        conn.commit()
    finally:
        conn.close()


def all_statuses(path):
    """{question_id: {"status": str, "updated_at": str}} for every record."""
    conn = init(path)
    try:
        rows = conn.execute(
            "SELECT question_id, status, updated_at FROM progress").fetchall()
        return {r[0]: {"status": r[1], "updated_at": r[2]} for r in rows}
    finally:
        conn.close()


def chapter_summary(path):
    """Per-chapter rollups of the *recorded* statuses.

    Returns {chNN: {"attempted", "green", "yellow", "red", "mastery"}}.
    mastery = (2*green + yellow) / (2*attempted), a percentage; unattempted
    questions are excluded entirely.
    """
    per = {}
    for qid, entry in all_statuses(path).items():
        m = CHAPTER_RE.match(qid)
        if not m:
            continue
        c = per.setdefault(m.group(1),
                           {"attempted": 0, "green": 0,
                            "yellow": 0, "red": 0})
        c["attempted"] += 1
        c[entry["status"]] += 1
    for c in per.values():
        pts = 2 * c["green"] + c["yellow"]
        c["mastery"] = (round(pts / (2 * c["attempted"]) * 100, 1)
                        if c["attempted"] else 0.0)
    return per
