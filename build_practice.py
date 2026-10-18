#!/usr/bin/env python3
"""Practice pages: per-chapter exercises + key points, plus a filter toolbar.
Usage (standalone, after build_site.py):  python build_practice.py [book_dir]
Or just run build_site.py, which calls generate() for you.
Only writes under site/docs/; never touches split/, images/ or the source.
The .qa/.kp containers are *blockquotes* (core Markdown), not raw-HTML divs:
markdown-in-html divs are unreliable for this content in Python-Markdown.
"""
import argparse
import json
import re
import shutil
from pathlib import Path

BOOK_DEFAULT = Path("Maths Pure 2 & 3-clean_MD")

ANCHOR = '<a id="{}"></a>'
ANCHOR_RE = re.compile(r'^<a id="[^"]+"></a>$')
HEAD_RE = re.compile(r"^#{1,6}\s+(.*)$")
HEAVY_RE = re.compile(r"^(?:\||\$\$?|!\[|\\|[-*+]\s|\d+[.)]\s)")
QID_RE = re.compile(r"^(ch\d\d)-(.+?)-(?:q|ps|p)(\d+)$")


def _shared():
    from build_site import align_fix, reflow, page_title
    return align_fix, reflow, page_title


def slice_to_next(lines, anchor_id, next_id):
    start = end = None
    for i, ln in enumerate(lines):
        if start is None and ANCHOR.format(anchor_id) in ln:
            start = i
        elif start is not None and next_id and ANCHOR.format(next_id) in ln:
            end = i
            break
    if start is None:
        return []
    return lines[start + 1: (end if end is not None else len(lines))]


def strip_headings_and_anchors(lines):
    out = []
    for ln in lines:
        if ANCHOR_RE.match(ln.strip()) or HEAD_RE.match(ln.strip()):
            continue
        out.append(ln)
    return out


def tight_content(lines):
    """Content after a key point header: keep contiguous content up to the
    first blank line + plain prose paragraph; table/$$/list/image lines stay
    attached; a heading or an anchor ends it."""
    body, pending = [], []
    for ln in lines:
        s = ln.strip()
        if s == "":
            pending.append(ln)
            continue
        if s.startswith("#") or s.startswith("<a id"):
            break
        if HEAVY_RE.match(s):
            body += pending + [ln]
            pending = []
            continue
        if body:
            break
        body += pending + [ln]
        pending = []
    return body


def keypoint_body(lines, anchor_id, next_id, full):
    blk = slice_to_next(lines, anchor_id, next_id)
    k = 0
    while k < len(blk) and not blk[k].strip():
        k += 1
    if k < len(blk) and blk[k].lstrip().startswith("#"):
        blk = blk[k + 1:]
    while blk and not blk[0].strip():
        blk = blk[1:]
    while blk and not blk[-1].strip():
        blk = blk[:-1]
    return blk if full else tight_content(blk)


def answer_id_for(qid):
    m = QID_RE.match(qid)
    if not m:
        return None
    return f"{m.group(1)}-ans-{m.group(2)}-q{m.group(3)}"


def first_heading(lines):
    for ln in lines:
        m = HEAD_RE.match(ln.strip())
        if m:
            return m.group(1).strip()
    return ""


def anchor_pos(lines, anchor_id):
    for i, ln in enumerate(lines):
        if ANCHOR.format(anchor_id) in ln:
            return i
    return 10 ** 9


def attr(s):
    return s.replace('"', "'")


def blockquote(lines, cls, data_section):
    return lines


def toolbar_html():
    return ('<div id="practice-toolbar">\n'
            '  <select id="pt-select" aria-label="Section">'
            '<option value="All">All sections</option></select>\n'
            '  <input id="pt-text" type="search" '
            'placeholder="Filter by text..." aria-label="Filter">\n'
            '  <button id="pt-expand" type="button">Expand all answers</button>\n'
            '  <button id="pt-collapse" type="button">Collapse all</button>\n'
            '  <span id="pt-count"></span>\n'
            '</div>')


def exercise_page(lines, fname, ch_title, idx):
    out = [f"# {ch_title} — Exercises", "", toolbar_html(), ""]
    stats = {"questions": 0, "linked": 0, "unlinked": []}
    entries = []
    for iid, e in idx.items():
        if e["file"] == fname and e["type"] in ("exercise", "question"):
            entries.append((iid, e["type"]))
    entries.sort(key=lambda t: anchor_pos(lines, t[0]))

    sec_title = None
    pending_note = None
    for iid, typ in entries:
        e = idx[iid]
        if typ == "exercise":
            if pending_note is not None:
                out += ["", pending_note, ""]
            blk = slice_to_next(lines, iid, e.get("next_id"))
            sec_title = first_heading(blk) or iid
            out += ["", f"## {sec_title} "
                        f'{{data-section="{attr(sec_title)}"}}', ""]
            pending_note = ("*No question blocks here — the questions appear "
                            "in a table on the source page.*")
            continue
        if sec_title is None:
            continue
        pending_note = None
        m = QID_RE.match(iid)
        if not m:
            continue
        num = m.group(3)
        sfx = iid.rsplit("-", 1)[1]
        tag = "PS" if sfx.startswith("ps") else ("P" if sfx.startswith("p")
                                                 else "")
        blk = slice_to_next(lines, iid, e.get("next_id"))
        body = strip_headings_and_anchors(blk)
        while body and not body[0].strip():
            body.pop(0)
        while body and not body[-1].strip():
            body.pop()

        qa = [f"### Question {tag + ' ' if tag else ''}{num}", ""]
        qa += body
        qa += ["", f"[source](../split/{fname}#{iid})"]
        out += ['<div class="qa" markdown="1" '
                f'data-section="{attr(sec_title)}">', ""] + qa + ["",
                                                                    "</div>"]
        aid = answer_id_for(iid)
        if aid and aid in idx:
            an = idx[aid]
            ans_lines = slice_to_next(file_lines(an["file"]), aid,
                                      an.get("next_id"))
            ans_body = strip_headings_and_anchors(ans_lines)
            while ans_body and not ans_body[0].strip():
                ans_body.pop(0)
            while ans_body and not ans_body[-1].strip():
                ans_body.pop()
            details = ['??? success "Answer"']
            details += [("    " + ln) if ln.strip() else "" for ln in ans_body]
            out += ["", *details, ""]
            stats["linked"] += 1
        else:
            out += ["", "*Answer not linked*", ""]
            stats["unlinked"].append(iid)
        stats["questions"] += 1
    if pending_note is not None:
        out += ["", pending_note, ""]
    return out, stats


_BOOK = None
_CACHE = {}


def balance_dollars(lines):
    """Drop a stray trailing `$` on any non-math line with an odd count of
    `$`, so arithmatex never pairs a lone dollar across following lines."""
    out, in_block = [], False
    for ln in lines:
        s = ln.strip()
        if s.startswith("$$"):
            in_block = not in_block
            out.append(ln)
            continue
        if in_block or s.startswith("|"):
            out.append(ln)
            continue
        if ln.count("$") % 2 == 1:
            k = ln.rfind("$")
            ln = ln[:k] + ln[k + 1:]
        out.append(ln)
    return out


def file_lines(fname):
    if fname not in _CACHE:
        _CACHE[fname] = (Path(_BOOK) / "split" / fname) \
            .read_text(encoding="utf-8").split("\n")
    return _CACHE[fname]


def generate(docs_dir, book_dir=None, full_keypoints=False,
             boldsymbol_to_mathbf=False):
    global _BOOK, _CACHE, BOOK_DEFAULT
    _BOOK = str(Path(book_dir) if book_dir else BOOK_DEFAULT)
    BOOK_DEFAULT = Path(_BOOK)
    _CACHE = {}
    split = Path(_BOOK) / "split"
    docs = Path(docs_dir)
    practice = docs / "practice"

    align_fix, reflow, page_title = _shared()

    idx = json.loads((split / "index.json").read_text(encoding="utf-8"))
    print("index types:", sorted({e["type"] for e in idx.values()}))
    print("index keys:", len(idx))

    chmap = {}
    for p in split.glob("ch??-*.md"):
        m = re.match(r"^ch(\d\d)-", p.name)
        if m:
            chmap[int(m.group(1))] = p.name

    if practice.exists():
        shutil.rmtree(practice)
    practice.mkdir(parents=True)
    (docs / "stylesheets").mkdir(exist_ok=True)
    (docs / "javascripts").mkdir(exist_ok=True)

    summary = {"chapters": [],
               "totals": {"exercise_pages": 0, "questions": 0, "linked": 0,
                          "unlinked": 0, "keypoints": 0},
               "unlinked_all": []}
    kp_odd = []
    chapter_kps = {}

    for n in sorted(chmap):
        fname = chmap[n]
        ch_title = page_title(split / fname)
        lines = file_lines(fname)

        # ---- exercise page --------------
        md, st = exercise_page(lines, fname, ch_title, idx)
        text = align_fix("\n".join(md) + "\n")
        out, _, _ = reflow(text.split("\n"))
        out = balance_dollars(out)
        ex_file = f"ch{n:02d}-exercises.md"
        (practice / ex_file).write_text("\n".join(out) + "\n",
                                        encoding="utf-8")
        t = summary["totals"]
        t["exercise_pages"] += 1
        t["questions"] += st["questions"]
        t["linked"] += st["linked"]
        t["unlinked"] += len(st["unlinked"])
        summary["unlinked_all"].extend(st["unlinked"])

        # ---- key points --------------
        kps = []
        for iid, e in sorted(((i, e) for i, e in idx.items()
                              if e["file"] == fname
                              and e["type"] == "key-point"),
                             key=lambda t: anchor_pos(lines, t[0])):
            body = keypoint_body(lines, iid, e.get("next_id"),
                                 full_keypoints)
            ktitle = first_heading(
                slice_to_next(lines, iid, e.get("next_id"))) or iid
            if len(body) < 2 or len(body) > 40:
                kp_odd.append((fname, iid, len(body)))
            kps.append((ktitle, body, iid))
        chapter_kps[n] = kps

        kp_md = [f"# {ch_title} — Key points", "", toolbar_html(), ""]
        for ktitle, body, iid in kps:
            kq = [f"## {ktitle}", ""]
            kq += body
            kq += ["", f"[see in context](../split/{fname}#{iid})"]
            kp_md += blockquote(kq, "kp", ktitle)
            kp_md += [""]
        text = align_fix("\n".join(kp_md) + "\n")
        out, _, _ = reflow(text.split("\n"))
        out = balance_dollars(out)
        kp_file = f"ch{n:02d}-keypoints.md"
        (practice / kp_file).write_text("\n".join(out) + "\n",
                                        encoding="utf-8")
        t["keypoints"] += len(kps)

        summary["chapters"].append({
            "num": n, "title": ch_title, "exercises": ex_file,
            "keypoints": kp_file, "keypoint_count": len(kps),
            "questions": st["questions"], "linked": st["linked"],
            "unlinked": st["unlinked"]})

    # ---- combined all-keypoints -------
    ak = ["# All key points", "", toolbar_html(), ""]
    for n in sorted(chapter_kps):
        if not chapter_kps[n]:
            continue
        ch_title = summary["chapters"][n - 1]["title"]
        ak += ["", f"## {ch_title} {{data-section=\"{attr(ch_title)}\"}}", ""]
        for ktitle, body, iid in chapter_kps[n]:
            kq = [f"### {ktitle}", ""]
            kq += body
            kq += ["", f"[see in context](../split/{chmap[n]}#{iid})"]
            ak += blockquote(kq, "kp", ch_title)
            ak += [""]
    text = align_fix("\n".join(ak) + "\n")
    out, _, _ = reflow(text.split("\n"))
    out = balance_dollars(out)
    (practice / "all-keypoints.md").write_text("\n".join(out) + "\n",
                                               encoding="utf-8")

    # ---- practice landing page -------
    pl = ["# Practice", "",
          "Per-chapter exercise pages (with collapsible answers) and "
          "key-point round-ups.", "", "## Chapters", ""]
    for c in summary["chapters"]:
        pl.append(f"- **{c['title']}** — "
                  f"[exercises]({c['exercises']}) · "
                  f"[key points]({c['keypoints']})")
    pl += ["", "- [All key points](all-keypoints.md)", ""]
    text = align_fix("\n".join(pl) + "\n")
    out, _, _ = reflow(text.split("\n"))
    out = balance_dollars(out)
    (practice / "index.md").write_text("\n".join(out) + "\n",
                                       encoding="utf-8")

    (docs / "stylesheets" / "practice.css").write_text(CSS, encoding="utf-8")
    (docs / "javascripts" / "practice-filter.js").write_text(JS,
                                                             encoding="utf-8")

    # ---- report -------
    print(f"exercise pages: {t['exercise_pages']}")
    print(f"questions rendered: {t['questions']}")
    print(f"questions with a linked answer: {t['linked']}")
    print(f"questions 'Answer not linked' ({t['unlinked']}):")
    for u in summary["unlinked_all"]:
        print("   " + u)
    print("key points per chapter:")
    for c in summary["chapters"]:
        print(f"   ch{c['num']:02d} {c['title']}: {c['keypoint_count']}")
    print(f"total key points: {t['keypoints']}")
    print(f"key points where the tight rule may be wrong "
          f"(body <2 or >40 lines, {len(kp_odd)}):")
    for f, iid, ln in sorted(kp_odd):
        print(f"   {iid} ({f}) body={ln} lines")
    return summary


CSS = """\
#practice-toolbar {
  display: flex; flex-wrap: wrap; gap: .5rem; align-items: center;
  padding: .6rem .8rem; margin-bottom: 1rem; border: 1px solid
  var(--md-default-fg-color--lightest); border-radius: .4rem;
}
#practice-toolbar input[type=search] { flex: 1 1 12rem; min-width: 8rem; }
#pt-count { margin-left: auto; color: var(--md-default-fg-color--light); }
.qa, .kp {
  padding: .2rem 1rem .6rem; margin: 1rem 0;
  background: var(--md-default-bg-color);
  border-left: .25rem solid var(--md-primary-fg-color);
}
.qa > details.success > summary { cursor: pointer; font-weight: 700; }
@media (min-width: 900px) {
  .qa { display: grid; grid-template-columns: 1fr 1fr;
        column-gap: 1.6rem; }
  .qa > details { grid-column: 2; grid-row: 1 / -1; }
}
"""

JS = """\
(function () {
  function init() {
    var toolbar = document.getElementById('practice-toolbar');
    if (!toolbar) return;
    var select = document.getElementById('pt-select');
    var text = document.getElementById('pt-text');
    var expand = document.getElementById('pt-expand');
    var collapse = document.getElementById('pt-collapse');
    var count = document.getElementById('pt-count');
    var items = Array.prototype.slice.call(
      document.querySelectorAll('.qa, .kp'));
    var headings = Array.prototype.slice.call(
      document.querySelectorAll('h1, h2, h3, h4, h5, h6[data-section]'));
    var hasAnswers = !!document.querySelector('.qa details');

    var order = [], seen = {};
    document.querySelectorAll('[data-section]').forEach(function (el) {
      var v = el.getAttribute('data-section') || '';
      if (!(v in seen)) { seen[v] = 1; order.push(v); }
    });
    order.forEach(function (v) {
      var o = document.createElement('option');
      o.value = v; o.textContent = v; select.appendChild(o);
    });
    if (!hasAnswers) {
      expand.style.display = collapse.style.display = 'none';
    }

    function apply() {
      var q = (text.value || '').trim().toLowerCase();
      var sel = select.value;
      var vis = 0;
      items.forEach(function (it) {
        var sec = it.getAttribute('data-section') || '';
        var secOk = (sel === 'All' || sec === sel);
        var txtOk = !q || it.textContent.toLowerCase().indexOf(q) !== -1;
        it.style.display = (secOk && txtOk) ? '' : 'none';
        if (secOk && txtOk) vis++;
      });
      headings.forEach(function (el) {
        var sec = el.getAttribute('data-section') || '';
        var secOk = (sel === 'All' || sel === sec);
        if (!secOk) { el.style.display = 'none'; return; }
        var any = items.some(function (it) {
          return it.getAttribute('data-section') === sec &&
                 it.style.display !== 'none';
        });
        el.style.display = (!q || any) ? '' : 'none';
      });
      if (count) count.textContent = vis ? (vis + ' shown') : '0 shown';
    }
    select.addEventListener('change', apply);
    text.addEventListener('input', apply);
    expand.addEventListener('click', function () {
      document.querySelectorAll('.qa details').forEach(function (d) {
        d.open = true;
      });
    });
    collapse.addEventListener('click', function () {
      document.querySelectorAll('.qa details').forEach(function (d) {
        d.open = false;
      });
    });
    apply();
  }
  if (typeof document$ !== 'undefined' && document$.subscribe) {
    document$.subscribe(init);
  } else {
    document.addEventListener('DOMContentLoaded', init);
  }
})();
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book", nargs="?", default=str(BOOK_DEFAULT))
    ap.add_argument("--full-keypoints", action="store_true")
    ap.add_argument("--boldsymbol-to-mathbf", action="store_true")
    args = ap.parse_args()
    generate(Path("site/docs"), args.book, full_keypoints=args.full_keypoints)


if __name__ == "__main__":
    main()