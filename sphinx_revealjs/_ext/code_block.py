"""Internal extension for highlighting of Reveal.js."""
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.directives.code import CodeBlock

from .. import __version__


class RevealjsCodeBlock(CodeBlock):  # noqa: D101
    option_spec = {
        **CodeBlock.option_spec,
        "data-id": directives.unchanged,
        "data-line-numbers": directives.unchanged,
    }

    def run(self):  # noqa: D102
        nodes = super().run()
        if self.options.get("data-line-numbers"):
            nodes[0]["data-line-numbers"] = self.options.get("data-line-numbers")
        if self.options.get("data-id"):
            nodes[0]["data-id"] = self.options.get("data-id")
        return nodes


def setup(app: Sphinx):  # noqa: D103
    app.add_directive("revealjs-code-block", RevealjsCodeBlock)
    return {
        "version": __version__,
        "env_version": 2,
        "parallel_read_safe": True,
    }
