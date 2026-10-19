import { describe, expect, it } from "vitest";
import { buildClipboardText } from "../src/lib/clipboard";

const Q = "Solve $x^2=4$.\n\n**a** $x=2$\n\n**b** $x=-2$";
const A = "**a** $2$\n\n**b** $-2$";
const W = "Take logs.\n\n$$x=2$$";

describe("buildClipboardText (single copy button)", () => {
  it("copies the question when nothing else exists", () => {
    expect(
      buildClipboardText({ questionMd: Q, includeId: false })
    ).toBe(Q);
  });

  it("appends the answer when present", () => {
    expect(
      buildClipboardText({ questionMd: Q, answerMd: A, includeId: false })
    ).toBe(`${Q}\n\nAnswer:\n${A}`);
  });

  it("appends the working-out after the answer when present", () => {
    expect(
      buildClipboardText({ questionMd: Q, answerMd: A, workingMd: W, includeId: false })
    ).toBe(`${Q}\n\nAnswer:\n${A}\n\nWorking out:\n${W}`);
  });

  it("includes the working-out even without an answer", () => {
    expect(
      buildClipboardText({ questionMd: Q, workingMd: W, includeId: false })
    ).toBe(`${Q}\n\nWorking out:\n${W}`);
  });

  it("prepends the id when includeId is on", () => {
    expect(
      buildClipboardText({
        questionMd: Q,
        answerMd: A,
        workingMd: W,
        includeId: true,
        id: "ch02-ex2E-q1",
      })
    ).toBe(`ch02-ex2E-q1\n\n${Q}\n\nAnswer:\n${A}\n\nWorking out:\n${W}`);
  });

  it("ignores empty answer/working sections", () => {
    expect(
      buildClipboardText({ questionMd: Q, answerMd: "   ", workingMd: "", includeId: false })
    ).toBe(Q);
  });
});