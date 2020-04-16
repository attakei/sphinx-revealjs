"""Custom docutils nodes for Reveal.js."""
from docutils import nodes


class FlagAttribute(object):
    """Flag options for docutils node."""

    pass


class SectionTagRenderer(object):
    """Mix-in class to build attributes combined string."""

    def attributes_str(self):
        """Build string of attributes for Reveal.js sections.

        Catch only keys starting 'data-'.
        Others are skipped.
        """
        pair = []
        for k, v in self.attributes.items():
            if not k.startswith("data-"):
                continue
            if isinstance(v, FlagAttribute):
                pair.append(k)
                continue
            pair.append(f'{k}="{v}"')
        return " ".join(pair)


class revealjs_section(
    SectionTagRenderer, nodes.Structural, nodes.Element
):  # noqa: D101,E501
    pass


class revealjs_break(
    SectionTagRenderer, nodes.Structural, nodes.Element
):  # noqa: D101,E501
    pass


class revealjs_slide(nodes.Structural, nodes.Element):  # noqa: D101
    pass


class revealjs_fragments(nodes.Structural, nodes.Element):  # noqa: D101
    pass
