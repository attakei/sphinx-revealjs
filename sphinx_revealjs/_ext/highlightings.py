"""Internal extension for highlighting of Reveal.js."""
from docutils.parsers.rst import directives  # type: ignore
from sphinx.application import Sphinx
from sphinx.directives.code import CodeBlock, LiteralInclude

from .. import __version__


class RevealjsCodeBlock(CodeBlock):  # noqa: D101
    option_spec = {
        **CodeBlock.option_spec,
        "data-id": directives.unchanged,
        "data-line-numbers": directives.unchanged,
        "data-ln-start-from": directives.unchanged,
    }

    def run(self):  # noqa: D102
        nodes = super().run()
        if self.options.get("data-line-numbers"):
            nodes[0]["data-line-numbers"] = self.options.get("data-line-numbers")
        if self.options.get("data-id"):
            nodes[0]["data-id"] = self.options.get("data-id")
        if self.options.get("data-ln-start-from"):
            nodes[0]["data-ln-start-from"] = self.options.get("data-ln-start-from")
        return nodes


class RevealjsLiteralInclude(LiteralInclude):
    """Extends from ``literalinclude`` directive.

    This has ``data-line-numbers`` for step-by-step code highlighting.
    See `it <https://revealjs.com/code/>`_ for more information.
    """

    option_spec = {
        **LiteralInclude.option_spec,
        "data-id": directives.unchanged,
        "data-line-numbers": directives.unchanged,
        "data-ln-start-from": directives.unchanged,
    }

    def run(self):  # noqa: D102
        nodes = super().run()
        if self.options.get("data-line-numbers"):
            nodes[0]["data-line-numbers"] = self.options.get("data-line-numbers")
        if self.options.get("data-id"):
            nodes[0]["data-id"] = self.options.get("data-id")
        if self.options.get("data-ln-start-from"):
            nodes[0]["data-ln-start-from"] = self.options.get("data-ln-start-from")
        return nodes


def setup(app: Sphinx):  # noqa: D103
    app.add_directive("revealjs-code-block", RevealjsCodeBlock)
    app.add_directive("revealjs-literalinclude", RevealjsLiteralInclude)
    return {
        "version": __version__,
        "env_version": 2,
        "parallel_read_safe": True,
    }
