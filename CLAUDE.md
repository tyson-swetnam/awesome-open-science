# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Zensical-based documentation website that provides an "Awesome List" of open science platforms, tools, and resources for research and education. Zensical is a Rust-based build tool by the Material for MkDocs team. The site is published via GitHub Pages to https://tyson-swetnam.github.io/awesome-open-science/.

## Development Commands

### Local Development Server
```bash
zensical serve
```
Starts a local development server with live reload at http://127.0.0.1:8000/

### Install Dependencies
```bash
pip install -r requirements.txt
```
Installs all required Python packages including Zensical, plugins, and dependencies.

### Build Documentation
```bash
zensical build
```
Builds the static site into the `site/` directory.

### Deploy to GitHub Pages
Deployment is fully automated via GitHub Actions on push to main. No manual deployment command is needed.

## Repository Structure

- **`docs/`** - All documentation source files in Markdown format
  - `index.md` - Homepage with Open Science definitions and FAQ
  - Content organized by topic: `data.md`, `funding.md`, `edu.md`, `publishing.md`, `software.md`, etc.
  - `overrides/` - Custom HTML templates for MkDocs Material theme
  - `stylesheets/` - Custom CSS styles
  - `awesome_open_combined.md` - Combined version (untracked in git status)

- **`zensical.toml`** - Main configuration file (TOML format) defining:
  - Site metadata and URLs
  - Navigation structure (nav tree)
  - Material theme configuration with dark/light mode palette toggles
  - Markdown extensions (admonitions, tabs, mermaid diagrams, emoji, etc.)
  - Plugins: search, mkdocstrings, git-revision-date, mkdocs-jupyter

- **`requirements.txt`** - Python dependencies for Zensical and all plugins

- **`.github/workflows/publish-docs.yml`** - GitHub Actions workflow that auto-deploys on push to main

- **`MIGRATION.md`** - Documentation of the migration from MkDocs to Zensical

## Architecture Notes

### Zensical Build System
The site uses Zensical, a Rust-based build tool by the Material for MkDocs team:
- Faster build times compared to Python-based MkDocs
- Type-safe TOML configuration instead of YAML
- Built-in Material for MkDocs theme
- Full compatibility with MkDocs plugins and extensions
- Better error messages and validation

### Material for MkDocs Theme
The site uses the Material for MkDocs theme (via Zensical) with extensive customization:
- Color scheme toggles (auto/light/dark mode) with custom "custom-red" theme
- Custom fonts: Montserrat for text, Regular for code
- Social links in footer (ORCID, GitHub, Twitter, LinkedIn, Docker, YouTube)
- Google Analytics integration
- Material icon as favicon (material/sunglasses)

### Markdown Extensions
Heavy use of PyMdown Extensions for enhanced Markdown:
- **Admonitions** - Collapsible callout boxes (used extensively for Questions, Tips, Ideas)
- **Emoji** - Material Design icons via `:material-*:` and `:fontawesome-*:` syntax
- **Mermaid diagrams** - Flowcarts for visualizing open science concepts
- **Tabbed content** - For organizing complex information
- **Task lists** - Checkbox lists
- **Critic markup** - For showing edits/changes

### Content Organization Philosophy
Content files are curated lists of resources organized by topic:
- Each page focuses on a specific aspect of open science (data, funding, education, etc.)
- Links use `{target=_blank}` to open in new tabs
- YAML-style admonitions (`??? Question`, `??? Tip`) for collapsible FAQ sections
- Consistent use of Material icons for visual enhancement

## GitHub Actions CI/CD
The site automatically builds and deploys on every push to main:
- Uses Python 3.x (latest stable)
- Installs pngquant for image optimization
- Installs from requirements.txt
- Runs `zensical build` to generate static site
- Uses peaceiris/actions-gh-pages@v3 to deploy to gh-pages branch
- Implements caching for faster builds

## When Editing Content

- Content files are in `docs/` and use `.md` extension
- Navigation structure is defined in `zensical.toml` under the `nav =` array using TOML format
- Add new pages by creating `.md` files in `docs/` and updating `nav` in `zensical.toml`
- Use Material icons syntax: `:material-icon-name:` or `:fontawesome-solid-icon-name:`
- Follow the existing admonition patterns for consistency
- Links to external resources should include `{target=_blank}`

## TOML Configuration Format

Navigation uses TOML array syntax:
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

## Migration Notes

The site was migrated from MkDocs to Zensical in January 2026. See `MIGRATION.md` for details on:
- What changed (configuration format, build commands, dependencies)
- What stayed the same (all content, theme appearance, plugins)
- Troubleshooting common issues
- Developer workflow
