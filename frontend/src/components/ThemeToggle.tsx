import { useTheme, type ThemeMode } from "../hooks/useTheme";
import { IconMonitor, IconMoon, IconSun } from "./Icons";

const OPTIONS: { value: ThemeMode; label: string; Icon: typeof IconSun }[] = [
  { value: "light", label: "Light", Icon: IconSun },
  { value: "dark", label: "Dark", Icon: IconMoon },
  { value: "system", label: "System", Icon: IconMonitor },
];

export function ThemeToggle() {
  const [mode, setMode] = useTheme();
  return (
    <div
      role="radiogroup"
      aria-label="Theme"
      className="flex items-center rounded-lg border border-line p-0.5"
    >
      {OPTIONS.map(({ value, label, Icon }) => (
        <button
          key={value}
          type="button"
          role="radio"
          aria-checked={mode === value}
          title={label}
          aria-label={label}
          onClick={() => setMode(value)}
          className={`inline-flex items-center gap-1 rounded-md px-2 py-1 text-xs transition-colors ${
            mode === value
              ? "bg-accent text-white dark:text-ink dark:bg-accent-soft"
              : "text-muted hover:text-ink"
          }`}
        >
          <Icon aria-hidden="true" />
          <span className="hidden sm:inline">{label}</span>
        </button>
      ))}
    </div>
  );
}
