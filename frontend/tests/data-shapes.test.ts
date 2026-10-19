import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";
import type {
  ChapterData,
  Manifest,
  Mention,
  SearchEntry,
  Stats,
} from "../src/types";

const DATA = resolve(process.cwd(), "public", "data") + "/";

function load(name: string) {
  return JSON.parse(readFileSync(`${DATA}${name}`, "utf-8"));
}

describe("exported JSON shapes (observed, not assumed)", () => {
  const manifest = load("manifest.json") as Manifest;

  it("manifest has the expected top-level shape", () => {
    expect(manifest.schema_version).toBe(1);
    expect(Array.isArray(manifest.chapters)).toBe(true);
    expect(manifest.chapters.length).toBe(11);
    expect(manifest.chapters[0]).toHaveProperty("slug");
    expect(manifest.chapters[0].counts).toMatchObject({
      questions: expect.any(Number),
      answers: expect.any(Number),
      key_points: expect.any(Number),
      worked_examples: expect.any(Number),
      exercises: expect.any(Number),
      linked_answers: expect.any(Number),
    });
    expect(Array.isArray(manifest.non_chapter_files)).toBe(true);
  });

  it("chapter files are keyed consistently across chapters", () => {
    for (const c of manifest.chapters) {
      const ch = load(`chapters/${c.slug}.json`) as ChapterData;
      expect(ch.slug).toBe(c.slug);
      expect(ch.chapter).toBe(c.chapter);
      for (const key of [
        "sections",
        "exercises",
        "questions",
        "answers",
        "key_points",
        "worked_examples",
        "formulas",
        "mentions",
        "mentioned_by",
      ] as const) {
        expect(ch).toHaveProperty(key);
      }
    }
  });

  it("mentions and mentioned_by have the expected exact shape", () => {
    const ch = load("chapters/ch02-logarithmic-and-exponential-functions.json") as ChapterData;
    expect(Array.isArray(ch.mentions)).toBe(true);
    const m: Mention = ch.mentions[0];
    expect(m).toMatchObject({
      exercise_id: expect.any(String),
      from_block_id: expect.any(String),
      inferred: expect.any(Boolean),
      primary_mention: expect.any(Boolean),
      snippet: expect.any(String),
    });
    expect(m.question_number === null || typeof m.question_number === "number").toBe(true);
    // mentioned_by is an object of section-id -> array of exercise ids
    expect(typeof ch.mentioned_by).toBe("object");
    expect(Array.isArray(ch.mentioned_by)).toBe(false);
    // every section id referenced by a mention should exist as a section block
    const ids = new Set(ch.sections.map((s) => s.id));
    for (const mnt of ch.mentions) {
      if (mnt.from_block_id) expect(ids.has(mnt.from_block_id)).toBe(true);
    }
    // real mentions (non-inferred) are recorded in mentioned_by
    const ch6 = load("chapters/ch06-numerical-solutions-of-equations.json") as ChapterData;
    const real = ch6.mentions.filter((x) => !x.inferred);
    expect(real.length).toBeGreaterThan(0);
    expect(ch6.mentioned_by[real[0].from_block_id!]).toContain(real[0].exercise_id);
  });

  it("question -> answer linking follows the id rule", () => {
    const ch = load("chapters/ch02-logarithmic-and-exponential-functions.json") as ChapterData;
    for (const q of Object.values(ch.questions)) {
      if (q.answer_id) {
        expect(ch.answers[q.answer_id]).toBeDefined();
        expect(ch.answers[q.answer_id].question_id).toBe(q.id);
      }
    }
  });

  it("search index entries have id/chapter/title/text/type", () => {
    const s = load("search-index.json") as SearchEntry[];
    expect(s.length).toBeGreaterThan(0);
    for (const e of s) {
      expect(typeof e.id).toBe("string");
      expect(typeof e.chapter).toBe("number");
      expect(typeof e.title).toBe("string");
      expect(typeof e.text).toBe("string");
      expect(typeof e.type).toBe("string");
    }
  });

  it("stats.json mirrors the manifest counts", () => {
    const stats = load("stats.json") as Stats;
    for (const c of manifest.chapters) {
      const cs = stats.chapters[c.slug];
      expect(cs.questions).toBe(c.counts.questions);
      expect(cs.key_points).toBe(c.counts.key_points);
    }
  });

  it("all worked examples have a matching section block id", () => {
    for (const c of manifest.chapters) {
      const ch = load(`chapters/${c.slug}.json`) as ChapterData;
      const ids = new Set(ch.sections.map((s) => s.id));
      for (const we of ch.worked_examples) expect(ids.has(we.id)).toBe(true);
      for (const kp of ch.key_points) expect(ids.has(kp.id)).toBe(true);
    }
  });
});
