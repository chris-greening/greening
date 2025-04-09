from greening.greening_config import GreeningConfig

def init():
    config = GreeningConfig()

    if config.path.exists():
        print("⚠️ greening.yaml already exists.")
    else:
        config.write_default()

def help_init():
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