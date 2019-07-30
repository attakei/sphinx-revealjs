"""Theme handle module."""
from pathlib import Path


def get_theme_path(name: str) -> Path:
    """Return directory real path of itself."""
    here = Path(__file__).parent
    return here / name
