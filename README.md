<p align="center">
  <img src="media/logo.png" width="800px">
</p>

# 🌱 Greening

`greening` is an opinionated, full-stack Project as Code automation tool for solo developers and creative coders.

With just a few commands, you can scaffold a production-ready Python package complete with docs, tests, GitHub Actions workflows, PyPI packaging, and an auto-deployed GitHub Pages site.
No boilerplate or setup hell, just instant polish.

[![Downloads](https://static.pepy.tech/personalized-badge/greening?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=downloads)](https://pepy.tech/project/greening)
[![Issues](https://img.shields.io/github/issues/chris-greening/greening)](https://github.com/chris-greening/greening/issues)
[![License](https://img.shields.io/github/license/chris-greening/greening)](LICENSE)
[![Version](https://img.shields.io/pypi/v/greening?color=brightgreen)](https://pypi.org/project/greening/)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/chrisgreening)

## Table of Contents
* [🍃 Why `greening`?](#why-greening)
* [🌿 Key features](#key-features)
* [🌲 Getting started](#getting-started)
* [🌻 GitHub authentication](#github-authentication)
* [🌳 Blog posts](#blog)
* [🌴 Roadmap](#roadmap)
* [🍀 Support](#support)

---

## 🍃 Why `greening`? <a name="why-greening"></a>

Most devs never ship their tools. Not because the code isn’t good, but because the surrounding friction is too high:

- How do I structure the project?
- How do I set up CI/CD, tests, and linting?
- How do I make it look legit?
- How do I talk about it?

`greening` answers all of that in **one opinionated workflow**.

<p align="center">
  <img src="media/greening_usage_speed.gif" alt="User typing in commands greening init, greening new, and greening deploy and rapidly deploying a project", width="600px">
</p>

---

## 🌿 Key features <a name="key-features"></a>

`greening` automates your project creation pipeline:

✅ `greening init` - generates a starter `greening.yaml` config file
✅ `greening new` - scaffolds your entire Python project in-place

Additional features:

- Builds and pushes a polished GitHub Pages site
- Automatically initializes a Git repo
- Optionally creates a GitHub repository via API
- Optionally pushes to GitHub (main branch)
- Injects metadata throughout the project using Cookiecutter
- Uses Jekyll + Minimal Mistakes for clean, brandable documentation
- Auto-documentation with Sphinx + Read the Docs support
- Automatically wire in Google Analytics if configured
  
---

## 🌲 Getting started <a name="getting-started"></a>

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

`greening` will generate your project in-place and optionally push it to GitHub.

---

## 🌻 GitHub authentication <a name="github-authentication"></a>

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

See this [blog post](https://chris-greening.github.io/greening/how-to/github/setup/2024/04/04/how-to-get-github-token.html) for more

---

## 🌳 Blog posts <a name="blog"></a>
Check the blog out for more info [here](https://chris-greening.github.io/greening/blog/)

- [Introducing Greening: Ship Beautiful Software, Fast](https://chris-greening.github.io/greening/2025/04/04/introducing-greening.html)
- [Open Source is Soil: The Greening Philosophy](https://chris-greening.github.io/greening/2025/04/04/open-source-is-soil.html)
- [The Philosophy Behind Greening: Developer Momentum](https://chris-greening.github.io/greening/2025/04/04/the-philosophy-behind-greening.html)
- [How to Generate a GitHub Token for Pushing Repos with Greening](https://chris-greening.github.io/greening/how-to/github/setup/2024/04/04/how-to-get-github-token.html)
- [How to Enable Google Analytics Tracking in Your Greening-Deployed Site](https://chris-greening.github.io/greening/how-to/2025/04/04/how-to-enable-google-analytics.html)

## 🌴 Roadmap <a name="roadmap"></a>

A focused, opinionated roadmap toward making Greening the most seamless developer automation tool for launching and shipping polished open source projects.

- Plugin ecosystem to support custom features, commands, etc. within the greening command-line tool
- Custom template support for creating tailor-made templates
- Idempotent execution so commands are safe to run repeatedly with no unexpected side effects
- Cleanup partial builds in the event of a command failure to prevent half-baked launches

---

## 🍀 Support <a name="support"></a>

Reach out to me if you want to connect or have any questions and I will do my best to get back to you
* Email:
  * chris@christophergreening.com
* Twitter:
  * [@ChrisGreening](https://twitter.com/ChrisGreening)
* LinkedIn
  * [Chris Greening](https://www.linkedin.com/in/chris-greening-646411139/)
* Personal contact form: 
  * [www.christophergreening.com](https://www.christophergreening.com/contact)

<p align="center">
  <img src="media/syntax_image.png" alt="Python logo with greenery growing around it", width="300px">
</p>
