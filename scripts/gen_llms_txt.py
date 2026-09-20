#!/usr/bin/env python3
"""Generate llms.txt and llms-full.txt from docs/.

llms.txt      — linked outline of the site (llmstxt.org convention): every
                page in the `nav` of zensical.toml, in nav order, grouped by
                its nav section, with the page's frontmatter `description`
                and absolute URLs derived from site_url.
llms-full.txt — the whole corpus concatenated as Markdown, in the same order,
                so an agent can ingest the site in one request.

Both are written into docs/ so the static build ships them at the site root.
CI regenerates them and fails on drift (`git diff --exit-code docs/llms*.txt`).

The nav is the single source of truth for which pages exist and in what
order. A Markdown file under docs/ that is not in the nav (a retired page
kept for its redirect stub, say) is deliberately left out of both files.

Adapted from tyson-swetnam/AI-Automation-and-Agents (scripts/gen_llms_txt.py).

Usage: python3 scripts/gen_llms_txt.py
"""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

from agent_links import page_url, raw_source_url, rewrite_relative_targets, twin_url

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CONFIG = ROOT / "zensical.toml"


def load_config() -> dict:
    return tomllib.loads(CONFIG.read_text(encoding="utf-8"))


def site_url(cfg: dict) -> str:
    url = (cfg.get("project") or {}).get("site_url") or "/"
    return url.rstrip("/") + "/"


def walk_nav(cfg: dict) -> list[tuple[str, list[tuple[str, str]]]]:
    """Flatten the nav into [(section label, [(page label, docs-relative path)])].

    A top-level nav entry whose value is a list becomes a section holding its
    children. A top-level entry that is a single page becomes a section of one,
    keeping llms.txt in the same order and shape a reader sees in the sidebar.
    """
    sections: list[tuple[str, list[tuple[str, str]]]] = []
    for entry in (cfg.get("project") or {}).get("nav") or []:
        for label, value in entry.items():
            if isinstance(value, str):
                sections.append((label, [(label, value)]))
            else:
                pages = [(k, v) for child in value for k, v in child.items() if isinstance(v, str)]
                sections.append((label, pages))
    return sections


def frontmatter_description(text: str) -> str:
    """The `description:` from a page's YAML frontmatter, or "" if absent.

    Deliberately a small regex rather than a YAML parse: the only frontmatter
    this repository uses is a single-line description, and this keeps PyYAML
    out of the build dependencies.
    """
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.DOTALL)
    if not m:
        return ""
    d = re.search(r"^description:\s*(.+?)\s*$", m.group(1), re.MULTILINE)
    return d.group(1).strip().strip("\"'") if d else ""


def strip_frontmatter(text: str) -> str:
    return re.sub(r"^---\s*\n.*?\n---\s*\n?", "", text, count=1, flags=re.DOTALL)


def main() -> int:
    cfg = load_config()
    project = cfg.get("project") or {}
    base = site_url(cfg)
    name = project.get("site_name", "Site")
    sections = walk_nav(cfg)

    missing = [p for _, pages in sections for _, p in pages if not (DOCS / p).exists()]
    if missing:
        print(f"error: nav references missing pages: {', '.join(missing)}", file=sys.stderr)
        return 1

    no_desc = [
        p for _, pages in sections for _, p in pages
        if not frontmatter_description((DOCS / p).read_text(encoding="utf-8"))
    ]
    if no_desc:
        print(f"error: pages without a frontmatter description: {', '.join(no_desc)}",
              file=sys.stderr)
        return 1

    # ---- llms.txt -------------------------------------------------------
    out: list[str] = [
        f"# {name}",
        "",
        f"> {project.get('site_description', '').rstrip('.')}. "
        "This is a curated \"Awesome List\": each page is a set of links to open science "
        "tools, platforms and resources, grouped by topic, with a one-line description of "
        "each entry. It is a directory of external resources rather than documentation of "
        "a single piece of software.",
        "",
        f"Full corpus for ingestion: {base}llms-full.txt",
        "",
        "Every entry below lists three addresses that return the same content: the rendered "
        "page, its Markdown twin (the page URL plus `index.md`, served as `text/markdown`), "
        "and the raw source file on GitHub. Fetch whichever your sandbox allows; some permit "
        "github.com and raw.githubusercontent.com but not *.github.io.",
        "",
        "```",
        f"Site page        {base}<path>/",
        f"Markdown twin    {base}<path>/index.md",
        f"Raw source       {raw_source_url('<path>.md')}",
        "```",
        "",
        "Inside a Markdown twin, and inside llms-full.txt, links to other pages are absolute "
        "and already point at those pages' Markdown twins, so an agent can traverse the whole "
        "site without leaving Markdown; drop the trailing `index.md` to reach the rendered "
        f"page. Agent guide: {base}ai-agents/",
        "",
        "Notes for agents:",
        "",
        "- Entries are links to third-party projects. This site does not vouch for them beyond "
        "the curation criteria (open source or freely available, actively maintained, real "
        "adoption, documented); descriptions are written by the maintainers of this list, not "
        "by the projects.",
        "- Where an entry is archived, superseded or early-stage, its description says so. "
        "Carry that qualifier through rather than presenting the entry as a live recommendation.",
        "- Link rot is the main failure mode of a list like this. Check a URL before relying "
        "on it, and prefer the raw source on GitHub for the most recent revision.",
        "",
    ]

    for label, pages in sections:
        out.append(f"## {label}")
        out.append("")
        for page_label, rel in pages:
            text = (DOCS / rel).read_text(encoding="utf-8")
            desc = frontmatter_description(text)
            out.append(
                f"- [{page_label}]({page_url(base, rel)}): {desc} "
                f"Markdown twin: {twin_url(base, rel)} "
                f"Raw source: {raw_source_url(rel)}"
            )
        out.append("")

    (DOCS / "llms.txt").write_text("\n".join(out).rstrip("\n") + "\n", encoding="utf-8")

    # ---- llms-full.txt --------------------------------------------------
    full: list[str] = [
        f"# {name} — full corpus",
        "",
        f"> Every page of {base} concatenated as Markdown, in navigation order. "
        f"Generated by scripts/gen_llms_txt.py; do not edit by hand. "
        f"Outline with per-page links: {base}llms.txt",
        "",
        "Relative links have been rewritten to absolute URLs pointing at each page's Markdown "
        "twin. External links are unchanged.",
        "",
    ]
    for label, pages in sections:
        for page_label, rel in pages:
            text = strip_frontmatter((DOCS / rel).read_text(encoding="utf-8"))
            full.append("---")
            full.append("")
            full.append(f"# Page: {page_label}")
            full.append(f"Section: {label}")
            full.append(f"URL: {page_url(base, rel)}")
            full.append(f"Markdown twin: {twin_url(base, rel)}")
            full.append(f"Raw source: {raw_source_url(rel)}")
            full.append("")
            full.append(rewrite_relative_targets(text, rel, base).strip())
            full.append("")

    (DOCS / "llms-full.txt").write_text("\n".join(full).rstrip("\n") + "\n", encoding="utf-8")

    pages_total = sum(len(p) for _, p in sections)
    print(f"wrote docs/llms.txt and docs/llms-full.txt ({pages_total} pages, "
          f"{len(sections)} sections)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
