import yaml
import shutil
import subprocess
import tempfile
from pathlib import Path
from cookiecutter.main import cookiecutter
import importlib.resources as pkg_resources

from greening._helpers import _run_git

def deploy_site():
    """
    Public entrypoint: Renders the site-template via Cookiecutter
    and deploys it to the gh-pages branch of the current repo.
    """
    repo_root = Path.cwd()
    context = _load_project_context(repo_root)
    _render_site_template(context, repo_root)

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
        "project_slug": project_slug
    })
    print(context)
    return context

def _render_site_template(context: dict, repo_root: Path):
    template_path = pkg_resources.files("greening") / "templates" / "site-template"
    with tempfile.TemporaryDirectory() as tmpdir:
        cookiecutter(
            str(template_path),
            no_input=True,
            extra_context=context,  # ← don't nest inside {"cookiecutter": ...}
            output_dir=tmpdir,
            overwrite_if_exists=True
        )
        print(context)
        rendered_path = Path(tmpdir) / context["project_slug"]
        _deploy_rendered_site(rendered_path, repo_root, context["push"])

def _deploy_rendered_site(rendered_path: Path, repo_root: Path, should_push: bool):
    """
    Checks out or creates the gh-pages branch, clears the working tree,
    replaces it with the rendered site, commits and optionally pushes.
    """
    try:
        _run_git("git rev-parse --verify gh-pages", cwd=repo_root)
        _run_git("git checkout gh-pages", cwd=repo_root)
    except subprocess.CalledProcessError:
        _run_git("git checkout --orphan gh-pages", cwd=repo_root)

    _run_git("git rm -rf .", cwd=repo_root)

    for item in rendered_path.iterdir():
        shutil.move(str(item), str(repo_root / item.name))

    _run_git("git add .", cwd=repo_root)
    _run_git("git commit -m 'Deploy Jekyll site'", cwd=repo_root)

    if should_push:
        print("🚀 Pushing gh-pages to origin...")
        _run_git("git push -f origin gh-pages", cwd=repo_root)
    else:
        print("⚠️  Push skipped (set push: true in greening.yaml to enable)")

    _run_git("git checkout main", cwd=repo_root)
