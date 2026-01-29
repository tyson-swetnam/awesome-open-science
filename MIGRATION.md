# Migration to Zensical

This document describes the migration from MkDocs Material to Zensical for the awesome-open-science documentation site.

## Overview

**What is Zensical?**

Zensical is a Rust-based build tool created by the Material for MkDocs team that provides:
- Faster build times through Rust performance
- Type-safe configuration using TOML instead of YAML
- Built-in Material for MkDocs theme
- Full compatibility with existing MkDocs plugins and extensions
- Better error messages and validation

**Why migrate?**

- **Performance**: Faster builds, especially for larger documentation sites
- **Type safety**: TOML configuration with validation prevents configuration errors
- **Official support**: Maintained by the Material for MkDocs team
- **Modern tooling**: Rust-based with better dependency management
- **Future-proof**: Active development and long-term support

## What Changed

### Configuration Format
- **Old**: `mkdocs.yml` (YAML format)
- **New**: `zensical.toml` (TOML format)

The configuration structure is nearly identical, just converted to TOML syntax:
- YAML lists → TOML arrays `[...]`
- YAML mappings → TOML tables `{key = "value"}`
- YAML keys with underscores work the same way

### Build Commands
| Task | Old Command | New Command |
|------|-------------|-------------|
| Local dev server | `mkdocs serve` | `zensical serve` |
| Build static site | `mkdocs build` | `zensical build` |
| Deploy to GitHub Pages | `mkdocs gh-deploy --force` | Automated via GitHub Actions |

### Dependencies
**Removed** (bundled with Zensical):
- `mkdocs>=1.4.0`
- `mkdocs-material`
- `mkdocs-material-extensions>=1.0.3`

**Added**:
- `zensical` - The build tool itself
- `cairosvg` - For SVG rendering

**Updated**:
- `nbconvert==6.5` → `nbconvert>=7` - Updated to newer version

### Critical Configuration Changes

#### 1. Emoji Extension Paths
The most critical change is how emoji extensions are configured:

**Old (mkdocs.yml)**:
```yaml
- pymdownx.emoji:
    emoji_index: !!python/name:material.extensions.emoji.twemoji
    emoji_generator: !!python/name:material.extensions.emoji.to_svg
```

**New (zensical.toml)**:
```toml
[project.markdown_extensions.pymdownx.emoji]
emoji_index = "zensical.extensions.emoji.twemoji"
emoji_generator = "zensical.extensions.emoji.to_svg"
```

Using the old Python paths will cause build failures.

#### 2. Color Scheme Rename
The custom color scheme has been renamed from `agic` to `custom-red` for clarity:

**In zensical.toml**:
```toml
[[project.theme.palette]]
media = "(prefers-color-scheme: light)"
scheme = "custom-red"  # Was: agic
toggle = {icon = "material/brightness-7", name = "Switch to dark mode"}
```

**In docs/stylesheets/extra.css**:
```css
[data-md-color-scheme="custom-red"] {  /* Was: agic */
    --md-primary-fg-color:        #EE0F0F;
    --md-primary-fg-color--light: #ECB7B7;
    --md-primary-fg-color--dark:  #90030C;
}
```

#### 3. Favicon Change
The favicon now uses a Material icon instead of a missing file:

**Old**: `favicon: assets/favicon.png` (file not found)
**New**: `favicon: "material/sunglasses"`

#### 4. Copyright Year
Updated from 2022 to 2026:

**Old**: `copyright: 'Copyright &copy; 2022 Tyson Lee Swetnam'`
**New**: `copyright = "Copyright &copy; 2026 Tyson Lee Swetnam"`

### GitHub Actions Workflow
The deployment workflow was completely rewritten:

**Key changes**:
- Switched from `mkdocs gh-deploy` to `zensical build` + `peaceiris/actions-gh-pages@v3`
- Added caching for faster builds
- Added `pngquant` installation for image optimization
- Added `fetch-depth: 0` for git-revision-date plugin
- Changed Python version from `3.9` to `3.x` (latest stable)

## What Stayed the Same

### Content Files
✅ **All Markdown files unchanged** - No modifications needed to any `.md` files in `docs/`

### Directory Structure
✅ **Same structure**:
```
docs/
  index.md
  funding.md
  data.md
  ...
  overrides/
  stylesheets/
```

### Theme Appearance
✅ **Identical look and feel** - Material for MkDocs theme works exactly the same

### Navigation
✅ **Same navigation structure** - All menu items and hierarchy preserved

### Plugins
✅ **All plugins work** - search, mkdocstrings, git-revision-date, mkdocs-jupyter all compatible

### Markdown Extensions
✅ **All extensions supported** - admonitions, tabs, emoji, mermaid diagrams, etc.

### Custom CSS
✅ **Custom styles preserved** - `docs/stylesheets/extra.css` works identically (except scheme rename)

### Custom Overrides
✅ **Theme overrides work** - `docs/overrides/main.html` unchanged

## Developer Guide

### First-Time Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify Zensical installed**:
   ```bash
   zensical --version
   ```

3. **Build the site**:
   ```bash
   zensical build
   ```

4. **Start local server**:
   ```bash
   zensical serve
   ```
   Visit http://127.0.0.1:8000/

### Local Development Workflow

**Same as before**, just replace `mkdocs` with `zensical`:

```bash
# Start dev server with live reload
zensical serve

# Build static site
zensical build

# The site/ directory is generated just like before
```

### Editing Configuration

Configuration is now in `zensical.toml` instead of `mkdocs.yml`:

**Navigation** (TOML array format):
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

**Theme settings** (TOML tables):
```toml
[project.theme]
variant = "classic"
language = "en"
favicon = "material/sunglasses"

[project.theme.font]
text = "Montserrat"
code = "Regular"
```

**Multiple palettes** (TOML array of tables):
```toml
[[project.theme.palette]]
media = "(prefers-color-scheme)"
scheme = "default"
toggle = {icon = "material/brightness-auto", name = "Switch to light mode"}

[[project.theme.palette]]
media = "(prefers-color-scheme: light)"
scheme = "custom-red"
toggle = {icon = "material/brightness-7", name = "Switch to dark mode"}
```

### Adding New Pages

1. Create Markdown file in `docs/` (e.g., `docs/new-page.md`)
2. Add to navigation in `zensical.toml`:
   ```toml
   nav = [
     {"Home" = "index.md"},
     {"New Page" = "new-page.md"}  # Add this line
   ]
   ```
3. Changes appear immediately with `zensical serve`

### CI/CD

**Automatic deployment** on push to `main` branch:
1. GitHub Actions runs workflow (`.github/workflows/publish-docs.yml`)
2. Installs dependencies from `requirements.txt`
3. Runs `zensical build`
4. Deploys to `gh-pages` branch
5. Site updates at https://tyson-swetnam.github.io/awesome-open-science/

**No manual deployment** - The workflow handles everything automatically.

## Known Issues and Notes

### Color Scheme Rename
If you have bookmarks or documentation referencing the old `agic` color scheme, update them to `custom-red`.

### Favicon Change
The original favicon (`assets/favicon.png`) was not found in the repository, so we switched to using a Material icon (`material/sunglasses`) which matches the logo icon.

### Python Version
GitHub Actions now uses Python `3.x` (latest stable) instead of pinned `3.9`. This provides access to the latest features and security updates.

### Cache Directory
Zensical uses `.cache/` for build caching. This directory is gitignored and should not be committed.

### Build Output
The `site/` directory structure is identical to MkDocs output - same file paths, same HTML structure.

## Troubleshooting

### Build fails with emoji errors
**Symptom**: Errors mentioning `material.extensions.emoji`

**Solution**: Verify `zensical.toml` uses correct emoji paths:
```toml
[project.markdown_extensions.pymdownx.emoji]
emoji_index = "zensical.extensions.emoji.twemoji"
emoji_generator = "zensical.extensions.emoji.to_svg"
```

### Color scheme not applying
**Symptom**: Custom red colors don't appear

**Solution**: Check both files:
1. `zensical.toml` uses `scheme = "custom-red"`
2. `docs/stylesheets/extra.css` has `[data-md-color-scheme="custom-red"]`

### Local server won't start
**Symptom**: `zensical serve` fails

**Solution**:
1. Verify installation: `pip install -r requirements.txt`
2. Check for syntax errors in `zensical.toml`
3. Try rebuilding: `zensical build`

### GitHub Actions deployment fails
**Symptom**: Workflow fails on build or deploy step

**Solutions**:
- Check workflow file syntax (`.github/workflows/publish-docs.yml`)
- Verify `requirements.txt` has all dependencies
- Check GitHub Pages settings (should be enabled)
- Review workflow logs for specific errors

### Missing dependencies
**Symptom**: Import errors during build

**Solution**: Install missing packages:
```bash
pip install -r requirements.txt
```

If a specific package is missing, add it to `requirements.txt` and reinstall.

## Migration Comparison

Comparing with the successful awesome-fire-science migration:

| Aspect | awesome-fire-science | awesome-open-science | Status |
|--------|---------------------|---------------------|--------|
| Config conversion | mkdocs.yml → zensical.toml | mkdocs.yml → zensical.toml | ✅ Identical |
| Emoji paths | Updated to zensical | Updated to zensical | ✅ Same fix |
| Color scheme | Kept original name | Renamed agic → custom-red | ℹ️ Improved clarity |
| Favicon | Kept original file | Changed to Material icon | ℹ️ Better solution |
| Navigation complexity | 12 pages | 15 pages (with nested sections) | ✅ More complex, handled |
| Plugins | 4 plugins | 4 plugins (same set) | ✅ Same |
| Workflow | Same pattern | Same pattern | ✅ Proven approach |

## References

- **Zensical Documentation**: https://zensical.org/docs/
- **Material for MkDocs**: https://squidfunk.github.io/mkdocs-material/
- **Awesome Fire Science Migration**: Reference implementation for this migration pattern
- **Repository**: https://github.com/tyson-swetnam/awesome-open-science
- **Live Site**: https://tyson-swetnam.github.io/awesome-open-science/

## Version History

| Date | Version | Changes |
|------|---------|---------|
| 2026-01-29 | 1.0.0 | Initial migration from MkDocs Material to Zensical |

---

**Questions or issues?** Open an issue at https://github.com/tyson-swetnam/awesome-open-science/issues
