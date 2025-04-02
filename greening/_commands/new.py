import os
import requests
import subprocess
from pathlib import Path
from cookiecutter.main import cookiecutter
import importlib.resources as pkg_resources
import shutil
import tempfile

from greening.greening_config import GreeningConfig
from greening._helpers import _run_git

def new():
    """
    Public entrypoint: Scaffolds a new project in the current directory,
    initializes Git, optionally creates a virtual environment,
    and optionally pushes to a remote.
    """
    config = GreeningConfig()
    print("🧪 Final context passed to Cookiecutter:")
    _scaffold_project(config)
    _maybe_create_virtualenv(config)
    _maybe_initialize_git_repo(config)

def _scaffold_project(config: GreeningConfig):
    template_path = pkg_resources.files("greening") / "templates" / "python-package-template"

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

def _maybe_create_virtualenv(config: GreeningConfig):
    """
    Creates a virtual environment at 'venv/' if 'venv.create' is true in the config.
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

def _maybe_initialize_git_repo(config: GreeningConfig):
    """
    Initializes a Git repository and pushes to remote if specified.
    """
    project_dir = config.path.parent

    if (project_dir / ".git").exists():
        return

    print("🔧 Initializing git repo...")
    _run_git("git init", cwd=project_dir)
    _run_git("git add .", cwd=project_dir)
    _run_git("git commit -m 'Initial commit'", cwd=project_dir)
    _run_git("git branch -M main", cwd=project_dir)

    git_remote = config.data.get("git_remote")
    create_repo = config.data.get("create_github_repo", False)
    push_enabled = config.data.get("push", False)

    if not git_remote and create_repo:
        git_remote = _maybe_create_github_repo(config)
        if git_remote:
            config.data["git_remote"] = git_remote

    if git_remote:
        print(f"🔗 Adding git remote: {git_remote}")
        _run_git(f"git remote add origin {git_remote}", cwd=project_dir)

        if push_enabled:
            print("🚀 Pushing to GitHub...")
            _run_git("git push -u origin main", cwd=project_dir)
        else:
            print("⚠️  Push skipped (set push: true in greening.yaml to enable)")

def _maybe_create_github_repo(config: GreeningConfig) -> str | None:
    """
    Creates a GitHub repo using the GITHUB_TOKEN.
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
