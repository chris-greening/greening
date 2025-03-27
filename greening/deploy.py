import json
from pathlib import Path
import cookiecutter
import subprocess
import tempfile
import shutil

def deploy_site():
    repo_root = Path.cwd()
    template_path = Path(__file__).parent / "templates" / "site-template"

    # Load context from greening.json
    config_path = repo_root / "greening.json"
    extra_context = {}
    if config_path.exists():
        with config_path.open() as f:
            extra_context = json.load(f)

    extra_context.setdefault("project_name", repo_root.name.title())
    extra_context.setdefault("project_slug", repo_root.name)

    # Use cookiecutter to render the site
    with tempfile.TemporaryDirectory() as tmpdir:
        cookiecutter(
            str(template_path),
            no_input=True,
            extra_context=extra_context,
            output_dir=tmpdir
        )

        # Cookiecutter renders into a subfolder: tmpdir/project_slug/
        rendered_path = Path(tmpdir) / extra_context["project_slug"]

        # Switch to gh-pages branch (or create it)
        try:
            subprocess.run(["git", "rev-parse", "--verify", "gh-pages"], check=True, stdout=subprocess.DEVNULL)
            subprocess.run(["git", "checkout", "gh-pages"], check=True)
        except subprocess.CalledProcessError:
            subprocess.run(["git", "checkout", "--orphan", "gh-pages"], check=True)

        # Clean current contents
        subprocess.run(["git", "rm", "-rf", "."], check=True)

        # Move rendered site into repo root
        for item in rendered_path.iterdir():
            shutil.move(str(item), str(repo_root / item.name))

        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Deploy Jekyll site"], check=True)
        subprocess.run(["git", "push", "-f", "origin", "gh-pages"], check=True)

        # Return to main
        subprocess.run(["git", "checkout", "main"], check=True)