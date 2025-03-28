from pathlib import Path
import shlex
import subprocess

def _run_git(command: str, cwd: Path):
    """
    Runs a full git command string using shlex.split() for safety.
    e.g. 'git commit -m "message with spaces"'
    """
    args = shlex.split(command)
    subprocess.run(args, cwd=str(cwd), check=True)