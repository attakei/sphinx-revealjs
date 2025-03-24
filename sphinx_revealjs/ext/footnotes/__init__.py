"""Extension to add custom CSS for footnotes."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from sphinx.util.logging import getLogger

from ... import __version__ as core_version
from ...builders import RevealjsHTMLBuilder

if TYPE_CHECKING:
    from sphinx.application import Sphinx


here = Path(__file__).parent
logger = getLogger(__name__)


def register_extra_static_path(app: Sphinx):
    if not isinstance(app.builder, RevealjsHTMLBuilder):
        return
    app.builder.config.revealjs_static_path.append(str(here / "static"))
    app.builder.add_css_file("sphinx-revealjs/css/footnotes.css")


def register_css_context(app: Sphinx, ctx: dict):
    """Inject config values into builder's globalcontext."""
    ctx.setdefault(
        "revealjs_footnotes",
        {
            "font_size": app.config.revealjs_footnotes_font_size,
            "ref_font_size": app.config.revealjs_footnotes_ref_font_size,
        },
    )


def setup(app: Sphinx):
    """Entrypoint."""
    app.add_config_value("revealjs_footnotes_font_size", "50%", "env")
    app.add_config_value("revealjs_footnotes_ref_font_size", "70%", "env")
    app.connect("builder-inited", register_extra_static_path)
    app.connect("revealjs:ready-for-writing", register_css_context)
    return {
        "version": core_version,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
