// API client for question progress tracking (SQLite backend).
import type { ProgressEntry, QuestionStatus } from "../types";

export const PROGRESS_API = "/api/progress";

/** All recorded statuses, keyed by question id. Missing = unattempted. */
export async function loadProgress(): Promise<Record<string, ProgressEntry>> {
  const res = await fetch(`${PROGRESS_API}/questions`);
  if (!res.ok) throw new Error(`Failed to load progress: ${res.status}`);
  return res.json();
}

/** Record (or update) a question's status. */
export async function saveStatus(
  questionId: string,
  status: QuestionStatus
): Promise<void> {
  const res = await fetch(
    `${PROGRESS_API}/${encodeURIComponent(questionId)}`,
    {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ status }),
    }
  );
  if (!res.ok) throw new Error(`Failed to save progress: ${res.status}`);
}

/** Forget a question's status (back to unattempted). */
export async function clearProgress(questionId: string): Promise<void> {
  const res = await fetch(
    `${PROGRESS_API}/${encodeURIComponent(questionId)}`,
    { method: "DELETE" }
  );
  if (!res.ok) throw new Error(`Failed to clear progress: ${res.status}`);
}

/** Roll up a chapter's statuses against its question set (unattempted excluded).
 * Green = 2 points, yellow = 1, red = 0; mastery is a percentage of 2 per
 * attempted question. */
export function chapterProgress(
  statuses: Record<string, ProgressEntry>,
  questionIds: string[]
): { attempted: number; green: number; yellow: number; red: number; mastery: number } {
  let attempted = 0;
  let green = 0;
  let yellow = 0;
  let red = 0;
  for (const id of questionIds) {
    const e = statuses[id];
    if (!e) continue;
    attempted += 1;
    if (e.status === "green") green += 1;
    else if (e.status === "yellow") yellow += 1;
    else red += 1;
  }
  const mastery = attempted ? ((2 * green + yellow) / (2 * attempted)) * 100 : 0;
  return { attempted, green, yellow, red, mastery };
}
