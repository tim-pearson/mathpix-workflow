#!/usr/bin/env node
// Copy ../frontend-data/* into ./public/data/ (nested dirs included).
// Only rewrites files whose content changed.  Never writes into frontend-data/.
import { copyFileSync, mkdirSync, readFileSync, readdirSync, rmSync, statSync } from "node:fs";
import { dirname, join, relative, sep } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(fileURLToPath(import.meta.url)); // .../frontend/scripts
const src = join(root, "..", "..", "frontend-data");
const dst = join(root, "..", "public", "data");

function walk(dir) {
  const out = [];
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) out.push(...walk(p));
    else out.push(p);
  }
  return out;
}

if (!statSync(src).isDirectory()) {
  console.error(`sync-data: source not found: ${src}`);
  process.exit(1);
}

const files = walk(src).map((p) => relative(src, p).split(sep).join("/"));
mkdirSync(dst, { recursive: true });

let written = 0;
let unchanged = 0;
for (const rel of files) {
  const from = join(src, rel);
  const to = join(dst, rel);
  mkdirSync(dirname(to), { recursive: true });
  const same =
    statSync(to, { throwIfNoEntry: false })?.isFile() &&
    readFileSync(from).equals(readFileSync(to));
  if (!same) {
    copyFileSync(from, to);
    written += 1;
  } else {
    unchanged += 1;
  }
}

// Remove stale files in public/data that are no longer in frontend-data.
const existing = walk(dst).map((p) => relative(dst, p).split(sep).join("/"));
for (const rel of existing) {
  if (!files.includes(rel)) rmSync(join(dst, rel));
}

console.log(
  `sync-data: ${written} copied, ${unchanged} unchanged, ${files.length} total -> public/data/`
);
