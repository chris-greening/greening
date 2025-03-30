def help():
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

  greening deploy
    → Builds and deploys a static site to the gh-pages branch:
        - Renders the site template
        - Commits and pushes to GitHub if configured

  greening help
    → Displays this help message.

GitHub: https://github.com/chris-greening/greening
""")