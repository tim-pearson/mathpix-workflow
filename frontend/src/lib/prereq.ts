import type { Question } from "../types";

export interface ParsedPrereqQuestion {
  id: string;
  number: number;
  label: string;
  block: string;
  md: string;
  parts: string[];
  marks: number[];
  answer_id: string | null;
}

const NUMBER_RE = /^\s*(\d{1,2})\s+(.*)$/;
const PART_RE = /^\s*([a-z])\s+(.*)$/;

/**
 * PREREQUISITE KNOWLEDGE questions are embedded in a table on the chapter
 * side (the "Check your skills" column), not as separate question blocks, so
 * `exercise.questions` is empty for them.  This parses the real table from
 * the exercise block's markdown into Question-like cards, linking each to the
 * existing `chNN-ans-prerequisite-qN` answer when one exists.
 */
export function parsePrerequisiteQuestions(
  blockMd: string,
  exerciseId: string
): ParsedPrereqQuestion[] {
  const rows = blockMd
    .split("\n")
    .filter((l) => l.trimStart().startsWith("|"))
    .map((r) =>
      r
        .split("|")
        .map((c) => c.trim())
        .filter(Boolean)
    );

  const collected: { number: number; lines: string[] }[] = [];
  for (const row of rows) {
    if (row.length < 3) continue;
    const skill = row[row.length - 1];
    if (!skill || skill.startsWith(":--") || /Check your skills|Where it comes from/i.test(skill))
      continue;
    const text = skill
      .replace(/<br\s*\/?>/gi, "\n")
      .replace(/&#160;/g, " ")
      .replace(/&nbsp;/g, " ");
    let cur: { number: number; lines: string[] } | null = null;
    for (const raw of text.split("\n")) {
      const line = raw.trim();
      if (!line) continue;
      const num = line.match(NUMBER_RE);
      if (num) {
        cur = { number: parseInt(num[1], 10), lines: [num[2].trim()] };
        collected.push(cur);
        continue;
      }
      const part = line.match(PART_RE);
      if (part && cur) {
        cur.lines.push(`**${part[1]}** ${part[2].trim()}`);
        continue;
      }
      if (cur) cur.lines.push(line);
    }
  }

  const ansBase = exerciseId.replace(/^(ch\d\d)-/, "$1-ans-");
  return collected.map((q) => {
    const parts = q.lines
      .map((l) => l.match(/^\*\*([a-z])\*\*/)?.[1])
      .filter((p): p is string => Boolean(p));
    const marks = q.lines
      .map((l) => l.match(/`?\[(\d{1,2})\]`?\s*$/)?.[1])
      .filter((x): x is string => Boolean(x))
      .map(Number);
    return {
      id: `${exerciseId}-q${q.number}`,
      number: q.number,
      label: `Question ${q.number}`,
      block: exerciseId,
      md: q.lines.join("\n\n"),
      parts,
      marks,
      answer_id: `${ansBase}-q${q.number}`,
    };
  });
}

/** Number of questions an exercise shows, resolving prerequisites from the
 * table when the exercise has no question ids. */
export function exerciseQuestionCount(
  chapter: { sections: { id: string; md: string }[] },
  exercise: { id: string; kind: string; questions: string[] }
): number {
  if (exercise.questions.length > 0) return exercise.questions.length;
  if (exercise.kind === "prerequisite") {
    const block = chapter.sections.find((s) => s.id === exercise.id);
    if (block) return parsePrerequisiteQuestions(block.md, exercise.id).length;
  }
  return 0;
}

export type { Question };
