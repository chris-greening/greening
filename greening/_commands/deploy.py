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
    context = _load_site_context(repo_root)
    _render_site_template(context, repo_root)


def _load_site_context(repo_root: Path) -> dict:
    """
    Loads greening.yaml and builds the context for the site template.
    """
    config_path = repo_root / "greening.yaml"
    context = {}

    if config_path.exists():
        with config_path.open("r") as f:
            context = yaml.safe_load(f) or {}

    context.setdefault("project_name", repo_root.name.title())
    context.setdefault("project_slug", repo_root.name)

    return context


def _render_site_template(context: dict, repo_root: Path):
    """
    Renders the site template using Cookiecutter and deploys it
    to the gh-pages branch.
    """
    template_path = pkg_resources.files("greening") / "templates" / "site-template"

    with tempfile.TemporaryDirectory() as tmpdir:
        cookiecutter(
            str(template_path),
            no_input=True,
            extra_context=context,
            output_dir=tmpdir
        )

        rendered_path = Path(tmpdir) / context["project_slug"]
        _deploy_rendered_site(rendered_path, repo_root)


def _deploy_rendered_site(rendered_path: Path, repo_root: Path):
    """
    Checks out or creates the gh-pages branch, clears the working tree,
    replaces it with the rendered site, commits and pushes.
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
    _run_git("git push -f origin gh-pages", cwd=repo_root)
    _run_git("git checkout main", cwd=repo_root)
