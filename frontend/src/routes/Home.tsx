import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import type { ChapterData, Manifest } from "../types";
import { loadChapter } from "../data/load";
import { IconBook, IconCalculator, IconPencil } from "../components/Icons";

export interface HomeProps {
  manifest: Manifest | null;
}

export function Home({ manifest }: HomeProps) {
  const [chapters, setChapters] = useState<Record<string, ChapterData>>({});

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

      {/* Reserved for Step 4 — progress tracking is not implemented yet. */}
      <div className="mt-8 rounded-xl border border-dashed border-line bg-paper/50 p-4 text-center text-muted">
        <h2 className="font-semibold text-ink">Your progress</h2>
        <p className="mt-1 text-sm">
          Progress tracking is not implemented yet. It will appear here in a
          later step.
        </p>
      </div>
    </div>
  );
}
