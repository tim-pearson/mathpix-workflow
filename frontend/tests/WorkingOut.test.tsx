import { describe, expect, it } from "vitest";
import { render, screen } from "@testing-library/react";
import { WorkingOut } from "../src/components/WorkingOut";

describe("WorkingOut visibility", () => {
  it("renders nothing when working_md is absent", () => {
    const { container } = render(<WorkingOut workingMd={undefined} questionId="ch02-ex2E-q1" />);
    expect(container.firstChild).toBeNull();
    expect(screen.queryByText("Working out")).toBeNull();
  });

  it("renders the disclosure when working_md exists", () => {
    render(<WorkingOut workingMd="Let $x=1$.\n\nThen $y=2$." questionId="ch02-ex2E-q1" />);
    expect(screen.getByText("Working out")).toBeInTheDocument();
  });

  it("is closed by default", () => {
    render(<WorkingOut workingMd="Working text here." questionId="q1" />);
    const details = document.querySelector("details");
    expect(details).not.toBeNull();
    expect(details!.hasAttribute("open")).toBe(false);
  });

  it("can default to open", () => {
    render(<WorkingOut workingMd="Working text here." questionId="q1" defaultOpen />);
    expect(document.querySelector("details")!.hasAttribute("open")).toBe(true);
  });
});
