// Flag toggle for a rendered element (question/block). Marks a suspected
// mistake (skipped question, several questions glued into one card, …) with an
// optional note, persisted to the backend.
import { useState } from "react";
import { useFlags } from "../flags/FlagContext";

export function FlagButton({ targetId }: { targetId: string }) {
  const { flags, setFlag } = useFlags();
  const flag = flags[targetId];
  const [open, setOpen] = useState(false);
  const [note, setNote] = useState("");

  return (
    <>
      <button
        type="button"
        title={flag ? (flag.note || "Flagged — edit") : "Flag a problem"}
        aria-label={flag ? "Edit flag" : "Flag a problem"}
        aria-pressed={Boolean(flag)}
        onClick={() => {
          if (open) setOpen(false);
          else {
            setNote(flag?.note ?? "");
            setOpen(true);
          }
        }}
        className={`flex h-6 w-6 items-center justify-center rounded-full border text-xs ${
          flag
            ? "border-amber-400 bg-amber-400/25 text-amber-600 dark:text-amber-300"
            : "border-line text-muted hover:border-amber-400 hover:text-amber-500"
        }`}
      >
        ⚠
      </button>
      {open && (
        <div className="flex flex-wrap items-center gap-1 rounded-md border border-amber-400/50 bg-paper px-1.5 py-1">
          <input
            value={note}
            onChange={(e) => setNote(e.target.value)}
            placeholder="What looks wrong? (optional)"
            aria-label="Flag note"
            className="min-w-40 flex-1 rounded border border-line bg-pane/40 px-1.5 py-0.5 text-xs text-ink placeholder:text-muted focus:border-accent focus:outline-none"
          />
          <button
            type="button"
            onClick={() => {
              setFlag(targetId, note.trim() || null);
              setOpen(false);
            }}
            className="rounded bg-accent px-2 py-0.5 text-xs text-white"
          >
            Save
          </button>
          <button
            type="button"
            onClick={() => {
              setFlag(targetId, null, true);
              setOpen(false);
            }}
            className="rounded border border-line px-2 py-0.5 text-xs text-muted hover:text-danger"
          >
            Clear
          </button>
          <button
            type="button"
            onClick={() => setOpen(false)}
            aria-label="Cancel"
            className="rounded border border-line px-1.5 py-0.5 text-xs text-muted hover:text-ink"
          >
            ✕
          </button>
        </div>
      )}
    </>
  );
}
