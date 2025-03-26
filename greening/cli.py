import json
from pathlib import Path
from cookiecutter.main import cookiecutter

def new(project_name: str):
    template_path = Path(__file__).parent / "templates" / "python-package-template"
    user_config_path = Path.cwd() / "greening.json"

    # Load greening.json if it exists in current directory
    if user_config_path.exists():
        with open(user_config_path) as f:
            extra_context = json.load(f)
    else:
        extra_context = {}

    # Always inject the project_name and slug
    extra_context.update({
        "project_name": project_name,
        "project_slug": project_name.replace("-", "_"),
    })

    cookiecutter(
        str(template_path),
        no_input=True,
        extra_context=extra_context
    )
