import { beforeEach, describe, expect, it, vi } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { MemoryRouter } from "react-router-dom";
import { SearchBox } from "../src/components/SearchBox";
import type { SearchEntry } from "../src/types";

vi.mock("../src/data/load", () => ({
  loadSearchIndex: vi.fn(),
}));

import { loadSearchIndex } from "../src/data/load";

const entries: SearchEntry[] = [
  // note the duplicate id — as in the real export (section block + question)
  { id: "ch02-ex2E-q1", chapter: 2, title: "Question 1", text: "Solve 5^x = 18", type: "other" },
  { id: "ch02-ex2E-q1", chapter: 2, title: "Question 1", text: "Solve 5^x = 18", type: "question" },
  { id: "ch02-s-2.5", chapter: 2, title: "2.5 Solving exponential equations", text: "Solve using logs.", type: "section" },
];

function renderBox() {
  return render(
    <MemoryRouter>
      <SearchBox manifest={null} />
    </MemoryRouter>
  );
}

describe("SearchBox initialization", () => {
  beforeEach(() => {
    vi.mocked(loadSearchIndex).mockReset();
  });

  it("shows an accurate error when the index cannot be built/loaded", async () => {
    vi.mocked(loadSearchIndex).mockRejectedValueOnce(new Error("boom"));
    const user = userEvent.setup();
    renderBox();
    await user.type(screen.getByLabelText(/search/i), "solve");
    expect(
      await screen.findByText(/search is unavailable/i)
    ).toBeInTheDocument();
  });

  it("initialises successfully with duplicate ids and shows results", async () => {
    vi.mocked(loadSearchIndex).mockResolvedValueOnce(entries);
    const user = userEvent.setup();
    renderBox();
    await user.type(screen.getByLabelText(/search/i), "solve");
    await waitFor(() =>
      expect(screen.queryByText(/search is unavailable/i)).not.toBeInTheDocument()
    );
    const hits = await screen.findAllByText("Question 1");
    expect(hits.length).toBeGreaterThanOrEqual(1);
  });
});
