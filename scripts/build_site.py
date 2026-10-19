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

from math_normalize import normalise

BOOK_DEFAULT = Path("Maths Pure 2 & 3-clean_MD")
MATHJAX_CDN = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
BOLDSYMBOL_EXT = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/input/tex/" \
                 "extensions/boldsymbol.js"

CH_RE = re.compile(r"^ch(\d+)-")
H1_RE = re.compile(r"^#\s+(.*)$")


def page_title(path):
    for ln in path.read_text(encoding="utf-8").splitlines():
        m = H1_RE.match(ln.strip())
        if m:
            return m.group(1).strip()
    return path.stem.replace("-", " ").title()


def copy_md(src, dst, boldsymbol_to_mathbf=False, changed_headings=None):
    text = src.read_text(encoding="utf-8")
    bm_n = text.count("\\boldsymbol")
    if boldsymbol_to_mathbf:
        text = text.replace("\\boldsymbol", "\\mathbf")
    out = normalise(text, "mathjax")
    if changed_headings is not None:
        for b, a in zip(text.split("\n"), out.split("\n")):
            if b.strip().startswith("#") and b != a:
                changed_headings.append((src.name, b.strip(), a.strip()))
    dst.write_text(out, encoding="utf-8")
    return bm_n


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
    bm_n = 0
    for md in sorted(split.glob("*.md")):
        bm_n += copy_md(md, docs / "split" / md.name,
                        args.boldsymbol_to_mathbf, changed_headings)
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
    print(f"maths normalisation: math_normalize.normalise(..., 'mathjax')")
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