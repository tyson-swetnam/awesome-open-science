# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

An "Awesome List" of open science platforms, tools, and resources, published as a documentation
website. There is no application code — the repository is curated Markdown in `docs/` plus build
configuration. Content is the product.

Built with [Zensical](https://zensical.org/docs/), the Rust-based successor to MkDocs from the
Material for MkDocs team. Migrated from MkDocs in January 2026 (see `MIGRATION.md`).

## Commands

```bash
pip install -r requirements.txt   # prerequisite — zensical is usually not on PATH
zensical serve                    # dev server with live reload at http://127.0.0.1:8000/
zensical build                    # static site into site/
```

`zensical build` is the **only** verification gate in this repo: there are no tests, no linters,
and no Python source. Don't go looking for a test command. `site/` and `.cache/` are gitignored.

Deployment is automatic: `.github/workflows/publish-docs.yml` runs `zensical build` on every push
to `main` and publishes `site/` to the `gh-pages` branch via `peaceiris/actions-gh-pages@v3`. No
manual deploy step.

All site and navigation configuration lives in **`zensical.toml`**. (The legacy `mkdocs.yml` was
deleted in September 2026 — it had long since stopped being read by the build.)

## Configuration couplings that break silently

These pairs must be changed together — a mismatch produces a broken build or silently wrong styling:

| Coupling | Files |
|---|---|
| `custom-red` palette scheme name | `zensical.toml` palette **and** `docs/stylesheets/extra.css` `[data-md-color-scheme="custom-red"]` |
| Emoji extension paths must be `zensical.extensions.emoji.*` — the MkDocs `material.extensions.emoji.*` form **fails the build** | `zensical.toml` |
| `[project.plugins.mkdocstrings]` requires the `mkdocstrings` package — zensical **hard-errors**: `"mkdocstrings plugin is enabled, but mkdocstrings is not installed"`. This check is mkdocstrings-specific; `git-revision-date` being declared-but-missing builds fine. | `zensical.toml` **and** `requirements.txt` |
| Card grid / `category-header` / `hero-quote` classes | `docs/index.md` **and** `docs/stylesheets/extra.css` (requires the `md_in_html` extension) |

`MIGRATION.md` documents these gotchas in more depth, including troubleshooting for the emoji and
color-scheme failures.

## Adding or retiring a page

**Adding a page is three steps**, and step 3 is the one that gets missed:

1. Create `docs/<name>.md`.
2. Add it to `nav` in `zensical.toml` (TOML array-of-tables syntax):
   ```toml
   nav = [
     {"Home" = "index.md"},
     {"Research" = [
       {"Funding Opportunities" = "funding.md"},
       {"Data Management Plans" = "dmp.md"}
     ]},
     {"Data" = "data.md"}
   ]
   ```
3. Add a matching card to `docs/index.md` under the right `category-header` section — the homepage
   is a hand-built landing page, not generated from `nav`, so a new page is invisible there
   otherwise.

**Retiring a page**: when content is merged into another page, drop it from `nav` and leave a
`!!! Warning` redirect stub in the file pointing at the successor, so existing links don't break.
Delete the file only once the stub has been published long enough to be safe. (`cloud.md` went
through this cycle — merged into `cyberinfrastructure.md`, stubbed, then deleted.)

## Content conventions

Resource entries are **bare paragraphs, one per line — not bullet lists**:

```markdown
[ORCID](https://orcid.org/){target=_blank} - unique digital ID for every researcher
```

- Every external link carries `{target=_blank}`.
- Description follows a ` - ` separator, lowercase, no trailing period.
- `-` bullets are used only for sub-resources nested under a parent entry (e.g. OSF under Center
  for Open Science).
- Material icons prefix section headings and some entries: `:material-flask:`,
  `:fontawesome-brands-orcid:`.
- Admonitions are used sparingly — 12 across all thirteen pages. `??? Question` / `??? Tip` /
  `??? Idea` for collapsible FAQ items, `!!! Quote` / `!!! Note` / `!!! Warning` for callouts.
  Don't assume every section wants one.

Prior curation applied these inclusion criteria: open source or freely available, actively
maintained, real community or institutional adoption, documented, from a reputable source.

## Documentation files

- **`MIGRATION.md`** — historical record of the MkDocs→Zensical migration. Its emoji-path and
  color-scheme troubleshooting still applies; other sections (custom overrides, `mkdocs-jupyter`)
  describe files that have since been deleted.
- **`IMPLEMENTATION_SUMMARY.md`** — historical work log from a past content-expansion effort. Its
  "Remaining Work" / "Next Steps" sections are a snapshot, not current instructions.
- **`README.md`** — public-facing build instructions; keep its commands in sync with this file.

## Known discrepancy

`zensical.toml` sets `site_url = "https://tysonswetnam.com/awesome-open-science"`, which drives
canonical URLs, but with no `CNAME` file the site actually serves from
https://tyson-swetnam.github.io/awesome-open-science/. Both values are in the repo as-is; don't
"fix" one without asking.
