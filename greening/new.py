import json
from pathlib import Path
import cookiecutter
import subprocess

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