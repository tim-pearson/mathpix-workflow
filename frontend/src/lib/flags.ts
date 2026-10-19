// API client for question flags (SQLite backend) — annotate a rendered
// element when something looks wrong (skipped questions, several questions
// glued into one card, …) with an optional description.
import type { FlagEntry } from "../types";
import { API_BASE } from "./api";
export const FLAGS_API = `${API_BASE}/flags`;

/** All flags, keyed by target id (question or block id). */
export async function loadFlags(): Promise<Record<string, FlagEntry>> {
  const res = await fetch(FLAGS_API);
  if (!res.ok) throw new Error(`Failed to load flags: ${res.status}`);
  return res.json();
}

/** Flag a target with an optional note; null clears the note but keeps the flag. */
export async function saveFlag(
  targetId: string,
  note: string | null
): Promise<void> {
  const res = await fetch(`${FLAGS_API}/${encodeURIComponent(targetId)}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ note }),
  });
  if (!res.ok) throw new Error(`Failed to save flag: ${res.status}`);
}

/** Remove the flag entirely. */
export async function clearFlag(targetId: string): Promise<void> {
  const res = await fetch(`${FLAGS_API}/${encodeURIComponent(targetId)}`, {
    method: "DELETE",
  });
  if (!res.ok) throw new Error(`Failed to clear flag: ${res.status}`);
}
