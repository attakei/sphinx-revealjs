"""Internal extension for 'Fragments' of Reveal.js."""
from sphinx.application import Sphinx
from sphinx.directives import SphinxDirective
from sphinx.util.docutils import nodes

from .. import __version__
from ..writers import not_write


class revealjs_fragments(nodes.Structural, nodes.Element):  # noqa: D101
    pass


class RevealjsFragments(SphinxDirective):  # noqa: D101
    has_content = True

    def run(self):  # noqa: D102
        node = revealjs_fragments()
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, node)
        # TODO: Parameter ?
        for child in node.children:
            if not isinstance(child, nodes.Sequential):
                child["classes"].append("fragment")
                continue
            for c in child:
                c["classes"].append("fragment")
        return [
            node,
        ]


def setup(app: Sphinx):  # noqa: D103
    app.add_node(
        revealjs_fragments,
        html=(not_write, not_write),
        latex=(not_write, not_write),
        text=(not_write, not_write),
        man=(not_write, not_write),
        texinfo=(not_write, not_write),
        revealjs=(not_write, not_write),
        dirrevealjs=(not_write, not_write),
    )
    app.add_directive("revealjs-fragments", RevealjsFragments)
    return {
        "version": __version__,
        "env_version": 2,
        "parallel_read_safe": True,
    }
