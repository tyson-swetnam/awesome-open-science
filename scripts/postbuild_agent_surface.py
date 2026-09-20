#!/usr/bin/env python3
"""Post-build step: make the rendered site consumable by AI agents.

Run AFTER `zensical build`. It:

1. Mirrors every page's Markdown source into the built site at that page's
   pretty URL:
       docs/a/b.md      -> site/a/b/index.md      (page URL + "index.md")
       docs/index.md    -> site/index.md
   so any agent can turn a page URL into its canonical Markdown by appending
   `index.md`. GitHub Pages serves these as `text/markdown; charset=utf-8`.
   Relative links in the mirror are rewritten to absolute URLs pointing at
   the linked page's own Markdown twin (scripts/agent_links.py): the mirror
   sits one directory deeper than its source, and an agent reading Markdown
   should keep getting Markdown as it traverses. The sources under docs/ are
   never modified.
2. Injects a Markdown alternate into each page's <head>:
       <link rel="alternate" type="text/markdown" href="index.md">
3. Adds a *visible* pointer to every page, because text extraction and
   link-derived URL allowlists never see <head>: a "Machine-readable" line at
   the end of the article linking the Markdown twin, the raw source on
   GitHub, llms.txt and llms-full.txt.
4. Writes robots.txt advertising sitemap.xml, /llms.txt, /llms-full.txt, the
   Markdown mirror and raw-source conventions, and the agent guide.

Only pages listed in the nav are mirrored, matching gen_llms_txt.py: a page
kept outside the nav (a retired page's redirect stub) is not part of the
agent surface.

Adapted from tyson-swetnam/AI-Automation-and-Agents
(scripts/postbuild_agent_surface.py).

Usage: python3 scripts/postbuild_agent_surface.py [site_dir]
"""

from __future__ import annotations

import html
import re
import sys
import tomllib
from pathlib import Path

from agent_links import page_url, raw_source_url, rewrite_relative_targets, site_url

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# Crawlers explicitly named so that AI agents and their search surfaces are
# allowed rather than left to a default they may read conservatively.
AGENTS = [
    "Googlebot", "Google-Extended", "GoogleOther", "Google-CloudVertexBot",
    "GPTBot", "OAI-SearchBot", "ChatGPT-User",
    "ClaudeBot", "Claude-User", "Claude-SearchBot",
    "PerplexityBot", "cohere-ai", "Applebot-Extended", "CCBot",
    "meta-externalagent", "Amazonbot", "DuckAssistBot", "MistralAI-User",
]


def nav_pages(cfg: dict) -> list[str]:
    """Every docs-relative page path in the nav, in order."""
    pages: list[str] = []
    for entry in (cfg.get("project") or {}).get("nav") or []:
        for _, value in entry.items():
            if isinstance(value, str):
                pages.append(value)
            else:
                pages.extend(v for child in value for v in child.values() if isinstance(v, str))
    return pages


def mirror_path(site: Path, rel: str) -> Path:
    """Where a docs-relative page's Markdown twin belongs in the built site."""
    if rel == "index.md":
        return site / "index.md"
    if rel.endswith("/index.md"):
        return site / rel
    return site / rel[: -len(".md")] / "index.md"


def strip_frontmatter(text: str) -> str:
    return re.sub(r"^---\s*\n.*?\n---\s*\n?", "", text, count=1, flags=re.DOTALL)


def machine_readable_block(base: str, rel: str) -> str:
    twin = page_url(base, rel) + "index.md"
    raw = raw_source_url(rel)
    return (
        '<hr class="agent-surface-rule">\n'
        '<p class="agent-surface"><strong>Machine-readable:</strong> '
        f'<a href="{html.escape(twin)}">this page as Markdown</a> · '
        f'<a href="{html.escape(raw)}">raw source on GitHub</a> · '
        f'<a href="{html.escape(base)}llms.txt">llms.txt</a> · '
        f'<a href="{html.escape(base)}llms-full.txt">llms-full.txt</a> · '
        f'<a href="{html.escape(base)}ai-agents/">agent guide</a></p>'
    )


def inject_html(page: Path, base: str, rel: str) -> bool:
    """Add the Markdown alternate to <head> and the visible pointer to the article."""
    text = page.read_text(encoding="utf-8")
    changed = False

    if 'type="text/markdown"' not in text and "</head>" in text:
        text = text.replace(
            "</head>",
            '<link rel="alternate" type="text/markdown" href="index.md">\n</head>',
            1,
        )
        changed = True

    if 'class="agent-surface"' not in text:
        # Close of the page article, as Material renders it.
        m = list(re.finditer(r"</article>", text))
        if m:
            at = m[0].start()
            text = text[:at] + machine_readable_block(base, rel) + "\n" + text[at:]
            changed = True

    if changed:
        page.write_text(text, encoding="utf-8")
    return changed


def write_robots(site: Path, base: str, name: str) -> None:
    lines = [
        f"# {name}",
        f"# {base}",
        "# This site is published for people AND for AI agents.",
        "User-agent: *",
        "Allow: /",
        "",
    ]
    for agent in AGENTS:
        lines += [f"User-agent: {agent}", "Allow: /", ""]
    lines += [
        f"Sitemap: {base}sitemap.xml",
        "",
        "# AI agents and harnesses:",
        f"#   Machine-readable outline:  {base}llms.txt",
        f"#   Full corpus (one file):    {base}llms-full.txt",
        "#   Markdown source of any page: append `index.md` to the page URL. Its",
        "#   links are absolute and point at other pages' Markdown twins.",
        f"#   Raw Markdown on GitHub:    {raw_source_url('<path>.md')}",
        f"#   Agent guide:               {base}ai-agents/",
        "",
    ]
    (site / "robots.txt").write_text("\n".join(lines), encoding="utf-8")


def main(argv: list[str]) -> int:
    site = Path(argv[1] if len(argv) > 1 else "site").resolve()
    if not site.is_dir():
        print(f"error: {site} is not a directory; run `zensical build` first", file=sys.stderr)
        return 1

    cfg = tomllib.loads((ROOT / "zensical.toml").read_text(encoding="utf-8"))
    base = site_url()
    name = (cfg.get("project") or {}).get("site_name", "Site")

    mirrored = injected = 0
    for rel in nav_pages(cfg):
        source = DOCS / rel
        if not source.exists():
            print(f"error: nav references missing page {rel}", file=sys.stderr)
            return 1

        target = mirror_path(site, rel)
        target.parent.mkdir(parents=True, exist_ok=True)
        body = strip_frontmatter(source.read_text(encoding="utf-8"))
        target.write_text(rewrite_relative_targets(body, rel, base), encoding="utf-8")
        mirrored += 1

        rendered = target.parent / "index.html"
        if rendered.exists() and inject_html(rendered, base, rel):
            injected += 1

    write_robots(site, base, name)
    print(f"agent surface: {mirrored} Markdown twins, {injected} pages annotated, robots.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
