"""Custom directives for Reveal.js
"""
from docutils.parsers.rst import Directive, directives

from sphinx_revealjs.nodes import revealjs_section, FlagAttribute


class RevealjsSection(Directive):
    option_spec = {
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

    def run(self):
        node = revealjs_section()
        node.attributes = self.options
        return [node, ]
