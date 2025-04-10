"""
Handles the `greening new` command.

This module provides the core logic to scaffold a new project using the
configuration defined in `greening.yaml`. It supports project generation
via Cookiecutter, optional virtual environment setup, and Git/GitHub
initialization and push.
"""

import os
import requests
import subprocess
from pathlib import Path
from cookiecutter.main import cookiecutter
from importlib_resources import files
import shutil
import tempfile
from typing import Union

from greening.greening_config import GreeningConfig
from greening.helpers import run_git

def new() -> None:
    """
    Scaffolds a new project using `greening.yaml`, initializes Git,
    optionally creates a virtual environment, and optionally pushes
    to a GitHub remote.

    This is the public entry point used by `greening new`.
    """
    config = GreeningConfig()
    print("🧪 Final context passed to Cookiecutter:")
    _scaffold_project(config)
    _maybe_create_virtualenv(config)
    _maybe_initialize_git_repo(config)

def help_new() -> None:
    """
    Displays help text for the `greening new` CLI command.

    Prints usage instructions and configuration-based behavior such as
    GitHub repo creation, virtual environment setup, and project scaffolding.
    """
    print("""Usage: greening new [OPTIONS]

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
""")

def _scaffold_project(config: GreeningConfig) -> None:
    template_path = files("greening") / "templates" / "python-package-template"

    with tempfile.TemporaryDirectory() as tmpdir:
        cookiecutter(
            str(template_path),
            no_input=True,
            extra_context=config.to_cookiecutter_context(),
            output_dir=tmpdir,
            overwrite_if_exists=True,
        )

        rendered_path = Path(tmpdir) / config.data["project_slug"]

        # 🔥 Move everything from rendered_path into current directory
        for item in rendered_path.iterdir():
            dest = config.path.parent / item.name
            if dest.exists():
                if dest.is_dir():
                    shutil.rmtree(dest)
                else:
                    dest.unlink()
            shutil.move(str(item), str(dest))

        print(f"✅ Project files copied into {config.path.parent}")

def _maybe_create_virtualenv(config: GreeningConfig) -> None:
    """
    Creates a virtual environment at `venv/` if enabled in `greening.yaml`.

    Parameters
    ----------
    config : GreeningConfig
        The parsed greening.yaml configuration which may include a 'venv' block
        with `create` and `python` settings.

    Notes
    -----
    Uses `subprocess.run` to invoke `python -m venv`. If the virtual environment
    already exists or is disabled, no action is taken.
    """
    venv_config = config.data.get("venv", {})
    if not venv_config.get("create", False):
        return

    venv_path = config.path.parent / "venv"
    python_exe = venv_config.get("python", "python3")

    print(f"🐍 Creating virtual environment at {venv_path}...")
    try:
        subprocess.run(
            [python_exe, "-m", "venv", str(venv_path)],
            check=True
        )
        print("✅ Virtual environment created.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create virtual environment: {e}")

def _maybe_initialize_git_repo(config: GreeningConfig) -> None:
    """
    Initializes a Git repository in the current project directory and optionally
    creates a remote GitHub repo and pushes to it.

    Parameters
    ----------
    config : GreeningConfig
        The parsed greening.yaml configuration, which may include flags for
        GitHub repo creation, remote addition, and pushing to origin.

    Notes
    -----
    This function uses `run_git` to perform Git operations. If a `.git` folder
    already exists, the function exits early.
    """
    project_dir = config.path.parent

    if (project_dir / ".git").exists():
        return

    print("🔧 Initializing git repo...")
    run_git("git init", cwd=project_dir)
    run_git("git add .", cwd=project_dir)
    run_git("git commit -m 'Initial commit'", cwd=project_dir)
    run_git("git branch -M main", cwd=project_dir)

    git_remote = config.data.get("git_remote")
    create_repo = config.data.get("create_github_repo", False)
    push_enabled = config.data.get("push", False)

    if not git_remote and create_repo:
        git_remote = _maybe_create_github_repo(config)
        if git_remote:
            config.data["git_remote"] = git_remote

    if git_remote:
        print(f"🔗 Adding git remote: {git_remote}")
        run_git(f"git remote add origin {git_remote}", cwd=project_dir)

        if push_enabled:
            print("🚀 Pushing to GitHub...")
            run_git("git push -u origin main", cwd=project_dir)
        else:
            print("⚠️  Push skipped (set push: true in greening.yaml to enable)")

def _maybe_create_github_repo(config: GreeningConfig) -> Union[str, None]:
    """
    Creates a GitHub repository using the GitHub API and returns the remote URL.

    Parameters
    ----------
    config : GreeningConfig
        The parsed greening.yaml configuration, including the GitHub username
        and project slug for repository creation.

    Returns
    -------
    str or None
        The SSH remote URL for the created repository, or None if creation fails
        or required fields are missing.

    Notes
    -----
    Requires a valid `GITHUB_TOKEN` in the environment. If the repository already
    exists, returns the expected Git URL without re-creating it.
    """
    token = os.getenv("GITHUB_TOKEN")
    username = config.data.get("github_username")
    repo_slug = config.data.get("project_slug")

    if not token:
        print("🔒 No GITHUB_TOKEN found. Skipping GitHub repo creation.")
        return None

    if not username or not repo_slug:
        print("⚠️ Missing github_username or project_slug. Cannot create repo.")
        return None

    print(f"📡 Creating repo {username}/{repo_slug} on GitHub...")

    response = requests.post(
        "https://api.github.com/user/repos",
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github+json"
        },
        json={
            "name": repo_slug,
            "private": False,
            "auto_init": False,
            "description": config.data.get("project_name", "")
        }
    )

    if response.status_code == 201:
        print(f"✅ GitHub repo created: {username}/{repo_slug}")
        return f"git@github.com:{username}/{repo_slug}.git"
    elif response.status_code == 422:
        print(f"⚠️ Repo already exists: {username}/{repo_slug}")
        return f"git@github.com:{username}/{repo_slug}.git"
    else:
        print(f"❌ Failed to create repo: {response.status_code} - {response.text}")
        return None