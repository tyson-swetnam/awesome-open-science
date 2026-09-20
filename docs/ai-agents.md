---
description: How AI agents can consume this site — llms.txt, llms-full.txt, per-page Markdown, and robots.txt.
---

# :material-robot-happy-outline: For AI Agents

This Awesome List is published for people **and** for AI agents. Every page is
available as Markdown at a predictable URL, and the whole corpus is available
as a single file.

## Discovery

| Endpoint | What it is |
|---|---|
| [`/robots.txt`](https://tyson-swetnam.github.io/awesome-open-science/robots.txt) | Crawl policy. Names the major AI crawlers explicitly and points at everything below |
| [`/sitemap.xml`](https://tyson-swetnam.github.io/awesome-open-science/sitemap.xml) | Every rendered page |
| [`/llms.txt`](https://tyson-swetnam.github.io/awesome-open-science/llms.txt) | Linked outline — one entry per page with a one-line description, in navigation order ([llmstxt.org](https://llmstxt.org/){target=_blank} convention) |
| [`/llms-full.txt`](https://tyson-swetnam.github.io/awesome-open-science/llms-full.txt) | The entire site concatenated as Markdown, for ingestion in one request |

## Reading any page as Markdown

Append `index.md` to any page URL:

```
Site page        https://tyson-swetnam.github.io/awesome-open-science/software/
Markdown twin    https://tyson-swetnam.github.io/awesome-open-science/software/index.md
Raw source       https://raw.githubusercontent.com/tyson-swetnam/awesome-open-science/main/docs/software.md
```

All three return the same content. GitHub Pages serves the twin as
`text/markdown; charset=utf-8`. Fetch whichever your sandbox allows — some
permit `github.com` and `raw.githubusercontent.com` but not `*.github.io`.

Inside a Markdown twin, and inside `llms-full.txt`, links to other pages are
absolute and already point at those pages' Markdown twins, so you can traverse
the whole site without leaving Markdown. Drop the trailing `index.md` to reach
the rendered page.

Each rendered page also declares its twin in `<head>`:

```html
<link rel="alternate" type="text/markdown" href="index.md">
```

## What this site is, and how to cite it

This is a **curated directory of links to third-party projects**, not
documentation of a single piece of software. That shapes how its content
should be used:

- Entries are selected against the criteria below, but this list does not
  vouch for the projects beyond that. Descriptions are written by the
  maintainers of this list, not by the projects themselves.
- Where an entry is archived, superseded, or early-stage, its description says
  so. Carry that qualifier through rather than presenting the entry as a live
  recommendation.
- Link rot is the main failure mode of a list like this. Verify a URL before
  relying on it, and prefer the raw source on GitHub for the most recent
  revision.

Inclusion criteria: open source or freely available, actively maintained, real
community or institutional adoption, documented, from a reputable source.

## How it is generated

The agent surface is built in CI, not committed by hand, except for the two
index files which are committed so that drift is visible in review:

| Script | Role |
|---|---|
| `scripts/gen_llms_txt.py` | Writes `docs/llms.txt` and `docs/llms-full.txt` from the `nav` in `zensical.toml`. CI regenerates and fails on drift |
| `scripts/postbuild_agent_surface.py` | After `zensical build`: writes the Markdown twins, injects the `<link rel="alternate">` and the visible "Machine-readable" line, and writes `robots.txt` |
| `scripts/agent_links.py` | Shared link rewriting, so twins and `llms-full.txt` resolve identically |

The `nav` is the single source of truth for which pages exist. A Markdown file
under `docs/` that is not in the nav is deliberately excluded from the agent
surface.

## Contributing

Pull requests are welcome. New pages need a `description:` in YAML frontmatter
(it becomes the page's `llms.txt` entry and its HTML meta description), a `nav`
entry in `zensical.toml`, and a card on the [home page](index.md). Run
`python scripts/gen_llms_txt.py` and commit the regenerated index files.
