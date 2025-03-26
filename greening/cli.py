import json
import sys
from pathlib import Path

from cookiecutter.main import cookiecutter

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "new":
        print("Usage: greening new <project_name>")
        sys.exit(1)

    project_name = sys.argv[2]
    new(project_name)

def new(project_path: str):
    cwd = Path.cwd()

    # Handle "." or absolute/relative folder paths
    project_dir = Path(project_path).resolve()
    is_in_place = project_dir == cwd or project_path == "."

    # Extract project slug (used in naming, etc.)
    project_slug = project_dir.name

    # Load greening.json from project_dir
    config_path = project_dir / "greening.json"
    extra_context = {}

    if config_path.exists():
        print(f"🔧 Using {config_path} for extra context")
        with config_path.open() as f:
            extra_context = json.load(f)

    # Always inject essential values
    extra_context.update({
        "project_name": project_slug.replace("_", " ").title(),
        "project_slug": project_slug,
    })

    # Path to your local template
    template_path = Path(__file__).parent / "templates" / "python-package-template"

    # Generate directly into this folder (no nesting)
    cookiecutter(
        str(template_path),
        no_input=True,
        extra_context=extra_context,
        output_dir=str(project_dir.parent if is_in_place else "."),
        overwrite_if_exists=True
    )
