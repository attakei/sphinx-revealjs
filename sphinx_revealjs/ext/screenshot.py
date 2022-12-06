"""Extension to generate screenshot for first page of presentation.

This is optional extension.
You need install extra and configure to use it.
"""
import copy
import json
from pathlib import Path
from typing import Any, Dict, Set

from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.environment import BuildEnvironment
from sphinx.errors import ExtensionError
from sphinx.util.docutils import nodes
from sphinx.util.logging import getLogger
from sphinx.util.matching import Matcher

from ..nodes import revealjs_slide

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    msg = (
        f"{__name__} need playwright."
        "you should run \"pip install 'sphinx-revealjs[screenshot]'\"."
    )
    raise ExtensionError(msg)

from .. import __version__ as core_version

DEFAULT_VIEWPORT_SIZE = {
    "width": 640,
    "height": 480,
}

logger = getLogger(__name__)
_targets: Dict[str, str] = dict()


def calc_viewport(config: Config, doctree: nodes.document) -> Dict[str, int]:
    """Configure viewport for capturing screen."""
    viewport = copy.deepcopy(DEFAULT_VIEWPORT_SIZE)
    # Override by conf.py
    if config.revealjs_script_conf:
        if "width" in config.revealjs_script_conf:
            viewport["width"] = config.revealjs_script_conf["width"]
        if "height" in config.revealjs_script_conf:
            viewport["height"] = config.revealjs_script_conf["height"]
    # Override by revealjs-slide directive
    slide_nodes = list(doctree.findall(revealjs_slide))
    if slide_nodes:
        node = slide_nodes[0]
        if "conf" in node.attributes:
            conf = json.loads(node.attributes["conf"])
            if "width" in conf:
                viewport["width"] = conf["width"]
            if "height" in conf:
                viewport["height"] = conf["height"]
    return viewport


def collect_screenshot_targets(
    app: Sphinx,
    env: BuildEnvironment,
    added: Set[str],
    changed: Set[str],
    removed: Set[str],
):
    global _targets
    _targets = {}
    for docname in added:
        _targets[docname] = f"{app.config.revealjs_screenshot_path}/{docname}.png"
    for docname in changed:
        _targets[docname] = f"{app.config.revealjs_screenshot_path}/{docname}.png"
    return []


def insert_og_image(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: Dict[str, Any],
    doctree: nodes.document,
):
    image_url = f"{app.config.revealjs_screenshot_url}/{_targets[pagename]}"
    context.setdefault("metatags", "")
    context["metatags"] += f'\n<meta property="og:image" content="{image_url}" >'


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
            page.set_viewport_size(
                calc_viewport(app.config, app.env.get_doctree(docname))
            )
            page.goto(f"file://{page_path}")
            page.screenshot(path=image_path)


def setup(app: Sphinx):
    """Entryoint."""
    app.add_config_value("revealjs_screenshot_url", "http://localhost:8000", "env")
    app.add_config_value("revealjs_screenshot_path", "_images/ogp", "env")
    app.add_config_value("revealjs_screenshot_excludes", [], "env")
    app.connect("env-get-outdated", collect_screenshot_targets)
    app.connect("html-page-context", insert_og_image)
    app.connect("build-finished", generate_screenshots)
    return {
        "version": core_version,
        "env_version": 1,
        "parallel_read_safe": True,
    }
