"""Custom directives for Reveal.js
"""
from docutils.parsers.rst import Directive, directives

from .nodes import revealjs_section


class RevealjsSection(Directive):
    option_spec = {
        'background_color': directives.unchanged,
        'background_image': directives.unchanged,
        'background_video': directives.unchanged,
    }

    def run(self):
        node = revealjs_section()
        meta = {}
        if 'background_color' in self.options:
            meta.update({
                'data-background-color': self.options['background_color'],
            })
        if 'background_image' in self.options:
            meta.update({
                'data-background': self.options['background_image'],
                'data-background-size': 'contain',
            })
        if 'background_video' in self.options:
            meta.update({
                'data-background-video': self.options['background_video'],
            })
        node['meta'] = meta
        return [node, ]
