#!/usr/bin/env python3
"""Local checks for claude-code-agent-skills-guide-. Python 3 standard library only.

1. File names: no underscores; carry a version number like v0.1 (README.md, LICENSE exempt).
2. Relative Markdown/HTML links point to files that exist.
3. SVG files are well-formed XML.
4. No real-looking secrets (Anthropic/OpenAI/GitHub/AWS key prefixes).
"""
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
EXEMPT = {"README.md", "LICENSE"}
errors = []

files = [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]

for p in files:
    if p.name in EXEMPT:
        continue
    if "_" in p.name:
        errors.append(f"underscore in name: {p.relative_to(ROOT)}")
    if not re.search(r"v\d+\.\d+", p.name):
        errors.append(f"missing version number: {p.relative_to(ROOT)}")

link_re = re.compile(r"\]\(([^)\s]+)\)|href=\"([^\"]+)\"|src=\"([^\"]+)\"")
for p in files:
    if p.suffix != ".md":
        continue
    text = p.read_text(encoding="utf-8")
    # ignore fenced code blocks
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    for m in link_re.finditer(text):
        target = next(g for g in m.groups() if g)
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        path = target.split("#")[0]
        if path and not (p.parent / path).exists():
            errors.append(f"broken link in {p.relative_to(ROOT)}: {target}")

for p in files:
    if p.suffix == ".svg":
        try:
            ET.parse(p)
        except ET.ParseError as exc:
            errors.append(f"invalid SVG {p.relative_to(ROOT)}: {exc}")

secret_re = re.compile(r"(sk-ant-[A-Za-z0-9_\-]{20,}|sk-[A-Za-z0-9]{32,}|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|AKIA[0-9A-Z]{16})")
for p in files:
    if p.suffix in {".md", ".py", ".svg", ".json", ".txt", ""}:
        text = p.read_text(encoding="utf-8", errors="ignore")
        if secret_re.search(text):
            errors.append(f"possible secret in {p.relative_to(ROOT)}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(files)} files checked")
