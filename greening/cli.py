import json
import sys
import shutil
import subprocess
import tempfile
from pathlib import Path

from cookiecutter.main import cookiecutter
from cookiecutter.exceptions import OutputDirExistsException

from greening.new import new
from greening.deploy import deploy_site

def main():
    if len(sys.argv) < 2:
        print("Usage: greening <command> [args]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "new" and len(sys.argv) >= 3:
        project_name = sys.argv[2]
        new(project_name)
    elif command == "deploy":
        deploy_site()
    else:
        print("Usage:")
        print("  greening new <project_name>")
        print("  greening deploy")
        sys.exit(1)


