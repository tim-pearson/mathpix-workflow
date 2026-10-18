#!/usr/bin/env python3
"""Build a local MkDocs Material site from the split book + images.
Usage: python build_site.py [book_dir] [--local-mathjax]
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
MJ_JS_LOCAL = "javascripts/tex-mml-chtml.js"

CH_RE = re.compile(r"^ch(\d+)-")
H1_RE = re.compile(r"^#\s+(.*)$")

# normalise inline maths arithmatex rejects: "$ x $", "$x $", "$ x$" -> "$x$"
# opener $ must be at line-start or after whitespace so "$x$ and $y$" is safe.
SLOPPY_INLINE = re.compile(
    r"(?<![\S])\$[ \t]+([^$]+?)[ \t]+\$(?=[ \t.,;:!?)\]}]|$)")
# "$ x = 2 $" written on one line -> its own $$..$$ block
SAME_LINE_DOLLARS = re.compile(r"\$\$(?:\s*)([^$]+?)(?:\s*)\$\$")


def page_title(path):
    for ln in path.read_text(encoding="utf-8").splitlines():
        m = H1_RE.match(ln.strip())
        if m:
            return m.group(1).strip()
    return path.stem.replace("-", " ").title()


def copy_md(src, dst):
    text = src.read_text(encoding="utf-8")
    align_n = sum(text.count(p) for p in (
        "\\begin{align}", "\\end{align}",
        "\\begin{align*}", "\\end{align*}"))
    text = (text.replace("\\begin{align*}", "\\begin{aligned*}")
                .replace("\\end{align*}", "\\end{aligned*}")
                .replace("\\begin{align}", "\\begin{aligned}")
                .replace("\\end{align}", "\\end{aligned}"))

    out, in_block, trim_n, dollars_n = [], False, 0, 0
    for ln in text.split("\n"):
        s = ln.lstrip()
        if s.startswith("$$"):
            in_block = not in_block
            out.append(ln)
            continue
        if in_block:
            out.append(ln)
            continue
        new, t = SLOPPY_INLINE.subn(
            lambda m: "$" + m.group(1) + "$", ln)
        trim_n += t
        if not s.startswith("|"):          # never reflow table rows
            new, n = SAME_LINE_DOLLARS.subn(
                lambda m: "$$\n" + m.group(1) + "\n$$", new)
            dollars_n += n
        out.append(new)

    dst.write_text("\n".join(out), encoding="utf-8")
    return align_n, trim_n, dollars_n


def fetch(url, dest, timeout=60):
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
                    help="download the MathJax es5 bundle into "
                         "site/docs/javascripts/ and use it instead of the CDN")
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

    pages, chmap = {}, {}
    align_n = trim_n = dollars_n = 0
    for md in sorted(split.glob("*.md")):
        a, t, d = copy_md(md, docs / "split" / md.name)
        align_n += a
        trim_n += t
        dollars_n += d
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

    # ---- mathjax.js (exact Material recipe, class must match arithmatex) ----
    (docs / "javascripts" / "mathjax.js").write_text(
        "window.MathJax = {\n"
        "  tex: {\n"
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

    # ---- mathjax loader: pinned jsDelivr CDN, or a local copy ------------
    loader = MATHJAX_CDN
    if args.local_mathjax:
        dest = docs / "javascripts" / "tex-mml-chtml.js"
        if fetch(MATHJAX_CDN, dest):
            loader = MJ_JS_LOCAL
            print(f"[local-mathjax] saved {dest} ({dest.stat().st_size} bytes)")
        else:
            print(f"[local-mathjax] using CDN instead. To vendor it yourself: "
                  f"curl -L -o {dest} {MATHJAX_CDN}")

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
        "extra_javascript:\n"
        "  - javascripts/mathjax.js\n"
        "  - " + loader + "\n"
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
    print(f"mathjax loader: {loader}")
    print(f"intent: cd {site} && mkdocs serve")


if __name__ == "__main__":
    main()