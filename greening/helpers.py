from pathlib import Path
import shlex
import subprocess
from typing import Union
import os

def run_git(command: str, cwd: Path) -> None:
    """
    Run a Git command in a subprocess.

    Uses `shlex.split()` to safely tokenize the command string, then executes it
    using `subprocess.run()` with the specified working directory.

    Parameters
    ----------
    command : str
        The full Git command as a string, e.g., 'git commit -m "message"'.
    cwd : Path
        The working directory in which to run the command.

    Raises
    ------
    subprocess.CalledProcessError
        If the Git command fails.
    """
    args = shlex.split(command)
    subprocess.run(args, cwd=str(cwd), check=True)

def get_git_config_username() -> Union[str, None]:
    """
    Get the Git username from global git config.

    Returns
    -------
    str or None
        The Git username if found, otherwise None.
    """
    try:
        return subprocess.check_output(
            ["git", "config", "--get", "user.name"],
            universal_newlines=True
        ).strip()
    except subprocess.CalledProcessError:
        return None

def get_git_config_email() -> Union[str, None]:
    """
    Get the Git email from global git config.

    Returns
    -------
    str or None
        The Git email if found, otherwise None.
    """
    try:
        return subprocess.check_output(
            ["git", "config", "--get", "user.email"],
            universal_newlines=True
        ).strip()
    except subprocess.CalledProcessError:
        return None

def has_github_token() -> bool:
    """
    Check if a GitHub token is set in the environment.

    Returns
    -------
    bool
        True if GITHUB_TOKEN is present in the environment, False otherwise.
    """
    return bool(os.getenv("GITHUB_TOKEN"))

def generate_git_section() -> str:
    """
    Generate the Git configuration block for greening.yaml.

    Returns a YAML-formatted string with recommended Git settings:
    - Suggests a `git_remote` URL based on the local Git username and slug
    - Enables or disables automatic GitHub repo creation and pushing
      based on the presence of GITHUB_TOKEN

    Returns
    -------
    str
        A YAML snippet containing Git-related configuration.
    """
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
