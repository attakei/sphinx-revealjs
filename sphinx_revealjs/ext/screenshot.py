"""Extension to generate screenshot for first page of presentation.

This is optional extension.
You need install extra and configure to use it.
"""
from pathlib import Path
from typing import Set

from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.errors import ExtensionError
from sphinx.util.logging import getLogger

from .. import __version__ as core_version

logger = getLogger(__name__)
_targets = set()


def collect_screenshot_targets(
    app: Sphinx,
    env: BuildEnvironment,
    added: Set[str],
    changed: Set[str],
    removed: Set[str],
):
    global _targets
    _targets = added.union(changed)
    return []


def generate_screenshots(app: Sphinx, exception: Exception):
    logger.info("Generating screenshot")
    for docname in _targets:
        image_url = f"{app.config.revealjs_screenshot_url}/{docname}.png"
        out_path = Path(app.outdir) / image_url
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.touch()


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

    app.add_config_value("revealjs_screenshot_url", "_images/ogp", "env")
    app.connect("env-get-outdated", collect_screenshot_targets)
    app.connect("build-finished", generate_screenshots)
    return {
        "version": core_version,
        "env_version": 1,
        "parallel_read_safe": True,
    }
