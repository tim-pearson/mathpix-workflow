import { useEffect } from "react";
import { useLocalStorage } from "./useLocalStorage";

export type ThemeMode = "light" | "dark" | "system";

const THEME_KEY = "tutex-theme";

/** Apply the resolved theme to <html> (also called by the inline script in
 * index.html before first paint). */
export function applyTheme(mode: ThemeMode): void {
  const dark =
    mode === "dark" ||
    (mode === "system" &&
      window.matchMedia("(prefers-color-scheme: dark)").matches);
  document.documentElement.classList.toggle("dark", dark);
  document.documentElement.style.colorScheme = dark ? "dark" : "light";
}

export function useTheme(): [ThemeMode, (m: ThemeMode) => void] {
  const [mode, setMode] = useLocalStorage<ThemeMode>(THEME_KEY, "system");

  useEffect(() => {
    applyTheme(mode);
    if (mode !== "system") return;
    const mq = window.matchMedia("(prefers-color-scheme: dark)");
    const on = () => applyTheme(mode);
    mq.addEventListener("change", on);
    return () => mq.removeEventListener("change", on);
  }, [mode]);

  return [mode, setMode];
}
