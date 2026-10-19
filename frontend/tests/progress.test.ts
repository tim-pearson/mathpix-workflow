import { afterEach, describe, expect, it, vi } from "vitest";
import type { ProgressEntry } from "../src/types";
import {
  chapterProgress,
  clearProgress,
  loadProgress,
  saveStatus,
} from "../src/lib/progress";

const entries = (m: Record<string, "green" | "yellow" | "red">) => {
  const out: Record<string, ProgressEntry> = {};
  for (const [id, status] of Object.entries(m)) {
    out[id] = { status, updated_at: "2026-01-01T00:00:00+00:00" };
  }
  return out;
};

afterEach(() => vi.unstubAllGlobals());

describe("chapterProgress", () => {
  it("counts statuses and excludes unattempted from the counts", () => {
    const s = entries({
      "ch02-ex2E-q1": "green",
      "ch02-ex2E-q2": "yellow",
      "ch02-ex2E-q3": "red",
      "ch02-ex2E-q4": "green",
    });
    const q = ["ch02-ex2E-q1", "ch02-ex2E-q2", "ch02-ex2E-q3",
               "ch02-ex2E-q4", "ch02-ex2E-q5"];
    // mastery = (3*2 + 2*1 + 1*1) / (5 * 3) = 9/15 = 60%
    expect(chapterProgress(s, q)).toEqual({
      attempted: 4, green: 2, yellow: 1, red: 1, mastery: 60,
    });
  });

  it("mastery is red=1, yellow=2, green=3 over ALL questions", () => {
    // 2 questions, one unattempted (counts as 0)
    expect(chapterProgress(entries({ a: "green" }), ["a", "b"]).mastery).toBe(50);
    expect(chapterProgress(entries({ a: "yellow" }), ["a", "b"]).mastery)
      .toBeCloseTo(100 / 3);
    expect(chapterProgress(entries({ a: "red" }), ["a", "b"]).mastery)
      .toBeCloseTo(100 / 6);
    // all green -> 100%
    expect(chapterProgress(entries({ a: "green", b: "green" }), ["a", "b"]).mastery)
      .toBe(100);
    // empty chapter -> 0 (avoids 0/0)
    expect(chapterProgress({}, []).mastery).toBe(0);
  });

  it("returns zeros when nothing is attempted", () => {
    expect(chapterProgress({}, ["a", "b"])).toEqual({
      attempted: 0, green: 0, yellow: 0, red: 0, mastery: 0,
    });
  });
});

describe("progress API client", () => {
  it("loadProgress returns the status map", async () => {
    const payload = entries({ "ch01-ex1A-q1": "green" });
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({
      ok: true, status: 200, json: async () => payload,
    }));
    await expect(loadProgress()).resolves.toEqual(payload);
    expect(fetch).toHaveBeenCalledWith("/api/progress/questions");
  });

  it("saveStatus PUTs the status", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({ ok: true, status: 200 }));
    await saveStatus("ch01-ex1A-q1", "yellow");
    expect(fetch).toHaveBeenCalledWith(
      "/api/progress/ch01-ex1A-q1",
      expect.objectContaining({
        method: "PUT",
        body: JSON.stringify({ status: "yellow" }),
      })
    );
  });

  it("clearProgress DELETEs the record", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({ ok: true, status: 204 }));
    await clearProgress("ch01-ex1A-q1");
    expect(fetch).toHaveBeenCalledWith(
      "/api/progress/ch01-ex1A-q1",
      expect.objectContaining({ method: "DELETE" })
    );
  });
});
