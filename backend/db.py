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
# flags may target a question id or a whole block/exercise id (ch03-ex3A)
TARGET_RE = re.compile(r"^ch\d\d-[\w-]+$")
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
    conn.execute(
        "CREATE TABLE IF NOT EXISTS flags ("
        " target_id TEXT PRIMARY KEY,"
        " note TEXT,"
        " created_at TEXT NOT NULL)")
    conn.commit()
    return conn


def valid_question_id(qid):
    return bool(QID_RE.match(qid))


def valid_flag_target(tid):
    if QID_RE.match(tid):
        return True
    # block/exercise id, e.g. "ch03-ex3A" (but not a dangling "-q")
    return bool(TARGET_RE.match(tid)) \
        and not re.search(r"-(?:q|ps|p|m)\d*$", tid)


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


def set_flag(path, target_id, note=None):
    """Flag a rendered element (question/block) as suspected wrong.

    `note` is an optional free-text description; None/"" stores no note.
    """
    if not valid_flag_target(target_id):
        raise ValueError(f"invalid flag target: {target_id!r}")
    note = (note or "").strip() or None
    conn = init(path)
    try:
        conn.execute(
            "INSERT INTO flags (target_id, note, created_at)"
            " VALUES (?, ?, ?)"
            " ON CONFLICT(target_id) DO UPDATE SET"
            "  note = excluded.note, created_at = excluded.created_at",
            (target_id, note, now_iso()))
        conn.commit()
    finally:
        conn.close()


def clear_flag(path, target_id):
    """Remove a flag so the element is unflagged again."""
    conn = init(path)
    try:
        conn.execute("DELETE FROM flags WHERE target_id = ?", (target_id,))
        conn.commit()
    finally:
        conn.close()


def all_flags(path):
    """{target_id: {"note": str|null, "created_at": str}} for every flag."""
    conn = init(path)
    try:
        rows = conn.execute(
            "SELECT target_id, note, created_at FROM flags").fetchall()
        return {r[0]: {"note": r[1], "created_at": r[2]} for r in rows}
    finally:
        conn.close()


def chapter_summary(path):
    """Per-chapter rollups of the *recorded* statuses.

    Returns {chNN: {"attempted", "green", "yellow", "red"}}.  The mastery
    percentage is computed by the frontend, because it needs the chapter's
    full question count (which lives in the exported course data, not here):
    mastery = (3*green + 2*yellow + 1*red) / (total_questions * 3).
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
    return per
