import os
import yaml
import requests
import subprocess
from pathlib import Path
from cookiecutter.main import cookiecutter
import importlib.resources as pkg_resources

from greening._helpers import _run_git

def new():
    """
    Public entrypoint: Scaffolds a new project in the current directory,
    initializes Git, optionally creates a virtual environment,
    and optionally pushes to a remote.
    """
    project_dir = Path.cwd()
    context = _load_project_context(project_dir)
    print("🧪 Final context passed to Cookiecutter:")
    _scaffold_project(project_dir, context)
    _maybe_create_virtualenv(project_dir, context)
    _maybe_initialize_git_repo(project_dir, context)

def _load_project_context(project_dir: Path) -> dict:
    """
    Loads greening.yaml if present and builds the full context
    for the cookiecutter template.
    """
    config_path = project_dir / "greening.yaml"
    context = {}

    if config_path.exists():
        print(f"🔧 Using {config_path} for extra context")
        with config_path.open("r") as f:
            context = yaml.safe_load(f) or {}

    project_slug = project_dir.name
    context.update({
        "project_name": project_slug.replace("_", " ").title(),
        "project_slug": project_slug,
    })

    return context

def _scaffold_project(project_dir: Path, context: dict):
    """
    Runs Cookiecutter to scaffold a project using the local template.
    """
    template_path = pkg_resources.files("greening") / "templates" / "python-package-template"

    cookiecutter(
        str(template_path),
        no_input=True,
        extra_context=context,
        output_dir=str(project_dir.parent),  # Avoid nested folder
        overwrite_if_exists=True,
    )

def _maybe_create_virtualenv(project_dir: Path, context: dict):
    """
    Creates a virtual environment at 'venv/' if 'venv.create' is true in the config.
    This is intentionally opinionated: the venv will always be named 'venv'.
    """
    venv_config = context.get("venv", {})
    if not venv_config.get("create", False):
        return

    venv_path = project_dir / "venv"  # Enforced naming convention
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

def _maybe_initialize_git_repo(project_dir: Path, context: dict):
    """
    Initializes a Git repository if one does not already exist,
    and pushes to remote if 'push: true' is defined in greening.yaml.
    Optionally auto-creates the GitHub repo if 'create_github_repo: true'
    and GITHUB_TOKEN is set.
    """
    if (project_dir / ".git").exists():
        return

    print("🔧 Initializing git repo...")
    _run_git("git init", cwd=project_dir)
    _run_git("git add .", cwd=project_dir)
    _run_git("git commit -m 'Initial commit'", cwd=project_dir)
    _run_git("git branch -M main", cwd=project_dir)

    git_remote = context.get("git_remote")
    create_repo = context.get("create_github_repo", False)
    push_enabled = context.get("push", False)

    if not git_remote and create_repo:
        git_remote = _maybe_create_github_repo(context)
        if git_remote:
            context["git_remote"] = git_remote

    if git_remote:
        print(f"🔗 Adding git remote: {git_remote}")
        _run_git(f"git remote add origin {git_remote}", cwd=project_dir)

        if push_enabled:
            print("🚀 Pushing to GitHub...")
            _run_git("git push -u origin main", cwd=project_dir)
        else:
            print("⚠️  Push skipped (set push: true in greening.yaml to enable)")

def _maybe_create_github_repo(context: dict) -> str | None:
    """
    Creates a GitHub repo using the GITHUB_TOKEN if configured and enabled.
    Returns the SSH git remote URL or None.
    """
    token = os.getenv("GITHUB_TOKEN")
    username = context.get("github_username")
    repo_slug = context.get("project_slug")

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
            "description": context.get("project_name", "")
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
