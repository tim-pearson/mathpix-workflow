import { useEffect, useMemo, useState } from "react";
import { Link, useParams } from "react-router-dom";
import type { ChapterData, Exercise, Manifest } from "../types";
import { loadChapter } from "../data/load";
import { Drawer } from "../components/Drawer";
import { QuestionCard } from "../components/QuestionCard";
import { FormulaPanel } from "../components/FormulaPanel";
import { IconBook, IconChevronRight } from "../components/Icons";
import { resolveChapterSlug } from "./Reader";
import { exerciseSectionId, sectionTitle } from "../lib/chapter";
import { useLocalStorage } from "../hooks/useLocalStorage";
import { exerciseQuestionCount, parsePrerequisiteQuestions } from "../lib/prereq";
import { useProgress } from "../progress/ProgressContext";
import type { Question } from "../types";

export interface PracticeProps {
  manifest: Manifest | null;
}

const INCLUDE_ID_KEY = "tutex-copy-include-id";

function PracticeSidebar({
  manifest,
  chapter,
  currentExercise,
}: {
  manifest: Manifest;
  chapter: ChapterData | null;
  currentExercise: string | null;
}) {
  const [expanded, setExpanded] = useState<string | null>(null);
  useEffect(() => {
    setExpanded((cur) => (chapter ? chapter.slug : cur));
  }, [chapter]);

  return (
    <nav aria-label="Exercises" className="h-full overflow-y-auto p-3">
      <ul className="space-y-1">
        {manifest.chapters.map((c) => {
          const open = expanded === c.slug;
          const ch = c.slug === chapter?.slug ? chapter : null;
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
                  to={`/practice/${c.slug}`}
                  className={`flex-1 truncate rounded px-1.5 py-1 text-sm ${
                    chapter?.slug === c.slug
                      ? "bg-accent-soft font-medium text-accent"
                      : "text-ink hover:bg-line/40"
                  }`}
                >
                  <span className="text-muted">{c.chapter}.</span> {c.title}
                </Link>
              </div>
              {open && ch && (
                <ul className="ml-4 mt-0.5 space-y-0.5 border-l border-line pl-2">
                  {ch.exercises.map((ex) => (
                    <li key={ex.id}>
                      <Link
                        to={`/practice/${c.slug}/${ex.id}`}
                        className={`flex items-baseline justify-between gap-1 rounded px-1.5 py-0.5 text-sm ${
                          currentExercise === ex.id
                            ? "bg-accent-soft font-medium text-accent"
                            : "text-muted hover:text-ink"
                        }`}
                      >
                        <span className="truncate">{ex.title}</span>
                        <span className="shrink-0 text-xs opacity-70">
                          {exerciseQuestionCount(ch, ex)}
                        </span>
                      </Link>
                    </li>
                  ))}
                </ul>
              )}
            </li>
          );
        })}
      </ul>
    </nav>
  );
}

const EXERCISE_KIND_LABEL: Record<string, string> = {
  exercise: "Exercise",
  review: "Review",
  cross: "Cross-topic review",
  prerequisite: "Prerequisite",
};

function ExerciseHeading({ chapter, exercise }: { chapter: ChapterData; exercise: Exercise }) {
  const sourceSection = exerciseSectionId(chapter, exercise.id);
  const sourceTitle = sectionTitle(chapter, sourceSection);
  return (
    <div className="mb-4">
      <h2 className="flex flex-wrap items-center gap-2 text-xl font-bold text-ink">
        {exercise.title}
        <span className="rounded-full border border-line px-2 py-0.5 text-xs font-medium text-muted">
          {EXERCISE_KIND_LABEL[exercise.kind] ?? exercise.kind}
        </span>
        <span className="text-sm font-normal text-muted">
          {exerciseQuestionCount(chapter, exercise)} questions
        </span>
      </h2>
      {sourceTitle && (
        <Link
          to={`/read/${chapter.slug}/${sourceSection ?? ""}`}
          className="inline-flex items-center gap-1 text-sm text-muted hover:text-accent"
        >
          <IconBook aria-hidden="true" /> In the textbook: {sourceTitle}
        </Link>
      )}
    </div>
  );
}

export function Practice({ manifest }: PracticeProps) {
  const { chapter: chapterParam, exerciseId } = useParams();
  const slug = resolveChapterSlug(manifest, chapterParam ?? "ch01");
  const [chapter, setChapter] = useState<ChapterData | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [statusFilter, setStatusFilter] = useState<
    "all" | "unattempted" | "green" | "yellow" | "red"
  >("all");
  const [allOpen, setAllOpen] = useState(false);
  const [includeId, setIncludeId] = useLocalStorage<boolean>(INCLUDE_ID_KEY, false);
  const [queryId, setQueryId] = useState<string | null>(null);
  const { statuses } = useProgress();

  useEffect(() => {
    if (!slug) return;
    setChapter(null);
    setError(null);
    loadChapter(slug)
      .then(setChapter)
      .catch((e) => setError(String(e)));
  }, [slug]);

  // honour ?q= deep link
  useEffect(() => {
    const params = new URLSearchParams(window.location.hash.split("?")[1] ?? "");
    setQueryId(params.get("q"));
  }, [exerciseId, slug]);

  const exercise: Exercise | undefined = useMemo(() => {
    if (!chapter) return undefined;
    if (exerciseId) {
      const ex = chapter.exercises.find((e) => e.id === exerciseId);
      if (ex) return ex;
    }
    // default to the first real exercise (not the prerequisite table)
    return (
      chapter.exercises.find((e) => e.kind === "exercise") ??
      chapter.exercises.find((e) => e.kind === "review") ??
      chapter.exercises[0]
    );
  }, [chapter, exerciseId]);

  // resolved questions (parsing prerequisites from the table when needed)
  const resolvedQuestions = useMemo<Question[]>(() => {
    if (!exercise) return [];
    if (exercise.kind === "prerequisite" && exercise.questions.length === 0) {
      const block = chapter?.sections.find((s) => s.id === exercise.id);
      if (block) {
        return parsePrerequisiteQuestions(block.md, exercise.id).map((q) => ({
          ...q,
          answer_id:
            q.answer_id && chapter!.answers[q.answer_id] ? q.answer_id : null,
        }));
      }
      return [];
    }
    return (exercise.questions ?? [])
      .map((id) => chapter!.questions[id])
      .filter((q): q is Question => Boolean(q));
  }, [exercise, chapter]);

  const filteredQuestions = useMemo(() => {
    return resolvedQuestions.filter((x) => {
      const st = statuses[x.id]?.status ?? null;
      if (statusFilter === "all") return true;
      if (statusFilter === "unattempted") return st == null;
      return st === statusFilter;
    });
  }, [resolvedQuestions, statuses, statusFilter]);

  // deep link: scroll to and flash the target question
  useEffect(() => {
    if (!queryId) return;
    const el = document.getElementById(queryId);
    if (el) {
      el.scrollIntoView({ block: "center" });
      el.classList.add("flash-target");
      const t = window.setTimeout(() => el.classList.remove("flash-target"), 1800);
      return () => window.clearTimeout(t);
    }
  }, [queryId, exercise?.id]);

  if (!manifest) return <div className="p-8 text-muted">Loading…</div>;
  if (!slug) return <div className="p-8 text-danger">Unknown chapter: {chapterParam}</div>;

  return (
    <div className="flex h-full">
      <aside className="hidden w-64 shrink-0 border-r border-line bg-pane lg:block">
        <PracticeSidebar manifest={manifest} chapter={chapter} currentExercise={exercise?.id ?? null} />
      </aside>
      <div className="flex min-w-0 flex-1 flex-col">
        <div className="flex items-center gap-2 border-b border-line px-3 py-2 lg:hidden">
          <Drawer
            label="Exercises"
            render={() => (
              <PracticeSidebar manifest={manifest} chapter={chapter} currentExercise={exercise?.id ?? null} />
            )}
          />
          <span className="truncate text-sm font-medium text-ink">{exercise?.title ?? ""}</span>
        </div>
        <div className="flex-1 overflow-y-auto">
          {error ? (
            <div className="p-8 text-danger">{error}</div>
          ) : !chapter ? (
            <div className="p-8 text-muted">Loading chapter…</div>
          ) : (
            <div className="mx-auto max-w-3xl px-4 py-6">
              {exercise && (
                <>
                  <ExerciseHeading chapter={chapter} exercise={exercise} />

                  {/* filter by progress status (chapters are in the sidebar/drawer) */}
                  <div className="mb-4 flex flex-wrap items-center gap-2 rounded-lg border border-line bg-pane/60 p-2">
                    {(
                      [
                        ["all", "All"],
                        ["unattempted", "Unattempted"],
                        ["green", "Green"],
                        ["yellow", "Yellow"],
                        ["red", "Red"],
                      ] as const
                    ).map(([value, label]) => {
                      const active = statusFilter === value;
                      return (
                        <button
                          key={value}
                          type="button"
                          onClick={() => setStatusFilter(value)}
                          className={`rounded-md px-2 py-1 text-sm ${
                            active
                              ? "bg-accent font-medium text-white"
                              : "text-muted hover:text-ink"
                          }`}
                        >
                          {label}
                        </button>
                      );
                    })}
                    <span className="ml-auto flex items-center gap-3">
                      <button
                        type="button"
                        onClick={() => setAllOpen((v) => !v)}
                        className="rounded-md border border-line px-2 py-1 text-sm text-muted hover:text-ink"
                      >
                        {allOpen ? "Collapse all" : "Expand all"}
                      </button>
                      <label className="flex items-center gap-1.5 text-sm text-muted">
                        <input
                          type="checkbox"
                          checked={includeId}
                          onChange={(e) => setIncludeId(e.target.checked)}
                        />
                        Include id
                      </label>
                    </span>
                  </div>

                  {filteredQuestions.length === 0 ? (
                    <p className="text-sm text-muted">
                      {resolvedQuestions.length === 0
                        ? "No questions in this exercise."
                        : "No questions match the filter."}
                    </p>
                  ) : (
                    <div className="space-y-4">
                      {filteredQuestions.map((q) => (
                        <QuestionCard
                          key={q.id}
                          chapter={chapter}
                          question={q}
                          includeId={includeId}
                          defaultOpen={allOpen}
                        />
                      ))}
                    </div>
                  )}
                </>
              )}
            </div>
          )}
        </div>
      </div>
      {chapter && <FormulaPanel chapter={chapter} />}
    </div>
  );
}
