"""Custom directives for Reveal.js."""
import json

from docutils.parsers.rst import Directive, directives

from sphinx_revealjs.nodes import (
    FlagAttribute, revealjs_break, revealjs_fragments, revealjs_section,
    revealjs_slide
)


def raw_json(argument):
    """Type of direction attribute."""
    if argument is None:
        return directives.unchanged(argument)
    try:
        json.loads(argument)
    except json.decoder.JSONDecodeError:
        return ''
    return argument


REVEALJS_SECTION_ATTRIBUTES = {
    # Color backgrounds
    'data-background-color': directives.unchanged,
    # Image backgrounds
    'data-background-image': directives.unchanged,
    'data-background-position': directives.unchanged,
    'data-background-repeat': directives.unchanged,
    # Video backgrounds
    'data-background-video': directives.unchanged,
    'data-background-video-loop': directives.unchanged,
    'data-background-video-muted': directives.unchanged,
    # Image/Video backgrounds
    'data-background-size': directives.unchanged,
    'data-background-opacity': directives.unchanged,
    # Iframe backgrounds
    'data-background-iframe': directives.unchanged,
    'data-background-interactive': lambda x: FlagAttribute(),
    # Transition
    'data-transition': directives.unchanged,
    'data-background-transition': directives.unchanged,
}


class RevealjsSection(Directive):  # noqa: D101
    option_spec = REVEALJS_SECTION_ATTRIBUTES

    def run(self):  # noqa: D102
        node = revealjs_section()
        node.attributes = self.options
        return [node, ]


class RevealjsBreak(Directive):  # noqa: D101
    option_spec = dict(
        # if it is set, next section does not display title
        notitle=lambda x: FlagAttribute(),
        **REVEALJS_SECTION_ATTRIBUTES
    )

    def run(self):  # noqa: D102
        node = revealjs_break()
        node.attributes = self.options
        return [node, ]


class RevealjsSlide(Directive):  # noqa: D101
    has_content = True

    option_spec = {
        'theme': directives.unchanged,
        'google_font': directives.unchanged,
        'config': raw_json,
    }

    def run(self):  # noqa: D102
        node = revealjs_slide()
        node.attributes = self.options
        if self.content:
            node.content = "".join(self.content)
        else:
            node.content = """
            {
                controls: true,
                progress: true,
                history: true,
                center: true,
                transition: "slide", // none/fade/slide/convex/concave/zoom
                // More info https://github.com/hakimel/reveal.js#dependencies
                dependencies: [
                    { src: "{{ pathto('_static/revealjs/plugin/notes/notes.js', 1) }}", async: true },
                    { src: "{{ pathto('_static/revealjs/plugin/highlight/highlight.js', 1) }}", async: true, callback: function() { hljs.initHighlightingOnLoad(); } }
                ]
            }
            """
        return [node, ]


class RevealjsFragments(Directive):  # noqa: D101
    has_content = True

    def run(self):  # noqa: D102
        node = revealjs_fragments()
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, node)
        # TODO: Parameter ?
        for child in node.children[0].children:
            child['classes'].append('fragment')
        return [node, ]
