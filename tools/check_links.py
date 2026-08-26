#!/usr/bin/env python3
"""Check every relative link and heading anchor in the repository's Markdown.

Why: moves and renames break links silently — a broken link is only found by
the reader who follows it. Run before every commit that touches file names,
headings or links:

    python3 tools/check_links.py

Exit 0 and "OK" when everything resolves; otherwise lists what is broken and
exits 1. External links (http…) are not fetched. Anchors are slugified the
way GitHub does for simple headings (lowercase, punctuation dropped, spaces
to hyphens); exotic headings may need a manual check.
"""
import glob, os, re, sys

LINK = re.compile(r"\]\(([^)]+)\)")
HEAD = re.compile(r"^#+\s+(.*)$", re.M)


def slug(h):
    return re.sub(r"[^a-z0-9 -]", "", h.lower()).strip().replace(" ", "-")


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)
    broken = []
    for f in sorted(glob.glob("**/*.md", recursive=True)):
        base = os.path.dirname(f)
        text = open(f, encoding="utf-8").read()
        for m in LINK.finditer(text):
            target = m.group(1)
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            path, _, anchor = target.partition("#")
            file = os.path.normpath(os.path.join(base, path)) if path else f
            if not os.path.exists(file):
                broken.append((f, target, "missing file"))
                continue
            if anchor and os.path.isfile(file):
                heads = [slug(h) for h in HEAD.findall(open(file, encoding="utf-8").read())]
                if anchor not in heads:
                    broken.append((f, target, "missing anchor"))
    if broken:
        for f, t, why in broken:
            print(f"BROKEN  {f}: ({t}) — {why}")
        sys.exit(1)
    print("OK — all relative links and anchors resolve")


if __name__ == "__main__":
    main()
