import katex from "katex";

// Shared KaTeX options used by the Markdown renderer.  KaTeX errors are shown
// inline in the error colour (never thrown), trust is off, and macros is an
// empty object ready for future extensions.
export const KATEX_OPTIONS: katex.KatexOptions = {
  throwOnError: false,
  errorColor: "#e11d48",
  trust: false,
  macros: {},
  strict: false,
};
