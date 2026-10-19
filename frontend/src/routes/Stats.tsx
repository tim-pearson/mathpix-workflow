import { Fragment, useEffect, useState } from "react";
import type { Manifest, Stats as StatsData } from "../types";
import { loadStats } from "../data/load";

export interface StatsProps {
  manifest: Manifest | null;
}

export function Stats({ manifest }: StatsProps) {
  const [stats, setStats] = useState<StatsData | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [expanded, setExpanded] = useState<Set<string>>(new Set());

  useEffect(() => {
    loadStats()
      .then(setStats)
      .catch((e) => setError(String(e)));
  }, []);

  if (!manifest || !stats) {
    return <div className="p-8 text-muted">Loading statistics…</div>;
  }
  if (error) return <div className="p-8 text-danger">{error}</div>;

  const toggle = (slug: string) =>
    setExpanded((prev) => {
      const next = new Set(prev);
      if (next.has(slug)) next.delete(slug);
      else next.add(slug);
      return next;
    });

  const t = stats.totals;
  const maxQuestions = Math.max(
    ...manifest.chapters.map((c) => c.counts.questions),
    1
  );

  const summary: { label: string; value: number; hint: string }[] = [
    { label: "Questions", value: t.questions, hint: "exercise questions" },
    { label: "Linked answers", value: t.linked_answers, hint: "with a matching answer" },
    { label: "Unlinked", value: t.questions - t.linked_answers, hint: "no matching answer" },
    { label: "Answers", value: t.answers, hint: "answer entries" },
    { label: "Key points", value: t.key_points, hint: "formulas panel" },
    { label: "Worked examples", value: t.worked_examples, hint: "reader cards" },
    { label: "Exercises", value: t.exercises, hint: "exercise blocks" },
  ];

  return (
    <div className="mx-auto max-w-4xl px-4 py-8">
      <h1 className="text-2xl font-bold text-ink">Statistics</h1>
      <p className="mt-1 text-sm text-muted">
        Derived from <code>frontend-data/stats.json</code> and the manifest.
      </p>

      <div className="mt-6 grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-4">
        {summary.map((s) => (
          <div key={s.label} className="rounded-xl border border-line bg-paper p-3 shadow-sm">
            <div className="text-2xl font-bold text-accent">{s.value}</div>
            <div className="text-sm font-medium text-ink">{s.label}</div>
            <div className="text-xs text-muted">{s.hint}</div>
          </div>
        ))}
      </div>

      <h2 className="mt-8 mb-3 text-lg font-semibold text-ink">Per chapter</h2>
      <div className="overflow-x-auto rounded-xl border border-line bg-paper shadow-sm">
        <table className="w-full border-collapse text-sm">
          <thead>
            <tr className="border-b border-line bg-pane/60 text-left text-xs uppercase tracking-wide text-muted">
              <th className="px-3 py-2 font-semibold">Chapter</th>
              <th className="px-3 py-2 text-right font-semibold">Questions</th>
              <th className="px-3 py-2 text-right font-semibold">Linked</th>
              <th className="px-3 py-2 text-right font-semibold">Unlinked</th>
              <th className="px-3 py-2 text-right font-semibold">Answers</th>
              <th className="px-3 py-2 text-right font-semibold">Orphans</th>
              <th className="px-3 py-2 text-right font-semibold">Key pts</th>
              <th className="px-3 py-2 text-right font-semibold">Worked ex.</th>
              <th className="px-3 py-2 text-right font-semibold">Exercises</th>
            </tr>
          </thead>
          <tbody>
            {manifest.chapters.map((c) => {
              const s = stats.chapters[c.slug];
              const isOpen = expanded.has(c.slug);
              const unlinked = s?.unlinked_questions ?? [];
              const orphans = s?.orphan_answers ?? [];
              return (
                <Fragment key={c.slug}>
                  <tr
                    className="border-b border-line last:border-0 hover:bg-pane/40"
                  >
                    <td className="px-3 py-2 font-medium text-ink">
                      {c.chapter}. {c.title}
                    </td>
                    <td className="px-3 py-2 text-right text-ink">{c.counts.questions}</td>
                    <td className="px-3 py-2 text-right text-ink">{c.counts.linked_answers}</td>
                    <td className="px-3 py-2 text-right text-danger">
                      {c.counts.questions - c.counts.linked_answers}
                    </td>
                    <td className="px-3 py-2 text-right text-ink">{c.counts.answers}</td>
                    <td className="px-3 py-2 text-right text-danger">{orphans.length}</td>
                    <td className="px-3 py-2 text-right text-ink">{c.counts.key_points}</td>
                    <td className="px-3 py-2 text-right text-ink">{c.counts.worked_examples}</td>
                    <td className="px-3 py-2 text-right text-ink">{c.counts.exercises}</td>
                  </tr>
                  {(unlinked.length > 0 || orphans.length > 0) && (
                    <tr className="border-b border-line">
                      <td colSpan={9} className="px-3 py-1">
                        <button
                          type="button"
                          onClick={() => toggle(c.slug)}
                          className="text-xs font-medium text-accent hover:underline"
                          aria-expanded={isOpen}
                        >
                          {isOpen ? "Hide" : "Show"} unlinked &amp; orphan ids
                          ({unlinked.length} unlinked, {orphans.length} orphans)
                        </button>
                        {isOpen && (
                          <div className="mt-1 grid gap-2 pb-2 text-xs sm:grid-cols-2">
                            <div>
                              <div className="font-semibold text-muted">Unlinked questions</div>
                              <ul className="mt-0.5 list-inside list-disc text-ink">
                                {unlinked.length === 0 ? (
                                  <li className="text-muted">none</li>
                                ) : (
                                  unlinked.map((id) => <li key={id}>{id}</li>)
                                )}
                              </ul>
                            </div>
                            <div>
                              <div className="font-semibold text-muted">Orphan answers</div>
                              <ul className="mt-0.5 list-inside list-disc text-ink">
                                {orphans.length === 0 ? (
                                  <li className="text-muted">none</li>
                                ) : (
                                  orphans.map((id) => <li key={id}>{id}</li>)
                                )}
                              </ul>
                            </div>
                          </div>
                        )}
                      </td>
                    </tr>
                  )}
                </Fragment>
              );
            })}
          </tbody>
        </table>
      </div>

      <h2 className="mt-8 mb-3 text-lg font-semibold text-ink">Questions per chapter</h2>
      <div className="space-y-2">
        {manifest.chapters.map((c) => (
          <div key={c.slug} className="flex items-center gap-3 text-sm">
            <span className="w-40 shrink-0 truncate text-muted">
              {c.chapter}. {c.title}
            </span>
            <div className="h-4 flex-1 overflow-hidden rounded bg-line/40">
              <div
                className="h-full rounded bg-accent"
                style={{ width: `${(c.counts.questions / maxQuestions) * 100}%` }}
                title={`${c.counts.questions} questions`}
              />
            </div>
            <span className="w-10 shrink-0 text-right text-ink">{c.counts.questions}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
