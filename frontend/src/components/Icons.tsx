import type { SVGProps } from "react";

const base = {
  fill: "none",
  stroke: "currentColor",
  strokeWidth: 2,
  strokeLinecap: "round",
  strokeLinejoin: "round",
} as const;

type P = SVGProps<SVGSVGElement>;

export const IconCopy = (p: P) => (
  <svg viewBox="0 0 24 24" width="1em" height="1em" {...base} {...p}>
    <rect x="9" y="9" width="13" height="13" rx="2" ry="2" />
    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" />
  </svg>
);

export const IconCheck = (p: P) => (
  <svg viewBox="0 0 24 24" width="1em" height="1em" {...base} {...p}>
    <polyline points="20 6 9 17 4 12" />
  </svg>
);

export const IconSun = (p: P) => (
  <svg viewBox="0 0 24 24" width="1em" height="1em" {...base} {...p}>
    <circle cx="12" cy="12" r="5" />
    <line x1="12" y1="1" x2="12" y2="3" />
    <line x1="12" y1="21" x2="12" y2="23" />
    <line x1="4.2" y1="4.2" x2="5.6" y2="5.6" />
    <line x1="18.4" y1="18.4" x2="19.8" y2="19.8" />
    <line x1="1" y1="12" x2="3" y2="12" />
    <line x1="21" y1="12" x2="23" y2="12" />
    <line x1="4.2" y1="19.8" x2="5.6" y2="18.4" />
    <line x1="18.4" y1="5.6" x2="19.8" y2="4.2" />
  </svg>
);

export const IconMoon = (p: P) => (
  <svg viewBox="0 0 24 24" width="1em" height="1em" {...base} {...p}>
    <path d="M21 12.8A9 9 0 1 1 11.2 3 7 7 0 0 0 21 12.8z" />
  </svg>
);

export const IconMonitor = (p: P) => (
  <svg viewBox="0 0 24 24" width="1em" height="1em" {...base} {...p}>
    <rect x="2" y="3" width="20" height="14" rx="2" ry="2" />
    <line x1="8" y1="21" x2="16" y2="21" />
    <line x1="12" y1="17" x2="12" y2="21" />
  </svg>
);

export const IconSearch = (p: P) => (
  <svg viewBox="0 0 24 24" width="1em" height="1em" {...base} {...p}>
    <circle cx="11" cy="11" r="8" />
    <line x1="21" y1="21" x2="16.65" y2="16.65" />
  </svg>
);

export const IconMenu = (p: P) => (
  <svg viewBox="0 0 24 24" width="1em" height="1em" {...base} {...p}>
    <line x1="3" y1="6" x2="21" y2="6" />
    <line x1="3" y1="12" x2="21" y2="12" />
    <line x1="3" y1="18" x2="21" y2="18" />
  </svg>
);

export const IconBook = (p: P) => (
  <svg viewBox="0 0 24 24" width="1em" height="1em" {...base} {...p}>
    <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
    <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
  </svg>
);

export const IconPencil = (p: P) => (
  <svg viewBox="0 0 24 24" width="1em" height="1em" {...base} {...p}>
    <path d="M17 3a2.85 2.83 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5Z" />
  </svg>
);

export const IconCalculator = (p: P) => (
  <svg viewBox="0 0 24 24" width="1em" height="1em" {...base} {...p}>
    <rect x="4" y="2" width="16" height="20" rx="2" />
    <line x1="8" y1="6" x2="16" y2="6" />
    <line x1="8" y1="11" x2="8" y2="11.01" />
    <line x1="12" y1="11" x2="12" y2="11.01" />
    <line x1="16" y1="11" x2="16" y2="11.01" />
    <line x1="8" y1="15" x2="8" y2="15.01" />
    <line x1="12" y1="15" x2="12" y2="15.01" />
    <line x1="16" y1="15" x2="16" y2="15.01" />
    <line x1="8" y1="19" x2="8" y2="19.01" />
    <line x1="12" y1="19" x2="12" y2="19.01" />
    <line x1="16" y1="19" x2="16" y2="19.01" />
  </svg>
);

export const IconChevronRight = (p: P) => (
  <svg viewBox="0 0 24 24" width="1em" height="1em" {...base} {...p}>
    <polyline points="9 18 15 12 9 6" />
  </svg>
);

export const IconChevronDown = (p: P) => (
  <svg viewBox="0 0 24 24" width="1em" height="1em" {...base} {...p}>
    <polyline points="6 9 12 15 18 9" />
  </svg>
);

export const IconLightbulb = (p: P) => (
  <svg viewBox="0 0 24 24" width="1em" height="1em" {...base} {...p}>
    <path d="M9 18h6M10 22h4M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.4 1 2.3h6c0-.9.4-1.8 1-2.3A7 7 0 0 0 12 2z" />
  </svg>
);

export const IconInfo = (p: P) => (
  <svg viewBox="0 0 24 24" width="1em" height="1em" {...base} {...p}>
    <circle cx="12" cy="12" r="10" />
    <line x1="12" y1="16" x2="12" y2="12" />
    <line x1="12" y1="8" x2="12.01" y2="8" />
  </svg>
);

export const IconRefresh = (p: P) => (
  <svg viewBox="0 0 24 24" width="1em" height="1em" {...base} {...p}>
    <polyline points="23 4 23 10 17 10" />
    <path d="M20.5 15a9 9 0 1 1-2-9.4L23 10" />
  </svg>
);
