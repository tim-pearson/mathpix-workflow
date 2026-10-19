import type { Answer, ChapterData, Question } from "../types";
import { Md } from "./Md";
import { CopyButton } from "./CopyButton";
import { WorkingOut } from "./WorkingOut";
import { buildClipboardText } from "../lib/clipboard";

export interface QuestionCardProps {
  chapter: ChapterData;
  question: Question;
  includeId: boolean;
  defaultOpen: boolean;
}

/** A single exercise question card with answer + working-out disclosures,
 * marks badges and raw-markdown copy buttons. */
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

  const text = (mode: "question" | "answer" | "both") =>
    buildClipboardText({
      mode,
      questionMd: question.md,
      answerMd: answer?.md ?? "",
      includeId,
      id: question.id,
    });

  return (
    <article
      id={question.id}
      className="scroll-mt-16 rounded-xl border border-line bg-paper shadow-sm"
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
        <span className="ml-auto flex items-center gap-1">
          <CopyButton mode="question" label="Copy question" onCopy={text} />
          {hasAnswer && (
            <>
              <CopyButton mode="answer" label="Copy answer" onCopy={text} />
              <CopyButton mode="both" label="Copy question and answer" onCopy={text} />
            </>
          )}
        </span>
      </header>

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
