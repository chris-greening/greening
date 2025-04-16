from greening.greening_config import GreeningConfig

def init() -> None:
    """
    Initialize a `greening.yaml` configuration file in the current directory.

    This function checks whether `greening.yaml` already exists.
    If not, it creates a default configuration using environment-aware
    and git-aware introspection (e.g., GitHub username/email and token).

    - Detects git username and email via `git config`
    - Checks for presence of a `GITHUB_TOKEN` environment variable
    - Writes a default config only if one does not already exist
    """
    config = GreeningConfig()

    if config.path.exists():
        print("⚠️ greening.yaml already exists.")
    else:
        config.write_default()

def help_init() -> None:
    """
    Print usage information for the `greening init` command.

    This help text describes how `greening init` sets up an environment-aware
    greening.yaml configuration file, with examples and options.
    """
    print("""Usage: greening init

Initialize a new greening.yaml config file in the current directory.

This command inspects your environment and Git configuration to prepopulate sensible defaults:
- Auto-detects your GitHub username and email via git config
- Checks for a GITHUB_TOKEN in your environment
- Creates greening.yaml only if one does not already exist

Options:
  --help             Show this help message and exit

Examples:
  greening init
""")