"""Custom write module."""

from docutils.nodes import (  # type: ignore
    Element,
    SkipNode,
    comment,
    literal_block,
    section,
)
from sphinx.writers.html5 import HTML5Translator

from .nodes import revealjs_break


def has_child_sections(node: Element, name: str):
    """Search has specified section in children."""
    nodes = set([n.tagname for n in node.children])
    return name in nodes


def find_child_section(node: Element, name: str):
    """Search and return first specified section in children."""
    for n in node.children:
        if n.tagname == name:
            return n
    return None


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
        meta = find_child_section(node, "revealjs_section")
        if meta is not None:
            attrs = meta.attributes_str()
        else:
            attrs = ""
        if node.attributes.get("ids") and self.config.revealjs_use_section_ids:
            attrs += ' id="{}"'.format(node.attributes["ids"][-1])

        if self._nest_step > 0:
            self.body.append("</section>\n" * self._nest_step)
            self._nest_step = 0
        if self.section_level == 1:
            self._nest_step = 2
            self.builder.revealjs_slide = find_child_section(node, "revealjs_slide")
        elif has_child_sections(node, "section"):
            self._nest_step = 1

        if self._nest_step > 0:
            v_meta = find_child_section(node, "revealjs_vertical")
            v_attrs = v_meta.attributes_str() if v_meta is not None else ""
            self.body.append(f"<section {v_attrs}>\n")
        self.body.append(f"<section {attrs}>\n")

    def depart_section(self, node: section):
        """End ``section``.

        Dedent section level
        """
        self.section_level -= 1
        if self.section_level >= 3:
            return
        self.body.append("</section>\n")

    def visit_comment(self, node: comment):
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

    def visit_literal_block(self, node: literal_block):
        """Begin ``literal_block`` .

        Override base method, and open simply ``pre`` and ``code`` tags.
        """
        lang = node["language"]
        # add section id as data-id if it is exists
        if "data-id" in node:
            self.body.append(f"<pre data-id=\"{node['data-id']}\">")
        elif isinstance(node.parent, section) and len(node.parent["ids"]):
            self.body.append(f"<pre data-id=\"{node.parent['ids'][0]}\">")
        else:
            self.body.append("<pre>")
        self.body.append(f'<code data-trim data-noescape class="{lang}"')
        # use the emphasize-lines directive to create line for line animations
        if "data-line-numbers" in node:
            self.body.append(f" data-line-numbers=\"{node['data-line-numbers']}\"")
        else:
            # show line numbers
            if node["linenos"]:
                self.body.append(" data-line-numbers")
        if "data-ln-start-from" in node:
            self.body.append(f" data-ln-start-from=\"{node['data-ln-start-from']}\"")
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


def visit_revealjs_break(self, node: revealjs_break):
    """Close current section."""
    self.body.append("</section>\n")


def depart_revealjs_break(self, node: revealjs_break):
    """Open as next section.

    If node does not have attribute 'notitle',
    render title from current original section.
    """
    attrs = node.attributes_str()
    self.body.append(f"<section {attrs}>\n")
    if "notitle" not in node.attributes:
        title = find_child_section(node.parent, "title")
        # NOTE: It has possibility to work side effect because re-walk for used nodes.
        title.walkabout(self)
        self.body.append("\n")
