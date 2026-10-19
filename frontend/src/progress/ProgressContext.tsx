// Shared, persistent question progress (green / yellow / red).
// Loads the SQLite-backed statuses once, exposes an optimistic setter, and
// re-syncs every change to the backend.  Missing status = unattempted.
import {
  createContext,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from "react";
import type { ProgressEntry, QuestionStatus } from "../types";
import { clearProgress, loadProgress, saveStatus } from "../lib/progress";

interface ProgressContextValue {
  statuses: Record<string, ProgressEntry>;
  /** null removes the record (back to unattempted). */
  setStatus: (questionId: string, status: QuestionStatus | null) => void;
  ready: boolean;
}

const ProgressContext = createContext<ProgressContextValue | null>(null);

export function ProgressProvider({ children }: { children: ReactNode }) {
  const [statuses, setStatuses] = useState<Record<string, ProgressEntry>>({});
  const [ready, setReady] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadProgress()
      .then(setStatuses)
      .catch((e) => setError(String(e)))
      .finally(() => setReady(true));
  }, []);

  const value = useMemo<ProgressContextValue>(() => {
    const setStatus = (questionId: string, status: QuestionStatus | null) => {
      setStatuses((prev) => {
        const next = { ...prev };
        if (status) {
          next[questionId] = { status, updated_at: new Date().toISOString() };
        } else {
          delete next[questionId];
        }
        return next;
      });
      if (status) {
        saveStatus(questionId, status).catch((e) => setError(String(e)));
      } else {
        clearProgress(questionId).catch((e) => setError(String(e)));
      }
    };
    return { statuses, setStatus, ready };
  }, [statuses, ready]);

  return (
    <ProgressContext.Provider value={value}>
      {children}
      {error && (
        <div className="pointer-events-none fixed bottom-3 right-3 rounded-lg border border-danger/40 bg-paper px-3 py-2 text-xs text-danger shadow-sm">
          Progress API error: {error} — is the backend running?
        </div>
      )}
    </ProgressContext.Provider>
  );
}

export function useProgress(): ProgressContextValue {
  const ctx = useContext(ProgressContext);
  if (!ctx) throw new Error("useProgress must be used within ProgressProvider");
  return ctx;
}
