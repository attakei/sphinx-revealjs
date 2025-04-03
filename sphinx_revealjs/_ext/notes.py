"""Internal extension for Speaker view or Reveal.js."""

from __future__ import annotations

import html
from typing import TYPE_CHECKING

from docutils import nodes
from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from sphinx.util.docutils import SphinxDirective

from .. import __version__
from ..builders import RevealjsHTMLBuilder
from ..writers import not_write

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.writers.html5 import HTML5Translator


class revealjs_notes(nodes.Admonition, nodes.Element):  # noqa: D101
    pass


class RevealjsNotes(BaseAdmonition, SphinxDirective):  # noqa: D101
    has_content = True
    node_class = revealjs_notes

    def run(self):  # noqa: D102
        (node,) = super().run()
        if isinstance(node, (nodes.system_message, revealjs_notes)):
            return [node]


def visit_revealjs_notes(self: HTML5Translator, node: revealjs_notes):  # noqa: D103
    if not isinstance(self.builder, RevealjsHTMLBuilder):
        self.visit_admonition(node)
        return
    self.body.append(f'<aside class="notes">{html.escape(node.astext())}</aside>')
    raise nodes.SkipNode


def depart_revaljs_notes(self: HTML5Translator, node: revealjs_notes):  # noqa: D103
    if not isinstance(self.builder, RevealjsHTMLBuilder):
        self.depart_admonition(node)
        return


def setup(app: Sphinx):  # noqa: D103
    app.add_node(
        revealjs_notes,
        html=(visit_revealjs_notes, depart_revaljs_notes),
        latex=(not_write, not_write),
        text=(not_write, not_write),
        man=(not_write, not_write),
        texinfo=(not_write, not_write),
        revealjs=(visit_revealjs_notes, depart_revaljs_notes),
        dirrevealjs=(visit_revealjs_notes, depart_revaljs_notes),
    )
    app.add_directive("revealjs-notes", RevealjsNotes)
    app.add_config_value("revealjs_notes_from_comments", False, "env")
    return {
        "version": __version__,
        "env_version": 2,
        "parallel_read_safe": True,
    }
