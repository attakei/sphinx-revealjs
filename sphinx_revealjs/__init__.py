"""Root module for sphinx-revealjs."""

from __future__ import annotations

__version__ = "3.2.1"

from typing import TYPE_CHECKING

from sphinx.util import logging

from sphinx_revealjs import deprecated
from sphinx_revealjs.builders import (
    DirectoryRevealjsHTMLBuilder,
    RevealjsHTMLBuilder,
    convert_reveal_js_files,
)
from sphinx_revealjs.directives import (
    RevealjsBreak,
    RevealjsFragments,
    RevealjsSection,
    RevealjsSlide,
    RevealjsVertical,
)
from sphinx_revealjs.nodes import (
    revealjs_break,
    revealjs_fragments,
    revealjs_section,
    revealjs_slide,
    revealjs_vertical,
)
from sphinx_revealjs.themes import get_theme_path
from sphinx_revealjs.writers import (
    depart_revealjs_break,
    not_write,
    skip_node,
    visit_revealjs_break,
)

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.config import Config


logger = logging.getLogger(__name__)

BEHVIOR_FOR_BUILDERS: dict[str, dict] = {
    "skip_contents": {
        "html": (skip_node, None),
        "latex": (skip_node, None),
        "text": (skip_node, None),
        "texinfo": (skip_node, None),
        "revealjs": (skip_node, None),
        "dirrevealjs": (skip_node, None),
    },
    "walk_contents": {
        "html": (not_write, not_write),
        "latex": (not_write, not_write),
        "text": (not_write, not_write),
        "texinfo": (not_write, not_write),
        "revealjs": (not_write, not_write),
        "dirrevealjs": (not_write, not_write),
    },
}


def inherit_extension_nodes(app: Sphinx, config: Config):
    """Inherit behaviors of nodes from other sphinx extensions.

    .. note::

        I want to use add_node with override option,
        but sphinx app manage only names of nodes, not class types.
    """
    html_trans = app.registry.translation_handlers["html"]
    revealjs_trans = app.registry.translation_handlers["revealjs"]
    dirrevealjs_trans = app.registry.translation_handlers["dirrevealjs"]
    for n, b in html_trans.items():
        if n not in revealjs_trans:
            revealjs_trans[n] = b
    for n, b in revealjs_trans.items():
        if n not in dirrevealjs_trans:
            dirrevealjs_trans[n] = b


def setup(app: Sphinx):
    """Set up function called by Sphinx."""
    app.require_sphinx("7.0")
    app.add_event("revealjs:ready-for-writing")
    app.connect("config-inited", inherit_extension_nodes)
    app.connect("config-inited", convert_reveal_js_files)
    app.connect("config-inited", deprecated.handle)
    app.add_builder(RevealjsHTMLBuilder)
    app.add_builder(DirectoryRevealjsHTMLBuilder)
    app.add_node(
        revealjs_vertical,
        **BEHVIOR_FOR_BUILDERS["skip_contents"],
    )
    app.add_node(
        revealjs_section,
        **BEHVIOR_FOR_BUILDERS["skip_contents"],
    )
    app.add_node(
        revealjs_break,
        **{
            **BEHVIOR_FOR_BUILDERS["skip_contents"],
            "revealjs": (visit_revealjs_break, depart_revealjs_break),
            "dirrevealjs": (visit_revealjs_break, depart_revealjs_break),
        },
    )
    app.add_node(
        revealjs_slide,
        **BEHVIOR_FOR_BUILDERS["skip_contents"],
    )
    app.add_node(
        revealjs_fragments,
        **BEHVIOR_FOR_BUILDERS["walk_contents"],
    )
    app.add_directive("revealjs-vertical", RevealjsVertical)
    app.add_directive("revealjs-section", RevealjsSection)
    app.add_directive("revealjs-break", RevealjsBreak)
    app.add_directive("revealjs-slide", RevealjsSlide)
    app.add_directive("revealjs-fragments", RevealjsFragments)
    app.add_config_value("revealjs_html_theme", "revealjs-basic", "env")
    app.add_config_value("revealjs_use_section_ids", False, "env")
    app.add_config_value("revealjs_use_index", False, "env")
    app.add_config_value("revealjs_static_path", [], "env")
    app.add_config_value("revealjs_style_theme", "black", "env")
    app.add_config_value("revealjs_js_files", [], "env")
    app.add_config_value("revealjs_css_files", [], "env")
    app.add_config_value("revealjs_script_files", [], "env")
    app.add_config_value("revealjs_script_conf", None, "env")
    app.add_config_value("revealjs_script_plugins", [], "env")
    app.add_html_theme("revealjs-basic", str(get_theme_path("revealjs-basic")))
    app.add_html_theme("revealjs-simple", str(get_theme_path("revealjs-simple")))
    app.setup_extension("sphinx_revealjs._ext.highlightings")
    app.setup_extension("sphinx_revealjs._ext.notes")
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": False,
    }
