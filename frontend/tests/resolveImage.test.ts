import { describe, expect, it } from "vitest";
import { resolveImage } from "../src/lib/resolveImage";

describe("resolveImage", () => {
  it("maps exporter `images/...` paths under data/images/", () => {
    expect(resolveImage("images/abc.jpg")).toBe("data/images/abc.jpg");
    expect(resolveImage("images/sub/a.png")).toBe("data/images/sub/a.png");
  });

  it("keeps already-resolved data/ paths", () => {
    expect(resolveImage("data/images/abc.jpg")).toBe("data/images/abc.jpg");
    expect(resolveImage("./data/images/abc.jpg")).toBe("data/images/abc.jpg");
  });

  it("keeps absolute, protocol-relative and data/blob urls", () => {
    expect(resolveImage("https://example.com/a.jpg")).toBe("https://example.com/a.jpg");
    expect(resolveImage("//cdn.example.com/a.jpg")).toBe("//cdn.example.com/a.jpg");
    expect(resolveImage("/abs/a.jpg")).toBe("/abs/a.jpg");
    expect(resolveImage("data:image/png;base64,AAAA")).toBe("data:image/png;base64,AAAA");
    expect(resolveImage("blob:http://x")).toBe("blob:http://x");
  });

  it("handles empty / undefined", () => {
    expect(resolveImage("")).toBe("");
    expect(resolveImage(undefined)).toBe("");
    expect(resolveImage(null)).toBe("");
  });
});
