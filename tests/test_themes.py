import unittest
from pathlib import Path

from sphinx_testing import with_app

PROJECT_ROOT = Path(__file__).parents[1]
SPHINX_TESTAPP_CONF = {
    'buildername': 'revealjs',
    'srcdir': str(PROJECT_ROOT / 'tests' / 'testdocs'),
    'copy_srcdir_to_tmpdir': True,
}


class DemoMakeTesting(unittest.TestCase):
    @with_app(**SPHINX_TESTAPP_CONF)
    def test_theme_default(self, app, status, warning):
        app.build()
        html = (app.outdir / 'index.html').read_text()
        theme_url_path = f'_static/black.css'
        assert theme_url_path in html

    @with_app(**SPHINX_TESTAPP_CONF)
    def test_theme_by_directive(self, app, status, warning):
        app.build()
        html = (app.outdir / 'changed_theme.html').read_text()
        assert '<h1>Test for selecatable theme</h1>' in html
        theme_url_path = f'_static/solarized.css'
        assert theme_url_path in html
