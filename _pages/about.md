---
permalink: /about/
title: "About"
excerpt: "greening"
---

# About Greening

**Greening** is a creative dev automation engine built for solo developers who want to **ship beautiful software fast**—repeatably, scalably, and without wasting time on boilerplate.

This tool is for indie hackers, open-source tinkerers, and makers who want every project to look polished from the start. Greening handles the structure—**you bring the spark**.

---

## 💡 Philosophy

Greening is built around a few key beliefs:

- **Ship beautiful software fast**  
  Your time should go toward building—not wiring up the same files again and again.

- **Repeatable, scalable workflows**  
  Every project starts from a clean, consistent base that grows with you.

- **Documentation-first, self-explaining projects**  
  Greening scaffolds documentation and enforces code clarity through self-documenting principles, clean scope, and consistent structure.

- **Opinionated, solo-dev focused**  
  This tool is made for individuals who want their projects to feel studio-grade. No configuration chaos, just smart defaults that work.

- **Full lifecycle support**  
  - `greening init` creates your `greening.yaml`
  - `greening new` scaffolds the project structure
  - `greening deploy` builds and publishes your site to the `gh-pages` branch

  If configured, Greening can:
  - Automatically create your GitHub repo
  - Push the initial commit and site deploy with zero manual setup

---

## 🚀 Quickstart

1. Create a config:

```bash
greening init
```

2. Edit the `greening.yaml` that was created:

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

3. Scaffold the project:

```bash
greening new
```

4. Deploy your GitHub Pages site (optional):

```bash
greening deploy
```

---

## 🌱 Why Greening?

Greening is about growth. Not just of code, but of confidence, habits, and output. It's for creators who want to build with momentum and ship with pride.

> Make it beautiful.  
> Make it repeatable.  
> Make it yours.


[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/chrisgreening)
