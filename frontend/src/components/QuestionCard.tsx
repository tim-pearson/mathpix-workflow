import type { Answer, ChapterData, Question } from "../types";
import { Md } from "./Md";
import { CopyButton } from "./CopyButton";
import { WorkingOut } from "./WorkingOut";
import { StatusSelector } from "./StatusSelector";
import { FlagButton } from "./FlagButton";
import { useFlags } from "../flags/FlagContext";
import { buildClipboardText } from "../lib/clipboard";

export interface QuestionCardProps {
  chapter: ChapterData;
  question: Question;
  includeId: boolean;
  defaultOpen: boolean;
}

/** A single exercise question card with answer + working-out disclosures,
 * marks badges and one copy button that copies everything available. */
export function QuestionCard({
  chapter,
  question,
  includeId,
  defaultOpen,
}: QuestionCardProps) {
  const answer: Answer | undefined = question.answer_id
    ? chapter.answers[question.answer_id]
    : undefined;
  const hasAnswer = Boolean(answer && answer.md.trim());
  const flag = useFlags().flags[question.id];

  const copyText = () =>
    buildClipboardText({
      questionMd: question.md,
      answerMd: answer?.md ?? null,
      workingMd: question.working_md ?? null,
      includeId,
      id: question.id,
    });

  const copyLabel = hasAnswer
    ? question.working_md
      ? "Copy question, answer and working"
      : "Copy question and answer"
    : "Copy question";

  return (
    <article
      id={question.id}
      className={`scroll-mt-16 rounded-xl border bg-paper shadow-sm ${
        flag ? "border-amber-400/70" : "border-line"
      }`}
    >
      <header className="flex flex-wrap items-center gap-2 border-b border-line px-4 py-2">
        <h3 className="font-semibold text-ink">{question.label}</h3>
        {question.marks.length > 0 && (
          <span className="flex gap-1">
            {question.marks.map((m, i) => (
              <span
                key={i}
                className="rounded-full border border-line px-1.5 py-0.5 text-xs text-muted"
                title={`${m} mark${m === 1 ? "" : "s"}`}
              >
                {m}
              </span>
            ))}
          </span>
        )}
        <span className="ml-auto flex flex-wrap items-center gap-3">
          <FlagButton targetId={question.id} />
          <StatusSelector questionId={question.id} />
          <CopyButton label={copyLabel} onCopy={copyText} />
        </span>
      </header>

      {flag && (
        <div className="flex items-start gap-2 border-b border-amber-400/40 bg-amber-400/10 px-4 py-1.5 text-xs text-amber-700 dark:text-amber-300">
          <span aria-hidden="true">⚠</span>
          <span>{flag.note || "Flagged — suspected mistake."}</span>
        </div>
      )}

      <div className="px-4 py-3">
        <Md source={question.md} blockId={question.id} />

        <div className={hasAnswer && question.working_md ? "mt-3 grid gap-3 md:grid-cols-2" : "mt-3"}>
          {hasAnswer ? (
            <details className="rounded-lg border border-line" open={defaultOpen}>
              <summary className="cursor-pointer select-none px-3 py-1.5 font-medium text-ink hover:text-accent">
                Answer
              </summary>
              <div className="border-t border-line px-3 py-3">
                <Md source={answer!.md} blockId={answer!.id} />
              </div>
            </details>
          ) : (
            <p className="text-sm italic text-muted">Answer not linked</p>
          )}

          {question.working_md && (
            <WorkingOut
              workingMd={question.working_md}
              questionId={question.id}
              defaultOpen={defaultOpen}
            />
          )}
        </div>
      </div>
    </article>
  );
}
