import sys

from greening._commands.new import new
from greening._commands.deploy import deploy_site
from greening._commands.init import init
from greening._commands.help import help

def main():
    if len(sys.argv) < 2:
        print("Usage: greening <command> [args]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "new":
        new()
    elif command == "deploy":
        deploy_site()
    elif command == "init":
        init()
    elif command == "help":
        help()
    else:
        print("Usage:")
        print("  greening init")
        print("  greening new")
        print("  greening deploy")
        sys.exit(1)


