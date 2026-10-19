// Shared flags (suspected mistakes in rendered content), persisted to SQLite.
// Loads all flags once and exposes an optimistic setter that syncs to the
// backend.  A flag is keyed by a question or block id and carries an optional
// note describing the suspected problem.
import {
  createContext,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from "react";
import type { FlagEntry } from "../types";
import { clearFlag, loadFlags, saveFlag } from "../lib/flags";

interface FlagContextValue {
  flags: Record<string, FlagEntry>;
  /** note=null keeps the flag without a description; pass clear to unflag. */
  setFlag: (targetId: string, note: string | null, clear?: boolean) => void;
  ready: boolean;
}

const FlagContext = createContext<FlagContextValue | null>(null);

export function FlagProvider({ children }: { children: ReactNode }) {
  const [flags, setFlags] = useState<Record<string, FlagEntry>>({});
  const [ready, setReady] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadFlags()
      .then(setFlags)
      .catch((e) => setError(String(e)))
      .finally(() => setReady(true));
  }, []);

  const value = useMemo<FlagContextValue>(() => {
    const setFlag = (
      targetId: string,
      note: string | null,
      clear = false
    ) => {
      setFlags((prev) => {
        const next = { ...prev };
        if (clear) {
          delete next[targetId];
        } else {
          next[targetId] = { note, created_at: new Date().toISOString() };
        }
        return next;
      });
      if (clear) clearFlag(targetId).catch((e) => setError(String(e)));
      else saveFlag(targetId, note).catch((e) => setError(String(e)));
    };
    return { flags, setFlag, ready };
  }, [flags, ready]);

  return (
    <FlagContext.Provider value={value}>
      {children}
      {error && (
        <div className="pointer-events-none fixed bottom-3 left-3 rounded-lg border border-danger/40 bg-paper px-3 py-2 text-xs text-danger shadow-sm">
          Flags API error: {error} — is the backend running?
        </div>
      )}
    </FlagContext.Provider>
  );
}

export function useFlags(): FlagContextValue {
  const ctx = useContext(FlagContext);
  if (!ctx) throw new Error("useFlags must be used within FlagProvider");
  return ctx;
}
