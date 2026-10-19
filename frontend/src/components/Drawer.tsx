import { useEffect, useState, type ReactNode } from "react";
import { IconMenu } from "./Icons";

export interface DrawerProps {
  /** The sidebar content shown on desktop and inside the drawer on mobile. */
  render: (close: () => void) => ReactNode;
  /** Accessible label for the mobile hamburger. */
  label: string;
}

/**
 * Responsive sidebar: static on lg+ screens, a slide-over drawer (with
 * backdrop) on smaller screens.  Content is rendered once via `render`.
 */
export function Drawer({ render, label }: DrawerProps) {
  const [open, setOpen] = useState(false);

  useEffect(() => {
    if (!open) return;
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") setOpen(false);
    };
    document.addEventListener("keydown", onKey);
    document.body.style.overflow = "hidden";
    return () => {
      document.removeEventListener("keydown", onKey);
      document.body.style.overflow = "";
    };
  }, [open]);

  return (
    <>
      <button
        type="button"
        onClick={() => setOpen(true)}
        aria-label={label}
        title={label}
        className="inline-flex items-center rounded-md border border-line p-1.5 text-muted hover:text-ink lg:hidden"
      >
        <IconMenu aria-hidden="true" />
      </button>

      {/* desktop static sidebar */}
      <div className="hidden lg:block">{render(() => setOpen(false))}</div>

      {/* mobile drawer */}
      {open && (
        <div className="fixed inset-0 z-50 lg:hidden">
          <div
            className="absolute inset-0 bg-black/40"
            onClick={() => setOpen(false)}
            aria-hidden="true"
          />
          <div
            role="dialog"
            aria-modal="true"
            className="absolute left-0 top-0 h-full w-[min(20rem,85vw)] overflow-y-auto border-r border-line bg-pane shadow-xl"
          >
            <div className="flex items-center justify-end border-b border-line p-2">
              <button
                type="button"
                onClick={() => setOpen(false)}
                aria-label="Close"
                className="rounded-md p-1.5 text-muted hover:text-ink"
              >
                ✕
              </button>
            </div>
            {render(() => setOpen(false))}
          </div>
        </div>
      )}
    </>
  );
}
