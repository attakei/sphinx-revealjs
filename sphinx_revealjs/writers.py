"""Custom write module."""

from __future__ import annotations

import posixpath
from typing import TYPE_CHECKING

from docutils.nodes import (
    SkipChildren,
    SkipNode,
    image,
    section,
    title,
)
from sphinx.writers.html5 import HTML5Translator

from .nodes import (
    revealjs_section,
    revealjs_slide,
    revealjs_vertical,
)

if TYPE_CHECKING:
    from typing import Union

    from docutils.nodes import (
        Element,
        comment,
        literal_block,
    )
    from sphinx.builders.html import StandaloneHTMLBuilder

    from .nodes import revealjs_break


def build_attributes_str(
    node: Union[revealjs_section, revealjs_break, revealjs_vertical],
    builder: StandaloneHTMLBuilder,
) -> str:
    node = node.deepcopy()
    img_idx = node.first_child_matching_class(image)
    if img_idx is not None:
        img: image = node.children[img_idx]  # type: ignore[assignment]
        if "data-background-image" in node.attributes:
            node["data-background-image"] = posixpath.join(
                builder.imgpath, builder.images[img["uri"]]
            )
        if "data-background-video" in node.attributes:
            node["data-background-video"] = posixpath.join(
                builder.imgpath, builder.images[img["uri"]]
            )
        if "data-background-iframe" in node.attributes:
            node["data-background-iframe"] = posixpath.join(
                builder.imgpath, builder.images[img["uri"]]
            )
    return node.attributes_str()


class RevealjsSlideTranslator(HTML5Translator):
    """Translate Reveal.js HTML class."""

    permalink_text = False

    def __init__(self, builder, *args, **kwds):  # noqa: D107
        super().__init__(builder, *args, **kwds)
        self.builder.add_permalinks = False
        self._nest_step = 0

    def visit_section(self, node: section):
        """Begin ``section`` node.

        - Find first ``revealjs_section`` node and build attributes string.
        - When enter next section, nest level.
        """
        self.section_level += 1
        if self.section_level >= 4:
            return
        idx = node.first_child_matching_class(revealjs_section)
        attrs = ""
        if idx is not None:
            attrs = build_attributes_str(node.children[idx], self.builder)  # type: ignore[arg-type]

        if node.attributes.get("ids") and self.config.revealjs_use_section_ids:
            attrs += ' id="{}"'.format(node.attributes["ids"][-1])

        if self._nest_step > 0:
            self.body.append("</section>\n" * self._nest_step)
            self._nest_step = 0
        if self.section_level == 1:
            self._nest_step = 2
            s_idx = node.first_child_matching_class(revealjs_slide)
            self.builder.revealjs_slide = (  # type: ignore[attr-defined]
                None if s_idx is None else node.children[s_idx]
            )
        elif self.section_level == 2:
            self._nest_step = 1

        if self._nest_step > 0:
            v_idx = node.first_child_matching_class(revealjs_vertical)
            v_attrs = (
                ""
                if v_idx is None
                else build_attributes_str(node.children[v_idx], self.builder)  # type: ignore[arg-type]
            )
            self.body.append(f"<section {v_attrs}>\n")
        self.body.append(f"<section {attrs}>\n")

    def depart_section(self, node: section):
        """End ``section``.

        Dedent section level
        """
        self.section_level -= 1
        # NOTE:: When level changes 1 to 0, tag is closed by proc of ``_nest_step``.
        if self.section_level == 0:
            return
        # NOTE:: Reveal.js is max section level is 2.
        if self.section_level > 2:
            return
        self.body.append("</section>\n")

    def visit_comment(self, node: Element):
        """Begin ``comment`` node.

        comment node render as speaker note.
        """
        if self.builder.app.config.revealjs_notes_from_comments:
            self.body.append('<aside class="notes">\n')
        else:
            raise SkipNode

    def depart_comment(self, node: comment):
        """End ``comment`` node.

        Close speaker note.
        """
        if self.builder.app.config.revealjs_notes_from_comments:
            self.body.append("</aside>\n")

    def visit_literal_block(self, node: Element):
        """Begin ``literal_block`` .

        Override base method, and open simply ``pre`` and ``code`` tags.
        """
        # TODO: Add test
        if "language" not in node:
            return super().visit_literal_block(node)
        lang = node["language"]
        # add section id as data-id if it is exists
        if "data-id" in node:
            self.body.append(f'<pre data-id="{node["data-id"]}">')
        elif isinstance(node.parent, section) and len(node.parent["ids"]):
            self.body.append(f'<pre data-id="{node.parent["ids"][0]}">')
        else:
            self.body.append("<pre>")
        self.body.append(f'<code data-trim data-noescape class="{lang}"')
        # use the emphasize-lines directive to create line for line animations
        if "data-line-numbers" in node:
            self.body.append(f' data-line-numbers="{node["data-line-numbers"]}"')
        else:
            # show line numbers
            if node["linenos"]:
                self.body.append(" data-line-numbers")
        if "data-ln-start-from" in node:
            self.body.append(f' data-ln-start-from="{node["data-ln-start-from"]}"')
            if "data-line-numbers" not in node:
                self.body.append(" data-line-numbers")
        self.body.append(">")

    def depart_literal_block(self, node: literal_block):
        """End ``literal_block``.

        Override base method, and close begun tags.
        """
        self.body.append("</code></pre>\n")


def not_write(self, node):
    """visit/depart function for declare "no write"."""
    pass


def skip_node(self, node):
    """Skip child nodes if it is exists.

    This is used to explicit that it does not have sub tontents in nodes.
    """
    raise SkipNode()


def visit_revealjs_break(self, node: revealjs_break):
    """Close current section."""
    self.body.append("</section>\n")
    raise SkipChildren


def depart_revealjs_break(self, node: revealjs_break):
    """Open as next section.

    If node does not have attribute 'notitle',
    render title from current original section.
    """
    attrs = build_attributes_str(node, self.builder)
    self.body.append(f"<section {attrs}>\n")
    if "notitle" not in node.attributes:
        idx = node.parent.first_child_matching_class(title)
        if idx is None:
            return
        # NOTE: It has possibility to work side effect because re-walk for used nodes.
        node.parent.children[idx].walkabout(self)
        self.body.append("\n")
