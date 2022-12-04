"""Extension to generate screenshot for first page of presentation.

This is optional extension.
You need install extra and configure to use it.
"""
from sphinx.application import Sphinx
from sphinx.errors import ExtensionError
from sphinx.util.logging import getLogger

from .. import __version__ as core_version

logger = getLogger(__name__)


def setup(app: Sphinx):
    """Entryoint."""
    try:
        import playwright  # noqa: F401
    except ImportError:
        msg = (
            f"{__name__} need playwright."
            "you should run \"pip install 'sphinx-revealjs[screenshot]'\"."
        )
        raise ExtensionError(msg)

    return {
        "version": core_version,
        "env_version": 1,
        "parallel_read_safe": True,
    }
