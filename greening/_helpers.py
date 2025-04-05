from pathlib import Path
import shlex
import subprocess
from typing import Union
import os

def _run_git(command: str, cwd: Path):
    """
    Runs a full git command string using shlex.split() for safety.
    e.g. 'git commit -m "message with spaces"'
    """
    args = shlex.split(command)
    subprocess.run(args, cwd=str(cwd), check=True)

def get_git_config_username():
    try:
        return subprocess.check_output(
            ["git", "config", "--get", "user.name"],
            universal_newlines=True
        ).strip()
    except subprocess.CalledProcessError:
        return None

def get_git_config_email():
    try:
        return subprocess.check_output(
            ["git", "config", "--get", "user.email"],
            universal_newlines=True
        ).strip()
    except subprocess.CalledProcessError:
        return None

def has_github_token() -> bool:
    return bool(os.getenv("GITHUB_TOKEN"))

def generate_git_section() -> str:
        token_present = has_github_token()
        username = get_git_config_username()
        slug = "my_greening_project"  # This should be dynamically set based on the project slug

        if token_present:
            return f"""\
# git_remote: git@github.com:{username}/{slug}.git
push: true
create_github_repo: true
    """
        else:
            return f"""\
git_remote: git@github.com:{username}/{slug}.git
push: false
# create_github_repo: false
    """
