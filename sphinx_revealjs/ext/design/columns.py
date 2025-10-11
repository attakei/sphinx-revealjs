"""Multiple column layout."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from ... import __version__

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.config import Config


def setup_config(app: Sphinx, config: Config):
    """Update config values for this."""
    ext_static_path = Path(__file__).parent / "_static"
    if str(ext_static_path) not in config.revealjs_static_path:
        config.revealjs_static_path.append(str(ext_static_path))
    config.revealjs_css_files.append("sphinx-revealjs/design/columns.css")


def setup(app: Sphinx):
    app.connect("config-inited", setup_config)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": False,
    }
