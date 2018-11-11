"""Custom directives for Reveal.js
"""
from docutils.parsers.rst import Directive

from .nodes import revealjs_section


class RevealjsSection(Directive):
    def run(self):
        return [revealjs_section(), ]
