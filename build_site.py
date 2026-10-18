#!/usr/bin/env python3
"""Build a local MkDocs Material site from the split book + images.
Usage: python build_site.py [book_dir] [--local-mathjax] [--boldsymbol-to-mathbf]
Everything is generated under ./site/ and the book files are never modified.
"""
import argparse
import json
import re
import shutil
import sys
import urllib.request
from pathlib import Path

BOOK_DEFAULT = Path("Maths Pure 2 & 3-clean_MD")
MATHJAX_CDN = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
BOLDSYMBOL_EXT = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/input/tex/" \
                 "extensions/boldsymbol.js"

CH_RE = re.compile(r"^ch(\d+)-")
H1_RE = re.compile(r"^#\s+(.*)$")

# normalise inline maths arithmatex rejects: "$ x" / "x $" cases ->
# "$x".  Openers are guarded by (start|whitespace) before the $ and
# non-space after, so "$x$ and $y$" is never touched.
OPEN_SPACE = re.compile(r"(?<![\S])\$[ \t]+(?=[^ \t])")
CLOSE_SPACE = re.compile(r"[ \t]+\$(?=[ \t.,;:!?)\]}]|$)")
# "$ x = 2 $" written on one line -> its own $$..$$ block
SAME_LINE_DOLLARS = re.compile(r"\$\$(?:\s*)([^$]+?)(?:\s*)\$\$")

# crude LaTeX -> plain text for maths inside headings (sidebar/TOC can't
# typeset).  Ordered: operatorname first (may be spaced/nested), then the
# unbrace-able formatting commands, then \frac/\sqrt, then a symbol map.
HEAD_MATH = re.compile(r"\$([^$\n]+?)\$")

SYMBOLS = {"pm": "\u00b1", "cdot": "\u00b7", "cdots": "\u2026",
           "ldots": "\u2026", "to": "\u2192", "Rightarrow": "\u21d2",
           "Leftrightarrow": "\u21d4", "ne": "\u2260", "le": "\u2264",
           "ge": "\u2265", "leq": "\u2264", "geq": "\u2265",
           "infty": "\u221e", "times": "\u00d7", "div": "\u00f7",
           "circ": "\u00b0", "prime": "\u2032", "alpha": "\u03b1",
           "beta": "\u03b2", "theta": "\u03b8", "gamma": "\u03b3",
           "delta": "\u03b4", "pi": "\u03c0", "mu": "\u03bc",
           "lambda": "\u03bb", "phi": "\u03c6", "omega": "\u03c9"}


def math_to_plain(s):
    s = re.sub(r"\\(?:operatorname)\s*\{\s*([^{}]*?)\s*\}",
               lambda m: re.sub(r"\s+", "", m.group(1)), s)
    for cmd in ("boldsymbol", "mathbf", "mathbb", "mathrm", "text"):
        s = re.sub(r"\\" + cmd + r"\s*\{([^{}]*)\}", r"\1", s)
    brace = r"([^{}]*(?:\{[^{}]*\}[^{}]*)*)"
    s = re.sub(r"\\frac\s*\{" + brace + r"\}\s*\{" + brace + r"\}",
               lambda m: m.group(1) + "/" + m.group(2), s)
    s = re.sub(r"\\sqrt(?:\[[^\]]*\])?\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}",
               lambda m: "sqrt(" + m.group(1) + ")", s)
    for cmd, rep in SYMBOLS.items():
        s = s.replace("\\" + cmd, rep)
    s = re.sub(r"\\(?:left|right)\b", "", s)
    s = re.sub(r"\\[a-zA-Z@]+\b", "", s)
    return re.sub(r"\s+", " ", s.replace("\\", "").replace("{", "")
                  .replace("}", "").replace("~", "")).strip()


def page_title(path):
    for ln in path.read_text(encoding="utf-8").splitlines():
        m = H1_RE.match(ln.strip())
        if m:
            return m.group(1).strip()
    return path.stem.replace("-", " ").title()


ALIGN_SUBS = [("\\begin{align*}", "\\begin{aligned*}"),
              ("\\end{align*}", "\\end{aligned*}"),
              ("\\begin{align}", "\\begin{aligned}"),
              ("\\end{align}", "\\end{aligned}")]


def align_fix(text):
    for a, b in ALIGN_SUBS:
        text = text.replace(a, b)
    return text


def reflow(lines, changed_headings=None, fname=None):
    """Per-line markdown normalisation shared by every generated page:
    `$ x $` trims, same-line `$$..$$` blocks, and heading-maths stripping.
    Returns (out_lines, trim_count, dollar_block_count)."""
    out, in_block, trim_n, dollars_n = [], False, 0, 0
    for ln in lines:
        s = ln.lstrip()
        if s.startswith("$$"):
            in_block = not in_block
            out.append(ln)
            continue
        if in_block:
            out.append(ln)
            continue
        new, t = OPEN_SPACE.subn("", ln)
        new, t2 = CLOSE_SPACE.subn("", new)
        trim_n += t + t2
        if not s.startswith("|"):          # never reflow table rows
            new, n = SAME_LINE_DOLLARS.subn(
                lambda m: "$$\n" + m.group(1) + "\n$$", new)
            dollars_n += n
        if s.startswith("#") and "$" in new:   # headings: plain text for TOC
            conv = HEAD_MATH.sub(lambda m: math_to_plain(m.group(1)), new)
            if conv != new and changed_headings is not None:
                changed_headings.append((fname, new.strip(), conv.strip()))
            new = conv
        out.append(new)
    return out, trim_n, dollars_n


def copy_md(src, dst, boldsymbol_to_mathbf=False, changed_headings=None):
    text = src.read_text(encoding="utf-8")
    align_n = sum(text.count(p) for p, _ in ALIGN_SUBS)
    text = align_fix(text)
    bm_n = text.count("\\boldsymbol")
    if boldsymbol_to_mathbf:
        text = text.replace("\\boldsymbol", "\\mathbf")
    out, trim_n, dollars_n = reflow(text.split("\n"), changed_headings,
                                    src.name)
    dst.write_text("\n".join(out) + "\n", encoding="utf-8")
    return align_n, trim_n, dollars_n, bm_n


def fetch(url, dest, timeout=60):
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            dest.write_bytes(r.read())
        return True
    except Exception as e:
        print(f"[local-mathjax] download failed: {e}")
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book", nargs="?", default=str(BOOK_DEFAULT))
    ap.add_argument("--local-mathjax", action="store_true",
                    help="bundle MathJax + the boldsymbol extension into "
                         "site/docs/javascripts/ instead of using the CDN")
    ap.add_argument("--boldsymbol-to-mathbf", action="store_true",
                    help="replace \\boldsymbol with \\mathbf in the copies")
    ap.add_argument("--full-keypoints", action="store_true",
                    help="key point bodies use the full next-anchor slice "
                         "instead of the tight rule (see build_site.py)")
    args = ap.parse_args()

    book = Path(args.book)
    split, images = book / "split", book / "images"
    site, docs = Path("site"), Path("site/docs")
    for p in (docs, site / "site"):
        if p.exists():
            shutil.rmtree(p)
    (docs / "split").mkdir(parents=True)
    (docs / "images").mkdir()
    (docs / "javascripts").mkdir()

    images_copied = 0
    for img in images.glob("*"):
        if img.is_file():
            shutil.copy2(img, docs / "images" / img.name)
            images_copied += 1

    pages, chmap, changed_headings = {}, {}, []
    align_n = trim_n = dollars_n = bm_n = 0
    for md in sorted(split.glob("*.md")):
        a, t, d, b = copy_md(md, docs / "split" / md.name,
                             args.boldsymbol_to_mathbf, changed_headings)
        align_n += a
        trim_n += t
        dollars_n += d
        bm_n += b
        pages[md.name] = page_title(md)
        m = CH_RE.match(md.name)
        if m:
            chmap[int(m.group(1))] = md.name

    # ---- index.md landing page ----
    chapters = sorted(chmap)
    papers = [f"paper-pm{n}.md" for n in (2, 3)
              if f"paper-pm{n}.md" in pages] + \
             [f"anspaper-pm{n}.md" for n in (2, 3)
              if f"anspaper-pm{n}.md" in pages]
    glossary = "zz-glossary.md" if "zz-glossary.md" in pages else None
    index = "zz-index.md" if "zz-index.md" in pages else None

    lines = ["# Pure Mathematics 2 & 3",
             "",
             "MkDocs Material build of the coursebook. Math via MathJax.",
             "", "## Practice", "",
             "- [Exercise pages and key points](practice/index.md)",
             "", "## Chapters", ""]
    for n in chapters:
        chf = chmap[n]
        an = next((f for f in pages if f.startswith(f"ans{n:02d}-")), None)
        lines.append(f"- **{pages[chf]}** — "
                     f"[chapter](split/{chf})"
                     + (f" · [answers](split/{an})" if an else ""))
    lines += ["", "## Practice papers", ""]
    for p in papers:
        lines.append(f"- [{pages[p]}](split/{p})")
    lines += ["", "## Reference", ""]
    if glossary:
        lines.append(f"- [Glossary](split/{glossary})")
        lines.append(f"- [Index](split/{index})" if index else "- Index")
    (docs / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # ---- mathjax.js: boldsymbol extension + arithmatex class hook ---------
    (docs / "javascripts" / "mathjax.js").write_text(
        "window.MathJax = {\n"
        '  loader: { load: ["[tex]/boldsymbol"] },\n'
        "  tex: {\n"
        '    packages: { "[+]": ["boldsymbol"] },\n'
        '    inlineMath: [["\\\\(", "\\\\)"]],\n'
        '    displayMath: [["\\\\[", "\\\\]"]],\n'
        "    processEscapes: true,\n"
        "    processEnvironments: true\n"
        "  },\n"
        "  options: {\n"
        '    ignoreHtmlClass: "tex2jax_ignore|mathjax_ignore",\n'
        '    processHtmlClass: "arithmatex"\n'
        "  }\n"
        "};\n"
        "\n"
        "document$.subscribe(() => {\n"
        "  MathJax.startup.output.clearCache();\n"
        "  MathJax.typesetClear();\n"
        "  MathJax.texReset();\n"
        "  MathJax.typesetPromise();\n"
        "});\n", encoding="utf-8")

    # ---- mathjax loader: pinned jsDelivr CDN, or bundled locally ----------
    loader = MATHJAX_CDN
    if args.local_mathjax:
        bundle = docs / "javascripts" / "tex-mml-chtml.js"
        if fetch(MATHJAX_CDN, bundle):
            loader = "javascripts/tex-mml-chtml.js"
            print(f"[local-mathjax] saved {bundle} "
                  f"({bundle.stat().st_size} bytes)")
            ext = (docs / "javascripts" / "input" / "tex" / "extensions"
                   / "boldsymbol.js")
            if fetch(BOLDSYMBOL_EXT, ext):
                print(f"[local-mathjax] saved {ext}")
        else:
            print(f"[local-mathjax] using CDN instead. To vendor it yourself:\n"
                  f"  curl -L -o {bundle} {MATHJAX_CDN}\n"
                  f"  curl -L -o {ext} {BOLDSYMBOL_EXT}")

    # ---- practice pages (build_practice.py) ------------------------------
    import build_practice
    info = build_practice.generate(docs, book,
                                   full_keypoints=args.full_keypoints,
                                   boldsymbol_to_mathbf=args.boldsymbol_to_mathbf)

    # ---- mkdocs.yml ----
    nav = ["  - Home: index.md"]
    fm = "00-front-matter.md" if "00-front-matter.md" in pages else None
    if fm:
        nav.append(f"  - {json.dumps(pages[fm])}: split/{fm}")
    for n in chapters:
        chf = chmap[n]
        nav.append(f"  - {json.dumps(pages[chf])}: split/{chf}")
        an = next((f for f in pages if f.startswith(f"ans{n:02d}-")), None)
        if an:
            nav.append(f"  - {json.dumps(pages[an])}: split/{an}")
    nav.append("  - Practice:")
    nav.append('      - Overview: practice/index.md')
    for c in info["chapters"]:
        nav.append(f"      - {json.dumps(c['title'])}:")
        nav.append(f"          - Exercises: practice/{c['exercises']}")
        nav.append(f"          - Key points: practice/{c['keypoints']}")
    nav.append("      - All key points: practice/all-keypoints.md")
    for p in papers:
        nav.append(f"  - {json.dumps(pages[p])}: split/{p}")
    if glossary:
        nav.append(f"  - {json.dumps(pages[glossary])}: split/{glossary}")
    if index:
        nav.append(f"  - {json.dumps(pages[index])}: split/{index}")

    (site / "mkdocs.yml").write_text(
        "site_name: Maths Pure 2 & 3\n"
        "theme:\n"
        "  name: material\n"
        "  features:\n"
        "    - navigation.sections\n"
        "    - navigation.top\n"
        "    - toc.follow\n"
        "plugins:\n"
        "  - search\n"
        "markdown_extensions:\n"
        "  - toc:\n"
        "      permalink: true\n"
        "  - attr_list\n"
        "  - md_in_html\n"
        "  - admonition\n"
        "  - pymdownx.details\n"
        "  - pymdownx.arithmatex:\n"
        "      generic: true\n"
        "extra_css:\n"
        "  - stylesheets/practice.css\n"
        "extra_javascript:\n"
        "  - javascripts/mathjax.js\n"
        "  - " + loader + "\n"
        "  - javascripts/practice-filter.js\n"
        "nav:\n" + "\n".join(nav) + "\n", encoding="utf-8")

    # ---- .gitignore ----
    gi = Path(".gitignore")
    text = gi.read_text(encoding="utf-8") if gi.exists() else ""
    if not any(re.match(r"^\s*site/?\s*$", ln) for ln in text.splitlines()):
        gi.write_text(text + ("" if text.endswith("\n") else "\n") + "site/\n",
                      encoding="utf-8")

    print(f"pages: {len(pages) + 1} (index + {len(pages)} split files)")
    print(f"images copied: {images_copied}")
    print(f"align->aligned replacements: {align_n}")
    print(f"inline-$ space trims: {trim_n}")
    print(f"same-line $$ blocks split: {dollars_n}")
    print(f"\\boldsymbol occurrences in source: {bm_n}"
          + (" -> replaced with \\mathbf" if args.boldsymbol_to_mathbf else ""))
    if changed_headings:
        print(f"headings with maths made plain ({len(changed_headings)}):")
        for f, before, after in changed_headings:
            print(f"  {f}:\n    - {before}\n    + {after}")
    print(f"mathjax loader: {loader}")
    # practice pages summary (printed by build_practice; mirror totals here)
    print("practice: "
          f"{info['totals']['exercise_pages']} exercise pages, "
          f"{info['totals']['questions']} questions "
          f"({info['totals']['linked']} linked answers, "
          f"{info['totals']['unlinked']} not linked), "
          f"{info['totals']['keypoints']} key points")
    print(f"intent: cd {site} && mkdocs serve")


if __name__ == "__main__":
    main()