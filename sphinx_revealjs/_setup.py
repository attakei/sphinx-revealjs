"""
"""
from sphinx.application import Sphinx

from sphinx_revealjs.builders import RevealjsHTMLBuilder
from sphinx_revealjs.directives import RevealjsSection, RevealjsSlide
from sphinx_revealjs.nodes import revealjs_section, revealjs_slide
from sphinx_revealjs.themes import get_theme_path
from sphinx_revealjs.writers import not_write

from ._version import __version__


def setup(app: Sphinx):
    app.add_builder(RevealjsHTMLBuilder)
    app.add_node(
        revealjs_section,
        html=(not_write, not_write),
        revealjs=(not_write, not_write))
    app.add_node(
        revealjs_slide,
        html=(not_write, not_write),
        revealjs=(not_write, not_write))
    app.add_directive('revealjs_section', RevealjsSection)
    app.add_directive('revealjs_slide', RevealjsSlide)
    app.add_config_value('revealjs_theme', 'sphinx_revealjs', True)
    app.add_config_value('revealjs_theme_options', {}, True)
    app.add_html_theme(
        'sphinx_revealjs', str(get_theme_path('sphinx_revealjs')))
    return {
        'version': __version__,
        'env_version': 1,
        'parallel_read_safe': False,
    }
