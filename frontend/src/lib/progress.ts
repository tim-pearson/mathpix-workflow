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

/** Roll up a chapter's statuses against its full question set.
 * Red = 1, yellow = 2, green = 3; mastery is the sum over ALL questions
 * divided by (all questions × 3) — so 100% only when every question is green
 * and unattempted questions count as 0. */
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
  const denom = questionIds.length * 3;
  const mastery = denom ? ((3 * green + 2 * yellow + 1 * red) / denom) * 100 : 0;
  return { attempted, green, yellow, red, mastery };
}
