"""Theme handle module."""

from pathlib import Path

DEFAULT_THEME = "revealjs-basic"


def get_theme_path(name: str = DEFAULT_THEME) -> Path:
    """Return directory real path of itself."""
    here = Path(__file__).parent
    return here / name
