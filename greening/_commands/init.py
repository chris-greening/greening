from greening.greening_config import GreeningConfig

def init():
    config = GreeningConfig()

    if config.path.exists():
        print("⚠️ greening.yaml already exists.")
    else:
        config.write_default()