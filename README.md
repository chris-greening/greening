# 🌱 Greening

**Greening** is an opinionated, full-stack project automation tool for solo developers and creative coders.

With just a few commands, you can scaffold a production-ready Python package — complete with docs, tests, GitHub Actions workflows, PyPI packaging, and an auto-deployed GitHub Pages site.
No boilerplate. No setup hell. Just instant polish.

---

## 🤔 Why Greening?

Most devs never ship their tools — not because the code isn’t good, but because the surrounding friction is too high:

- How do I structure the project?
- How do I set up CI/CD, tests, and linting?
- How do I make it look legit?
- How do I talk about it?

Greening answers all of that in **one opinionated workflow**.

---

## ⚙️ What It Does

Greening automates your project creation pipeline:

✅ `greening init` – generates a starter `greening.yaml` config file
✅ `greening new` – scaffolds your entire Python project in-place
✅ `greening deploy` – builds and pushes a polished GitHub Pages site

Additional features:

- Automatically initializes a Git repo
- Optionally creates a GitHub repository via API
- Optionally pushes to GitHub (main branch)
- Injects metadata throughout the project using Cookiecutter
- Uses Jekyll + Minimal Mistakes for clean, brandable documentation

---

## 🚀 Getting Started

### 1. Install `greening`

```bash
pip install greening
```

### 2. Run `greening init`

This creates a starter config file in your current directory:

```
greening init
```

It generates `greening.yaml`:

```yaml
project_name: Test project
project_slug: test_project
github_username: chris-greening
author_name: Chris Greening
email: chris@christophergreening.com

# git_remote: git@github.com:chris-greening/test-repo.git
push: false
create_github_repo: true
```

### 3. Scaffold the project

Run this in the same directory as your config:

```
greening new
```

Greening will generate your project in-place and optionally push it to GitHub.

### 4. Deploy the GitHub Pages site

```
greening deploy
```

This builds a static site using your config and deploys it to the `gh-pages` branch.

---

## 🔐 GitHub Authentication

To enable GitHub repo creation and pushing:

1. [Generate a GitHub Personal Access Token](https://github.com/settings/tokens) with `repo` scope
2. Add it to your shell config:

```
export GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Then run:

```
source ~/.bashrc  # or ~/.zshrc
```

---

## ✨ Philosophy

Greening is about **removing friction** and **surfacing the soul of your work** — fast.
It empowers you to publish and polish your creative tools like they were real products, because they are.

---

## 💚 Created by @chris-greening

