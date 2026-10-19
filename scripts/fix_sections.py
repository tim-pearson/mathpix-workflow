#!/usr/bin/env python3
"""Normalise the structure of the split/ chapter files.

Heading scheme (applied to chNN-*/ansNN-* files):
  #            chapter / answer-section title
  ##           numbered sections (1.1, 11.5, ...)
  ###          EXERCISE / END-OF-CHAPTER REVIEW / CROSS-TOPIC REVIEW /
               PREREQUISITE KNOWLEDGE, and any other non-numbered sub-block
  ####         WORKED EXAMPLE / KEY POINT / EXPLORE / DID YOU KNOW /
               REWIND / FAST FORWARD / TIP
  #####        Question N (chapters) / Answer N (answers), converted from
               the bold **N** lines inside exercises/reviews/answers

Stable anchors: an explicit <a id="..."></a> line is placed directly above
each exercise, worked example, key point and question.  Answers carry the
matching ch<NN>-ans-<block>-q<N> id.

Also: exam citations ("Cambridge International ...") are italicised and
trailing mark numbers ([3]) are wrapped in backticks.  $$ blocks, inline
math and table rows are left untouched.

Writes files in place and generates split/index.json.  Each entry carries
id, type, chapter, file and line, plus next_id (the id of the next anchor
in the same file, or null at EOF) so later scripts can slice a block as
"from this anchor up to next_id" without relying on line numbers.

The index is derived by *parsing* the final text (anchor + following
heading), so it is identical no matter how many times the script runs.

CLI:
  python fix_sections.py [split_dir] [-n|--dry-run] [--check] [--callouts]
                         [--corrections PATH]

  -n / --dry-run   compute everything, print the report, write nothing
  --check          validate the files already on disk (idempotency,
                   unique anchors, question<->answer matching)
  --callouts       instead of #### box headings, wrap KEY POINT / EXPLORE /
                   DID YOU KNOW / REWIND / FAST FORWARD / TIP boxes in
                   > [!IMPORTANT] / [!NOTE] / [!TIP] callouts.  Off by
                   default.  Exercises, reviews, worked examples,
                   questions and anchors are unaffected.
  --corrections    JSON of hand-curated question/answer fixes keyed by id
                   (default: scripts/corrections.json next to this script).

Corrections JSON format:
  {
    "answers": {
      "ch04-ans-ex4A-q3": "$16 x+y=32$",      // body line(s): str or list
      "ch02-ans-review-q13": ["k=16"],
      "ch03-ans-review-q2": {"body": "131.8\u00b0", "match": "131.8\u00b0"},
      "ch11-ans-ex11C-q5": null                // null = delete this answer
    },
    "questions": {
      "ch04-ex4A-q3": "Find the equation ...",
      "ch04-ex4A-q5": null                     // null = delete this question
    }
  }
Keys are anchor ids exactly as they appear in split/index.json.  A non-null
value replaces the answer/question body (a string = one line, a list = many);
null removes the id.  An object form adds "match": the exact source line that
this correction owns, so a body line the heuristics would otherwise re-split
or mis-attribute is consumed by this id.  Missing answers/questions whose
correction exists are created (anchor + heading + corrected body) at the end
of their block, and ambiguous "N rest" answer lines are resolved to the
corrected id when a correction names a candidate number.  Everything is
applied inside the structural pass, so corrections work on the first run and
on re-runs, and running the script twice on its own output is still a no-op.

Idempotent: running it again on its own output is a no-op.
"""
import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

# sentinel: a corrections.json entry mapped to this means "remove the id"
DELETED = object()

ANCHOR = '<a id="{}"></a>'
ANCHOR_RE = re.compile(r'^<a id="([^"]+)"></a>$')

CH_RE = re.compile(r"^ch(\d{1,2})-")
ANS_RE = re.compile(r"^ans(\d{1,2})-")

HDR = r"(?:#{1,6}\s*)?"
KP_RE = re.compile(r"^" + HDR + r"KEY POINT\s+(\d+\.\d+)\s*$")
KP_TRAIL = re.compile(r"^" + HDR + r"KEY POINT\s+\d+\.\d+\s+\S")
EXPLORE_RE = re.compile(r"^" + HDR + r"EXPLORE\s+(\d+\.\d+)\s*$")
DYK_RE = re.compile(r"^" + HDR + r"(?:i\)\s*)?DID\s+YOU\s+KNOW\??\s*$", re.I)
REWIND_RE = re.compile(r"^" + HDR + r"REWIND\s*$")
FF_RE = re.compile(r"^" + HDR + r"FAST\s+FORWARD\s*$")
TIP_RE = re.compile(r"^" + HDR + r"TIP\s*$")
WE_RE = re.compile(r"^" + HDR + r"WORKED\s+EXAMPLE\s+(\d+\.\d+)\s*$")
EX_RE = re.compile(r"^" + HDR + r"EXERCISE\s+(\d+)([A-Z])\s*$", re.I)
REVIEW_RE = re.compile(
    r"^" + HDR + r"END-OF-CHAPTER REVIEW EXERCISE\s+(\d+)\s*$", re.I)
CROSS_RE = re.compile(
    r"^" + HDR + r"CROSS-TOPIC REVIEW EXERCISE\s+(\d+)\s*$", re.I)
PREREQ_RE = re.compile(r"^" + HDR + r"PREREQUISITE KNOWLEDGE\s*$", re.I)
SEC_RE = re.compile(r"^([#]{2,6})\s+(\d+(?:\.\d+)+)(\s.+)$")
EMPTY_H = re.compile(r"^#{1,6}\s*$")
STRAY_H = re.compile(r"^#{2}\s+[A-Za-z]\s*$")
GEN_H2 = re.compile(r"^##\s+\S")

Q_RE = re.compile(r"^\*\*(?:(PS|P|M)\s+)?(\d+)\*\*(.*)$")
# plain Modelling prefix used by ch10 exercise 10B: "M 1 Write ..."
MQ_RE = re.compile(r"^M\s+(\d+)\s*(.*)$")
CITE_RE = re.compile(r"^(Cambridge International .*)$")
MARK_RE = re.compile(r"\s\[(\d{1,2})\]\s*$")

# answer-file lines that carry the question number inside an inline maths
# span: "$2 \frac{1}{5}$", "$6 x=...$", "$1 w=0.02r^{3}$"
MATH_NUM = re.compile(r"^\$(\d+)\s+([^$]*)\$")
# bare/glued answer-number lines: "316 x+y=32" or "316x+y=32" (the leading
# number may itself be a question number glued to a longer answer)
BARE_NUM = re.compile(r"^(\d+)(.*)$")
# bare part labels in answers: "b 4", "c 1", ...
LABEL_BARE = re.compile(r"^([a-z])\s+(\S.*)$")
LABEL_BOLD = re.compile(r"^\*\*([a-z])\*\*(\s|$)")

CALL_RE = re.compile(r"^> \[!(IMPORTANT|NOTE|TIP)\]\s*(.*)$")

CALL_TYPE = {"KEY POINT": "IMPORTANT", "EXPLORE": "NOTE", "REWIND": "NOTE",
             "FAST FORWARD": "NOTE", "DID YOU KNOW": "TIP", "TIP": "TIP"}

# question numbers in non-bold forms, seen on the chapter side:
# "(7) 14", "(E) 4", ") 5", "E1", "e 3", "Ex 13", "EX 11", "PS 10.", "PS $9", "$4 z="
CH_FORM = re.compile(
    r"^(?:\(\s*(?:[EePpMm]|\d+)\s*\)\s*|\)\s*|[Ee][Xx]?\s*|"
    r"(?:[Pp][Ss])\s+\$?\s*|\$\s*)(\d+)")
MESSY_NUM = re.compile(r"^(\d+\.?\d*)\s*$")


def norm_qid(qid):
    """ps7 / p7 / m7 -> q7 and drop the -ans- segment, so chapter-side and
    answer-side ids can be compared (ch02-ex2E-q7 vs ch02-ans-ex2E-q7)."""
    aid = re.sub(r"-ans-", "-", qid, count=1)
    return re.sub(r"(?<=-)(?:ps|p|m)(\d+)$", r"q\1", aid)


CALL_TYPE = {"KEY POINT": "IMPORTANT", "EXPLORE": "NOTE", "REWIND": "NOTE",
             "FAST FORWARD": "NOTE", "DID YOU KNOW": "TIP", "TIP": "TIP"}


def is_structural(line):
    """A line that ends a callout body (headings, box headers, labels,
    anchors for the next block)."""
    s = line.strip()
    if not s:
        return False
    if s.startswith("#") or s.startswith("> [!") or ANCHOR_RE.match(s):
        return True
    return any(rx.match(s) for rx in (
        KP_RE, KP_TRAIL, EXPLORE_RE, DYK_RE, REWIND_RE, FF_RE, TIP_RE,
        WE_RE, EX_RE, REVIEW_RE, CROSS_RE, PREREQ_RE))


def wrap_marks(line):
    m = MARK_RE.search(line)
    if not m:
        return line
    pre = line[:m.start()]
    if pre.count("$") % 2 == 1:
        return line
    return pre + " `[%s]`%s" % (m.group(1), line[m.end():])


class FileProcessor:
    def __init__(self, path, callouts=False, ans_nums=None, ch_qnums=None,
                 ans_corr=None, q_corr=None):
        self.path = path
        self.name = path.name
        mch = CH_RE.match(self.name)
        mans = ANS_RE.match(self.name)
        self.chapter = int(mch.group(1)) if mch else (
            int(mans.group(1)) if mans else 0)
        self.full = bool(mch or mans)      # structural pass (ch/ans files)
        self.ch_side = bool(mch)           # questions (True) vs answers
        self.callouts = callouts and bool(mch or mans)
        self.ans_nums = ans_nums or {}     # block base -> set of answer numbers
        self.ch_qnums = ch_qnums or {}     # block base -> set of chapter question numbers

        def norm_corr(v):
            if v is None or v is DELETED:
                return DELETED, None
            if isinstance(v, dict):
                b = v.get("body")
                return ((DELETED if b is None else
                         ([b] if isinstance(b, str) else list(b))),
                        v.get("match"))
            return ([v] if isinstance(v, str) else list(v), None)

        self.ans_corr, self.ans_match = {}, {}
        for k, v in (ans_corr or {}).items():
            body, match = norm_corr(v)
            self.ans_corr[k] = body
            if match:
                self.ans_match[k] = match
        self.q_corr, self.q_match = {}, {}
        for k, v in (q_corr or {}).items():
            body, match = norm_corr(v)
            self.q_corr[k] = body
            if match:
                self.q_match[k] = match
        self.out = []
        self.cnt = Counter()
        self.flags = []
        self.in_math = False
        self.in_callout = False
        self.in_existing_callout = False
        self.block = None
        self.block_base = None
        self.prev = None
        self.part = None                 # last part label letter within an answer
        self.block_log = []              # per block: base + accepted numbers
        self.notes = []                  # file:line list of lines this feature touches
        self.corr_notes = []             # file:line list of corrections applied
        self.corr_applied = set()        # ids that were actually applied
        self.last_anchor_id = None       # id of the most recent anchor line
        self.skip_after = False          # discard lines until the next anchor/heading
        self.skip_pid = None             # id whose old body is being skipped
        self._emitted = set()            # ids emitted this pass
        self._block_ranges = []          # [base, start_out_len, (end_out_len)]
        self.ans_mathsplit = 0           # answer headings created from $N math
        self.ans_bare = 0                # answer headings from bare/glued N rest
        self.ans_label = 0               # bare labels bolded
        self.orig = path.read_text(encoding="utf-8")

    def _corr_body(self, corr, pid):
        """Return 'delete' | body-lines | None for pid in `corr`."""
        if pid not in corr:
            return None
        v = corr[pid]
        return "delete" if v is DELETED else v

    def _is_deleted(self, pid):
        return (pid in self.ans_corr and self.ans_corr[pid] is DELETED) \
            or (pid in self.q_corr and self.q_corr[pid] is DELETED)

    def flag(self, line_no, kind, snippet):
        self.flags.append(f"{self.name}:{line_no} [{kind}] {snippet[:70]}")

    def accept_question(self, n):
        """Resync rule for the chapter side: accept N if N == 1 (block
        start), or last < N <= last+3, or N is one of the answer numbers for
        the same block (answer side is ground truth for which numbers exist).
        Never accepts N <= last accepted."""
        block_nums = self.ans_nums.get(self.block_base, ())
        if self.prev is None:
            return n == 1 or n in block_nums
        return (self.prev < n <= self.prev + 3) \
            or (n in block_nums and n > self.prev)

    def anchor(self, aid):
        if self.out and self.out[-1] == ANCHOR.format(aid):
            return len(self.out)          # already present from an earlier run
        out_line = len(self.out) + 1
        self.out.append(ANCHOR.format(aid))
        return out_line

    def add_heading(self, aid, text):
        self.anchor(aid)
        self.out.append(text)

    def end_block(self):
        if self._block_ranges and self._block_ranges[-1][0] == self.block_base:
            self._block_ranges[-1].append(len(self.out))
        self.block = None
        self.block_base = None
        self.prev = None
        self.part = None

    def start_block(self, kind, base):
        self.block = kind
        self.block_base = base
        self.prev = None
        self.part = None
        self._block_ranges.append([base, len(self.out)])
        self.block_log.append({"base": base, "nums": []})

    def log_num(self, n):
        if self.block_log:
            self.block_log[-1]["nums"].append(n)

    def match_question(self, line):
        """(tag, n, rest) for a question-start line, or None.  Handles the
        bold forms **N** / **PS N** / **P N** / **M N** and, on the chapter
        side, the plain Modelling prefix "M N ..."."""
        m = Q_RE.match(line)
        if m:
            return m.group(1), int(m.group(2)), m.group(3)
        if self.ch_side:
            mm = MQ_RE.match(line)
            if mm:
                return "M", int(mm.group(1)), mm.group(2)
        return None

    def _form_tag(self, line):
        """Detect a PS / P / M tag on a non-bold question-number form line."""
        s = line.lstrip()
        if re.match(r"^\(\s*[Pp][Ss]\s*\)", s) or re.match(r"^[Pp][Ss]\b", s):
            return "PS"
        if re.match(r"^\(\s*[Pp]\s*\)", s) or re.match(r"^[Pp]\s+\$?\d", s):
            return "P"
        if re.match(r"^\(\s*[Mm]\s*\)", s) or re.match(r"^[Mm]\s+\$?\d", s):
            return "M"
        return None

    def _emit_question(self, tag, n, rest, line_no):
        """Create a `##### Question/Answer N` heading + anchor for a number we
        have accepted, then append the (stripped) rest as the first body line."""
        self.part = None
        sfx = f"{tag.lower()}{n}" if tag else f"q{n}"
        pid = f"{self.block_base}-{sfx}"
        corr = self.ans_corr if not self.ch_side else self.q_corr
        body = self._corr_body(corr, pid)
        if body == "delete":
            self.skip_after = True
            self.skip_pid = pid
            return None
        self.prev = n
        self.log_num(n)
        head = f"##### {'Question' if self.ch_side else 'Answer'}"
        head += f" {tag + ' ' if tag else ''}{n}"
        self.cnt["question" if self.ch_side else "answer"] += 1
        self._emitted.add(pid)
        self.add_heading(pid, head)
        if body is not None:
            self.corr_applied.add(pid)
            self.corr_notes.append(f"{self.name}:{line_no} [corr-override] {pid}")
            for bl in body:
                self.out.append(wrap_marks(bl))
            return None
        rest = rest.strip()
        if rest:
            if not self.ch_side:
                mb = LABEL_BOLD.match(rest)
                if mb:
                    self.part = mb.group(1)
                else:
                    ml = LABEL_BARE.match(rest)
                    if ml:
                        expected_part = "a" if self.part is None \
                            else chr(ord(self.part) + 1)
                        if ml.group(1) == expected_part:
                            self.part = ml.group(1)
                            rest = f"**{ml.group(1)}** {ml.group(2)}"
            self.out.append(wrap_marks(rest))
        return None

    def _note_or_promote_form(self, line, line_no):
        """Chapter-side non-bold question-number forms.  When the number is a
        real question for this block (the answer set is ground truth), promote
        it to a proper `##### Question N` heading + anchor instead of just
        flagging it.  Otherwise keep the existing note/flag behaviour."""
        n = None
        rest = ""
        fm = CH_FORM.match(line)
        if fm:
            n = int(fm.group(1))
            rest = line[fm.end():]
            if line.lstrip().startswith("$"):
                rest = "$" + rest            # restore the inline-math span
        else:
            mn = MESSY_NUM.match(line)
            if mn:
                n = int(float(mn.group(1)))
        if n is None:
            return line
        block_nums = self.ans_nums.get(self.block_base, set())
        pid = f"{self.block_base}-q{n}"
        if n in block_nums and (self.prev is None or n > self.prev):
            return self._emit_question(self._form_tag(line), n, rest, line_no)
        if self._corr_body(self.q_corr, pid) is not None \
                and (self.prev is None or n > self.prev):
            return self._emit_question(self._form_tag(line), n, rest, line_no)
        if self.prev is None or n > self.prev:
            self.prev = n
        self.cnt["noted"] += 1
        self.flag(line_no, "question-number-form", line)
        return line

    def process_block_question(self, line, line_no):
        qm = self.match_question(line)
        if qm is None:
            if self.ch_side:
                return self._note_or_promote_form(line, line_no)
            return self.answer_plain_line(line, line_no)
        tag, n, rest = qm
        if self.ch_side:
            # resync rule (accept_question) replaces the old "+3 of previous"
            # rejection which could cascade: one miss rejected every later
            # question.
            if not self.accept_question(n):
                pid = f"{self.block_base}-" \
                    + (f"{tag.lower()}{n}" if tag else f"q{n}")
                if self._corr_body(self.q_corr, pid) is not None:
                    # a correction names this question: force it through
                    return self._emit_question(tag, n, rest, line_no)
                if self.prev is not None and n <= self.prev:
                    reason = f"number {n} <= previous {self.prev}"
                elif self.prev is None:
                    reason = f"block starts at {n} (expected 1 or in answer set)"
                else:
                    reason = (f"number {n} more than +3 past {self.prev} "
                              "and not in answer set")
                self.flag(line_no, "question-skip", reason)
                return line
        else:
            if self.prev is not None and n <= self.prev:
                self.flag(line_no, "question-skip",
                          f"number {n} <= previous {self.prev}")
                return line
            if self.prev is not None and n - self.prev > 15:
                self.flag(line_no, "question-skip",
                          f"number {n} implausible after {self.prev}")
                return line
            if self.prev is not None and n - self.prev > 3:
                self.flag(line_no, "question-gap",
                          f"answer numbering jumps {self.prev} -> {n} "
                          "(earlier answers likely used unlabelled/math forms)")
        return self._emit_question(tag, n, rest, line_no)

    def _digit_hits(self, digits, rest):
        """Every way a leading digit run `digits` (glued to `rest`) can be read
        as a question number for this block: split the run at each point, take
        the prefix as the number and the suffix + `rest` as the answer body.
        `rest` is the raw remainder after `digits` (may start with the space
        that separated the two).  A reading counts when the body is non-empty
        and the number is the next expected answer (prev+1 / 1) or is a
        chapter question number for this block that has not been emitted yet.
        Returns [(n, body), ...]."""
        expected = 1 if self.prev is None else self.prev + 1
        ch_block = re.sub(r"-ans-", "-", self.block_base or "", count=1)
        ch_nums = self.ch_qnums.get(ch_block, set())
        hits = []
        for k in range(1, len(digits) + 1):
            n = int(digits[:k])
            body = (digits[k:] + rest).strip()
            if not body:
                continue
            if n == expected \
                    or (n in ch_nums and (self.prev is None or n > self.prev)):
                hits.append((n, body))
        return hits

    def _would_resplit(self, n, emitted):
        """True if emitting `Answer n` with body line `emitted` is unsafe: a
        re-run would split the body again (a glued-number cascade, e.g.
        "$36 a=...$" -> Answer 3 + "$6 a=...$" -> Answer 6).  Such a split
        would break idempotency, so callers must refuse it and flag it."""
        save_prev = self.prev
        self.prev = n
        try:
            s = emitted.strip()
            if s.startswith("$"):
                m = MATH_NUM.match(s)
                if not m:
                    return False
                sep = s[m.start(1) + len(m.group(1)):m.start(2)]
                return len(self._digit_hits(m.group(1), sep + m.group(2))) >= 1
            m = BARE_NUM.match(s)
            if not m:
                return False
            return len(self._digit_hits(m.group(1), m.group(2))) >= 1
        finally:
            self.prev = save_prev

    def _split_emitted(self, n, body, line, line_no, math_trailing, kind):
        """Emit a `##### Answer N` heading + body for a bare/glued number
        split.  kind is "math" (math-span line, body re-wrapped in `$...$`
        with `math_trailing` appended) or "bare" (plain line, body verbatim).
        The full-number reading of a math line counts as a [math-split]; every
        other reading (a shorter prefix that is a real question number) counts
        as a [bare-split]."""
        pid = f"{self.block_base}-q{n}"
        corr_body = self._corr_body(self.ans_corr, pid)
        if corr_body == "delete":
            self.skip_after = True
            self.skip_pid = pid
            return None
        self.prev = n
        self.part = None
        self.log_num(n)
        self.cnt["answer"] += 1
        self._emitted.add(pid)
        if kind == "math":
            self.ans_mathsplit += 1
            tag = "math-split"
        else:
            self.ans_bare += 1
            tag = "bare-split"
        self.notes.append(
            f"{self.name}:{line_no} [{tag}] {line.strip()[:64]}")
        self.add_heading(pid, f"##### Answer {n}")
        if corr_body is not None:
            self.corr_applied.add(pid)
            self.corr_notes.append(f"{self.name}:{line_no} [corr-override] {pid}")
            for bl in corr_body:
                self.out.append(wrap_marks(bl))
            return None
        if math_trailing is not None:
            body = "$" + body + "$" + math_trailing
        if body.strip():
            self.out.append(wrap_marks(body))

    def _emit_corr_answer(self, n, pid, body, line_no):
        """Emit `##### Answer N` with a correction-provided body (used when no
        source line produced this answer, or to resolve an ambiguous line)."""
        self.prev = n
        self.part = None
        self.log_num(n)
        self.cnt["answer"] += 1
        self._emitted.add(pid)
        self.corr_applied.add(pid)
        self.corr_notes.append(f"{self.name}:{line_no} [corr-create] {pid}")
        self.add_heading(pid, f"##### Answer {n}")
        for bl in body:
            self.out.append(wrap_marks(bl))

    def _corr_resolve(self, digits, rest, line, line_no):
        """If a correction names an answer this candidate line can represent
        (the leading number, one of its glued prefixes, or the next expected
        number), emit that answer with the corrected body.  Returns True if
        the line was consumed."""
        expected = 1 if self.prev is None else self.prev + 1
        cands = {expected}
        for k in range(1, len(digits) + 1):
            cands.add(int(digits[:k]))
        for n in sorted(c for c in cands
                        if self.prev is None or c > self.prev):
            pid = f"{self.block_base}-q{n}"
            body = self._corr_body(self.ans_corr, pid)
            if body is not None and body != "delete":
                self._emit_corr_answer(n, pid, body, line_no)
                return True
        return False

    def _corr_owner(self, s):
        """Answer correction id whose explicit "match" equals this line."""
        for pid, match in self.ans_match.items():
            if match == s:
                return pid
        return None

    def _corr_match(self, line, line_no):
        """If a correction explicitly names this exact source line, emit its
        answer with the corrected body.  Used when a body line would otherwise
        be re-split or left mis-attributed (e.g. "131.8°" is Answer 2's
        content, not "13"+"1.8°").  Returns True if the line was consumed."""
        s = line.strip()
        for pid, match in self.ans_match.items():
            if match != s or not pid.startswith(self.block_base + "-"):
                continue
            m = re.match(rf"^{re.escape(self.block_base)}-"
                        r"((?:q|ps|p|m)(\d+))$", pid)
            if not m or (self.prev is not None
                         and int(m.group(2)) <= self.prev):
                continue
            body = self._corr_body(self.ans_corr, pid)
            if body is not None and body != "delete":
                self._emit_corr_answer(int(m.group(2)), pid, body, line_no)
                return True
        return False

    def _finish_blocks(self):
        """Close any block left open at EOF, then create the answer/question
        ids that a correction mandates but no source line produced."""
        for r in self._block_ranges:
            if len(r) == 2:
                r.append(len(self.out))
        corr = self.ans_corr if not self.ch_side else self.q_corr
        for base, _start, end in reversed(self._block_ranges):
            created = []
            for pid, body in sorted(corr.items()):
                if body is DELETED or pid in self._emitted:
                    continue
                m = re.match(rf"^{re.escape(base)}-((?:q|ps|p|m)(\d+))$", pid)
                if not m:
                    continue
                n = int(m.group(2))
                for rec in self.block_log:
                    if rec["base"] == base:
                        rec["nums"].append(n)
                self._emitted.add(pid)
                self.corr_applied.add(pid)
                self.corr_notes.append(f"{self.name}:{end + 1} [corr-create] {pid}")
                created.append(ANCHOR.format(pid))
                created.append(
                    f"##### {'Question' if self.ch_side else 'Answer'} {n}")
                created.extend(wrap_marks(bl) for bl in body)
                created.append("")
            if created:
                self.out[end:end] = created

    def answer_plain_line(self, line, line_no):
        """Answer-file plain lines: part labels and $N-in-maths question
        numbers. Only fires while a question block is active."""
        if self._corr_match(line, line_no):
            return None
        mb = LABEL_BOLD.match(line)
        if mb:
            self.part = mb.group(1)
            return line
        mm = MATH_NUM.match(line)
        if mm:
            expected = 1 if self.prev is None else self.prev + 1
            # ground truth: the chapter question numbers for this block.  A
            # `$N <answer>$` line is an unambiguous answer start when exactly
            # one reading of the leading number matches an expected question
            # (the whole number, or a glued prefix like the "3" in
            # "$316 x+y=32$"), so answers that the OCR numbered inline are
            # split correctly even when earlier answers were skipped/mangled.
            sep = line[mm.start(1) + len(mm.group(1)):mm.start(2)]
            hits = self._digit_hits(mm.group(1), sep + mm.group(2))
            if len(hits) == 1:
                n, body = hits[0]
                emitted = "$" + body + "$" + line[mm.end():]
                if self._would_resplit(n, emitted):
                    if self._corr_resolve(mm.group(1), sep + mm.group(2),
                                          line, line_no):
                        return None
                    self.flag(line_no, "math-split-ambiguous",
                              f"{line.strip()[:40]} "
                              f"(ambiguous: {n} would re-split)")
                    return line
                kind = "math" if n == int(mm.group(1)) else "bare"
                self._split_emitted(n, body, line, line_no,
                                    line[mm.end():], kind)
                return None
            if self._corr_resolve(mm.group(1), sep + mm.group(2),
                                  line, line_no):
                return None
            if len(hits) > 1:
                cands = " or ".join(str(h[0]) for h in hits)
                self.flag(line_no, "math-split-ambiguous",
                          f"{line.strip()[:40]} (ambiguous: {cands})")
                return line
            self.flag(line_no, "math-split-ambiguous",
                      f"{line.strip()[:50]} (expected {expected})")
            return line
        mn = BARE_NUM.match(line)
        if mn:
            # bare/glued numbered answer line, e.g. "316 x+y=32" or "316x+y=32"
            hits = self._digit_hits(mn.group(1), mn.group(2))
            if len(hits) == 1:
                n, body = hits[0]
                if self._would_resplit(n, body):
                    if self._corr_resolve(mn.group(1), mn.group(2),
                                          line, line_no):
                        return None
                    self.flag(line_no, "bare-num-ambiguous",
                              f"{line.strip()[:40]} "
                              f"(ambiguous: {n} would re-split)")
                    return line
                self._split_emitted(n, body, line, line_no, None, "bare")
                return None
            if self._corr_resolve(mn.group(1), mn.group(2), line, line_no):
                return None
            if len(hits) > 1:
                cands = " or ".join(str(h[0]) for h in hits)
                self.flag(line_no, "bare-num-ambiguous",
                          f"{line.strip()[:40]} (ambiguous: {cands})")
                return line
        ml = LABEL_BARE.match(line)
        if ml and "a" <= ml.group(1) <= "z":
            expected_part = "a" if self.part is None \
                else chr(ord(self.part) + 1)
            if ml.group(1) == expected_part:
                self.part = ml.group(1)
                self.ans_label += 1
                self.notes.append(
                    f"{self.name}:{line_no} [label-bold] {line.strip()[:64]}")
                return f"**{ml.group(1)}** {ml.group(2)}"
        return line

    def run(self):
        raw = self.orig.split("\n")
        for i, line in enumerate(raw, 1):
            stripped = line.strip()
            if self.skip_after:
                # discard a deleted/overridden answer's old body until the
                # next anchor, a non-##### heading, or a line that a different
                # correction owns (its content belongs to another answer)
                am = ANCHOR_RE.match(stripped)
                if am:
                    if self._is_deleted(am.group(1)):
                        continue
                    self.skip_after = False
                    self.skip_pid = None
                    self.last_anchor_id = am.group(1)
                    self.out.append(line)
                    continue
                if stripped.startswith("#"):
                    if re.match(r"^#{5}\s+(?:Answer|Question)\b", stripped):
                        continue
                    self.skip_after = False
                    self.skip_pid = None
                else:
                    owner = self._corr_owner(stripped)
                    if owner is not None and owner != self.skip_pid:
                        self.skip_after = False
                        self.skip_pid = None
                    else:
                        continue
            if self.full:
                am = ANCHOR_RE.match(stripped)
                if am:
                    if self._is_deleted(am.group(1)):
                        self.skip_after = True
                        self.skip_pid = am.group(1)
                        continue
                    self.last_anchor_id = am.group(1)
                    self.out.append(line)
                    continue
            if self.callouts:
                cm = CALL_RE.match(stripped)
                if cm:
                    self.end_block()
                    self.in_callout = False
                    self.in_existing_callout = True
                    self.cnt["kp" if cm.group(2).startswith("KEY POINT ")
                              else "boxes"] += 1
                    self.out.append(line)
                    continue
                if self.in_existing_callout:
                    if stripped.startswith(">"):
                        self.out.append(line)
                        continue
                    self.in_existing_callout = False
                if self.in_callout:
                    if is_structural(stripped):
                        self.in_callout = False
                    else:
                        self.out.append("> " + line.lstrip() if stripped
                                        else ">")
                        continue
            if self.in_math:
                self.out.append(line)
                if stripped == "$$":
                    self.in_math = False
                continue
            if stripped == "$$":
                self.in_math = True
                self.out.append(line)
                continue
            if stripped.startswith("|"):
                self.out.append(line)
                continue
            if self.full:
                self.full_line(stripped, i)
            else:
                self.light_line(line, stripped)
        self._finish_blocks()
        return "\n".join(self.out)

    def light_line(self, line, stripped):
        if stripped.startswith("#"):
            m = SEC_RE.match(stripped)
            if m:
                if len(m.group(1)) > 2:
                    self.out.append("## " + m.group(2) + m.group(3))
                else:
                    self.out.append(line)
                return
            if GEN_H2.match(stripped):
                self.out.append("###" + line[2:])
                return
            self.out.append(line)
            return
        self.out.append(wrap_marks(line))

    def full_line(self, stripped, i):
        if KP_TRAIL.match(stripped):
            self.end_block()
            self.flag(i, "box-trailing", stripped)
            self.out.append(stripped)
            return
        m = KP_RE.match(stripped)
        if m:
            self.end_block()
            self.cnt["kp"] += 1
            title = f"KEY POINT {m.group(1)}"
            self.box_emit("KEY POINT", title,
                          f"ch{self.chapter:02d}-kp-{m.group(1)}")
            return
        m = EXPLORE_RE.match(stripped)
        if m:
            self.end_block()
            self.cnt["boxes"] += 1
            self.box_emit("EXPLORE", f"EXPLORE {m.group(1)}", None)
            return
        m = DYK_RE.match(stripped)
        if m:
            self.end_block()
            self.cnt["boxes"] += 1
            self.box_emit("DID YOU KNOW", "DID YOU KNOW?", None)
            return
        for text in ("REWIND", "FAST FORWARD", "TIP"):
            rx = {"REWIND": REWIND_RE, "FAST FORWARD": FF_RE,
                  "TIP": TIP_RE}[text]
            if rx.match(stripped):
                self.end_block()
                self.cnt["boxes"] += 1
                self.box_emit(text, text, None)
                return
        m = WE_RE.match(stripped)
        if m:
            self.end_block()
            self.cnt["we"] += 1
            self.add_heading(f"ch{self.chapter:02d}-we-{m.group(1)}",
                             f"#### WORKED EXAMPLE {m.group(1)}")
            return
        pre = "" if self.ch_side else "ans-"
        m = REVIEW_RE.match(stripped)
        if m:
            self.start_block("review", f"ch{self.chapter:02d}-{pre}review")
            self.cnt["reviews"] += 1
            self.add_heading(f"ch{self.chapter:02d}-{pre}review",
                             f"### END-OF-CHAPTER REVIEW EXERCISE {m.group(1)}")
            return
        m = CROSS_RE.match(stripped)
        if m:
            self.start_block("cross", f"ch{self.chapter:02d}-{pre}cross")
            self.cnt["cross"] += 1
            self.add_heading(f"ch{self.chapter:02d}-{pre}cross",
                             f"### CROSS-TOPIC REVIEW EXERCISE {m.group(1)}")
            return
        m = PREREQ_RE.match(stripped)
        if m:
            self.start_block("prerequisite",
                             f"ch{self.chapter:02d}-{pre}prerequisite")
            self.cnt["prereq"] += 1
            self.add_heading(f"ch{self.chapter:02d}-{pre}prerequisite",
                             "### PREREQUISITE KNOWLEDGE")
            return
        m = EX_RE.match(stripped)
        if m:
            base = f"{pre}ex{m.group(1)}{m.group(2)}"
            self.start_block("exercise", f"ch{self.chapter:02d}-{base}")
            self.cnt["exercises"] += 1
            self.add_heading(f"ch{self.chapter:02d}-{base}",
                             f"### EXERCISE {m.group(1)}{m.group(2)}")
            return
        if stripped.startswith("#"):
            if self.ch_side and self.block is not None \
                    and stripped.startswith("##### Question"):
                qm = re.match(r"^##### Question(?:\s+(PS|P|M))?\s+(\d+)\s*$",
                              stripped)
                if qm:
                    # already-converted question: keep the block active so a
                    # later raw **N** can still be attributed to this block
                    n = int(qm.group(2))
                    pid = self.last_anchor_id
                    if not (pid and pid.startswith(self.block_base + "-")):
                        pid = f"{self.block_base}-q{n}"
                    body = self._corr_body(self.q_corr, pid)
                    if body == "delete":
                        self.skip_after = True
                        self.skip_pid = pid
                        return
                    self.prev = n
                    self.part = None
                    self.log_num(n)
                    self.out.append(stripped)
                    if body is not None:
                        self._emitted.add(pid)
                        self.corr_applied.add(pid)
                        self.corr_notes.append(
                            f"{self.name}:{i} [corr-override] {pid}")
                        for bl in body:
                            self.out.append(wrap_marks(bl))
                        self.out.append("")
                        self.skip_after = True
                        self.skip_pid = pid
                    return
            if not self.ch_side and self.block is not None \
                    and stripped.startswith("##### Answer"):
                am = re.match(r"^##### Answer(?: PS| P)? (\d+)\s*$", stripped)
                if am:
                    n = int(am.group(1))
                    pid = self.last_anchor_id
                    if not (pid and pid.startswith(self.block_base + "-")):
                        pid = f"{self.block_base}-q{n}"
                    body = self._corr_body(self.ans_corr, pid)
                    if body == "delete":
                        self.skip_after = True
                        self.skip_pid = pid
                        return
                    self.prev = n
                    self.part = None
                    self.log_num(n)
                    self.out.append(stripped)
                    if body is not None:
                        self._emitted.add(pid)
                        self.corr_applied.add(pid)
                        self.corr_notes.append(
                            f"{self.name}:{i} [corr-override] {pid}")
                        for bl in body:
                            self.out.append(wrap_marks(bl))
                        self.out.append("")
                        self.skip_after = True
                        self.skip_pid = pid
                    return
            if EMPTY_H.match(stripped):
                # an empty heading is just a separator inside a review block;
                # keep the block active (do NOT end_block) so questions after
                # it are still attributed to the same block.
                self.flag(i, "empty-heading", stripped)
                self.out.append(stripped)
                return
            m = SEC_RE.match(stripped)
            if m:
                self.end_block()
                self.cnt["sections"] += 1
                if len(m.group(1)) > 2:
                    self.out.append("## " + m.group(2) + m.group(3))
                else:
                    self.out.append(stripped)
                return
            if STRAY_H.match(stripped) and self.ch_side:
                self.end_block()
                self.flag(i, "stray-h2", stripped)
                self.out.append(stripped)
                return
            if GEN_H2.match(stripped):
                self.end_block()
                self.cnt["generic"] += 1
                self.out.append("###" + stripped[2:])
                return
            self.end_block()
            self.out.append(stripped)
            return
        if self.block is not None:
            res = self.process_block_question(stripped, i)
            if res is None:
                return
            if res != stripped:
                self.out.append(res)
                return
        cm = CITE_RE.match(stripped)
        if cm and not stripped.startswith("*"):
            self.cnt["citations"] += 1
            self.out.append("*" + stripped + "*")
            return
        self.out.append(wrap_marks(stripped))

    def box_emit(self, name, title, aid):
        if self.callouts:
            self.out.append(f"> [!{CALL_TYPE[name]}] {title}")
            self.in_callout = True
        elif aid:
            self.add_heading(aid, f"#### {title}")
        else:
            self.out.append(f"#### {title}")

    @property
    def new_text(self):
        text = "\n".join(self.out)
        if not text.endswith("\n"):
            text += "\n"
        return text


EX_HEAD_KIND = [
    (r"^### END-OF-CHAPTER REVIEW EXERCISE \d+", "review"),
    (r"^### CROSS-TOPIC REVIEW EXERCISE \d+", "cross"),
    (r"^### PREREQUISITE KNOWLEDGE\s*$", "prerequisite"),
    (r"^### EXERCISE \d+[A-Z]\s*$", "exercise"),
    (r"^#### WORKED EXAMPLE \d+\.\d+\s*$", "worked-example"),
    (r"^#### KEY POINT \d+\.\d+\s*$", "key-point"),
]


def parse_entries(name, text):
    """Build the id-keyed index by parsing the (final) text: each anchor
    followed by its heading. Run-count independent."""
    mch = CH_RE.match(name)
    mans = ANS_RE.match(name)
    chapter = int(mch.group(1)) if mch else (int(mans.group(1)) if mans else 0)
    ch_side = bool(mch)
    entries = {}
    pending_id = None
    pending_line = None
    for ln, line in enumerate(text.split("\n"), 1):
        am = ANCHOR_RE.match(line)
        if am:
            pending_id, pending_line = am.group(1), ln
            continue
        if pending_id is None:
            continue
        typ = kind = None
        if line.startswith("##### "):
            if ch_side:
                typ = "question"
            else:
                typ = "answer"
            kind = None
        else:
            cm = CALL_RE.match(line)
            if cm and cm.group(2).startswith("KEY POINT "):
                typ, kind = "key-point", "key-point"
            else:
                for rx, k in EX_HEAD_KIND:
                    if re.match(rx, line):
                        typ = "exercise" if k in ("exercise", "review",
                                                  "cross", "prerequisite") \
                            else k
                        kind = k
                        break
        if typ:
            e = {"id": pending_id, "type": typ, "chapter": chapter,
                 "file": name, "line": pending_line}
            if kind:
                e["kind"] = kind
            entries[pending_id] = e
        pending_id = pending_line = None
    return entries


def add_next_ids(entries):
    by_file = defaultdict(list)
    for e in entries.values():
        by_file[e["file"]].append(e)
    for lst in by_file.values():
        lst.sort(key=lambda e: e["line"])
        for k, e in enumerate(lst):
            e["next_id"] = lst[k + 1]["id"] if k + 1 < len(lst) else None


def report(results, files, entries, ans_corr=None, q_corr=None):
    print("per-file counts:")
    hdr_keys = ["sections", "exercises", "reviews", "cross", "prereq",
                "boxes", "we", "kp", "question", "answer", "msplit", "bare",
                "lbl", "citations", "generic", "flags"]
    width = max(len(f) for f in files) + 2
    print(("  " + "file").ljust(width + 7), *hdr_keys)
    grand = Counter()
    for f in files:
        c = results[f].cnt
        c["msplit"], c["lbl"] = results[f].ans_mathsplit, results[f].ans_label
        c["bare"] = results[f].ans_bare
        grand.update(c)
        print("  " + f.ljust(width),
              *[str(c.get(k, "")).rjust(9 if k == "flags" else 2)
                for k in hdr_keys])
    print("  " + "total".ljust(width),
          *[str(grand.get(k, "")).rjust(9 if k == "flags" else 2)
            for k in hdr_keys])

    notes = [n for f in files for n in results[f].notes]
    print(f"\nanswer-file lines affected ({len(notes)}):")
    for n in notes:
        print("  " + n)
    if not notes:
        print("  (none)")

    corr_notes = [n for f in files for n in results[f].corr_notes]
    print(f"\ncorrections applied ({len(corr_notes)}):")
    for n in corr_notes:
        print("  " + n)
    if not corr_notes:
        print("  (none)")

    flags = [fl for f in files for fl in results[f].flags]
    print(f"\nflagged lines ({len(flags)}):")
    for fl in flags:
        print("  " + fl)
    if not flags:
        print("  (none)")

    print("\ngaps in answer numbering per block (missing in 1..max):")
    nada = True
    for f in files:
        for rec in results[f].block_log:
            nums = sorted(set(rec["nums"]))
            if not nums:
                continue
            present = set(nums)
            missing = [i for i in range(1, nums[-1] + 1)
                       if i not in present]
            if missing:
                print(f"  {results[f].name} {rec['base']}: "
                      f"missing {missing}")
                nada = False
    if nada:
        print("  (none)")

    all_q = [aid for aid, e in entries.items() if e["type"] == "question"]
    all_a = [aid for aid, e in entries.items() if e["type"] == "answer"]
    qnorm = {norm_qid(q) for q in all_q}
    anorm = {norm_qid(a) for a in all_a}
    unmatched = sorted(q for q in all_q if norm_qid(q) not in anorm)
    print(f"\nchapter-side questions with no matching answer id"
          f" ({len(unmatched)}):")
    for u in unmatched:
        print("  " + u)
    extra = sorted(a for a in all_a if norm_qid(a) not in qnorm)
    print(f"\nanswer-side ids with no matching question id ({len(extra)}):"
          + (f"  e.g. {extra[:10]}" if extra else ""))

    dup = Counter()
    for f in files:
        for ln in results[f].new_text.split("\n"):
            am = ANCHOR_RE.match(ln.strip())
            if am:
                dup[am.group(1)] += 1
    dup = [k for k, v in dup.items() if v > 1]
    print(f"\nduplicate anchor ids: {len(dup)}"
          + (f" -> {dup[:20]}" if dup else ""))

    if ans_corr or q_corr:
        applied = set()
        for f in files:
            applied |= results[f].corr_applied
        unused = sorted(
            (set(ans_corr) | set(q_corr)) - applied)
        print(f"\ncorrections ids not applied ({len(unused)}):"
              + (f" -> {unused[:20]}" if unused else ""))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("split", nargs="?",
                    default="Maths Pure 2 & 3-clean_MD/split")
    ap.add_argument("-n", "--dry-run", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--callouts", action="store_true",
                    help="wrap box headers in [!IMPORTANT]/[!NOTE]/[!TIP] "
                         "callouts instead of #### headings (off by default)")
    ap.add_argument("--corrections", default=None,
                    help="corrections JSON (default: scripts/corrections.json)")
    args = ap.parse_args(argv)

    p_dir = Path(args.split)
    if not p_dir.is_dir():
        sys.exit(f"not a directory: {p_dir}")
    files = sorted(p.name for p in p_dir.glob("*.md"))
    if not files:
        sys.exit(f"no .md files in {p_dir}")

    corr_path = Path(args.corrections) if args.corrections \
        else Path(__file__).resolve().parent / "corrections.json"

    ans_corr, q_corr = {}, {}
    if corr_path.exists():
        data = json.loads(corr_path.read_text(encoding="utf-8"))
        ans_corr = data.get("answers", {})
        q_corr = data.get("questions", {})
    else:
        print(f"(no corrections file at {corr_path})")

    results = {}
    text_of = {}

    def collect_nums(fprocs, normalize_ans):
        """block base -> set of numbers, from the final run of each file."""
        nums = {}
        for f in fprocs:
            for rec in fprocs[f].block_log:
                base = rec["base"]
                if normalize_ans:
                    base = re.sub(r"-ans-", "-", base, count=1)
                nums.setdefault(base, set()).update(rec["nums"])
        return nums

    ans_nums = {}
    ch_qnums = {}
    # Converge to a fixed point: the chapter-side promotion uses the answer
    # set as ground truth and the answer-side split uses the chapter question
    # set, so the two can feed each other (each pass only adds numbers, so it
    # terminates quickly).
    def freeze(nums):
        return frozenset((k, frozenset(v)) for k, v in nums.items())

    converged = False
    for _ in range(10):
        prev = (freeze(ans_nums), freeze(ch_qnums))
        # pass A: answer files (chapter questions as ground truth for $N splits)
        for f in files:
            if f.startswith("ans"):
                results[f] = FileProcessor(p_dir / f, callouts=args.callouts,
                                           ch_qnums=ch_qnums,
                                           ans_corr=ans_corr)
                results[f].run()
                text_of[f] = results[f].new_text
        ans_nums = collect_nums(results, normalize_ans=True)
        # pass B: chapter files (answer set as ground truth for promotion)
        for f in files:
            if f.startswith("ans"):
                continue
            results[f] = FileProcessor(p_dir / f, callouts=args.callouts,
                                       ans_nums=ans_nums,
                                       q_corr=q_corr)
            results[f].run()
            text_of[f] = results[f].new_text
        ch_qnums = collect_nums(results, normalize_ans=False)
        if (freeze(ans_nums), freeze(ch_qnums)) == prev:
            converged = True
            break
    if not converged:
        print("WARNING: fix_sections fixed-point loop did not converge after "
              "10 iterations; chapter/answer numbers kept changing. The last "
              "round's output was used.", file=sys.stderr)

    if args.check:
        disk = {f: (p_dir / f).read_text(encoding="utf-8") for f in files}
        diffs = [f for f in files if text_of[f] != disk[f]]
        entries = {}
        for f in files:
            entries.update(parse_entries(f, disk[f]))
        report(results, files, entries, ans_corr, q_corr)
        print(f"\n[check] files that changed on re-run: {len(diffs)}"
              + (f" -> {diffs}" if diffs else ""))
        return

    entries = {}
    for f in files:
        entries.update(parse_entries(f, text_of[f]))
    report(results, files, entries, ans_corr, q_corr)

    if args.dry_run:
        print("\n[dry run] nothing was written.")
        return

    for f in files:
        if text_of[f] != results[f].orig:
            (p_dir / f).write_text(text_of[f], encoding="utf-8")
    add_next_ids(entries)
    (p_dir / "index.json").write_text(
        json.dumps(entries, indent=1, sort_keys=True) + "\n",
        encoding="utf-8")
    print(f"\nwrote files in place + index.json in {p_dir}")
    print("re-run with --check to verify idempotency, anchors and matching.")


if __name__ == "__main__":
    import sys
    main()