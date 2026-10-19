import { NavLink } from "react-router-dom";
import type { Manifest } from "../types";
import { SearchBox } from "./SearchBox";
import { ThemeToggle } from "./ThemeToggle";
import { IconBook, IconPencil } from "./Icons";

export interface TopBarProps {
  manifest: Manifest | null;
}

const navClass = ({ isActive }: { isActive: boolean }) =>
  "inline-flex items-center gap-1.5 rounded-md px-2.5 py-1.5 text-sm font-medium transition-colors " +
  (isActive
    ? "bg-accent-soft text-accent"
    : "text-muted hover:bg-line/40 hover:text-ink");

export function TopBar({ manifest }: TopBarProps) {
  return (
    <header className="sticky top-0 z-30 flex h-14 items-center gap-3 border-b border-line bg-paper/90 px-3 backdrop-blur sm:px-4">
      <NavLink to="/" className="flex items-center gap-2 font-semibold text-ink">
        <span className="grid h-7 w-7 place-items-center rounded-md bg-accent text-white">
          <IconBook aria-hidden="true" />
        </span>
        <span className="hidden text-sm md:inline">Pure Maths 2 &amp; 3</span>
      </NavLink>

      <nav aria-label="Mode" className="flex items-center gap-1 rounded-lg border border-line p-0.5">
        <NavLink to="/read/ch01" className={navClass}>
          <IconBook aria-hidden="true" /> Reader
        </NavLink>
        <NavLink to="/practice/ch01" className={navClass}>
          <IconPencil aria-hidden="true" /> Exercises
        </NavLink>
        <NavLink to="/stats" className={navClass}>
          Stats
        </NavLink>
      </nav>

      <div className="ml-auto flex items-center gap-2">
        <SearchBox manifest={manifest} className="w-44 sm:w-64" />
        <ThemeToggle />
      </div>
    </header>
  );
}

