// Types derived from the actual JSON in frontend-data/ (see the structural
// report in tests/data-shapes.test.ts and README).  Do not invent fields:
// every interface below corresponds to a key observed in the exported data.

export interface ManifestCounts {
  answers: number;
  exercises: number;
  key_points: number;
  linked_answers: number;
  questions: number;
  worked_examples: number;
}

export interface ManifestChapter {
  chapter: number;
  counts: ManifestCounts;
  slug: string;
  title: string;
}

export interface NonChapterFile {
  file: string;
  title: string;
  type: string;
}

export interface Manifest {
  book: string;
  chapters: ManifestChapter[];
  non_chapter_files: NonChapterFile[];
  schema_version: number;
}

/** Section block type as emitted by export_data.py. */
export type SectionType =
  | "section"
  | "worked-example"
  | "key-point"
  | "explore"
  | "did-you-know"
  | "rewind"
  | "fast-forward"
  | "exercise"
  | "other";

export interface SectionBlock {
  heading: string;
  id: string;
  level: number;
  md: string;
  title: string;
  type: SectionType;
}

export type ExerciseKind = "exercise" | "review" | "cross" | "prerequisite";

export interface Exercise {
  id: string;
  kind: ExerciseKind;
  questions: string[];
  title: string;
}

export interface Question {
  answer_id: string | null;
  block: string;
  id: string;
  label: string;
  marks: number[];
  md: string;
  number: number;
  parts: string[];
  /** Present only when a working/<question-id>.md file existed at export. */
  working_md?: string;
}

export interface Answer {
  id: string;
  md: string;
  question_id: string | null;
}

export interface KeyPoint {
  id: string;
  md: string;
  number: string;
  section_id: string;
}

export interface WorkedExample {
  answer_md: string | null;
  id: string;
  number: string;
  question_md: string;
  section_id: string;
}

export interface Formula {
  id: string;
  md: string;
  title: string;
}

export interface Mention {
  exercise_id: string;
  from_block_id: string | null;
  inferred: boolean;
  primary_mention: boolean;
  question_number: number | null;
  snippet: string;
}

/** Reverse map: section block id -> exercise ids it mentions. */
export type MentionedBy = Record<string, string[]>;

export interface ChapterData {
  answers: Record<string, Answer>;
  chapter: number;
  counts: ManifestCounts;
  exercises: Exercise[];
  formulas: Formula[];
  key_points: KeyPoint[];
  mentioned_by: MentionedBy;
  mentions: Mention[];
  questions: Record<string, Question>;
  sections: SectionBlock[];
  slug: string;
  title: string;
  worked_examples: WorkedExample[];
}

export type SearchEntryType =
  | "answer"
  | "other"
  | "question"
  | "worked-example"
  | "section"
  | "key-point"
  | "exercise"
  | "explore"
  | "did-you-know"
  | "rewind"
  | "fast-forward";

export interface SearchEntry {
  chapter: number;
  id: string;
  text: string;
  title: string;
  type: SearchEntryType;
}

export interface ChapterStats {
  answers: number;
  chapter: number;
  exercises: number;
  key_points: number;
  linked_answers: number;
  orphan_answers: string[];
  questions: number;
  title: string;
  unlinked_questions: string[];
  worked_examples: number;
}

export interface Stats {
  chapters: Record<string, ChapterStats>;
  schema_version: number;
  totals: ManifestCounts;
}
