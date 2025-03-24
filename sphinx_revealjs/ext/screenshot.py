"""Extension to generate screenshot for first page of presentation.

This is optional extension.
You need install extra and configure to use it.
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from sphinx.errors import ExtensionError
from sphinx.util.logging import getLogger
from sphinx.util.matching import Matcher

from ..builders import RevealjsHTMLBuilder

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.environment import BuildEnvironment

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    msg = (
        f"{__name__} need playwright."
        "you should run \"pip install 'sphinx-revealjs[screenshot]'\"."
    )
    raise ExtensionError(msg)

from .. import __version__ as core_version

logger = getLogger(__name__)
_targets: dict[str, str] = dict()


def collect_screenshot_targets(
    app: Sphinx,
    env: BuildEnvironment,
    added: set[str],
    changed: set[str],
    removed: set[str],
):
    global _targets
    _targets = {}
    for docname in added:
        _targets[docname] = f"{app.config.revealjs_screenshot_outdir}/{docname}.png"
    for docname in changed:
        _targets[docname] = f"{app.config.revealjs_screenshot_outdir}/{docname}.png"
    return []


def generate_screenshots(app: Sphinx, exception: Exception):
    logger.info("Generating screenshot")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        matcher = Matcher(app.config.revealjs_screenshot_excludes)
        for docname, image_url in _targets.items():
            if matcher(docname):
                continue
            page_path = Path(app.outdir) / app.builder.get_target_uri(docname)
            if page_path.is_dir():
                page_path = page_path / "index.html"
            image_path = Path(app.outdir) / image_url
            page.goto(f"file://{page_path}")
            conf = page.evaluate("Reveal.getConfig()")
            page.set_viewport_size({"width": conf["width"], "height": conf["height"]})
            page.screenshot(path=image_path)


def connect_extension_events(app: Sphinx):
    if isinstance(app.builder, RevealjsHTMLBuilder):
        app.connect("env-get-outdated", collect_screenshot_targets)
        app.connect("build-finished", generate_screenshots)


def setup(app: Sphinx):
    """Entrypoint."""
    app.add_config_value("revealjs_screenshot_outdir", "_images/ogp", "env")
    app.add_config_value("revealjs_screenshot_excludes", [], "env")
    app.connect("builder-inited", connect_extension_events)
    return {
        "version": core_version,
        "env_version": 1,
        "parallel_read_safe": True,
    }
