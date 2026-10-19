import MiniSearch from "minisearch";
import type { SearchEntry } from "../types";

export interface StoredSearchResult {
  id: string;
  title: string;
  type: string;
  chapter: number;
  text: string;
}

interface IndexedDoc extends SearchEntry {
  /** Unique per-document key for MiniSearch; the exported search index has
   * duplicate `id` values (a question appears once as a section block and once
   * as a question), and MiniSearch rejects duplicate ids. */
  uid: number;
}

export function createSearchIndex(entries: SearchEntry[]): MiniSearch<SearchEntry> {
  const docs: IndexedDoc[] = [];
  for (let i = 0; i < entries.length; i += 1) {
    const e = entries[i];
    if (e && typeof e.id === "string" && typeof e.title === "string") {
      docs.push({ ...e, uid: i });
    }
  }
  const ms = new MiniSearch<SearchEntry>({
    idField: "uid",
    fields: ["title", "text"],
    storeFields: ["id", "title", "type", "chapter", "text"],
    searchOptions: {
      boost: { title: 5, text: 1 },
      prefix: true,
      fuzzy: 0.2,
      combineWith: "AND",
    },
  });
  ms.addAll(docs);
  return ms;
}

export interface GroupedResultItem {
  id: string;
  title: string;
  type: string;
  chapter: number;
  snippet: string;
}

export interface GroupedResult {
  group: string;
  items: GroupedResultItem[];
}

const GROUP_LABEL: Record<string, string> = {
  section: "Section",
  explore: "Section",
  "did-you-know": "Section",
  rewind: "Section",
  "fast-forward": "Section",
  other: "Section",
  "worked-example": "Worked example",
  "key-point": "Key point",
  question: "Question",
  answer: "Answer",
  exercise: "Exercise",
};

/** Build a snippet around the first matched term, falling back to a truncation. */
function snippet(text: string, terms: string[], max = 160): string {
  const lower = text.toLowerCase();
  let best = -1;
  let bestTerm = "";
  for (const t of terms) {
    const at = lower.indexOf(t.toLowerCase());
    if (at >= 0 && (best === -1 || at < best)) {
      best = at;
      bestTerm = t;
    }
  }
  if (best === -1) {
    return text.length > max ? text.slice(0, max).trimEnd() + "…" : text;
  }
  const start = Math.max(0, best - 40);
  const end = Math.min(text.length, best + bestTerm.length + 80);
  return (start > 0 ? "…" : "") + text.slice(start, end).trim() + (end < text.length ? "…" : "");
}

export function groupResults(
  results: (StoredSearchResult & { terms: string[] })[]
): GroupedResult[] {
  const groups = new Map<string, GroupedResultItem[]>();
  for (const r of results) {
    const label = GROUP_LABEL[r.type] ?? "Section";
    const snip = snippet(r.text ?? "", r.terms ?? []);
    if (!groups.has(label)) groups.set(label, []);
    groups.get(label)!.push({ id: r.id, title: r.title, type: r.type, chapter: r.chapter, snippet: snip });
  }
  const order = ["Section", "Worked example", "Key point", "Question", "Answer", "Exercise"];
  return order
    .filter((g) => groups.has(g))
    .map((g) => ({ group: g, items: groups.get(g)! }))
    .concat(
      [...groups.keys()]
        .filter((g) => !order.includes(g))
        .map((g) => ({ group: g, items: groups.get(g)! }))
    );
}
