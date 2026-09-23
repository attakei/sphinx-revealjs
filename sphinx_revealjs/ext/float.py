"""Extension to add revealjs-float directive for grid layouts.

This is optional extension.

This implements a "Grid Layouts" feature similar to GitPitch for positioning
content boxes on slides with width, height, x, and y coordinates.
"""

from __future__ import annotations

import string
from typing import TYPE_CHECKING

from docutils import nodes
from docutils.nodes import SkipNode
from docutils.parsers.rst import Directive, directives

from .. import __version__ as core_version

if TYPE_CHECKING:
    from sphinx.application import Sphinx


class revealjs_float(nodes.General, nodes.Element):
    """Node for revealjs-float directive."""

    pass


class RevealjsFloat(Directive):
    """Directive for creating floating content boxes on slides.

    This directive creates absolutely positioned content boxes that can be
    placed anywhere on a slide using width, height, x, and y coordinates.

    Options:
        drag: Width and height of the box
              (e.g., "40 50" for 40% width, 50% height)
        drop: X and Y position of the box
              (e.g., "10 15" for 10% from left, 15% from top)
              Use negative values for positioning from right/bottom
              (e.g., "-40 -20")
        bg: Background color of the box (e.g., "yellow", "#ff0000")
    """

    has_content = True
    option_spec = {
        "drag": directives.unchanged,
        "drop": directives.unchanged,
        "bg": directives.unchanged,
    }

    def run(self):
        node = revealjs_float()
        node.attributes = self.options
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def visit_revealjs_float(self, node: revealjs_float):
    """Render revealjs-float node for revealjs builder."""
    styles = {
        "position": "absolute",
    }
    if "bg" in node.attributes:
        styles["background-color"] = node.attributes["bg"]
    if "drag" in node.attributes:
        x, y = node.attributes["drag"].split()
        styles["width"] = x if x[-1] not in string.digits else f"{x}%"
        styles["height"] = y if y[-1] not in string.digits else f"{y}%"
    if "drop" in node.attributes:
        x, y = node.attributes["drop"].split()
        if x[0] == "-":
            styles["right"] = x[1:] if x[-1] not in string.digits else f"{x[1:]}%"
        else:
            styles["left"] = x if x[-1] not in string.digits else f"{x}%"
        if y[0] == "-":
            styles["bottom"] = y[1:] if y[-1] not in string.digits else f"{y[1:]}%"
        else:
            styles["top"] = y if y[-1] not in string.digits else f"{y}%"
    style = "; ".join([f"{k}: {v}" for k, v in styles.items()])
    style = f'style="{style}"'
    self.body.append(f"<div {style}>")


def depart_revealjs_float(self, node: revealjs_float):
    """Close revealjs-float div."""
    self.body.append("</div>\n")


def not_write(self, node):
    """visit/depart function for declare "no write"."""
    raise SkipNode


def setup(app: Sphinx):
    """Entrypoint."""
    app.add_node(
        revealjs_float,
        html=(not_write, not_write),
        latex=(not_write, not_write),
        text=(not_write, not_write),
        texinfo=(not_write, not_write),
        revealjs=(visit_revealjs_float, depart_revealjs_float),
        dirrevealjs=(visit_revealjs_float, depart_revealjs_float),
    )
    app.add_directive("revealjs-float", RevealjsFloat)
    return {
        "version": core_version,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
