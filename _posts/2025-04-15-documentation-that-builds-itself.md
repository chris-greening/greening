---
title: "Documentation That Builds Itself with Sphinx + Read the Docs"
date: 2025-04-17
categories: [features]
tags: [docs, sphinx, readthedocs, automation, python]
---

What if your documentation built itself?

With the latest update to **Greening**, it kind of does.

---

## 🌿 Docs with Zero Effort

When you run:

```bash
greening new
```

Greening now automatically scaffolds a complete [Sphinx](https://www.sphinx-doc.org/) documentation setup right alongside your project.

That includes:

- A fully wired `docs/` directory
- Smart `conf.py` configuration with your project name, slug, author, and version
- Automatic API reference generation using `autodoc` and `autosummary`
- Recursive scanning of your codebase
- The clean and familiar [Read the Docs theme](https://sphinx-rtd-theme.readthedocs.io/)

All of this is driven directly from your `greening.yaml` — no manual setup required.

---

## 🚀 Instant Hosting with Read the Docs

Once your project is pushed to GitHub, all you have to do is:

1. Go to [readthedocs.org](https://readthedocs.org/)
2. Link your GitHub repo
3. ✅ Done

Read the Docs will:
- Automatically detect your `docs/` folder
- Install any dependencies listed in `requirements.txt`
- Build your documentation from your actual code
- Rebuild it every time you push to `main`

Your code is documented. Your documentation is hosted. Everything just works.

---

## 🪴 Summary

No need for extra steps or boilerplate.

Just run:

```bash
greening init
greening new
```

And your project ships with full developer-facing docs, automatically generated and deployed with zero extra effort.

Because documentation should be part of the build, not a separate to-do list.
