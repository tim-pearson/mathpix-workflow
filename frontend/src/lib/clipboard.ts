// Clipboard helpers.  Copy raw Markdown (not rendered HTML).

export type CopyMode = "question" | "answer" | "both";

export interface ClipboardInput {
  mode: CopyMode;
  questionMd: string;
  answerMd?: string | null;
  includeId: boolean;
  id?: string;
}

/**
 * Build the raw-markdown text for a copy operation.
 *  - question: the question Markdown (optionally prefixed with the id).
 *  - answer:   the answer Markdown (optionally prefixed with the id).
 *  - both:     question Markdown + blank line + `Answer:` + answer Markdown,
 *              optionally prefixed with the id.
 */
export function buildClipboardText(input: ClipboardInput): string {
  const { mode, questionMd, answerMd, includeId, id } = input;
  const prefix = includeId && id ? [id] : [];
  if (mode === "both") {
    return [...prefix, questionMd, `Answer:\n${answerMd ?? ""}`].join("\n\n");
  }
  const body = mode === "question" ? questionMd : answerMd ?? "";
  return [...prefix, body].join("\n\n");
}

/** Copy text via the async clipboard API, falling back to execCommand. */
export async function copyToClipboard(text: string): Promise<boolean> {
  try {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
      return true;
    }
  } catch (e) {
    // fall through to the execCommand fallback
  }
  try {
    const ta = document.createElement("textarea");
    ta.value = text;
    ta.setAttribute("readonly", "");
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.select();
    const ok = document.execCommand("copy");
    document.body.removeChild(ta);
    return ok;
  } catch (e) {
    return false;
  }
}
