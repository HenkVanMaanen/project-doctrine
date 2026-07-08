#!/usr/bin/env python3
"""Structural validation for the Project Doctrine repository.

Checks (default, fast, no network):
  1. Backticked doctrine-file references (`foo.md`) in doctrine/, SKILL.md,
     README.md, AGENTS.md resolve to real files in doctrine/.
  2. The Doctrine Files table in skills/apply-doctrine/SKILL.md lists exactly
     the files in doctrine/ (standards-versions.md excluded by design).
  3. The README doctrine table lists every file in doctrine/.
  4. Every source doctrine file named in SKILL.md's Phase 3 output table exists.
  5. (warning only) lowercase must/should in doctrine Requirements lines.

With --links (scheduled CI): every http(s) URL responds; 404/410 fail.
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCTRINE = ROOT / "doctrine"
SKILL = ROOT / "skills" / "apply-doctrine" / "SKILL.md"
README = ROOT / "README.md"
AGENTS = ROOT / "AGENTS.md"

errors: list[str] = []
warnings: list[str] = []

REF_RE = re.compile(r"`([a-z0-9][a-z0-9-]*\.md)`")


def doctrine_files() -> set[str]:
    return {p.name for p in DOCTRINE.glob("*.md")}


def check_references(files: set[str]) -> None:
    sources = list(DOCTRINE.glob("*.md")) + [SKILL, README, AGENTS]
    for src in sources:
        text = src.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), 1):
            for ref in REF_RE.findall(line):
                # `docs/foo.md` style paths never match REF_RE (no slash in
                # pattern), so every hit should be a doctrine file.
                if ref not in files:
                    errors.append(
                        f"{src.relative_to(ROOT)}:{lineno}: reference `{ref}` "
                        f"does not exist in doctrine/"
                    )


def check_skill_table(files: set[str]) -> None:
    text = SKILL.read_text(encoding="utf-8")
    table = set(re.findall(r"^\|\s*`doctrine/([a-z0-9-]+\.md)`", text, re.M))
    expected = files - {"standards-versions.md"}
    for missing in sorted(expected - table):
        errors.append(f"SKILL.md Doctrine Files table is missing doctrine/{missing}")
    for extra in sorted(table - expected):
        errors.append(f"SKILL.md Doctrine Files table lists nonexistent doctrine/{extra}")


def check_readme_table(files: set[str]) -> None:
    text = README.read_text(encoding="utf-8")
    table = set(re.findall(r"\]\(doctrine/([a-z0-9-]+\.md)\)", text))
    for missing in sorted(files - table):
        errors.append(f"README.md doctrine table is missing doctrine/{missing}")
    for extra in sorted(table - files):
        errors.append(f"README.md doctrine table lists nonexistent doctrine/{extra}")


def check_output_table(files: set[str]) -> None:
    text = SKILL.read_text(encoding="utf-8")
    rows = re.findall(r"^\|\s*`docs/[a-z0-9-]+\.md`\s*\|([^|]+)\|", text, re.M)
    for cell in rows:
        cleaned = re.sub(r"\([^)]*\)", "", cell)
        for token in (t.strip() for t in cleaned.split(",")):
            if not token:
                continue
            if f"{token}.md" not in files:
                errors.append(
                    f"SKILL.md Phase 3 output table names source '{token}' "
                    f"but doctrine/{token}.md does not exist"
                )


def check_rfc2119_case() -> None:
    pattern = re.compile(r"(?<![A-Za-z])(must not|must|shall)(?![A-Za-z])")
    for src in sorted(DOCTRINE.glob("*.md")):
        in_requirements = False
        for lineno, line in enumerate(src.read_text(encoding="utf-8").splitlines(), 1):
            if line.startswith("## "):
                in_requirements = line.strip() == "## Requirements"
                continue
            if in_requirements and line.lstrip().startswith(("-", "|", "1", "2", "3")):
                if pattern.search(line):
                    warnings.append(
                        f"{src.relative_to(ROOT)}:{lineno}: lowercase RFC 2119 "
                        f"keyword in a requirement line (use MUST/SHALL if normative)"
                    )


URL_RE = re.compile(r"https?://[^\s\)\]`>|\"']+")


def check_links() -> None:
    urls: dict[str, str] = {}
    for src in list(DOCTRINE.glob("*.md")) + [SKILL, README, AGENTS]:
        for url in URL_RE.findall(src.read_text(encoding="utf-8")):
            urls.setdefault(url.rstrip(".,;"), str(src.relative_to(ROOT)))
    for url, where in sorted(urls.items()):
        req = urllib.request.Request(url, method="GET", headers={"User-Agent": "doctrine-linkcheck"})
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                if resp.status in (404, 410):
                    errors.append(f"{where}: dead link {url} ({resp.status})")
        except urllib.error.HTTPError as exc:
            if exc.code in (404, 410):
                errors.append(f"{where}: dead link {url} ({exc.code})")
            else:
                warnings.append(f"{where}: {url} returned {exc.code} (not treated as dead)")
        except Exception as exc:  # noqa: BLE001 - report and continue
            warnings.append(f"{where}: {url} unreachable ({exc.__class__.__name__})")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--links", action="store_true", help="also verify external URLs")
    args = parser.parse_args()

    files = doctrine_files()
    check_references(files)
    check_skill_table(files)
    check_readme_table(files)
    check_output_table(files)
    check_rfc2119_case()
    if args.links:
        check_links()

    for w in warnings:
        print(f"WARNING: {w}")
    for e in errors:
        print(f"ERROR: {e}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
