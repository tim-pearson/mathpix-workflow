import { useEffect, useRef, useState } from "react";
import { copyToClipboard } from "../lib/clipboard";
import { IconCheck, IconCopy } from "./Icons";

export interface CopyButtonProps {
  label: string; // accessible label, e.g. "Copy question, answer and working"
  onCopy: () => string; // returns the raw text to copy
  className?: string;
}

/** Icon-only copy button: shows a check for ~1.2s after a successful copy. */
export function CopyButton({ label, onCopy, className }: CopyButtonProps) {
  const [copied, setCopied] = useState(false);
  const timer = useRef<number | null>(null);

  useEffect(() => () => {
    if (timer.current) window.clearTimeout(timer.current);
  }, []);

  const handle = async () => {
    const ok = await copyToClipboard(onCopy());
    if (ok) {
      setCopied(true);
      if (timer.current) window.clearTimeout(timer.current);
      timer.current = window.setTimeout(() => setCopied(false), 1200);
    }
  };

  return (
    <button
      type="button"
      title={label}
      aria-label={label}
      onClick={handle}
      className={
        "inline-flex items-center justify-center rounded-md border border-line p-1.5 text-muted " +
        "transition-colors hover:border-accent hover:text-accent " +
        "focus:outline-none focus-visible:ring-2 focus-visible:ring-accent " +
        (copied ? "text-accent" : "") +
        (className ? ` ${className}` : "")
      }
    >
      {copied ? <IconCheck className="text-accent" /> : <IconCopy aria-hidden="true" />}
    </button>
  );
}