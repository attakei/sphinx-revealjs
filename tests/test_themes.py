import unittest

from sphinx_testing import with_app

from testutils import gen_testdoc_conf


class DemoMakeTesting(unittest.TestCase):
    @with_app(**gen_testdoc_conf())
    def test_theme_default(self, app, status, warning):
        app.build()
        html = (app.outdir / 'index.html').read_text()
        theme_url_path = f'_static/black.css'
        assert theme_url_path in html

    @with_app(**gen_testdoc_conf())
    def test_theme_by_directive(self, app, status, warning):
        app.build()
        html = (app.outdir / 'theme_changed.html').read_text()
        assert '<h1>Test for selecatable theme</h1>' in html
        theme_url_path = f'_static/solarized.css'
        assert theme_url_path in html
