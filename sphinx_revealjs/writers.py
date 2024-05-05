"""Custom write module."""

from docutils.nodes import (  # type: ignore
    Element,
    SkipNode,
    comment,
    literal_block,
    section,
)
from sphinx.util.docutils import nodes
from sphinx.writers.html5 import HTML5Translator

from . import _patches
from .nodes import revealjs_break, revealjs_slide


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

    visit_title = _patches.visit_title

    def __init__(self, builder, *args, **kwds):  # noqa: D107
        super().__init__(builder, *args, **kwds)
        self.builder.add_permalinks = False
        self._nest_step = 0

    def visit_section(self, node: section):
        """Begin ``section`` node.

        * In first access, find and bind <revealjs-slide> node
        * If section has 'revealjs' attribute,
          use it (binded from <revealjs-section>, <revealjs-break> and <revealjs-vertical>).
        """  # noqa: E501
        if self.section_level == 0:
            slide_ = list(node.parent.findall(revealjs_slide))
            self.builder.revealjs_slide = slide_[0] if slide_ else None
        self.section_level += 1

        attrs = node.attributes.get("revealjs", "")
        if node.attributes.get("ids") and self.config.revealjs_use_section_ids:
            attrs += ' id="{}"'.format(node.attributes["ids"][-1])

        self.body.append(f"<section {attrs}>\n")

    def section_title_tags(self, node: nodes.title):
        """Create title tag pair for headings.

        * This is forked from :meth:`docutils.writers._html_base.HTMLTranslator.section_title_tags`.
        * When this class is used,
          doctree is transformed by :func:`sphinx_revealjs.transforms.bind_title_level`
          and title of section has 'heading'.
        * There is only logic of ``h_level`` about difference of original.
        """  # noqa: E501
        atts = {}
        h_level = node.attributes.get("heading", self.section_level + 2)
        # Only 6 heading levels have dedicated HTML tags.
        tagname = "h%i" % min(h_level, 6)
        if h_level > 6:
            atts["aria-level"] = h_level
        start_tag = self.starttag(node, tagname, "", **atts)
        if node.hasattr("refid"):
            atts = {}
            atts["class"] = "toc-backref"
            atts["role"] = "doc-backlink"  # HTML5 only
            atts["href"] = "#" + node["refid"]
            start_tag += self.starttag(nodes.reference(), "a", "", **atts)
            close_tag = "</a></%s>\n" % tagname
        else:
            close_tag = "</%s>\n" % tagname
        return start_tag, close_tag

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
        self.body.append(f"<h{self.section_level}>")
        self.body.append(title.children[0])
        self.body.append(f"</h{self.section_level}>")
        self.body.append("\n")
