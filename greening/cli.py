import json
import sys
import shutil
import subprocess
import tempfile
from pathlib import Path

from cookiecutter.main import cookiecutter
from cookiecutter.exceptions import OutputDirExistsException

def main():
    if len(sys.argv) < 2:
        print("Usage: greening <command> [args]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "new" and len(sys.argv) >= 3:
        project_name = sys.argv[2]
        new(project_name)
    elif command == "deploy":
        deploy_site()
    else:
        print("Usage:")
        print("  greening new <project_name>")
        print("  greening deploy")
        sys.exit(1)

def new(project_path: str):
    cwd = Path.cwd()
    project_dir = Path(project_path).resolve()
    is_in_place = project_dir == cwd or project_path == "."
    project_slug = project_dir.name

    config_path = project_dir / "greening.json"
    extra_context = {}
    git_remote = None

    if config_path.exists():
        print(f"🔧 Using {config_path} for extra context")
        with config_path.open() as f:
            config_data = json.load(f)
            extra_context = config_data
            git_remote = config_data.get("git_remote")

    extra_context.update({
        "project_name": project_slug.replace("_", " ").title(),
        "project_slug": project_slug,
    })

    template_path = Path(__file__).parent / "templates" / "python-package-template"

    # Run cookiecutter to generate project files
    cookiecutter(
        str(template_path),
        no_input=True,
        extra_context=extra_context,
        output_dir=str(project_dir.parent if is_in_place else "."),
        overwrite_if_exists=True
    )

    # Git init
    if not (project_dir / ".git").exists():
        print("🔧 Initializing git repo...")
        subprocess.run(["git", "init"], cwd=str(project_dir))
        subprocess.run(["git", "add", "."], cwd=str(project_dir))
        subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=str(project_dir))

        if git_remote:
            print(f"🔗 Adding git remote: {git_remote}")
            subprocess.run(["git", "remote", "add", "origin", git_remote], cwd=str(project_dir))
            subprocess.run(["git", "branch", "-M", "main"], cwd=str(project_dir))
            subprocess.run(["git", "push", "-u", "origin", "main"], cwd=str(project_dir))

def deploy_site():
    repo_root = Path.cwd()
    template_site = Path(__file__).parent / "templates" / "site-template"

    if not template_site.exists():
        print("❌ No templates/site-template/ found in greening package.")
        sys.exit(1)

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        shutil.copytree(template_site, tmp_path, dirs_exist_ok=True)

        try:
            subprocess.run(["git", "rev-parse", "--verify", "gh-pages"], check=True, stdout=subprocess.DEVNULL)
            subprocess.run(["git", "checkout", "gh-pages"], check=True)
        except subprocess.CalledProcessError:
            subprocess.run(["git", "checkout", "--orphan", "gh-pages"], check=True)

        subprocess.run(["git", "rm", "-rf", "."], check=True)

        for item in tmp_path.iterdir():
            shutil.move(str(item), str(repo_root / item.name))

        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Deploy Jekyll site"], check=True)
        subprocess.run(["git", "push", "-f", "origin", "gh-pages"], check=True)

        print("✅ Deployed Jekyll site to gh-pages branch.")
