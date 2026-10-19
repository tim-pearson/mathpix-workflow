import { useState } from "react";
import type { ChapterData } from "../types";
import { Md } from "./Md";
import { IconCalculator } from "./Icons";

/** Fixed formulas panel: a slim vertical tab on wide screens that opens a
 * sticky, independently scrolling panel; a floating button + bottom sheet on
 * narrow screens.  Entries are collapsible and titled with their real title
 * (e.g. "KEY POINT 2.3"). */
export function FormulaPanel({ chapter }: { chapter: ChapterData }) {
  const [open, setOpen] = useState(false);
  const formulas = chapter.formulas;

  if (formulas.length === 0) return null;

  return (
    <>
      {/* wide-screen: slim vertical tab */}
      <button
        type="button"
        onClick={() => setOpen((o) => !o)}
        className="fixed right-0 top-1/2 z-40 hidden -translate-y-1/2 items-center gap-1 rounded-l-lg border border-r-0 border-line bg-paper px-1.5 py-3 text-xs font-semibold text-muted shadow-sm transition-colors hover:text-accent lg:flex"
        style={{ writingMode: "vertical-rl" }}
        aria-expanded={open}
      >
        <IconCalculator aria-hidden="true" /> Formulas
      </button>

      {open && (
        <div className="fixed right-0 top-14 z-30 hidden max-h-[calc(100vh-3.5rem)] w-[min(24rem,70vw)] flex-col border-l border-line bg-paper shadow-2xl lg:flex">
          <div className="flex items-center justify-between border-b border-line px-3 py-2">
            <span className="font-semibold text-ink">Formulas — {chapter.title}</span>
            <button
              type="button"
              onClick={() => setOpen(false)}
              aria-label="Close formulas"
              className="rounded p-1 text-muted hover:text-ink"
            >
              ✕
            </button>
          </div>
          <div className="flex-1 overflow-y-auto p-3">
            {formulas.map((f) => (
              <details key={f.id} className="mb-2 rounded-lg border border-line">
                <summary className="cursor-pointer select-none px-3 py-1.5 text-sm font-medium text-ink hover:text-accent">
                  {f.title}
                </summary>
                <div className="border-t border-line px-3 py-2">
                  <Md source={f.md} blockId={f.id} />
                </div>
              </details>
            ))}
          </div>
        </div>
      )}

      {/* narrow-screen: floating button */}
      <button
        type="button"
        onClick={() => setOpen((o) => !o)}
        aria-label="Formulas"
        className="fixed bottom-5 right-4 z-40 inline-flex items-center gap-1.5 rounded-full bg-accent px-4 py-2.5 text-sm font-medium text-white shadow-lg lg:hidden"
      >
        <IconCalculator aria-hidden="true" /> Formulas
      </button>

      {open && (
        <div className="fixed inset-x-0 bottom-0 z-40 max-h-[75vh] flex-col rounded-t-xl border border-b-0 border-line bg-paper shadow-2xl lg:hidden">
          <div className="flex items-center justify-between border-b border-line px-3 py-2">
            <span className="font-semibold text-ink">Formulas — {chapter.title}</span>
            <button
              type="button"
              onClick={() => setOpen(false)}
              aria-label="Close formulas"
              className="rounded p-1 text-muted hover:text-ink"
            >
              ✕
            </button>
          </div>
          <div className="flex-1 overflow-y-auto p-3">
            {formulas.map((f) => (
              <details key={f.id} className="mb-2 rounded-lg border border-line">
                <summary className="cursor-pointer select-none px-3 py-1.5 text-sm font-medium text-ink hover:text-accent">
                  {f.title}
                </summary>
                <div className="border-t border-line px-3 py-2">
                  <Md source={f.md} blockId={f.id} />
                </div>
              </details>
            ))}
          </div>
        </div>
      )}
    </>
  );
}
