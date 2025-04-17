def general_help() -> None:
    """
    Print a general overview of Greening's CLI commands.

    Displays descriptions of all available subcommands, including:
    - `init`: Generates a greening.yaml configuration file
    - `new`: Scaffolds a new project using greening.yaml and Cookiecutter
    - `help`: Prints this overview help message

    Includes GitHub project link for reference.
    """
    print("""
🌿 Greening — Ship Beautiful Software Fast
-----------------------------------------

Available Commands:

  greening init
    → Creates a default greening.yaml config file in the current directory.

  greening new
    → Scaffolds a new project using greening.yaml:
        - Sets up project structure via Cookiecutter
        - Optionally creates a virtual environment
        - Initializes Git
        - Optionally creates and pushes to a GitHub repo

  greening help
    → Displays this help message.

GitHub: https://github.com/chris-greening/greening
""")