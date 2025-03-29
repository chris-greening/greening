---
permalink: /quickstart/
title: "Quickstart"
excerpt: "greening"
---

Greening is a dev automation tool for solo developers who want to ship polished software fast, without spending hours setting up the same boilerplate over and over.

This guide walks you through creating a new project from scratch using Greening.

---

## ⚙️ What the Commands Do

- **`greening init`**
  Creates a starter `greening.yaml` config file in your current directory.

- **`greening new`**
  Scaffolds a complete project using the config:
  - Sets up your Python project
  - Creates a virtual environment at `venv/` (optional)
  - Initializes a Git repo
  - Optionally creates and pushes to a GitHub repo

- **`greening deploy`**
  Builds and deploys a static site to GitHub Pages (like your docs or about page) to the `gh-pages` branch.
  Great for publishing your project landing page.

---

## 🚀 Step-by-Step

### 1. Create a Config File

Run:

```bash
greening init
```

Then edit the newly created `greening.yaml`:

```yaml
project_name: My Greening Project
project_slug: my_greening_project
author_name: Your Name
email: you@example.com
github_username: your-handle
create_github_repo: true
push: true

venv:
  create: true
  python: python3
```

> 🔒 You’ll also need a `GITHUB_TOKEN` set in your environment to auto-create/push the repo. See [GitHub docs here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#personal-access-tokens-classic)

---

### 2. Scaffold the Project

Run:

```bash
greening new
```

Greening will:
- Generate the project structure using a Cookiecutter template
- Create a `venv/` if configured
- Initialize Git and optionally push to GitHub

---

### 3. Deploy Your Site (Optional)

With a single command you can generate a clean GitHub Pages site that auto-deploys to GitHub

```bash
greening deploy
```

This:
- Renders your site using Cookiecutter
- Checks out (or creates) a `gh-pages` branch
- Commits and optionally pushes your static site

---

## 🧪 Example Folder After Scaffolding

```
my_greening_project/
├── venv/               # Optional virtual environment
├── my_greening_project/    # Your Python package
├── tests/
├── pyproject.toml
├── README.md
├── .git/
├── .github/
└── greening.yaml
```

---

## 🔁 Reusability & Scale

Once your config is dialed in, you can reuse it across every project. Greening ensures:

- Consistent structure
- Documented from day one
- Ready to publish at any moment