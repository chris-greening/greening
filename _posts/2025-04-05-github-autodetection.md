---
title: GitHub Autodetection Comes to Greening
date: 2024-04-05 12:00:00 -0500
categories: [features]
---

Tired of typing your GitHub username for the hundredth time?

We were too.

Greening now **automatically detects your GitHub username and email** from your local Git configuration, and **intelligently sets up your project YAML** based on whether you’ve authenticated with a `GITHUB_TOKEN`.

This small change adds up to a **much smoother "greening init" experience**, with fewer fields to fill out and fewer reasons to stall when inspiration hits.

## How It Works

When you run:

```bash
greening init
```

Greening now looks for:

```bash
git config user.name
git config user.email
```

If found, it pre-fills those values in `greening.yaml`. No need to remember your GitHub handle, no need to copy-paste your email again.

But it goes one step further…

If you’ve already set a `GITHUB_TOKEN` in your environment (to allow GitHub repo creation), Greening assumes you want automation mode engaged.

So instead of prompting you to manually fill out a `git_remote`, it will:

- Autocomment the `git_remote:` line
- Uncomment and set `create_github_repo: true`

This means when you run:

```bash
greening new
```

You’ll get a **fully scaffolded project**, **GitHub repo automatically created**, and everything pushed in seconds — all without editing a single config field.

## Why We Did This

The philosophy behind Greening has always been:

> If you’ve done it more than twice, Greening should probably do it for you.

Even tiny points of friction — like having to setup a GitHub repo — can break flow. And we’re obsessed with keeping you in flow.

Every saved keystroke, every reduced prompt, every automated step is another seed planted toward a finished project.

## What's Next

We’re actively working on a **plugin system**, smarter defaults, and automatic detection for even more fields. Because the less you have to think about setup, the more you can focus on building.

Try it out. Set your GitHub token, run `greening init`, and just build.

---

📌 [Greening on GitHub](https://github.com/chris-greening/greening)

```bash
pip install greening
```