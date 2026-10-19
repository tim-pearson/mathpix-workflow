#!/usr/bin/env python3
"""Export split/ + images/ into frontend-data/ for the new React frontend.

The React frontend (KaTeX, one shared renderer for reader mode and exercise
mode) does not read split/ directly.  This script is its ONLY reader: it
produces a self-contained, deterministic data bundle under frontend-data/
that is regenerated from scratch on every run.

Outputs (all under frontend-data/):
  manifest.json          chapters + non-chapter files + schema version
  chapters/chNN.json     per chapter: sections, exercises, questions,
                         answers, key_points, worked_examples, formulas,
                         mentions (PART 1 + PART 2)
  images/                copy of images/, only when changed (hash compare);
                         ../images/ links are rewritten to images/...
  search-index.json      every searchable item with maths stripped to text
  stats.json             per-chapter counts + unlinked id lists

Optional working/ directory (PART 3): `<question id>.md` files become
questions[id].working_md.  working/README.md and a .sample are also written.

Invariants:
  * never modifies split/, images/ or any other script;
  * standard library only;
  * idempotent and byte-identical on re-run (sorted keys, stable ordering,
    indent=1).  No timestamps anywhere.
  * no text is lost: the concatenated section block md reproduces the
    normalised chapter (asserted per chapter).

Usage:  python scripts/export_data.py [book_dir] [--out OUT] [--working DIR]
"""
import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import math_normalize as mn

BOOK_DEFAULT = Path("Maths Pure 2 & 3-clean_MD")
OUT_DEFAULT = Path("frontend-data")
WORKING_DEFAULT = Path("working")
SCHEMA_VERSION = 1
IMG_BASE = "images"                       # ../images/ links are rewritten to this

ANCHOR_RE = re.compile(r'^<a id="([^"]+)"></a>$')
EMPTY_H = re.compile(r"^#{1,6}\s*$")
H_RE = re.compile(r"^(#{1,6})\s*(.*)$")
SEC_RE = re.compile(r"^##\s+(\d+(?:\.\d+)+)(.*)$")
KP_RE = re.compile(r"^####\s+KEY POINT\s+(\d+\.\d+)\s*$", re.I)
WE_RE = re.compile(r"^####\s+WORKED EXAMPLE\s+(\d+\.\d+)\s*$", re.I)
EXPLORE_RE = re.compile(r"^####\s+EXPLORE\s+(\d+\.\d+)\s*$", re.I)
DYK_RE = re.compile(r"^####\s+(?:i\)\s*)?DID\s+YOU\s+KNOW\??\s*$", re.I)
REWIND_RE = re.compile(r"^####\s+REWIND\s*$", re.I)
FF_RE = re.compile(r"^####\s+FAST FORWARD\s*$", re.I)
TIP_RE = re.compile(r"^####\s+TIP\s*$", re.I)
EX_RE = re.compile(r"^###\s+EXERCISE\s+(\d+)([A-Z])\s*$", re.I)
REVIEW_RE = re.compile(r"^###\s+END-OF-CHAPTER REVIEW EXERCISE\s+(\d+)\s*$",
                       re.I)
CROSS_RE = re.compile(r"^###\s+CROSS-TOPIC REVIEW EXERCISE\s+(\d+)\s*$",
                      re.I)
PREREQ_RE = re.compile(r"^###\s+PREREQUISITE KNOWLEDGE\s*$", re.I)
QH_RE = re.compile(r"^#####\s+Question(?:\s+(PS|P|M))?\s+(\d+)\s*$", re.I)
ANSWER_LINE = re.compile(r"^Answer\s*$")
IMG_RE = re.compile(r"!\[([^\]]*)\]\([^)]*\)")
QID_RE = re.compile(r"^(ch\d\d)-(.+?)-(?:q|ps|p|m)(\d+)$")
ROMAN = {"i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5, "vi": 6, "vii": 7,
         "viii": 8, "ix": 9, "x": 10, "xi": 11, "xii": 12, "xiii": 13,
         "xiv": 14, "xv": 15, "xvi": 16, "xvii": 17, "xviii": 18,
         "xix": 19, "xx": 20}


def finalize(text):
    """Shared katex normalisation + the single consistent image-link base."""
    return mn.normalise(text, "katex").replace("../images/", IMG_BASE + "/")


def strip_inline_math(line):
    out = list(line)
    for s, e, inner in reversed(mn._inline_spans(line)):
        out[s:e] = list(mn.math_to_plain(inner))
    return "".join(out)


def plain_text(md):
    """Maths stripped to plain readable text (for search + mention snippets)."""
    out = []
    in_block = False
    for line in md.split("\n"):
        s = line
        if ANCHOR_RE.match(s.strip()):
            continue
        if re.match(r"^\s*\$\$\s*$", s):
            in_block = not in_block
            continue
        if in_block:
            out.append(mn.math_to_plain(s))
            continue
        s = IMG_RE.sub(lambda m: (m.group(1) or "").strip(), s)
        if s.lstrip().startswith("#"):
            s = re.sub(r"^#{1,6}\s*", "", s)
        s = strip_inline_math(s)
        s = s.replace("**", " ")
        s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
        s = re.sub(r"<br\s*/?>", " ", s, flags=re.I)
        s = s.replace("&nbsp;", " ").replace("&#160;", " ")
        s = s.replace("|", " ").replace("`", "")
        out.append(s)
    return re.sub(r"\s+", " ", " ".join(out)).strip()


def heading_title(line):
    s = re.sub(r"^#{1,6}\s*", "", line)
    return strip_inline_math(s).strip()


def trim_lines(lines):
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    j = len(lines)
    while j > i and not lines[j - 1].strip():
        j -= 1
    return lines[i:j]


def body_lines(block):
    """Block lines without the leading anchor and heading line(s)."""
    rest = block["lines"][1:] if block["anchor"] else block["lines"]
    while rest and H_RE.match(rest[0].strip()) \
            and not EMPTY_H.match(rest[0].strip()):
        rest = rest[1:]
    return rest


def answer_id_for(qid):
    m = QID_RE.match(qid)
    return f"{m.group(1)}-ans-{m.group(2)}-q{m.group(3)}" if m else None


def question_id_for(aid):
    m = re.match(r"^(ch\d\d)-ans-(.+?)-q(\d+)$", aid)
    if not m:
        return None
    return f"{m.group(1)}-{m.group(2)}-q{m.group(3)}"


def block_of(qid):
    m = QID_RE.match(qid)
    return f"{m.group(1)}-{m.group(2)}" if m else None


def parse_qid(qid):
    m = QID_RE.match(qid)
    if not m:
        return None, None
    sfx = qid.rsplit("-", 1)[1]
    tag = ("PS" if sfx.startswith("ps")
           else "P" if sfx.startswith("p")
           else "M" if sfx.startswith("m")
           else "")
    return int(m.group(3)), tag


def parse_question_heading(heading):
    m = QH_RE.match(heading.strip())
    if m:
        return int(m.group(2)), (m.group(1) or None)
    return None, None


def is_part(lab):
    return len(lab) == 1 or lab in ROMAN


def detect_parts(lines):
    parts, seen = [], set()
    for l in lines:
        m = re.match(r"^\*\*([a-z]+)\*\*(\s|$)", l.lstrip())
        if not m:
            continue
        lab = m.group(1)
        if lab in seen or not is_part(lab):
            continue
        parts.append(lab)
        seen.add(lab)
    return parts


def detect_marks(lines):
    marks = []
    for l in lines:
        m = re.search(r"`?\[(\d{1,2})\]`?\s*$", l.rstrip())
        if m:
            marks.append(int(m.group(1)))
    return marks


# --------------------------------------------------------------------------
# block splitting
# --------------------------------------------------------------------------
def classify_heading(s, chapter, seq):
    pre = f"ch{chapter:02d}"
    if s.startswith("# "):
        return "section", f"{pre}-intro"
    m = SEC_RE.match(s)
    if m:
        return "section", f"{pre}-s-{m.group(1)}"
    m = EXPLORE_RE.match(s)
    if m:
        return "explore", f"{pre}-explore-{m.group(1)}"
    if DYK_RE.match(s):
        seq["dyk"] += 1
        return "did-you-know", f"{pre}-dyk-{seq['dyk']}"
    if REWIND_RE.match(s):
        seq["rewind"] += 1
        return "rewind", f"{pre}-rewind-{seq['rewind']}"
    if FF_RE.match(s):
        seq["ff"] += 1
        return "fast-forward", f"{pre}-fast-forward-{seq['ff']}"
    if TIP_RE.match(s):
        seq["tip"] += 1
        return "other", f"{pre}-tip-{seq['tip']}"
    if KP_RE.match(s):
        seq["generic"] += 1
        return "key-point", f"{pre}-g-{seq['generic']}"
    if WE_RE.match(s):
        seq["generic"] += 1
        return "worked-example", f"{pre}-g-{seq['generic']}"
    if EX_RE.match(s) or REVIEW_RE.match(s) or CROSS_RE.match(s) \
            or PREREQ_RE.match(s):
        seq["generic"] += 1
        return "exercise", f"{pre}-g-{seq['generic']}"
    seq["generic"] += 1
    return "section", f"{pre}-g-{seq['generic']}"


def make_block(lines, chapter, seq, idx):
    anchor = None
    m = ANCHOR_RE.match(lines[0].strip())
    if m:
        anchor = m.group(1)
    heading = None
    for l in lines:
        s = l.strip()
        if H_RE.match(s) and not EMPTY_H.match(s):
            heading = s
            break
    if anchor:
        e = idx.get(anchor, {})
        blk_type = {"question": "other", "exercise": "exercise",
                    "worked-example": "worked-example",
                    "key-point": "key-point"}.get(e.get("type"), "other")
        kind = e.get("kind") if blk_type == "exercise" else None
        ident = anchor
    else:
        blk_type, ident = classify_heading(heading or lines[0], chapter, seq)
        kind = None
    level = len(H_RE.match(heading).group(1)) if heading else 0
    return {"id": ident, "anchor": anchor, "type": blk_type, "kind": kind,
            "heading": heading or "", "title": heading_title(heading)
            if heading else "", "level": level, "lines": lines}


def split_file(name, chapter, lines, idx):
    n = len(lines)
    bounds = []
    for i, l in enumerate(lines):
        if ANCHOR_RE.match(l.strip()):
            bounds.append(i)
            continue
        s = l.strip()
        if s.startswith("#") and not EMPTY_H.match(s):
            prev = i - 1
            while prev >= 0 and not lines[prev].strip():
                prev -= 1
            if prev < 0 or not ANCHOR_RE.match(lines[prev].strip()):
                bounds.append(i)
    bounds = sorted(set(bounds))
    if not bounds or bounds[0] != 0:
        bounds.insert(0, 0)
    seq = defaultdict(int)
    blocks = []
    for k, start in enumerate(bounds):
        end = bounds[k + 1] if k + 1 < len(bounds) else n
        b = make_block(lines[start:end], chapter, seq, idx)
        b["line_start"] = start
        blocks.append(b)
    return blocks


# --------------------------------------------------------------------------
# per-chapter assembly
# --------------------------------------------------------------------------
def assemble_chapter(book, ch_num, ch_file, ans_file, idx):
    lines = (book / "split" / ch_file).read_text(encoding="utf-8").split("\n")
    blocks = split_file(ch_file, ch_num, lines, idx)

    # section bookkeeping
    last_section = last_numbered = None
    for b in blocks:
        if b["type"] == "section":
            last_section = b["id"]
            if b["level"] == 2 and SEC_RE.match(b["heading"].strip() or ""):
                last_numbered = b["id"]
        b["section_id"] = last_section
        b["fallback_section"] = (last_numbered if last_numbered
                                 else (last_section or f"ch{ch_num:02d}-intro"))

    # md for every block
    for b in blocks:
        b["md"] = finalize("\n".join(b["lines"]))

    # ---- no-text-lost assertion --------------------------------------
    full = finalize("\n".join(lines))
    recon = []
    for b in blocks:
        recon.extend(b["md"].split("\n"))
    if recon != full.split("\n"):
        raise AssertionError(
            f"{ch_file}: concatenated block md does not reproduce the "
            f"normalised chapter ({len(recon)} vs {len(full.split(chr(10)))})")

    # ---- questions ----------------------------------------------------
    ans_ids = set()
    ans_blocks = []
    if ans_file:
        ans_lines = (book / "split" / ans_file).read_text(
            encoding="utf-8").split("\n")
        ans_blocks = split_file(ans_file, ch_num, ans_lines, idx)
        ans_ids = {b["anchor"] for b in ans_blocks
                   if b["anchor"] and idx.get(b["anchor"], {}).get("type")
                   == "answer"}
    questions, qorder = {}, []
    for b in blocks:
        if b["type"] != "other" or not b["anchor"]:
            continue
        if idx.get(b["anchor"], {}).get("type") != "question":
            continue
        qid = b["anchor"]
        num, tag = parse_question_heading(b["heading"])
        if num is None:
            num, tag = parse_qid(qid)
        body = body_lines(b)
        md = finalize("\n".join(trim_lines(body)))
        aid = answer_id_for(qid)
        if aid not in ans_ids:
            aid = None
        questions[qid] = {
            "id": qid,
            "number": num,
            "label": (f"Question {num}" if not tag else f"{tag} {num}"),
            "block": block_of(qid),
            "md": md,
            "parts": detect_parts(body),
            "marks": detect_marks(body),
            "answer_id": aid,
        }
        qorder.append(qid)

    # ---- answers ------------------------------------------------------
    answers = {}
    for b in ans_blocks:
        if b["type"] != "other" or not b["anchor"]:
            continue
        if idx.get(b["anchor"], {}).get("type") != "answer":
            continue
        aid = b["anchor"]
        body = body_lines(b)
        md = finalize("\n".join(trim_lines(body)))
        qid = question_id_for(aid)
        if qid not in questions:
            m = re.match(r"^(ch\d\d)-ans-(.+?)-q(\d+)$", aid)
            if m:
                ch, blk, num = m.group(1), m.group(2), m.group(3)
                qid = next((f"{ch}-{blk}-{t}{num}" for t in ("q", "ps", "p", "m")
                            if f"{ch}-{blk}-{t}{num}" in questions), None)
        answers[aid] = {"id": aid, "question_id": qid, "md": md}

    # ---- exercises ----------------------------------------------------
    exercises = []
    for b in blocks:
        if b["type"] != "exercise" or not b["anchor"]:
            continue
        if idx.get(b["anchor"], {}).get("type") != "exercise":
            continue
        eid = b["anchor"]
        qids = [q for q in qorder if block_of(q) == eid]
        exercises.append({"id": eid, "kind": idx[eid].get("kind"),
                          "title": b["title"], "questions": qids})

    # ---- key points ---------------------------------------------------
    key_points = []
    for b in blocks:
        if b["type"] != "key-point" or not b["anchor"]:
            continue
        number = re.sub(r"^.*-kp-", "", b["anchor"])
        md = finalize("\n".join(trim_lines(body_lines(b))))
        key_points.append({"id": b["anchor"], "number": number, "md": md,
                           "section_id": b["section_id"]})

    # ---- worked examples ----------------------------------------------
    worked_examples, we_no_answer = [], []
    for b in blocks:
        if b["type"] != "worked-example" or not b["anchor"]:
            continue
        number = re.sub(r"^.*-we-", "", b["anchor"])
        rest = body_lines(b)
        at = None
        for i, l in enumerate(rest):
            if ANSWER_LINE.match(l.strip()):
                at = i
                break
        if at is None:
            qmd = finalize("\n".join(trim_lines(rest)))
            worked_examples.append({"id": b["anchor"], "number": number,
                                    "question_md": qmd, "answer_md": None,
                                    "section_id": b["section_id"]})
            we_no_answer.append(b["anchor"])
        else:
            qmd = finalize("\n".join(trim_lines(rest[:at])))
            amd = finalize("\n".join(trim_lines(rest[at + 1:])))
            worked_examples.append({"id": b["anchor"], "number": number,
                                    "question_md": qmd,
                                    "answer_md": amd or None,
                                    "section_id": b["section_id"]})

    # ---- formulas -----------------------------------------------------
    formulas = []
    for b in blocks:
        if b["anchor"] == f"ch{ch_num:02d}-prerequisite":
            md = finalize("\n".join(trim_lines(body_lines(b))))
            formulas.append({"id": b["anchor"],
                             "title": "PREREQUISITE KNOWLEDGE", "md": md})
    for kp in key_points:
        formulas.append({"id": kp["id"],
                         "title": f"KEY POINT {kp['number']}", "md": kp["md"]})

    # ---- mentions (PART 2) --------------------------------------------
    mentions, mentioned_by = find_mentions(blocks, exercises)

    sections = [{"id": b["id"], "type": b["type"], "heading": b["heading"],
                 "title": b["title"], "level": b["level"], "md": b["md"]}
                for b in blocks]

    return {
        "chapter": ch_num,
        "file": ch_file,
        "slug": ch_file[:-3],
        "title": title_of(blocks),
        "sections": sections,
        "exercises": exercises,
        "questions": questions,
        "answers": answers,
        "key_points": key_points,
        "worked_examples": worked_examples,
        "formulas": formulas,
        "mentions": mentions,
        "mentioned_by": mentioned_by,
        "we_no_answer": we_no_answer,
    }


def title_of(blocks):
    for b in blocks:
        if b["type"] == "section" and b["heading"].startswith("# "):
            return re.sub(r"^Chapter\s+\d+:\s*", "", b["title"], flags=re.I)
    return blocks[0]["title"]


def build_exercise_pattern(ex):
    kind = ex["kind"]
    if kind == "exercise":
        num, letter = ex.get("num"), ex.get("letter")
        return re.compile(rf"\bexercises?\s+{num}\s*\.?\s*{letter}\b", re.I)
    if kind == "review":
        num = ex.get("num")
        return re.compile(
            rf"\b(?:end[\- ]of[\- ]chapter\s+)?review\s+exercise\s+{num}\b",
            re.I)
    if kind == "cross":
        num = ex.get("num")
        return re.compile(
            rf"\bcross[\- ]topic\s+review\s+exercise\s+{num}\b", re.I)
    return re.compile(r"\bprerequisite\s+knowledge\b", re.I)


def exercise_num_letter(eid, kind, heading):
    if kind == "exercise":
        m = re.match(r"^ch\d\d-ex(\d+)([A-Z])$", eid)
        if m:
            return {"num": int(m.group(1)), "letter": m.group(2)}
        m = re.match(r"^EXERCISE\s+(\d+)([A-Z])", heading, re.I)
        if m:
            return {"num": int(m.group(1)), "letter": m.group(2)}
    if kind in ("review", "cross"):
        m = re.search(r"(\d+)\s*$", heading)
        if m:
            return {"num": int(m.group(1))}
    return {}


def find_mentions(blocks, exercises):
    search_types = {"section", "worked-example", "key-point", "explore",
                    "did-you-know", "rewind", "fast-forward"}
    ex_recs = []
    for ex in exercises:
        rec = {"id": ex["id"], "kind": ex["kind"]}
        rec.update(exercise_num_letter(ex["id"], ex["kind"], ex["title"]))
        rec["pattern"] = build_exercise_pattern(rec)
        ex_recs.append(rec)
    found = defaultdict(list)       # exercise_id -> [mention dicts]
    mentioned_by = defaultdict(list)
    for b in blocks:
        if b["type"] not in search_types:
            continue
        text = plain_text(b["md"])
        hits = []
        for ex in ex_recs:
            for m in ex["pattern"].finditer(text):
                qn = None
                mm = re.search(r"\b(?:question|Q)\.?\s*(\d+)\b",
                               text[m.end():m.end() + 80])
                if mm:
                    qn = int(mm.group(1))
                hits.append((m.start(), ex["id"], qn, m))
        hits.sort(key=lambda t: t[0])
        for _, exid, qn, m in hits:
            start = max(0, m.start() - 20)
            end = min(len(text), m.start() + 100)
            snip = re.sub(r"\s+", " ", text[start:end]).strip()[:120]
            found[exid].append({"from_block_id": b["id"], "snippet": snip,
                                "question_number": qn})
            mentioned_by[b["id"]].append(exid)
    for sec, lst in mentioned_by.items():
        seen, out = set(), []
        for x in lst:
            if x not in seen:
                seen.add(x)
                out.append(x)
        mentioned_by[sec] = out
    mentions = []
    fallback = {}
    for b in blocks:
        if b["type"] == "exercise" and b["anchor"]:
            fallback[b["anchor"]] = b["fallback_section"]
    for ex in exercises:
        fl = found.get(ex["id"], [])
        if fl:
            for k, f in enumerate(fl):
                mentions.append({"exercise_id": ex["id"],
                                 "from_block_id": f["from_block_id"],
                                 "snippet": f["snippet"],
                                 "question_number": f["question_number"],
                                 "primary_mention": k == 0, "inferred": False})
        else:
            mentions.append({"exercise_id": ex["id"],
                             "from_block_id": fallback.get(ex["id"]),
                             "snippet": "", "question_number": None,
                             "primary_mention": True, "inferred": True})
    mentions.sort(key=lambda m: m["exercise_id"])
    return mentions, dict(mentioned_by)


def chapter_counts(ch):
    questions = ch["questions"]
    answers = ch["answers"]
    return {
        "questions": len(questions),
        "answers": len(answers),
        "linked_answers": sum(1 for q in questions.values() if q["answer_id"]),
        "key_points": len(ch["key_points"]),
        "worked_examples": len(ch["worked_examples"]),
        "exercises": len(ch["exercises"]),
    }


# --------------------------------------------------------------------------
# search index + stats + manifest
# --------------------------------------------------------------------------
def build_search(ch):
    entries = []
    for b in ch["sections"]:
        entries.append({"id": b["id"], "chapter": ch["chapter"],
                        "type": b["type"], "title": b["title"],
                        "text": plain_text(b["md"])})
    for qid, q in sorted(ch["questions"].items()):
        entries.append({"id": qid, "chapter": ch["chapter"], "type": "question",
                        "title": q["label"], "text": plain_text(q["md"])})
    for aid, a in sorted(ch["answers"].items()):
        entries.append({"id": aid, "chapter": ch["chapter"], "type": "answer",
                        "title": "Answer " + aid.rsplit("-q", 1)[-1],
                        "text": plain_text(a["md"])})
    for kp in ch["key_points"]:
        entries.append({"id": kp["id"], "chapter": ch["chapter"],
                        "type": "key-point", "title": f"KEY POINT {kp['number']}",
                        "text": plain_text(kp["md"])})
    for we in ch["worked_examples"]:
        text = plain_text(we["question_md"]) + " " + plain_text(we["answer_md"] or "")
        entries.append({"id": we["id"], "chapter": ch["chapter"],
                        "type": "worked-example",
                        "title": f"WORKED EXAMPLE {we['number']}",
                        "text": text.strip()})
    return entries


def build_stats(chapters):
    totals = {k: 0 for k in ("questions", "answers", "linked_answers",
                             "key_points", "worked_examples", "exercises")}
    per = {}
    for ch in chapters:
        c = chapter_counts(ch)
        for k in totals:
            totals[k] += c[k]
        unlinked = sorted(qid for qid, q in ch["questions"].items()
                          if not q["answer_id"])
        orphans = sorted(aid for aid, a in ch["answers"].items()
                         if a["question_id"] is None)
        per[ch["slug"]] = {"chapter": ch["chapter"], "title": ch["title"],
                           **c, "unlinked_questions": unlinked,
                           "orphan_answers": orphans}
    return {"schema_version": SCHEMA_VERSION, "totals": totals,
            "chapters": per}


# --------------------------------------------------------------------------
# working/ (PART 3)
# --------------------------------------------------------------------------
WORKING_README = """# working/ — working-out files for the exercise frontend

Drop a markdown file here named after the exact question id, e.g.

    working/ch02-ex2E-q1.md

and `scripts/export_data.py` will attach it to the matching question as
`questions[id].working_md` in `frontend-data/chapters/ch02-*.json`.

Naming convention
-----------------
The file name (without the `.md` extension) must be the question's anchor id
from `split/index.json`:

- plain question    `ch<NN>-<block>-qN`          e.g. `ch02-ex2E-q1`
- PS / P question   `ch<NN>-<block>-psN` / `-pN` e.g. `ch03-ex3A-ps14`

`<NN>` is the zero-padded chapter number (01-11) and `<block>` is the
exercise block id (`ex2E`, `review`, `cross`, `prerequisite`).

Content
-------
The file is normalised with the same KaTeX target as everything else in the
export, so write it in the same markdown-with-maths style as the book:
`$...$` for inline maths, `$$ ... $$` for display maths.

A file whose id does not match any question is reported but ignored.
A template lives at `ch02-ex2E-q1.md.sample` (`.sample` is not picked up).
"""

WORKING_SAMPLE = """# ch02-ex2E-q1

Question: Solve, giving your answers correct to 3 significant figures.

**a** $5^{x}=18$

**b** $2^{x}=35$

**c** $3^{2 x}=8$

---

**a**

Take logs of both sides:

$$
\\begin{aligned}
\\log 5^{x} & =\\log 18 \\\\
x \\log 5 & =\\log 18 \\\\
x & =\\frac{\\log 18}{\\log 5}
\\end{aligned}
$$

So $x=1.80$ to 3 significant figures.
"""


def process_working(working_dir, chapters):
    missing = []
    if not working_dir.is_dir():
        working_dir.mkdir(parents=True, exist_ok=True)
    for p in sorted(working_dir.glob("ch*.md")):
        qid = p.stem
        holder = next((ch for ch in chapters if qid in ch["questions"]), None)
        if holder is None:
            missing.append(qid)
            continue
        holder["questions"][qid]["working_md"] = finalize(
            p.read_text(encoding="utf-8"))
    (working_dir / "README.md").write_text(WORKING_README, encoding="utf-8")
    sample = working_dir / "ch02-ex2E-q1.md.sample"
    if not sample.exists():
        sample.write_text(WORKING_SAMPLE, encoding="utf-8")
    return missing


# --------------------------------------------------------------------------
# output assembly + writing
# --------------------------------------------------------------------------
def build_files(book, out, working):
    idx = json.loads((book / "split" / "index.json").read_text(
        encoding="utf-8"))
    ch_files = sorted(p.name for p in (book / "split").glob("ch??-*.md"))
    chapters = []
    for f in ch_files:
        n = int(re.match(r"^ch(\d\d)-", f).group(1))
        ans_file = next((a for a in (book / "split").glob(f"ans{n:02d}-*.md")
                         if a.is_file()), None)
        ch = assemble_chapter(book, n, f, ans_file.name if ans_file else None,
                              idx)
        chapters.append(ch)
    chapters.sort(key=lambda c: c["chapter"])

    missing_working = process_working(working, chapters)

    search = []
    for ch in chapters:
        search.extend(build_search(ch))

    stats = build_stats(chapters)

    counts_by_ch = {c["slug"]: chapter_counts(c) for c in chapters}
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "book": "Maths Pure 2 & 3",
        "chapters": [{"chapter": c["chapter"], "title": c["title"],
                      "slug": c["slug"], "counts": counts_by_ch[c["slug"]]}
                     for c in chapters],
        "non_chapter_files": non_chapter_files(book),
    }

    files = {}
    files["manifest.json"] = json.dumps(manifest, indent=1,
                                        sort_keys=True).encode() + b"\n"
    files["search-index.json"] = json.dumps(search, indent=1,
                                            sort_keys=True).encode() + b"\n"
    files["stats.json"] = json.dumps(stats, indent=1,
                                     sort_keys=True).encode() + b"\n"
    for c in chapters:
        data = {k: v for k, v in c.items() if k not in ("we_no_answer", "file")}
        data["counts"] = counts_by_ch[c["slug"]]
        files[f"chapters/{c['slug']}.json"] = json.dumps(
            data, indent=1, sort_keys=True).encode() + b"\n"

    for img in sorted((book / "images").glob("*")):
        if img.is_file():
            files[f"{IMG_BASE}/{img.name}"] = img.read_bytes()
    return files, chapters, missing_working


def non_chapter_files(book):
    split = book / "split"
    entries = []
    fm = split / "00-front-matter.md"
    if fm.exists():
        entries.append({"file": fm.name, "type": "front-matter",
                        "title": "Front matter"})
    for n in (2, 3):
        for tag, typ in (("paper-pm", "practice-paper"),
                         ("anspaper-pm", "practice-paper-answers")):
            p = split / f"{tag}{n}.md"
            if p.exists():
                entries.append({"file": p.name, "type": typ,
                                "title": page_title(p)})
    for fname, typ in (("zz-glossary.md", "glossary"), ("zz-index.md", "index")):
        p = split / fname
        if p.exists():
            entries.append({"file": fname, "type": typ,
                            "title": page_title(p)})
    return entries


def page_title(path):
    for ln in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^#\s+(.*)$", ln.strip())
        if m:
            return m.group(1).strip()
    return path.stem


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def write_files(files, out):
    written = 0
    for rel in sorted(files):
        data = files[rel]
        dest = out / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        changed = True
        if dest.exists():
            # hash compare: only rewrite when the bytes differ
            if sha256(dest.read_bytes()) == sha256(data):
                changed = False
        if changed:
            dest.write_bytes(data)
            written += 1
    img_dir = out / IMG_BASE
    if img_dir.is_dir():
        for p in img_dir.iterdir():
            if p.is_file() and f"{IMG_BASE}/{p.name}" not in files:
                p.unlink()
    return written


# --------------------------------------------------------------------------
# validation + report (PART 4)
# --------------------------------------------------------------------------
def validate(chapters):
    issues = defaultdict(list)
    section_ids = []
    entity_ids = defaultdict(list)
    empty_md = []
    katex_unsafe = []
    for ch in chapters:
        for b in ch["sections"]:
            section_ids.append(b["id"])
            if not b["md"].strip():
                empty_md.append(b["id"])
            for pat, name in ((r"\\longdiv", "longdiv"),
                              (r"\\begin\{align\}", "align"),
                              (r"\\end\{align\}", "align"),
                              (r"\\begin\{align\*\}", "align"),
                              (r"\\end\{align\*\}", "align"),
                              (r"\\begin\{equation\*?\}", "equation"),
                              (r"\\end\{equation\*?\}", "equation")):
                if re.search(pat, b["md"]):
                    katex_unsafe.append((b["id"], name))
        for ex in ch["exercises"]:
            entity_ids["exercise"].append(ex["id"])
            for qid in ex["questions"]:
                if qid not in ch["questions"]:
                    issues["exercise_question_missing"].append(
                        f"{ex['id']} -> {qid}")
        for qid, q in ch["questions"].items():
            entity_ids["question"].append(qid)
            if not q["md"].strip():
                empty_md.append(qid)
            if q.get("working_md") is not None and not q["working_md"].strip():
                empty_md.append(qid + " (working)")
        for aid, a in ch["answers"].items():
            entity_ids["answer"].append(aid)
            if a["question_id"] is not None \
                    and a["question_id"] not in ch["questions"]:
                issues["answer_question_missing"].append(
                    f"{aid} -> {a['question_id']}")
            if not a["md"].strip():
                empty_md.append(aid)
        for kp in ch["key_points"]:
            entity_ids["key-point"].append(kp["id"])
            if not kp["md"].strip():
                empty_md.append(kp["id"])
        for we in ch["worked_examples"]:
            entity_ids["worked-example"].append(we["id"])
            if not we["question_md"].strip():
                empty_md.append(we["id"] + " (question)")
            if we["answer_md"] and not we["answer_md"].strip():
                empty_md.append(we["id"] + " (answer)")
        for f in ch["formulas"]:
            if not f["md"].strip():
                empty_md.append(f["id"] + " (formula)")
    dup_sections = sorted({i for i in section_ids
                           if section_ids.count(i) > 1})
    dup_entities = {}
    for cat, ids in entity_ids.items():
        dup = sorted({i for i in ids if ids.count(i) > 1})
        if dup:
            dup_entities[cat] = dup
    return {
        "duplicate_section_ids": dup_sections,
        "duplicate_entity_ids": dup_entities,
        "exercise_question_missing": sorted(issues["exercise_question_missing"]),
        "answer_question_missing": sorted(issues["answer_question_missing"]),
        "empty_md": sorted(set(empty_md)),
        "katex_unsafe": sorted(set(katex_unsafe)),
    }


def report(book, chapters, missing_working, files, out):
    val = validate(chapters)
    print("=== schema check ===")
    print(f"  duplicate section ids: {len(val['duplicate_section_ids'])}"
          + (f" -> {val['duplicate_section_ids'][:10]}"
             if val['duplicate_section_ids'] else ""))
    print(f"  duplicate entity ids per type: "
          f"{val['duplicate_entity_ids'] or 'none'}")
    print(f"  exercise->question ids not in questions: "
          f"{len(val['exercise_question_missing'])}")
    for x in val["exercise_question_missing"][:10]:
        print("     " + x)
    print(f"  answer.question_id not in questions: "
          f"{len(val['answer_question_missing'])}")
    for x in val["answer_question_missing"][:10]:
        print("     " + x)
    print(f"  empty md fields: {len(val['empty_md'])}")
    for x in val["empty_md"][:20]:
        print("     " + x)

    print("\n=== counts ===")
    nq = sum(len(c["questions"]) for c in chapters)
    na = sum(len(c["answers"]) for c in chapters)
    nl = sum(1 for c in chapters for q in c["questions"].values()
             if q["answer_id"])
    nkp = sum(len(c["key_points"]) for c in chapters)
    nwe = sum(len(c["worked_examples"]) for c in chapters)
    nwe_no = sum(len(c["we_no_answer"]) for c in chapters)
    nex = sum(len(c["exercises"]) for c in chapters)
    nblocks = sum(len(c["sections"]) for c in chapters)
    nmentions = sum(len(c["mentions"]) for c in chapters)
    ninferred = sum(1 for c in chapters for m in c["mentions"] if m["inferred"])
    nreal = nmentions - ninferred
    nno_mention = sum(1 for c in chapters for m in c["mentions"]
                      if m["inferred"])
    print(f"  chapters: {len(chapters)}")
    print(f"  section blocks: {nblocks}")
    print(f"  questions: {nq}  (linked answers: {nl}, unlinked: {nq - nl})")
    print(f"  answers: {na}")
    print(f"  key points: {nkp}")
    print(f"  worked examples: {nwe}  (without Answer marker: {nwe_no})")
    print(f"  exercises: {nex}")
    print(f"  mentions: {nreal} real, {ninferred} inferred fallbacks "
          f"(exercises with no mention: {nno_mention})")

    print("\n=== KaTeX-unsafe constructs remaining in md ===")
    from collections import Counter
    uc = Counter(name for _, name in val["katex_unsafe"])
    print("  " + ", ".join(f"{k}: {v}" for k, v in sorted(uc.items()))
          or "  none")
    for iid, name in val["katex_unsafe"][:30]:
        print(f"     {iid}  [{name}]")

    if missing_working:
        print("\n=== working files with unknown ids ===")
        for m in missing_working:
            print("     " + m)
    else:
        print("\n=== working files with unknown ids: none ===")

    print("\n=== ch02 excerpt ===")
    ch = next(c for c in chapters if c["chapter"] == 2)
    ex2e = next(e for e in ch["exercises"] if e["id"] == "ch02-ex2E")
    q1 = ch["questions"]["ch02-ex2E-q1"]
    ans = ch["answers"].get(q1["answer_id"]) if q1["answer_id"] else None
    kp23 = next(k for k in ch["key_points"] if k["id"] == "ch02-kp-2.3")
    we211 = next(w for w in ch["worked_examples"]
                 if w["id"] == "ch02-we-2.11")
    excerpt = {
        "exercise_2E": ex2e,
        "question_1_with_answer": {"question": q1, "answer": ans},
        "key_point_2.3": kp23,
        "worked_example_2.11": we211,
    }
    print(json.dumps(excerpt, indent=1, sort_keys=True, ensure_ascii=False))

    print("\n=== sizes ===")
    total = sum(len(d) for d in files.values())
    biggest = max(files, key=lambda f: len(files[f]))
    print(f"  total frontend-data size: {total} bytes "
          f"({total / 1024 / 1024:.2f} MiB)")
    print(f"  largest file: {biggest} ({len(files[biggest])} bytes)")
    print(f"  output: {out}")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("book", nargs="?", default=str(BOOK_DEFAULT))
    ap.add_argument("--out", default=str(OUT_DEFAULT))
    ap.add_argument("--working", default=str(WORKING_DEFAULT))
    args = ap.parse_args(argv)

    book = Path(args.book)
    out = Path(args.out)
    working = Path(args.working)
    if not (book / "split").is_dir():
        sys.exit(f"not a book dir: {book} (expected split/ inside)")

    files, chapters, missing_working = build_files(book, out, working)
    # run twice and confirm the bundle is byte-identical
    files2, _, _ = build_files(book, out, working)
    if files != files2:
        diffs = [k for k in files if files[k] != files2.get(k)]
        sys.exit(f"ERROR: frontend-data not byte-identical on re-run: {diffs}")
    write_files(files, out)
    report(book, chapters, missing_working, files, out)
    print("\nfrontend-data regenerated (idempotent).")


if __name__ == "__main__":
    main()
