#!/usr/bin/env python3
"""Rewrite the relative links in a Markdown page to absolute URLs.

Used by the two scripts that publish Markdown for agents rather than for the
site build:

* `postbuild_agent_surface.py` mirrors every page at its pretty URL
  (`docs/a/b.md` -> `site/a/b/index.md`), one directory deeper than the
  source, so a relative link copied verbatim would resolve one level too low.
* `gen_llms_txt.py` concatenates every page into `llms-full.txt`, where a
  relative link has no base to resolve against at all.

Both need the same rule, so it lives here rather than in either script.

A link to another **page** resolves to that page's Markdown twin — the page
URL plus `index.md` — so an agent reading Markdown keeps getting Markdown as
it traverses. Drop the trailing `index.md` to reach the rendered page.
Anchors, external URLs, `mailto:`, fragment-only links and paths that are
already absolute are left alone.

The sources under `docs/` are never modified: the site build needs the
relative links.

Adapted from tyson-swetnam/AI-Automation-and-Agents (scripts/okf_links.py).
"""

from __future__ import annotations

import posixpath
import re
from pathlib import Path

# Markdown inline link or image: the target sits between "](" and ")".
# The match stops at the closing paren, so a trailing attr-list such as
# {target=_blank} is left alone.
MD_TARGET = re.compile(r"(!?\[[^\]]*\]\()([^)\s]+)(\s+\"[^\"]*\")?(\))")
# Raw HTML attribute, for the pages that embed a div or image directly.
HTML_TARGET = re.compile(r"""\b(src|href)=(["'])([^"'>]+)\2""")
SKIP_PREFIXES = ("http://", "https://", "//", "mailto:", "tel:", "#", "/", "data:")

ROOT = Path(__file__).resolve().parent.parent


def page_url(base: str, rel: str) -> str:
    """The rendered URL of a docs-relative Markdown path."""
    if rel == "index.md":
        return base
    if rel.endswith("/index.md"):
        return base + rel[: -len("index.md")]
    return base + rel[: -len(".md")] + "/"


def twin_url(base: str, rel: str) -> str:
    """The Markdown twin of a docs-relative Markdown path."""
    return page_url(base, rel) + "index.md"


def absolutize(target: str, source_rel: str, base: str) -> str:
    """Resolve one relative target found in `source_rel` to an absolute URL."""
    if not target or target.startswith(SKIP_PREFIXES):
        return target
    path, sep, anchor = target.partition("#")
    if not path:
        return target
    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(source_rel), path))
    if resolved.startswith(".."):  # escapes docs/; leave it as written
        return target
    url = twin_url(base, resolved) if resolved.endswith(".md") else base + resolved
    return url + sep + anchor


def rewrite_relative_targets(text: str, source_rel: str | Path, base: str) -> str:
    """Return `text` with every relative Markdown and HTML target made absolute.

    `source_rel` is the page's path relative to docs/ (e.g. `hardware.md`), `base`
    the site URL with a trailing slash. Fenced code blocks are left untouched, so
    example paths inside them still read as written.
    """
    source_rel = str(source_rel)

    def md(m: re.Match) -> str:
        return m.group(1) + absolutize(m.group(2), source_rel, base) + (m.group(3) or "") + m.group(4)

    def attr(m: re.Match) -> str:
        return f'{m.group(1)}={m.group(2)}{absolutize(m.group(3), source_rel, base)}{m.group(2)}'

    out, fence = [], None
    for line in text.split("\n"):
        stripped = line.lstrip()
        if fence is None and (stripped.startswith("```") or stripped.startswith("~~~")):
            fence = stripped[:3]
        elif fence is not None and stripped.startswith(fence):
            fence = None
        elif fence is None:
            line = MD_TARGET.sub(md, line)
            line = HTML_TARGET.sub(attr, line)
        out.append(line)
    return "\n".join(out)


def _config() -> str:
    return (ROOT / "zensical.toml").read_text(encoding="utf-8")


def site_url() -> str:
    """The site_url from zensical.toml, with a trailing slash."""
    m = re.search(r'^site_url\s*=\s*"([^"]+)"', _config(), re.MULTILINE)
    return (m.group(1) if m else "/").rstrip("/") + "/"


def raw_source_url(rel: str = "") -> str:
    """raw.githubusercontent.com URL of a docs-relative path ("" if repo_url is unset).

    The branch comes from edit_uri ("edit/<branch>/docs/"), so the page URL, the
    Markdown twin and the raw source stay in step if the repository moves.
    """
    cfg = _config()
    repo = re.search(r'^repo_url\s*=\s*"([^"]+)"', cfg, re.MULTILINE)
    if not repo or "github.com/" not in repo.group(1):
        return ""
    slug = repo.group(1).rstrip("/").split("github.com/")[-1]
    edit = re.search(r'^edit_uri\s*=\s*"([^"]+)"', cfg, re.MULTILINE)
    parts = edit.group(1).strip("/").split("/") if edit else []
    branch = parts[1] if len(parts) > 1 else "main"
    return f"https://raw.githubusercontent.com/{slug}/{branch}/docs/{rel}"
