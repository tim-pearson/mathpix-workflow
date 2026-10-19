import { Md } from "./Md";

export interface WorkingOutProps {
  workingMd?: string;
  questionId?: string;
  defaultOpen?: boolean;
}

/** Working-out disclosure.  Renders nothing when there is no working markdown,
 * so it only ever appears when `questions[id].working_md` exists. */
export function WorkingOut({ workingMd, questionId, defaultOpen = false }: WorkingOutProps) {
  if (!workingMd) return null;
  return (
    <details className="rounded-lg border border-line" open={defaultOpen}>
      <summary className="cursor-pointer select-none px-3 py-1.5 font-medium text-ink hover:text-accent">
        Working out
      </summary>
      <div className="border-t border-line px-3 py-3">
        <Md source={workingMd} blockId={`${questionId ?? "q"}·working`} />
      </div>
    </details>
  );
}
