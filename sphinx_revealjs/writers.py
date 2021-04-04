"""Custom write module."""
from docutils.nodes import Element, comment, literal_block, section
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
        self._proc_first_on_section = False

    def visit_section(self, node: section):
        """Begin ``section`` node.

        - Find first ``revealjs_section`` node and build attributes string.
        - When enter next section, nest level.
        """
        self.section_level += 1
        meta = find_child_section(node, "revealjs_section")
        if meta is not None:
            attrs = meta.attributes_str()
        else:
            attrs = ""
        if node.attributes.get("ids") and self.config.revealjs_use_section_ids:
            attrs += ' id="{}"'.format(node.attributes["ids"][-1])
        if self.section_level == 1:
            self.builder.revealjs_slide = find_child_section(node, "revealjs_slide")
            self._proc_first_on_section = True
            self.body.append(f"<section {attrs}>\n")
            return
        if self._proc_first_on_section:
            self._proc_first_on_section = False
            self.body.append("</section>\n")

        if has_child_sections(node, "section"):
            self._proc_first_on_section = True
            self.body.append("<section>\n")
        self.body.append(f"<section {attrs}>\n")

    def depart_section(self, node: section):
        """End ``section``.

        Dedent section level
        """
        self.section_level -= 1
        if self.section_level >= 1:
            self.body.append("</section>\n")

    def visit_comment(self, node: comment):
        """Begin ``comment`` node.

        comment node render as speaker note.
        """
        self.body.append('<aside class="notes">\n')

    def depart_comment(self, node: comment):
        """End ``comment`` node.

        Close speaker note.
        """
        self.body.append("</aside>\n")

    def visit_literal_block(self, node: literal_block):
        """Begin ``literal_block`` .

        Override base method, and open simply ``pre`` and ``code`` tags.
        """
        lang = node["language"]
        self.body.append(f'<pre><code data-trim data-noescape class="{lang}">\n')

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
        self.body.append(f"<h{self.section_level}>")
        self.body.append(title.children[0])
        self.body.append(f"</h{self.section_level}>")
        self.body.append("\n")
