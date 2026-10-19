import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";
import { parsePrerequisiteQuestions } from "../src/lib/prereq";

const SAMPLE = `<a id="ch02-prerequisite"></a>
### PREREQUISITE KNOWLEDGE

| Where it comes from | What you should be able to do | Check your skills |
| :--- | :--- | :--- |
| IGCSE / O Level Mathematics | Use and interpret positive, negative, fractional and zero indices. | 1 Evaluate.<br>&#160;&#160;a $5^{-2}$<br>&#160;&#160;b $8^{\\frac{2}{3}}$<br>&#160;&#160;c $7^{0}$<br>2 Solve $32^{x}=2$.<br> |
| IGCSE / O Level Mathematics | Use the rules of indices. | 3 Simplify.<br>&#160;&#160;a $3 x^{-4}$<br>&#160;&#160;b $\\frac{2}{5} x^{\\frac{1}{2}}$<br> |
`;

describe("parsePrerequisiteQuestions", () => {
  it("parses questions and parts from the table", () => {
    const qs = parsePrerequisiteQuestions(SAMPLE, "ch02-prerequisite");
    expect(qs.length).toBe(3);
    expect(qs.map((q) => q.number)).toEqual([1, 2, 3]);
    expect(qs[0].label).toBe("Question 1");
    expect(qs[0].parts).toEqual(["a", "b", "c"]);
    expect(qs[0].md).toContain("**a** $5^{-2}$");
    expect(qs[0].md).toContain("**c** $7^{0}$");
    expect(qs[1].md).toContain("Solve $32^{x}=2$.");
    expect(qs[2].parts).toEqual(["a", "b"]);
  });

  it("builds linkable ids and answer ids", () => {
    const qs = parsePrerequisiteQuestions(SAMPLE, "ch02-prerequisite");
    expect(qs[0].id).toBe("ch02-prerequisite-q1");
    expect(qs[0].answer_id).toBe("ch02-ans-prerequisite-q1");
  });

  it("returns an empty array for non-table markdown", () => {
    expect(parsePrerequisiteQuestions("Just some prose.", "ch02-prerequisite")).toEqual([]);
  });

  it("parses the real exported chapter 2 prerequisite table", () => {
    const path = resolve(process.cwd(), "public", "data", "chapters", "ch02-logarithmic-and-exponential-functions.json");
    const ch = JSON.parse(readFileSync(path, "utf-8"));
    const block = ch.sections.find((s: { id: string }) => s.id === "ch02-prerequisite");
    const qs = parsePrerequisiteQuestions(block.md, "ch02-prerequisite");
    expect(qs.length).toBeGreaterThanOrEqual(3);
    expect(qs.map((q) => q.number)).toEqual([1, 2, 3]);
    // every parsed question can be answered from the exported answers
    for (const q of qs) {
      expect(ch.answers[q.answer_id!]).toBeDefined();
    }
  });
});
