import { useEffect, useMemo, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import type { Manifest } from "../types";
import { loadSearchIndex } from "../data/load";
import { createSearchIndex, groupResults, type GroupedResultItem } from "../lib/search";
import { IconSearch } from "./Icons";

export interface SearchBoxProps {
  manifest: Manifest | null;
  className?: string;
}

function navigateTarget(
  result: Pick<GroupedResultItem, "id" | "type" | "chapter">,
  manifest: Manifest | null
): string | null {
  const chapter = manifest?.chapters.find((c) => c.chapter === result.chapter);
  if (!chapter) return null;
  const slug = chapter.slug;
  if (result.type === "question") {
    // ch02-ex2E-q1 -> block ch02-ex2E
    const m = result.id.match(/^(ch\d\d)-(.+)-(?:q|ps|p|m)\d+$/);
    const block = m ? `${m[1]}-${m[2]}` : null;
    return block
      ? `#/practice/${slug}/${block}?q=${result.id}`
      : `#/practice/${slug}`;
  }
  if (result.type === "answer") {
    const qid = result.id.replace("-ans-", "-");
    const m = qid.match(/^(ch\d\d)-(.+)-(?:q|ps|p|m)\d+$/);
    const block = m ? `${m[1]}-${m[2]}` : null;
    return block
      ? `#/practice/${slug}/${block}?q=${qid}`
      : `#/practice/${slug}`;
  }
  return `#/read/${slug}/${result.id}`;
}

export function SearchBox({ manifest, className }: SearchBoxProps) {
  const [query, setQuery] = useState("");
  const [open, setOpen] = useState(false);
  const [active, setActive] = useState(0);
  const [index, setIndex] = useState<ReturnType<typeof createSearchIndex> | null>(null);
  const [error, setError] = useState<string | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);
  const listRef = useRef<HTMLDivElement>(null);
  const navigate = useNavigate();

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "/" && !open && document.activeElement?.tagName !== "INPUT") {
        e.preventDefault();
        inputRef.current?.focus();
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [open]);

  // load the search index on first interaction with the field (retry allowed)
  const ensureIndex = async () => {
    if (index) return;
    try {
      const entries = await loadSearchIndex();
      setIndex(createSearchIndex(entries));
      setError(null);
    } catch (e) {
      console.error("[search] failed to initialise search index:", e);
      setError(
        "Search is unavailable: the search index could not be loaded. " +
          "In frontend/ run `npm run sync-data`, then try again."
      );
    }
  };

  const results = useMemo(() => {
    if (!index || !query.trim()) return [];
    const raw = index.search(query.trim(), {
      prefix: true,
      fuzzy: 0.2,
      boost: { title: 5, text: 1 },
      combineWith: "AND",
    }) as unknown as (GroupedResultItem & { text: string; terms: string[] })[];
    return groupResults(raw.slice(0, 50));
  }, [index, query]);

  const flat = useMemo(
    () => results.flatMap((g) => g.items),
    [results]
  );

  useEffect(() => setActive(0), [query]);

  const go = (item: GroupedResultItem) => {
    const target = navigateTarget(item, manifest);
    if (target) {
      setOpen(false);
      setQuery("");
      navigate(target.slice(1)); // strip leading '#'
    }
  };

  const onKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "ArrowDown") {
      e.preventDefault();
      setActive((a) => Math.min(a + 1, flat.length - 1));
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      setActive((a) => Math.max(a - 1, 0));
    } else if (e.key === "Enter") {
      e.preventDefault();
      const item = flat[active];
      if (item) go(item);
    } else if (e.key === "Escape") {
      setOpen(false);
      inputRef.current?.blur();
    }
  };

  const chapterTitle = (n: number) =>
    manifest?.chapters.find((c) => c.chapter === n)?.title ?? `Chapter ${n}`;

  return (
    <div className={`relative ${className ?? ""}`} onBlur={() => setOpen(false)}>
      <div className="relative">
        <span className="pointer-events-none absolute left-2.5 top-1/2 -translate-y-1/2 text-muted">
          <IconSearch aria-hidden="true" />
        </span>
        <input
          ref={inputRef}
          value={query}
          onChange={(e) => {
            setQuery(e.target.value);
            ensureIndex();
            if (e.target.value.trim()) setOpen(true);
            else setOpen(false);
          }}
          onFocus={() => {
            ensureIndex();
            if (query.trim()) setOpen(true);
          }}
          onKeyDown={onKeyDown}
          placeholder="Search…  ( / )"
          aria-label="Search"
          className="w-full rounded-lg border border-line bg-paper py-1.5 pl-8 pr-3 text-sm text-ink placeholder:text-muted focus:border-accent focus:outline-none focus:ring-1 focus:ring-accent"
        />
      </div>
      {open && query.trim() && (
        <div
          ref={listRef}
          className="absolute z-40 mt-1 max-h-[26rem] w-[min(28rem,90vw)] overflow-auto rounded-lg border border-line bg-paper shadow-xl dark:shadow-black/40"
        >
          {error ? (
            <div className="px-3 py-2 text-sm text-danger">{error}</div>
          ) : results.length === 0 ? (
            <div className="px-3 py-2 text-sm text-muted">No results for “{query}”.</div>
          ) : (
            results.map((g) => (
              <div key={g.group}>
                <div className="sticky top-0 border-b border-line bg-paper px-3 py-1 text-xs font-semibold uppercase tracking-wide text-muted">
                  {g.group}
                </div>
                {g.items.map((item) => {
                  const i = flat.indexOf(item);
                  return (
                    <button
                      key={item.id}
                      type="button"
                      onMouseDown={(e) => e.preventDefault()}
                      onClick={() => go(item)}
                      onMouseEnter={() => setActive(i)}
                      className={`block w-full px-3 py-2 text-left text-sm ${
                        i === active ? "bg-accent-soft" : ""
                      }`}
                    >
                      <span className="flex items-baseline justify-between gap-2">
                        <span className="font-medium text-ink">{item.title || item.id}</span>
                        <span className="shrink-0 text-xs text-muted">
                          {chapterTitle(item.chapter)}
                        </span>
                      </span>
                      {item.snippet && (
                        <span className="mt-0.5 block truncate text-xs text-muted">
                          {item.snippet}
                        </span>
                      )}
                    </button>
                  );
                })}
              </div>
            ))
          )}
        </div>
      )}
    </div>
  );
}

// used by tests
export { navigateTarget };
