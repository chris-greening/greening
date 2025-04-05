from pathlib import Path
import yaml

class GreeningConfig:
    DEFAULT_YAML = """\
# Project metadata
project_name: My Greening Project
project_slug: my_greening_project
author_name: Your Name
email: your@email.com
github_username: your-github-handle

# Optional GitHub integration
# Uncomment to push to a remote
# git_remote: git@github.com:your-name/my-greening-project.git
push: false
create_github_repo: false

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
