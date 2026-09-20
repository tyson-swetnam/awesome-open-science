# awesome-open-science

[![pages-build-deployment](https://github.com/tyson-swetnam/awesome-open-science/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/tyson-swetnam/awesome-open-science/actions/workflows/pages/pages-build-deployment)

awesome list of open science platforms for research and education

https://tyson-swetnam.github.io/awesome-open-science/

# Build instructions

The site is built with [Zensical](https://zensical.org/docs/), the Rust-based build tool from the
Material for MkDocs team. Configuration lives in `zensical.toml`.

```
git clone https://github.com/tyson-swetnam/awesome-open-science

cd awesome-open-science

pip install -r requirements.txt

zensical serve
```

`zensical serve` starts a live-reloading dev server at http://127.0.0.1:8000/

To build the static site into `site/`:

```
zensical build
```

Deployment is automatic: pushes to `main` build and publish to GitHub Pages via
[.github/workflows/publish-docs.yml](.github/workflows/publish-docs.yml).
