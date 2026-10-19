"""Small FastAPI backend for question progress tracking.

Single shared student, no auth.  Endpoints:
  PUT    /api/progress/{question_id}   {"status": "green"|"yellow"|"red"}
  DELETE /api/progress/{question_id}   (back to unattempted)
  GET    /api/progress/questions       all recorded statuses
  GET    /api/progress/summary         per-chapter rollups
The SQLite file lives at $PROGRESS_DB (default ./progress.db; the Docker
service sets it to /data/progress.db on a persistent volume).
"""
import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from db import (VALID_STATUS, all_statuses, chapter_summary, clear_status,
                set_status, valid_question_id)

DB_PATH = os.environ.get("PROGRESS_DB", "progress.db")

app = FastAPI(title="Maths progress API", version="1.0.0")


class ProgressBody(BaseModel):
    status: str


@app.put("/api/progress/{question_id}")
def put_progress(question_id: str, body: ProgressBody):
    if not valid_question_id(question_id):
        raise HTTPException(status_code=422,
                            detail=f"invalid question id: {question_id!r}")
    if body.status not in VALID_STATUS:
        raise HTTPException(status_code=422,
                            detail=f"status must be one of "
                                   f"{sorted(VALID_STATUS)}")
    set_status(DB_PATH, question_id, body.status)
    return {"question_id": question_id,
            "status": body.status,
            "updated_at": all_statuses(DB_PATH)[question_id]["updated_at"]}


@app.delete("/api/progress/{question_id}", status_code=204)
def delete_progress(question_id: str):
    if not valid_question_id(question_id):
        raise HTTPException(status_code=422,
                            detail=f"invalid question id: {question_id!r}")
    clear_status(DB_PATH, question_id)


@app.get("/api/progress/questions")
def get_questions():
    return all_statuses(DB_PATH)


@app.get("/api/progress/summary")
def get_summary():
    return chapter_summary(DB_PATH)
