---
title: "🌱 New Feature: Beautiful Per-Command Help for the Greening CLI"
date: 2024-04-05
categories: [features]
---

🌿 One of the newest additions to the Greening CLI is intuitive, per-command help. You can now run:

```bash
greening <command> --help
```

or

```bash
greening help <command>
```

To instantly get detailed, actionable help for that specific command — no guesswork, no flipping to the docs mid-flow.

---

## 🌱 How It Works

Let’s say you want to scaffold a new project. Just type:

```bash
greening new --help
```

and you'll see:

```bash
Usage: greening new [OPTIONS]

Scaffold a new Python project using greening.yaml.

This command uses your greening.yaml configuration to generate a full project structure based on a customizable template.
It can also automatically:
- Initialize a GitHub repository
- Create and activate a virtual environment
- Commit and push the project to GitHub

Options:
  --help              Show this message and exit.

Examples:
  greening new
```

---

Want to initialize your config?

```bash
greening init --help
```

Outputs:

```text
Usage: greening init

Initialize a new greening.yaml config file in the current directory.

This command inspects your environment and Git configuration to prepopulate sensible defaults:
- Auto-detects your GitHub username and email via git config
- Checks for a GITHUB_TOKEN in your environment
- Creates greening.yaml only if one does not already exist

Options:
  --help              Show this help message and exit

Examples:
  greening init
```

---

## 🌾 Why This Matters

Greening is all about eliminating friction and helping you ship beautiful software fast. With these new help commands, you can:

- 🌱 Stay in flow
- 🌿 Learn Greening’s capabilities organically
- 🌾 Discover hidden features you might’ve missed

You don’t need to remember everything. You just need to remember:  
```bash
greening <command> --help
```

---

## 🌱 What’s Next?

As new features roll out, each command’s help will grow to reflect new flags, options, and workflows. All discoverable in the CLI — no context switching, no fluff.

Stay tuned — and keep planting those seeds. 🌿
