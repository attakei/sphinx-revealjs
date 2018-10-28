"""
"""
from pathlib import Path

from sphinx.application import Sphinx

from .builders import RevealjsHTMLBuilder

__version__ = '0.1.0'


def get_theme_path(name: str) -> Path:
    here = Path(__file__).parent
    return here / 'themes' / name


def setup(app: Sphinx):
    app.add_config_value('revealjs_version', '3.7.0', 'html')
    app.add_builder(RevealjsHTMLBuilder)
    app.add_html_theme(
        'revealjs_debugging', str(get_theme_path('debugging')))
    return {
        'version': __version__,
        'env_version': 1,
        'parallel_read_safe': False,
    }
