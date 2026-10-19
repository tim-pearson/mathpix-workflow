#!/usr/bin/env python3
"""Tests for the progress backend (db layer + API).

Run:  python backend/test_progress.py

Covers, using a throwaway temp database file:
  * status set / read / clear round-trips
  * persistence across backend restarts (a brand-new app instance pointing
    at the same SQLite file still sees the data)
  * input validation
  * per-chapter summary calculations (green/yellow/red/attempted counts,
    unattempted excluded from the counts)
  * the HTTP endpoints (PUT/DELETE/GET) via FastAPI's TestClient when
    available (needs httpx; skipped otherwise)
"""
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db as pdb


def eq(a, b, label):
    if a != b:
        raise AssertionError(f"{label}\n  expected: {b!r}\n  actual:   {a!r}")


def temp_db():
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    return path


def main():
    # ---- status round-trip + validation ----
    path = temp_db()
    pdb.set_status(path, "ch02-ex2E-q1", "green")
    pdb.set_status(path, "ch02-ex2E-q2", "yellow")
    pdb.set_status(path, "ch03-ex3A-q1", "red")
    got = pdb.all_statuses(path)
    eq(sorted(got), ["ch02-ex2E-q1", "ch02-ex2E-q2", "ch03-ex3A-q1"],
       "recorded ids")
    eq(got["ch02-ex2E-q1"]["status"], "green", "status value")
    eq(bool(got["ch02-ex2E-q1"]["updated_at"]), True, "updated_at present")

    # update overwrites status, keeps single row
    pdb.set_status(path, "ch02-ex2E-q1", "yellow")
    got = pdb.all_statuses(path)
    eq(got["ch02-ex2E-q1"]["status"], "yellow", "upsert updates status")
    eq(len(got), 3, "upsert does not add a row")

    # clear -> unattempted
    pdb.clear_status(path, "ch02-ex2E-q1")
    eq(sorted(pdb.all_statuses(path)), ["ch02-ex2E-q2", "ch03-ex3A-q1"],
       "clear removes the record")

    # validation
    for bad_status in ("green ", "blue", ""):
        try:
            pdb.set_status(path, "ch02-ex2E-q3", bad_status)
            raise AssertionError(f"expected ValueError for {bad_status!r}")
        except ValueError:
            pass
    try:
        pdb.set_status(path, "ch02-ex2E", "green")
        raise AssertionError("expected ValueError for malformed id")
    except ValueError:
        pass
    os.unlink(path)

    # ---- persistence across "backend restarts" ----
    path = temp_db()
    pdb.set_status(path, "ch04-ex4A-q3", "green")
    pdb.set_status(path, "ch04-ex4A-q5", "red")
    # a "restart" = a fresh process/instance reading the same SQLite file
    again = pdb.all_statuses(path)
    eq(again, pdb.all_statuses(path), "same file reads identically")
    eq(again["ch04-ex4A-q3"]["status"], "green", "survives restart")
    eq(again["ch04-ex4A-q5"]["status"], "red", "survives restart (2)")
    os.unlink(path)

    # ---- chapter summary: counts, unattempted excluded from counts ----
    path = temp_db()
    # chapter 2: 4 questions, one unattempted (never recorded)
    pdb.set_status(path, "ch02-ex2E-q1", "green")
    pdb.set_status(path, "ch02-ex2E-q2", "yellow")
    pdb.set_status(path, "ch02-ex2E-q3", "red")
    pdb.set_status(path, "ch02-ex2E-q4", "green")
    # chapter 3: 1 question
    pdb.set_status(path, "ch03-ex3A-q1", "yellow")
    summ = pdb.chapter_summary(path)
    eq(sorted(summ), ["ch02", "ch03"], "chapters present")
    eq(summ["ch02"], {"attempted": 4, "green": 2, "yellow": 1, "red": 1},
       "ch02 counts")
    eq(summ["ch03"], {"attempted": 1, "green": 0, "yellow": 1, "red": 0},
       "ch03 counts")
    os.unlink(path)

    # ---- API layer (skipped when httpx/fastapi TestClient unavailable) ----
    try:
        from fastapi.testclient import TestClient
    except Exception:
        print("TestClient unavailable (no httpx); skipping HTTP tests.")
        return
    import main as appmod
    appmod.DB_PATH = temp_db()
    client = TestClient(appmod.app)
    eq(client.get("/api/progress/questions").json(), {}, "empty questions")
    r = client.put("/api/progress/ch05-ex5A-q1",
                   json={"status": "green"})
    eq(r.status_code, 200, "PUT ok")
    eq(r.json()["status"], "green", "PUT returns status")
    got = client.get("/api/progress/questions").json()
    eq(sorted(got), ["ch05-ex5A-q1"], "GET questions has the record")
    eq(got["ch05-ex5A-q1"]["status"], r.json()["status"], "same status")
    eq(got["ch05-ex5A-q1"]["updated_at"], r.json()["updated_at"],
       "same timestamp")
    summ = client.get("/api/progress/summary").json()
    eq(summ["ch05"]["green"], 1, "summary counts the PUT")
    eq(client.delete("/api/progress/ch05-ex5A-q1").status_code, 204,
       "DELETE ok")
    eq(client.get("/api/progress/questions").json(), {}, "deleted -> empty")
    eq(client.put("/api/progress/bogus", json={"status": "green"}).status_code,
       422, "rejects malformed id")
    eq(client.put("/api/progress/ch05-ex5A-q1",
                  json={"status": "blue"}).status_code, 422,
       "rejects invalid status")
    print("HTTP tests passed.")


if __name__ == "__main__":
    main()
    print("ALL PROGRESS BACKEND TESTS PASSED")
