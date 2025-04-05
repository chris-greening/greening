from pathlib import Path
import shlex
import subprocess
from typing import Union

def _run_git(command: str, cwd: Path):
    """
    Runs a full git command string using shlex.split() for safety.
    e.g. 'git commit -m "message with spaces"'
    """
    args = shlex.split(command)
    subprocess.run(args, cwd=str(cwd), check=True)

def get_github_username() -> Union[str, None]:
        try:
            url = subprocess.check_output(["git", "config", "--get", "remote.origin.url"], text=True).strip()
            # Handle both SSH and HTTPS formats
            if "github.com" in url:
                if url.startswith("git@"):
                    return url.split(":")[1].split("/")[0]
                elif url.startswith("https://"):
                    return url.split("github.com/")[1].split("/")[0]
        except subprocess.CalledProcessError:
            pass
        return None