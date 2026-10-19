// Green / yellow / red question status picker (persisted via the backend).
import type { QuestionStatus } from "../types";
import { useProgress } from "../progress/ProgressContext";

const STATUSES: { status: QuestionStatus; label: string; dot: string; active: string }[] = [
  { status: "green", label: "Green", dot: "bg-emerald-500", active: "ring-emerald-500" },
  { status: "yellow", label: "Yellow", dot: "bg-yellow-400", active: "ring-yellow-400" },
  { status: "red", label: "Red", dot: "bg-rose-500", active: "ring-rose-500" },
];

export function StatusSelector({ questionId }: { questionId: string }) {
  const { statuses, setStatus } = useProgress();
  const current = statuses[questionId]?.status ?? null;

  return (
    <div className="flex items-center gap-1" role="group" aria-label="Question status">
      {STATUSES.map((s) => {
        const selected = current === s.status;
        return (
          <button
            key={s.status}
            type="button"
            title={s.label}
            aria-label={s.label}
            aria-pressed={selected}
            onClick={() => setStatus(questionId, selected ? null : s.status)}
            className={`flex h-6 w-6 items-center justify-center rounded-full border transition ${
              selected
                ? `border-transparent ring-2 ${s.active} ${s.dot}`
                : "border-line hover:border-muted"
            }`}
          >
            <span
              className={`h-3 w-3 rounded-full ${s.dot} ${
                selected ? "" : "opacity-40"
              }`}
            />
          </button>
        );
      })}
      {current && (
        <button
          type="button"
          title="Clear status"
          aria-label="Clear status"
          onClick={() => setStatus(questionId, null)}
          className="ml-1 rounded px-1 text-xs text-muted hover:text-danger"
        >
          ✕
        </button>
      )}
    </div>
  );
}
