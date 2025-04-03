"""Custom directives for Reveal.js."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, overload

from docutils import nodes
from docutils.nodes import Sequential
from docutils.parsers.rst import Directive, directives
from sphinx.util import logging

from sphinx_revealjs.nodes import (
    FlagAttribute,
    revealjs_break,
    revealjs_fragments,
    revealjs_section,
    revealjs_slide,
    revealjs_vertical,
)

if TYPE_CHECKING:
    from typing import Union

logger = logging.getLogger(__name__)


def raw_json(argument):
    """Type of direction attribute."""
    if argument is None:
        return directives.unchanged(argument)
    try:
        json.loads(argument)
    except json.decoder.JSONDecodeError:
        return ""
    return argument


class RevealjsSectionAttributes(dict):
    def __getitem__(self, key):
        """Extend dict for custom plugins of revealjs.

        Many plugins may refer ``data-`` attributes
        of ``section`` elements as optional behaviors.
        """
        if key in self:
            return super().__getitem__(key)
        if key.startswith("data-"):
            return directives.unchanged
        return None


REVEALJS_SECTION_ATTRIBUTES = {
    # Markup / Slide State
    "data-state": directives.unchanged,
    # Backgrounds / Color Backgrounds
    "data-background-color": directives.unchanged,
    # Backgrounds / Gradient Backgrounds
    "data-background-gradient": directives.unchanged,
    # Backgrounds / Image Backgrounds
    "data-background-image": directives.unchanged,
    "data-background-position": directives.unchanged,
    "data-background-repeat": directives.unchanged,
    # Backgrounds / Video Backgrounds
    "data-background-video": directives.unchanged,
    "data-background-video-loop": directives.unchanged,
    "data-background-video-muted": directives.unchanged,
    # Backgrounds / Image and Video Backgrounds
    "data-background-size": directives.unchanged,
    "data-background-opacity": directives.unchanged,
    # Backgrounds / Iframe Backgrounds
    "data-background-iframe": directives.unchanged,
    "data-background-interactive": lambda x: FlagAttribute(),
    # Slide Visibility
    "data-visibility": directives.unchanged,
    # Transitions
    "data-transition": directives.unchanged,
    "data-transition-speed": directives.unchanged,
    "data-background-transition": directives.unchanged,
    # Auto-Animate
    "data-auto-animate": lambda x: FlagAttribute(),
    "data-auto-animate-delay": directives.unchanged,
    "data-auto-animate-duration": directives.unchanged,
    "data-auto-animate-easing": directives.unchanged,
    "data-auto-animate-unmatched": directives.unchanged,
    "data-auto-animate-id": directives.unchanged,
    "data-auto-animate-restart": lambda x: FlagAttribute(),
    # Auto-Slide / Slide Timing
    "data-autoslide": directives.unchanged,
}


@overload
def inject_children(node: revealjs_section) -> revealjs_section: ...


@overload
def inject_children(node: revealjs_break) -> revealjs_break: ...


@overload
def inject_children(node: revealjs_vertical) -> revealjs_vertical: ...


def inject_children(
    node: Union[revealjs_section, revealjs_break, revealjs_vertical],
) -> Union[revealjs_section, revealjs_break, revealjs_vertical]:
    """Inject extra nodes as children."""

    def _configure_local_image(node, uri):
        if any([uri.startswith(p) for p in ("//", "http://", "https://")]):
            return
        child = nodes.image(uri=uri)
        node.append(child)

    if "data-background-image" in node.attributes:
        _configure_local_image(node, node.attributes["data-background-image"])
    if "data-background-video" in node.attributes:
        _configure_local_image(node, node.attributes["data-background-video"])
    if "data-background-iframe" in node.attributes:
        _configure_local_image(node, node.attributes["data-background-iframe"])

    return node


class RevealjsVertical(Directive):  # noqa: D101
    option_spec = RevealjsSectionAttributes(**REVEALJS_SECTION_ATTRIBUTES)

    def run(self):  # noqa: D102
        node = revealjs_vertical()
        node.attributes.update(self.options)
        return [
            inject_children(node),
        ]


class RevealjsSection(Directive):  # noqa: D101
    option_spec = RevealjsSectionAttributes(**REVEALJS_SECTION_ATTRIBUTES)

    def run(self):  # noqa: D102
        node = revealjs_section()
        node.attributes.update(self.options)
        return [
            inject_children(node),
        ]


class RevealjsBreak(Directive):  # noqa: D101
    option_spec = RevealjsSectionAttributes(
        # if it is set, next section does not display title
        notitle=lambda x: FlagAttribute(),
        **REVEALJS_SECTION_ATTRIBUTES,
    )

    def run(self):  # noqa: D102
        node = revealjs_break()
        node.attributes.update(self.options)
        return [
            inject_children(node),
        ]


class RevealjsSlide(Directive):  # noqa: D101
    has_content = True

    option_spec = {
        "theme": directives.unchanged,
        # TODO: Remove it next breaking changes.
        "google_font": directives.unchanged,
        "conf": raw_json,
    }

    def run(self):  # noqa: D102
        # TODO: Remove it next breaking changes.
        if "google_font" in self.options:
            logger.warning("DEPRECATED: 'google_font' is not working already.")
        node = revealjs_slide()
        node.attributes.update(self.options)
        node.content = "\n".join(self.content or [])
        return [
            node,
        ]


class RevealjsFragments(Directive):  # noqa: D101
    has_content = True

    option_spec = {
        "custom-effect": directives.unchanged,
    }

    def run(self):  # noqa: D102
        node = revealjs_fragments()
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, node)
        # TODO: Parameter ?
        for child in node.children:
            if not isinstance(child, Sequential):
                child["classes"].append("fragment")
                if "custom-effect" in self.options:
                    child["classes"] += ["custom", self.options["custom-effect"]]
                continue
            for c in child:
                c["classes"].append("fragment")
                if "custom-effect" in self.options:
                    c["classes"] += ["custom", self.options["custom-effect"]]
        return [
            node,
        ]
