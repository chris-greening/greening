from pathlib import Path
import yaml

from greening._helpers import get_git_config_username, get_git_config_email, generate_git_section

class GreeningConfig:
    DEFAULT_YAML = f"""\
# Project metadata
project_name: My Greening Project
project_slug: my_greening_project
author_name: Your Name
email: {get_git_config_email() or "your@email.com"}
github_username: {get_git_config_username() or "your-github-username"}

# Optional GitHub integration
# To enable GitHub repo creation, set GITHUB_TOKEN in your environment.
# This token must have repo scope.
# For more info: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
{generate_git_section()}

venv:
   create: false         # Whether to create a virtual environment
   python: python3      # Python interpreter to use (optional)

# google_analytics: G-XXXXXXXXXX
"""

    def __init__(self, path: Path = Path.cwd() / "greening.yaml"):
        self.path = path
        self.data = {}

        if self.path.exists():
            with self.path.open("r") as f:
                self.data = yaml.safe_load(f) or {}

        # Set derived fields
        project_slug = self.path.parent.name
        self.data.setdefault("project_name", project_slug.replace("_", " ").title())
        self.data.setdefault("project_slug", project_slug)

    def get(self, key, default=None):
        return self.data.get(key, default)

    def as_cookiecutter_context(self):
        return self.data

    def write_default(self):
        if self.path.exists():
            print("⚠️ greening.yaml already exists.")
            return

        self.path.write_text(self.DEFAULT_YAML)
        print(f"✅ Created default greening.yaml at {self.path}")

    def to_cookiecutter_context(self):
        return self.data