from pathlib import Path


def get_theme_path(name: str) -> Path:
    here = Path(__file__).parent
    return here / name
