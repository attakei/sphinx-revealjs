"""Patch functions and method for backportings.

This is collection of these:

* Copy implements
* Patched implements

These are to keep compatibility.
"""

from sphinx.util.docutils import nodes


def visit_title(self, node):
    """Handle title node (visited).

    :ref: https://github.com/docutils/docutils/blob/4fc504bafd6baf255bd5516273b5aa0f10df8a47/docutils/docutils/writers/_html_base.py

    .. todo:: Remove it when sphinx-revealjs drops Sphinx 4.x
    """  # noqa: E501
    close_tag = "</p>\n"
    if isinstance(node.parent, nodes.topic):
        # TODO: use role="heading" or <h1>? (HTML5 only)
        self.body.append(self.starttag(node, "p", "", CLASS="topic-title"))
        if self.settings.toc_backlinks and "contents" in node.parent["classes"]:
            self.body.append('<a class="reference internal" href="#top">')
            close_tag = "</a></p>\n"
    elif isinstance(node.parent, nodes.sidebar):
        # TODO: use role="heading" or <h1>? (HTML5 only)
        self.body.append(self.starttag(node, "p", "", CLASS="sidebar-title"))
    elif isinstance(node.parent, nodes.Admonition):
        self.body.append(self.starttag(node, "p", "", CLASS="admonition-title"))
    elif isinstance(node.parent, nodes.table):
        self.body.append(self.starttag(node, "caption", ""))
        close_tag = "</caption>\n"
    elif isinstance(node.parent, nodes.document):
        self.body.append(self.starttag(node, "h1", "", CLASS="title"))
        close_tag = "</h1>\n"
        self.in_document_title = len(self.body)
    else:
        assert isinstance(node.parent, nodes.section)
        # Get correct heading and evt. backlink tags
        start_tag, close_tag = self.section_title_tags(node)
        self.body.append(start_tag)
    self.context.append(close_tag)
