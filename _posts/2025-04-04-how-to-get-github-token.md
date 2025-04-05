---
title: How to Generate a GitHub Token for Pushing Repos with Greening
date: 2024-04-04 12:00:00 -0500
categories: how-to github setup
---

When using `greening new` to auto-create and push a repo to GitHub, you'll need a **GitHub token** with proper permissions. This token allows Greening to authenticate with the GitHub API on your behalf and create new repositories for your projects.

Here’s how to generate one and use it securely:

---

## 🔐 Step 1: Generate a New Token

1. Visit [github.com/settings/tokens](https://github.com/settings/tokens)
2. Click **"Generate new token"**
3. **Use the following settings**:
   - **Note**: `Greening CLI access`
   - **Expiration**: Choose one (90 days or custom)
   - **Scopes**: Check the box for:
     - `repo` (Full control of private repositories)
4. Click **"Generate token"** and **copy it immediately**.

---

## 🧠 Step 2: Add It to Your Environment

For security, never hard-code your token into your project.

Instead, add it to your environment using one of the following:

### Unix/macOS

```bash
export GITHUB_TOKEN=ghp_your_token_here
```

You can also add this to your `~/.bashrc`, `~/.zshrc`, or `~/.bash_profile`.

### Windows (Command Prompt)

```cmd
set GITHUB_TOKEN=ghp_your_token_here
```

### Windows (PowerShell)

```powershell
$env:GITHUB_TOKEN = "ghp_your_token_here"
```

---

## ✅ Step 3: Use It with Greening

Now that your token is available, Greening will detect it automatically.

Just run:

```bash
greening new
```

If you have `create_github_repo: true` in your `greening.yaml` config, Greening will:

- Create a new GitHub repo
- Add the remote
- Push your project

No extra steps. ✨

---

## 🧼 Bonus: Keeping Your Token Safe

- **Don’t commit `.env` files or shell profiles** to public repos.
- **Rotate your token periodically**, especially if it becomes exposed.
- **Use fine-grained tokens** for more control (GitHub now supports these).

---

Greening aims to make shipping your ideas painless — and this is a big part of that. By setting up your token once, you’ll unlock powerful automation across every new project.

Happy shipping 🌱

—

*Got questions? Open an issue or join the discussion at [greening](https://github.com/chris-greening/greening)*
