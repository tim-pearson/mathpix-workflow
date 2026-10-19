import { describe, expect, it } from "vitest";
import { buildClipboardText } from "../src/lib/clipboard";

const Q = "Solve $x^2=4$.\n\n**a** $x=2$\n\n**b** $x=-2$";
const A = "**a** $2$\n\n**b** $-2$";

describe("buildClipboardText", () => {
  it("copies raw question markdown", () => {
    expect(
      buildClipboardText({ mode: "question", questionMd: Q, answerMd: A, includeId: false })
    ).toBe(Q);
  });

  it("copies raw answer markdown", () => {
    expect(
      buildClipboardText({ mode: "answer", questionMd: Q, answerMd: A, includeId: false })
    ).toBe(A);
  });

  it("copies both: question, blank line, Answer:, answer", () => {
    const both = buildClipboardText({ mode: "both", questionMd: Q, answerMd: A, includeId: false });
    expect(both).toBe(`${Q}\n\nAnswer:\n${A}`);
  });

  it("prepends the id when includeId is on", () => {
    const t = buildClipboardText({
      mode: "question",
      questionMd: Q,
      answerMd: A,
      includeId: true,
      id: "ch02-ex2E-q1",
    });
    expect(t).toBe(`ch02-ex2E-q1\n\n${Q}`);
  });

  it("both with includeId keeps id first", () => {
    const t = buildClipboardText({
      mode: "both",
      questionMd: Q,
      answerMd: A,
      includeId: true,
      id: "ch02-ex2E-q1",
    });
    expect(t).toBe(`ch02-ex2E-q1\n\n${Q}\n\nAnswer:\n${A}`);
  });

  it("handles a missing answer", () => {
    expect(
      buildClipboardText({ mode: "both", questionMd: Q, answerMd: null, includeId: false })
    ).toBe(`${Q}\n\nAnswer:\n`);
  });
});
