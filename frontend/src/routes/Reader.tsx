import { Fragment, useEffect, useMemo, useRef, useState } from "react";
import { Link, useParams } from "react-router-dom";
import type { ChapterData, Manifest, SectionBlock } from "../types";
import { loadChapter } from "../data/load";
import { Md } from "../components/Md";
import { Drawer } from "../components/Drawer";
import {
  IconBook,
  IconCalculator,
  IconChevronRight,
  IconInfo,
  IconLightbulb,
  IconPencil,
  IconRefresh,
} from "../components/Icons";
import {
  exerciseTitle,
  numberedSections,
  practiceLinksForSection,
  sectionById,
} from "../lib/chapter";

export interface ReaderProps {
  manifest: Manifest | null;
}

export function resolveChapterSlug(manifest: Manifest | null, param: string): string | null {
  if (!manifest) return null;
  if (manifest.chapters.some((c) => c.slug === param)) return param;
  const m = param.match(/^ch(\d{1,2})$/);
  if (m) {
    const ch = manifest.chapters.find((c) => c.chapter === Number(m[1]));
    return ch?.slug ?? null;
  }
  return null;
}

function stripHeading(md: string): string {
  return md.replace(/^(?:<a id="[^"]*"><\/a>\n)?#{1,6}.*\n/, "");
}

const BOX_META: Record<string, { label: string; Icon: typeof IconLightbulb; cls: string }> = {
  explore: { label: "Explore", Icon: IconLightbulb, cls: "border-amber-400/50 bg-amber-50/60 dark:bg-amber-400/10" },
  "did-you-know": { label: "Did you know?", Icon: IconInfo, cls: "border-sky-400/50 bg-sky-50/60 dark:bg-sky-400/10" },
  rewind: { label: "Rewind", Icon: IconRefresh, cls: "border-emerald-400/50 bg-emerald-50/60 dark:bg-emerald-400/10" },
  "fast-forward": { label: "Fast forward", Icon: IconChevronRight, cls: "border-violet-400/50 bg-violet-50/60 dark:bg-violet-400/10" },
  tip: { label: "Tip", Icon: IconLightbulb, cls: "border-amber-400/50 bg-amber-50/60 dark:bg-amber-400/10" },
};

function useScrollSpy(sectionIds: string[], activeKey: string) {
  const [active, setActive] = useState<string | null>(null);
  useEffect(() => {
    setActive(null);
    if (sectionIds.length === 0) return;
    const observer = new IntersectionObserver(
      (entries) => {
        for (const e of entries) {
          if (e.isIntersecting) setActive(e.target.id);
        }
      },
      { rootMargin: "-72px 0px -70% 0px", threshold: 0 }
    );
    for (const id of sectionIds) {
      const el = document.getElementById(id);
      if (el) observer.observe(el);
    }
    return () => observer.disconnect();
  }, [sectionIds, activeKey]);
  return active;
}

function PractiseLinks({ chapter, sectionId }: { chapter: ChapterData; sectionId: string }) {
  const links = practiceLinksForSection(chapter, sectionId);
  if (links.length === 0) return null;
  return (
    <div className="mt-6 rounded-lg border border-line bg-pane/60 p-3">
      <span className="text-sm font-medium text-ink">Practise</span>
      <div className="mt-1 flex flex-wrap gap-2">
        {links.map((ex) => (
          <Link
            key={ex.id}
            to={`/practice/${chapter.slug}/${ex.id}`}
            className="inline-flex items-center gap-1 rounded-md bg-accent-soft px-2.5 py-1 text-sm text-accent hover:underline"
          >
            <IconPencil aria-hidden="true" />
            {exerciseTitle(chapter, ex.id)}
          </Link>
        ))}
      </div>
    </div>
  );
}

function WorkedExampleCard({
  chapter,
  block,
}: {
  chapter: ChapterData;
  block: SectionBlock;
}) {
  const we = chapter.worked_examples.find((w) => w.id === block.id);
  const matches =
    we &&
    blockMatches(block.md, we.question_md) &&
    blockMatches(block.md, we.answer_md);
  if (!we || !matches) {
    return (
      <section id={block.id} className="my-5">
        <Md source={block.md} blockId={block.id} />
      </section>
    );
  }
  return (
    <section id={block.id} className="my-5 scroll-mt-16 rounded-xl border border-line bg-paper shadow-sm">
      <div className="border-b border-line px-4 py-2 font-semibold text-accent">
        WORKED EXAMPLE {we.number}
      </div>
      <div className="px-4 py-3">
        <Md source={we.question_md} blockId={block.id} />
        {we.answer_md && (
          <details className="mt-3 rounded-lg border border-line">
            <summary className="cursor-pointer select-none px-3 py-1.5 font-medium text-ink hover:text-accent">
              Answer
            </summary>
            <div className="border-t border-line px-3 py-3">
              <Md source={we.answer_md} blockId={block.id} />
            </div>
          </details>
        )}
      </div>
    </section>
  );
}

function blockMatches(blockMd: string, entryMd: string | null | undefined): boolean {
  if (!entryMd) return true;
  return blockMd.includes(entryMd);
}

function KeyPointCallout({ chapter, block }: { chapter: ChapterData; block: SectionBlock }) {
  const kp = chapter.key_points.find((k) => k.id === block.id);
  const matches = kp && blockMatches(block.md, kp.md);
  return (
    <section id={block.id} className="my-5 scroll-mt-16 rounded-r-lg border-l-4 border-accent bg-accent-soft/40 px-4 py-3">
      <div className="mb-1 flex items-center gap-1.5 font-semibold text-accent">
        <IconCalculator aria-hidden="true" />
        KEY POINT {kp?.number ?? ""}
      </div>
      {matches && kp ? (
        <Md source={kp.md} blockId={block.id} />
      ) : (
        <Md source={block.md} blockId={block.id} />
      )}
    </section>
  );
}

function TintedBox({ block }: { block: SectionBlock }) {
  const key = block.type === "other" ? "tip" : block.type;
  const meta = BOX_META[key] ?? BOX_META.explore;
  const Icon = meta.Icon;
  return (
    <section id={block.id} className={`my-5 scroll-mt-16 rounded-lg border px-4 py-3 ${meta.cls}`}>
      <div className="mb-1 flex items-center gap-1.5 text-sm font-semibold text-ink">
        <Icon aria-hidden="true" />
        {meta.label}
      </div>
      <Md source={stripHeading(block.md)} blockId={block.id} />
    </section>
  );
}

function ExerciseCard({ chapter, block }: { chapter: ChapterData; block: SectionBlock }) {
  return (
    <section id={block.id} className="my-5 scroll-mt-16">
      <Link
        to={`/practice/${chapter.slug}/${block.id}`}
        className="flex items-center justify-between gap-2 rounded-xl border border-line bg-paper px-4 py-3 shadow-sm transition-colors hover:border-accent"
      >
        <span className="font-semibold text-ink">{block.title || block.heading.replace(/^#+\s*/, "")}</span>
        <span className="inline-flex items-center gap-1 text-sm text-accent">
          <IconPencil aria-hidden="true" /> Practise
        </span>
      </Link>
    </section>
  );
}

function ReaderBlock({ chapter, block }: { chapter: ChapterData; block: SectionBlock }) {
  if (block.type === "exercise") return <ExerciseCard chapter={chapter} block={block} />;
  if (block.type === "worked-example")
    return <WorkedExampleCard chapter={chapter} block={block} />;
  if (block.type === "key-point")
    return <KeyPointCallout chapter={chapter} block={block} />;
  if (["explore", "did-you-know", "rewind", "fast-forward"].includes(block.type))
    return <TintedBox block={block} />;
  if (block.type === "other") {
    // question blocks (##### Question N) are exercise content: skip here
    if (block.heading.trimStart().startsWith("##### Question")) return null;
    if (block.heading.trimStart().startsWith("#### TIP")) return <TintedBox block={block} />;
    return (
      <section id={block.id} className="my-5">
        <Md source={block.md} blockId={block.id} />
      </section>
    );
  }
  return (
    <section id={block.id} className="my-5 scroll-mt-16">
      <Md source={block.md} blockId={block.id} />
      {block.type === "section" && block.level === 2 && (
        <PractiseLinks chapter={chapter} sectionId={block.id} />
      )}
    </section>
  );
}

function ReaderSidebar({
  manifest,
  chapter,
  active,
}: {
  manifest: Manifest;
  chapter: ChapterData | null;
  active: string | null;
}) {
  const [expanded, setExpanded] = useState<string | null>(null);
  useEffect(() => {
    setExpanded((cur) => (chapter ? chapter.slug : cur));
  }, [chapter]);

  return (
    <nav aria-label="Chapters" className="h-full overflow-y-auto p-3">
      <ul className="space-y-1">
        {manifest.chapters.map((c) => {
          const open = expanded === c.slug;
          const isActive = chapter?.slug === c.slug;
          return (
            <li key={c.slug}>
              <div className="flex items-center gap-1">
                <button
                  type="button"
                  aria-label={open ? "Collapse" : "Expand"}
                  onClick={() => setExpanded(open ? null : c.slug)}
                  className="rounded p-0.5 text-muted hover:text-ink"
                >
                  <IconChevronRight
                    aria-hidden="true"
                    className={`transition-transform ${open ? "rotate-90" : ""}`}
                  />
                </button>
                <Link
                  to={`/read/${c.slug}`}
                  className={`flex-1 truncate rounded px-1.5 py-1 text-sm ${
                    isActive ? "bg-accent-soft font-medium text-accent" : "text-ink hover:bg-line/40"
                  }`}
                >
                  <span className="text-muted">{c.chapter}.</span> {c.title}
                </Link>
              </div>
              {open && chapter?.slug === c.slug && (
                <ul className="ml-4 mt-0.5 space-y-0.5 border-l border-line pl-2">
                  {numberedSections(chapter).map((s) => (
                    <li key={s.id}>
                      <Link
                        to={`/read/${c.slug}/${s.id}`}
                        className={`block truncate rounded px-1.5 py-0.5 text-sm ${
                          active === s.id
                            ? "bg-accent-soft font-medium text-accent"
                            : "text-muted hover:text-ink"
                        }`}
                      >
                        {s.title}
                      </Link>
                    </li>
                  ))}
                </ul>
              )}
            </li>
          );
        })}
      </ul>
      <div className="mt-4 border-t border-line pt-3">
        <div className="px-1.5 text-xs font-semibold uppercase tracking-wide text-muted">
          Reference
        </div>
        <ul className="mt-1 space-y-0.5">
          {manifest.non_chapter_files.map((f) => (
            <li
              key={f.file}
              title="Not exported to frontend-data yet"
              className="flex items-center gap-1.5 rounded px-1.5 py-1 text-sm text-muted"
            >
              <IconBook aria-hidden="true" />
              {f.title}
              <span className="text-xs opacity-70">(pending)</span>
            </li>
          ))}
        </ul>
      </div>
    </nav>
  );
}

export function Reader({ manifest }: ReaderProps) {
  const { chapter: chapterParam, sectionId } = useParams();
  const slug = resolveChapterSlug(manifest, chapterParam ?? "ch01");
  const [chapter, setChapter] = useState<ChapterData | null>(null);
  const [error, setError] = useState<string | null>(null);
  const mainRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!slug) return;
    setChapter(null);
    setError(null);
    loadChapter(slug)
      .then(setChapter)
      .catch((e) => setError(String(e)));
  }, [slug]);

  const sectionIds = useMemo(
    () => (chapter ? numberedSections(chapter).map((s) => s.id) : []),
    [chapter]
  );
  const active = useScrollSpy(sectionIds, chapter?.slug ?? "");

  // deep link: scroll to the requested block and flash it
  useEffect(() => {
    if (!sectionId || !chapter) return;
    const el = document.getElementById(sectionId);
    if (el) {
      el.scrollIntoView({ block: "start" });
      el.classList.add("flash-target");
      const t = window.setTimeout(() => el.classList.remove("flash-target"), 1800);
      return () => window.clearTimeout(t);
    }
  }, [sectionId, chapter]);

  const tocTitle = chapter
    ? sectionId === "keypoints"
      ? `Key points — ${chapter.title}`
      : (() => {
          const s = sectionId ? sectionById(chapter, sectionId) : undefined;
          return s ? s.title : chapter.title;
        })()
    : "";

  if (!manifest) return <div className="p-8 text-muted">Loading…</div>;
  if (!slug) return <div className="p-8 text-danger">Unknown chapter: {chapterParam}</div>;

  return (
    <div className="flex h-full">
      <aside className="hidden w-64 shrink-0 border-r border-line bg-pane lg:block">
        <ReaderSidebar manifest={manifest} chapter={chapter} active={active} />
      </aside>
      <div className="flex min-w-0 flex-1 flex-col">
        <div className="flex items-center gap-2 border-b border-line px-3 py-2 lg:hidden">
          <Drawer
            label="Chapters"
            render={() => <ReaderSidebar manifest={manifest} chapter={chapter} active={active} />}
          />
          <span className="truncate text-sm font-medium text-ink">{tocTitle}</span>
        </div>
        <div ref={mainRef} className="flex-1 overflow-y-auto">
          {error ? (
            <div className="p-8 text-danger">{error}</div>
          ) : !chapter ? (
            <div className="p-8 text-muted">Loading chapter…</div>
          ) : sectionId === "keypoints" ? (
            <article className="mx-auto max-w-prose px-4 py-6">
              <h1 className="text-2xl font-bold text-ink">Key points — {chapter.title}</h1>
              <p className="mt-1 text-sm text-muted">
                All key points for this chapter.
              </p>
              {chapter.key_points.map((kp, i) => (
                <Fragment key={kp.id}>
                  {i > 0 && (
                    <div className="mx-2 my-4 border-t border-line/70" aria-hidden="true" />
                  )}
                  <details
                    id={kp.id}
                    open
                    className="scroll-mt-16 rounded-r-lg border-l-4 border-accent bg-accent-soft/40 px-4 py-3"
                  >
                    <summary className="flex cursor-pointer select-none items-center gap-1.5 font-semibold text-accent">
                      <IconCalculator aria-hidden="true" />
                      KEY POINT {kp.number}
                    </summary>
                    <div className="mt-2 border-t border-accent/30 pt-2">
                      <Md source={kp.md} blockId={kp.id} />
                    </div>
                  </details>
                </Fragment>
              ))}
              {chapter.key_points.length === 0 && (
                <p className="text-sm text-muted">No key points in this chapter.</p>
              )}
            </article>
          ) : (
            <article className="mx-auto max-w-prose px-4 py-6">
              {chapter.sections.map((b) => (
                <ReaderBlock key={b.id} chapter={chapter} block={b} />
              ))}
              <div className="mt-8 border-t border-line pt-4 text-sm text-muted">
                End of {chapter.title}
              </div>
            </article>
          )}
        </div>
      </div>
    </div>
  );
}
