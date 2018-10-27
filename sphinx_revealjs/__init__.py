"""
"""
from sphinx.application import Sphinx

from .builders import RevealjsHTMLBuilder


__version__ = '0.1.0'


def setup(app: Sphinx):
    app.add_config_value('revealjs_version', '3.7.0', 'html')
    app.add_builder(RevealjsHTMLBuilder)
    return {
        'version': __version__,
        'env_version': 1,
        'parallel_read_safe': False,
    }
