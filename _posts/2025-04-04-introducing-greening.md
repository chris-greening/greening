---
title: "Introducing Greening: Ship Beautiful Software, Fast"
date: 2025-04-04
layout: single
author_profile: true
excerpt: "Greening is an open source automation tool that helps developers launch, document, and ship projects faster — with less boilerplate and more focus on what matters."
---

I built **Greening** because I was tired of boilerplating the same setup over and over again. GitHub Actions, README templates, virtualenvs, docs, deployment pipelines — it adds up fast. And even worse, it slows you down right at the moment you're most excited to build something new.

**Greening** is an open source automation tool that eliminates the friction of starting, documenting, and shipping your next software project. Whether it's a Python package, a portfolio project, or a polished GitHub Pages site, Greening handles the scaffolding, Git setup, documentation, and even optional Google Analytics integration — all in one command.

## Why I Built It

As a solo dev, context-switching kills momentum. I found myself avoiding small projects simply because I didn't want to spend an hour setting up the boilerplate. So I asked:

> What if I could *automate the launch of my projects* just like I automate my tests, builds, and deployments?

Greening grew from that idea.

## What It Does

- 📁 `greening new` creates a new project, scaffolds a clean structure, and optionally sets up Git, virtual environments, and GitHub remotes.
- 🌐 `greening deploy` generates and deploys a beautiful Jekyll-based GitHub Pages site — perfect for project documentation.
- 📊 Google Analytics integration? Just drop your tag into the config, and you're done.
- ⚙️ Customizable YAML-based config with opinionated defaults that get out of your way.

## Philosophy

Greening is built on a few key ideas:

- **Ship fast.** Don’t let tooling slow down your ideas.
- **Repeatable and scalable.** Make every project look clean and polished from day one.
- **Beautiful by default.** Your software deserves a good first impression.
- **Automation-first.** If you’ve done it more than twice, Greening should probably do it for you.

## What’s Next

I’m working toward a plugin-based ecosystem so you can extend Greening to match your exact workflow. Want to auto-generate CHANGELOGs? Autodoc your Python code? Auto-post releases to social media? That’s where we’re headed.

---

You can check out the project on GitHub here:  
👉 [https://github.com/chris-greening/greening](https://github.com/chris-greening/greening)
