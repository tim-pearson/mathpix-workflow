import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";
import { createSearchIndex, groupResults, type StoredSearchResult } from "../src/lib/search";
import type { SearchEntry } from "../src/types";

const entries: SearchEntry[] = [
  { chapter: 2, id: "ch02-s-2.5", title: "2.5 Solving exponential equations", text: "Solve exponential equations using logarithms.", type: "section" },
  { chapter: 2, id: "ch02-we-2.11", title: "WORKED EXAMPLE 2.11", text: "Solve 5^(2x+1) = 7", type: "worked-example" },
  { chapter: 2, id: "ch02-ex2E-q1", title: "Question 1", text: "Solve 5^x = 18", type: "question" },
  { chapter: 2, id: "ch02-ans-ex2E-q1", title: "Answer 1", text: "1.80", type: "answer" },
  { chapter: 2, id: "ch02-kp-2.3", title: "KEY POINT 2.3", text: "laws of logarithms", type: "key-point" },
];

type Result = StoredSearchResult & { terms: string[] };

describe("search grouping", () => {
  it("groups by display label and boosts titles", () => {
    const ms = createSearchIndex(entries);
    const raw = ms.search("Solve") as unknown as Result[];
    const grouped = groupResults(raw);
    const groups = grouped.map((g) => g.group);
    expect(groups).toContain("Question");
    expect(groups).toContain("Worked example");
    // 'Solve' is in section text, worked-example title, question text
    const qGroup = grouped.find((g) => g.group === "Question")!;
    expect(qGroup.items[0].id).toBe("ch02-ex2E-q1");
  });

  it("snippet contains the matched term", () => {
    const ms = createSearchIndex(entries);
    const raw = ms.search("logarithm") as unknown as Result[];
    const grouped = groupResults(raw);
    expect(grouped.length).toBeGreaterThan(0);
    const snips = grouped.flatMap((g) => g.items.map((i) => i.snippet));
    expect(snips.some((s) => s.includes("logarithm"))).toBe(true);
  });

  it("indexes the real exported search index (which has duplicate ids)", () => {
    const path = resolve(
      process.cwd(),
      "public",
      "data",
      "search-index.json"
    );
    const real = JSON.parse(readFileSync(path, "utf-8")) as SearchEntry[];
    // sanity: the export does contain duplicate ids
    const ids = new Set(real.map((e) => e.id));
    expect(real.length).toBeGreaterThan(ids.size);
    // the constructor must not throw (MiniSearch rejects duplicate ids)
    expect(() => createSearchIndex(real)).not.toThrow();
    const ms = createSearchIndex(real);
    const raw = ms.search("logarithm") as unknown as Result[];
    expect(raw.length).toBeGreaterThan(0);
  });

  it("ignores malformed entries without fabricating results", () => {
    const dirty = [
      ...entries,
      null as unknown as SearchEntry,
      {} as SearchEntry,
      { chapter: 2 } as unknown as SearchEntry,
    ];
    const ms = createSearchIndex(dirty);
    const raw = ms.search("Solve") as unknown as Result[];
    expect(raw.some((r) => r.id === "ch02-ex2E-q1")).toBe(true);
  });
});
