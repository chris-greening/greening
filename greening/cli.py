import sys

from greening._commands.new import new
from greening._commands.deploy import deploy_site

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


