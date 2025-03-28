import yaml
from pathlib import Path
from cookiecutter.main import cookiecutter
import importlib.resources as pkg_resources

from greening._helpers import _run_git

def new():
    """
    Public entrypoint: Scaffolds a new project in the current directory,
    initializes Git, and optionally pushes to a remote.
    """
    project_dir = Path.cwd()
    context = _load_project_context(project_dir)
    _scaffold_project(project_dir, context)
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
        output_dir=str(project_dir),
        overwrite_if_exists=True
    )

def _maybe_initialize_git_repo(project_dir: Path, context: dict):
    """
    Initializes a Git repository if one does not already exist,
    and pushes to remote if 'git_remote' is defined in greening.yaml.
    """
    if (project_dir / ".git").exists():
        return

    print("🔧 Initializing git repo...")
    _run_git("git init", cwd=project_dir)
    _run_git("git add .", cwd=project_dir)
    _run_git("git commit -m 'Initial commit'", cwd=project_dir)

    git_remote = context.get("git_remote")
    if git_remote:
        print(f"🔗 Adding git remote: {git_remote}")
        _run_git(f"git remote add origin {git_remote}", cwd=project_dir)
        _run_git("git branch -M main", cwd=project_dir)
        _run_git("git push -u origin main", cwd=project_dir)
