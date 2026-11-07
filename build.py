"""Wrap nas-mockup.html (the page fragment) into index.html, a full document for GitHub Pages.

Usage: python build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
src = (ROOT / "nas-mockup.html").read_text(encoding="utf-8")

# Everything before the app markup (title, meta, fonts, styles) belongs in <head>.
split = src.index('<div class="app">')
head, body = src[:split].rstrip(), src[split:].rstrip()

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Interactive 3D mockup of a NAS build with a passive Tesla V100 and a printed PETG intake duct.">
{head}
</head>
<body>
{body}
</body>
</html>
"""
(ROOT / "index.html").write_text(page, encoding="utf-8", newline="\n")
print(f"index.html: {len(page.encode('utf-8'))} bytes")
