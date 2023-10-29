"""Extension to add custom CSS for footnotes."""
from pathlib import Path

from sphinx.application import Sphinx
from sphinx.util.logging import getLogger

from ... import __version__ as core_version
from ...builders import RevealjsHTMLBuilder

here = Path(__file__).parent
logger = getLogger(__name__)


def register_extra_static_path(app: Sphinx):
    if not isinstance(app.builder, RevealjsHTMLBuilder):
        return
    app.builder.config.revealjs_static_path.append(str(here / "static"))
    app.builder.add_css_file("sphinx-revealjs/css/footnotes.css")


def setup(app: Sphinx):
    """Entryoint."""
    app.connect("builder-inited", register_extra_static_path)
    return {
        "version": core_version,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
