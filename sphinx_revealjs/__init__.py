"""
"""
from pathlib import Path

from sphinx.application import Sphinx

from .builders import RevealjsHTMLBuilder
from .directives import RevealjsSection
from .nodes import revealjs_section
from .writers import not_write

__version__ = '0.2.0'


def get_theme_path(name: str) -> Path:
    here = Path(__file__).parent
    return here / 'themes' / name


def setup(app: Sphinx):
    app.add_config_value('revealjs_version', '3.7.0', 'html')
    app.add_builder(RevealjsHTMLBuilder)
    app.add_node(
        revealjs_section,
        html=(not_write, not_write),
        revealjs=(not_write, not_write))
    app.add_directive('revealjs_section', RevealjsSection)
    app.add_html_theme(
        'revealjs', str(get_theme_path('revealjs')))
    app.add_html_theme(
        'revealjs_debugging', str(get_theme_path('debugging')))
    return {
        'version': __version__,
        'env_version': 1,
        'parallel_read_safe': False,
    }
