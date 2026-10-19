// Clipboard helpers.  Copy raw Markdown (not rendered HTML).

export interface ClipboardInput {
  questionMd: string;
  answerMd?: string | null;
  workingMd?: string | null;
  includeId: boolean;
  id?: string;
}

/**
 * Build the raw-markdown text for the single copy button.  Always includes the
 * question; includes the answer and/or working-out sections only when present.
 *  - question:            the question Markdown
 *  - answer present:      blank line + `Answer:` + answer Markdown
 *  - working present:     blank line + `Working out:` + working Markdown
 *  - includeId:           prepends the question id as the first line.
 */
export function buildClipboardText(input: ClipboardInput): string {
  const parts: string[] = [];
  if (input.includeId && input.id) parts.push(input.id);
  parts.push(input.questionMd);
  if (input.answerMd && input.answerMd.trim()) {
    parts.push(`Answer:\n${input.answerMd}`);
  }
  if (input.workingMd && input.workingMd.trim()) {
    parts.push(`Working out:\n${input.workingMd}`);
  }
  return parts.join("\n\n");
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
