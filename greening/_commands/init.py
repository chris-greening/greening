from pathlib import Path

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
# push: true
# create_github_repo: false

# venv:
#   create: true         # Whether to create a virtual environment
#   python: python3   # Python interpreter to use (optional)
"""

def init():
    config_path = Path.cwd() / "greening.yaml"

    if config_path.exists():
        print("⚠️ greening.yaml already exists.")
        return

    config_path.write_text(DEFAULT_YAML)
    print(f"✅ Created default greening.yaml at {config_path}")
