import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import type { ChapterData, Manifest } from "../types";
import { loadChapter } from "../data/load";
import { IconBook, IconCalculator, IconPencil } from "../components/Icons";
import { useProgress } from "../progress/ProgressContext";
import { chapterProgress } from "../lib/progress";

export interface HomeProps {
  manifest: Manifest | null;
}

export function Home({ manifest }: HomeProps) {
  const [chapters, setChapters] = useState<Record<string, ChapterData>>({});
  const { ready } = useProgress();

  useEffect(() => {
    if (!manifest) return;
    let alive = true;
    Promise.all(
      manifest.chapters.map((c) =>
        loadChapter(c.slug).catch(() => null)
      )
    ).then((list) => {
      if (!alive) return;
      const map: Record<string, ChapterData> = {};
      manifest.chapters.forEach((c, i) => {
        if (list[i]) map[c.slug] = list[i]!;
      });
      setChapters(map);
    });
    return () => {
      alive = false;
    };
  }, [manifest]);

  if (!manifest) {
    return <div className="p-8 text-muted">Loading…</div>;
  }

  return (
    <div className="mx-auto max-w-5xl px-4 py-8">
      <div className="mb-8 text-center">
        <h1 className="text-3xl font-bold text-ink">
          Pure Mathematics 2 &amp; 3
        </h1>
        <p className="mt-2 text-muted">
          Cambridge International AS &amp; A Level Mathematics
        </p>
        <div className="mt-6 flex flex-wrap justify-center gap-3">
          <Link
            to="/read/ch01"
            className="inline-flex items-center gap-2 rounded-lg bg-accent px-5 py-2.5 font-medium text-white shadow-sm transition-transform hover:scale-[1.02]"
          >
            <IconBook aria-hidden="true" /> Read
          </Link>
          <Link
            to="/practice/ch01"
            className="inline-flex items-center gap-2 rounded-lg border border-line bg-paper px-5 py-2.5 font-medium text-ink shadow-sm transition-transform hover:scale-[1.02]"
          >
            <IconPencil aria-hidden="true" /> Practise
          </Link>
        </div>
        <div className="mt-3 text-sm">
          <Link to="/stats" className="text-muted hover:text-accent">
            Statistics
          </Link>
        </div>
      </div>

      <h2 className="mb-3 text-lg font-semibold text-ink">Chapters</h2>
      <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
        {manifest.chapters.map((c) => {
          const data = chapters[c.slug];
          return (
            <div
              key={c.slug}
              className="rounded-xl border border-line bg-paper p-4 shadow-sm"
            >
              <div className="flex items-baseline justify-between gap-2">
                <h3 className="font-semibold text-ink">
                  <span className="mr-1 text-muted">{c.chapter}.</span>
                  {c.title}
                </h3>
              </div>
              <div className="mt-2 flex gap-3 text-xs text-muted">
                <span>{c.counts.questions} questions</span>
                <span>{c.counts.worked_examples} worked examples</span>
                <span>{c.counts.key_points} key points</span>
              </div>
              <div className="mt-3 flex flex-wrap gap-2 text-sm">
                <Link
                  to={`/read/${c.slug}`}
                  className="rounded-md bg-accent-soft px-2.5 py-1 text-accent hover:underline"
                >
                  Read
                </Link>
                <Link
                  to={`/practice/${c.slug}/${`ch${String(c.chapter).padStart(2, "0")}-prerequisite`}`}
                  className="rounded-md border border-line px-2.5 py-1 text-muted hover:text-ink"
                >
                  Prerequisites
                </Link>
                {data && data.key_points.length > 0 && (
                  <Link
                    to={`/read/${c.slug}/keypoints`}
                    className="inline-flex items-center gap-1 rounded-md border border-line px-2.5 py-1 text-muted hover:text-ink"
                    title={`Key points: ${data.key_points
                      .map((k) => `KEY POINT ${k.number}`)
                      .join(", ")}`}
                  >
                    <IconCalculator aria-hidden="true" /> Key points
                  </Link>
                )}
              </div>
            </div>
          );
        })}
      </div>

      <div className="mt-10">
        <ProgressDashboard
          manifest={manifest}
          chapters={chapters}
          ready={ready}
        />
      </div>
    </div>
  );
}

function StatusChip({ kind, count }: { kind: "green" | "yellow" | "red"; count: number }) {
  const dot =
    kind === "green"
      ? "bg-emerald-500"
      : kind === "yellow"
        ? "bg-yellow-400"
        : "bg-rose-500";
  return (
    <span className="inline-flex items-center gap-1">
      <span className={`h-2.5 w-2.5 rounded-full ${dot}`} aria-hidden="true" />
      <span className="tabular-nums text-ink">{count}</span>
    </span>
  );
}

/** Chapter dashboard: attempted/total, green/yellow/red counts, mastery %. */
function ProgressDashboard({
  manifest,
  chapters,
  ready,
}: {
  manifest: Manifest;
  chapters: Record<string, ChapterData>;
  ready: boolean;
}) {
  const { statuses } = useProgress();

  const rows = useMemo(() => {
    return manifest.chapters.map((c) => {
      const data = chapters[c.slug];
      const questionIds = data
        ? Object.keys(data.questions)
        : [];
      const total = c.counts.questions;
      const s = chapterProgress(statuses, questionIds);
      return { chapter: c, s, total };
    });
  }, [manifest, chapters, statuses]);

  const grand = useMemo(() => {
    let attempted = 0,
      green = 0,
      yellow = 0,
      red = 0;
    for (const r of rows) {
      attempted += r.s.attempted;
      green += r.s.green;
      yellow += r.s.yellow;
      red += r.s.red;
    }
    const total = rows.reduce((n, r) => n + r.total, 0);
    return {
      attempted,
      total,
      mastery: total ? ((3 * green + 2 * yellow + red) / (total * 3)) * 100 : 0,
    };
  }, [rows]);

  return (
    <div>
      <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
        <h2 className="text-lg font-semibold text-ink">Your progress</h2>
        {!ready ? (
          <span className="text-sm text-muted">Loading progress…</span>
        ) : (
          <span className="text-sm text-muted">
            {grand.attempted}/{grand.total} attempted ·{" "}
            {grand.mastery.toFixed(1)}% mastery
          </span>
        )}
      </div>

      <div className="overflow-x-auto rounded-xl border border-line bg-paper shadow-sm">
        <table className="w-full border-collapse text-sm">
          <thead>
            <tr className="border-b border-line bg-pane/60 text-left text-xs uppercase tracking-wide text-muted">
              <th className="px-3 py-2 font-semibold">Chapter</th>
              <th className="px-3 py-2 text-right font-semibold">Attempted</th>
              <th className="px-3 py-2 text-center font-semibold">Green</th>
              <th className="px-3 py-2 text-center font-semibold">Yellow</th>
              <th className="px-3 py-2 text-center font-semibold">Red</th>
              <th className="px-3 py-2 text-right font-semibold">Mastery</th>
            </tr>
          </thead>
          <tbody>
            {rows.map(({ chapter: c, s, total }) => (
              <tr key={c.slug} className="border-b border-line last:border-0">
                <td className="px-3 py-2 font-medium text-ink">
                  <Link to={`/practice/${c.slug}`} className="hover:text-accent">
                    <span className="mr-1 text-muted">{c.chapter}.</span>
                    {c.title}
                  </Link>
                </td>
                <td className="px-3 py-2 text-right tabular-nums text-ink">
                  {s.attempted}
                  <span className="text-muted">/{total}</span>
                </td>
                <td className="px-3 py-2 text-center">
                  <StatusChip kind="green" count={s.green} />
                </td>
                <td className="px-3 py-2 text-center">
                  <StatusChip kind="yellow" count={s.yellow} />
                </td>
                <td className="px-3 py-2 text-center">
                  <StatusChip kind="red" count={s.red} />
                </td>
                <td className="px-3 py-2 text-right">
                  <span className="inline-flex items-center gap-2">
                    <span className="h-1.5 w-16 overflow-hidden rounded bg-line/50">
                      <span
                        className="block h-full rounded bg-accent"
                        style={{ width: `${s.mastery}%` }}
                      />
                    </span>
                    <span className="w-12 tabular-nums text-ink">
                      {s.mastery.toFixed(1)}%
                    </span>
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}