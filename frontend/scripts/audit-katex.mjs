#!/usr/bin/env node
// KaTeX compatibility audit across ALL chapters.
//
// Loads the real exported JSON (frontend-data/), extracts inline $...$ and
// display $$...$$ maths from question, answer, section, worked-example,
// key-point and formula markdown, and renders each expression with KaTeX
// throwOnError:true.  Reports every block whose markdown contains a KaTeX
// error, plus the first error message, and distinguishes genuine KaTeX
// incompatibilities from preprocessor concerns.
import { readFileSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import katex from "katex";

const root = dirname(fileURLToPath(import.meta.url));
const dataDir = join(root, "..", "public", "data");
const chaptersDir = join(dataDir, "chapters");

// --- markdown maths extraction -------------------------------------------
// Display blocks first ($$...$$, may span lines), then inline $...$ per line.
function extractMath(md) {
  const out = [];
  let rest = md;
  const displayRe = /\$\$([\s\S]*?)\$\$/g;
  let m;
  const inlineParts = [];
  let last = 0;
  displayRe.lastIndex = 0;
  while ((m = displayRe.exec(rest)) !== null) {
    inlineParts.push(rest.slice(last, m.index));
    out.push({ tex: m[1], display: true });
    last = displayRe.lastIndex;
  }
  inlineParts.push(rest.slice(last));
  const inlineRe = /(?<!\\)\$([^$\n]*?)\$/g;
  for (const part of inlineParts) {
    let mm;
    inlineRe.lastIndex = 0;
    while ((mm = inlineRe.exec(part)) !== null) {
      const tex = mm[1].trim();
      if (tex) out.push({ tex, display: false });
    }
  }
  return out;
}

// --- gather blocks -------------------------------------------------------
const blocks = [];
for (const file of readdirSync(chaptersDir)) {
  const ch = JSON.parse(readFileSync(join(chaptersDir, file), "utf-8"));
  const add = (id, md, kind) => {
    if (md) blocks.push({ id, md, kind });
  };
  for (const s of ch.sections) add(s.id, s.md, "section");
  for (const [qid, q] of Object.entries(ch.questions)) add(qid, q.md, "question");
  for (const [aid, a] of Object.entries(ch.answers)) add(aid, a.md, "answer");
  for (const kp of ch.key_points) add(kp.id, kp.md, "key-point");
  for (const we of ch.worked_examples) {
    add(we.id, we.question_md, "worked-example");
    if (we.answer_md) add(`${we.id}#ans`, we.answer_md, "worked-example");
  }
  for (const f of ch.formulas) add(f.id, f.md, "formula");
}

// --- audit ---------------------------------------------------------------
let blocksChecked = 0;
let expressions = 0;
const failures = []; // {id, kind, tex, error}
for (const b of blocks) {
  blocksChecked += 1;
  for (const { tex, display } of extractMath(b.md)) {
    expressions += 1;
    try {
      katex.renderToString(tex, {
        throwOnError: true,
        displayMode: display,
        strict: false,
      });
    } catch (e) {
      failures.push({
        id: b.id,
        kind: b.kind,
        tex: tex.slice(0, 120),
        error: String(e.message || e),
      });
    }
  }
}

const byId = new Map();
for (const f of failures) {
  if (!byId.has(f.id)) byId.set(f.id, []);
  byId.get(f.id).push(f);
}

console.log(`blocks checked: ${blocksChecked}`);
console.log(`math expressions checked: ${expressions}`);
console.log(`blocks with KaTeX errors: ${byId.size}`);
for (const [id, list] of [...byId.entries()].sort()) {
  console.log(`  ${id}  (${list[0].kind})`);
  console.log(`      first: ${list[0].error}`);
  console.log(`      tex:   ${JSON.stringify(list[0].tex)}`);
  if (list.length > 1) console.log(`      (+${list.length - 1} more expressions)`);
}

// Summary of distinct error messages (helps classify genuine vs preprocessing).
const msgCount = new Map();
for (const f of failures) {
  const key = f.error.split("\n")[0].slice(0, 90);
  msgCount.set(key, (msgCount.get(key) || 0) + 1);
}
console.log("\nerror message histogram:");
for (const [msg, n] of [...msgCount.entries()].sort((a, b) => b[1] - a[1])) {
  console.log(`  ${n}x  ${msg}`);
}

if (failures.length === 0) {
  console.log("\nAUDIT OK: no KaTeX errors.");
  process.exit(0);
} else {
  console.log(`\nAUDIT FAILED: ${failures.length} expressions in ${byId.size} blocks.`);
  process.exit(1);
}
