import type { ChapterData, Exercise, SectionBlock } from "../types";

/** Numbered sections of the chapter (reader TOC). */
export function numberedSections(ch: ChapterData): SectionBlock[] {
  return ch.sections.filter((b) => b.type === "section" && b.level === 2);
}

/** The chapter-intro block (level 1), if any. */
export function introSection(ch: ChapterData): SectionBlock | undefined {
  return ch.sections.find((b) => b.type === "section" && b.level === 1);
}

export function sectionById(ch: ChapterData, id: string): SectionBlock | undefined {
  return ch.sections.find((b) => b.id === id);
}

export function sectionTitle(ch: ChapterData, id: string | null | undefined): string {
  if (!id) return "";
  const b = sectionById(ch, id);
  if (!b) return "";
  // strip leading hashes from the heading
  return b.heading.replace(/^#+\s*/, "");
}

/** The textbook section an exercise belongs to (from its mention, preferring
 * a real mention over the inferred fallback). */
export function exerciseSectionId(ch: ChapterData, exerciseId: string): string | null {
  const mentions = ch.mentions.filter((m) => m.exercise_id === exerciseId);
  const real = mentions.find((m) => !m.inferred);
  const any = mentions[0];
  const id = real?.from_block_id ?? any?.from_block_id ?? null;
  return id;
}

/** Exercises to offer as "Practise" links for a given section block id. */
export function practiceLinksForSection(
  ch: ChapterData,
  sectionId: string
): Exercise[] {
  const ids = new Set<string>(ch.mentioned_by[sectionId] ?? []);
  for (const m of ch.mentions) {
    if (m.from_block_id === sectionId) ids.add(m.exercise_id);
  }
  const byId = new Map(ch.exercises.map((e) => [e.id, e]));
  return [...ids]
    .map((id) => byId.get(id))
    .filter((e): e is Exercise => Boolean(e));
}

/** Display title for an exercise id, e.g. "EXERCISE 2E". */
export function exerciseTitle(ch: ChapterData, exerciseId: string): string {
  const e = ch.exercises.find((x) => x.id === exerciseId);
  return e?.title ?? exerciseId;
}

/** True when the worked-example / key-point entry corresponds to the section
 * block (i.e. the block's markdown contains the entry's markdown), so we can
 * render the split form without duplicating or inventing content. */
export function blockMatchesEntry(
  blockMd: string,
  entryMd: string | null | undefined
): boolean {
  if (!entryMd) return true;
  return blockMd.includes(entryMd);
}
