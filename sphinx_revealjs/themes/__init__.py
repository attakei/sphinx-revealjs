"""Theme handle module."""
from pathlib import Path

DEFAULT_THEME = "sphinx_revealjs"


def get_theme_path(name: str = DEFAULT_THEME) -> Path:
    """Return directory real path of itself."""
    here = Path(__file__).parent
    return here / name


def get_revealjs_path(theme_name: str = DEFAULT_THEME) -> Path:
    """Return path-object of bundled Reveal.js files."""
    return get_theme_path(theme_name) / "static" / "revealjs"
