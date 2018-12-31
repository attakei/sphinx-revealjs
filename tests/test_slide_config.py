import unittest

from sphinx_testing import with_app

from testutils import gen_testdoc_conf


class SlideConfigTesting(unittest.TestCase):
    @with_app(**gen_testdoc_conf())
    def test_valid_conf_in_rst(self, app, status, warning):
        app.build()
        html = (app.outdir / 'config_override.html').read_text()
        assert '<h1>Test for override config</h1>' in html
        assert 'Object.assign(revealConfig, {"transition": "none"});' in html

    @with_app(**gen_testdoc_conf('valid-conf'))
    def test_valid_conf_in_confpy(self, app, status, warning):
        app.build()
        html = (app.outdir / 'index.html').read_text()
        print(html)
        assert 'Object.assign(revealConfig, {"transition":"none"});' in html

    @with_app(**gen_testdoc_conf())
    def test_invalid_config_in_rst(self, app, status, warning):
        app.build()
        html = (app.outdir / 'config_invalid.html').read_text()
        assert '<h1>Test for invalid config</h1>' in html
        assert 'Object.assign(revealConfig, {transition:"});' not in html

    @with_app(**gen_testdoc_conf('invalid-conf'))
    def test_invalid_conf_in_confpy(self, app, status, warning):
        app.build()
        html = (app.outdir / 'index.html').read_text()
        assert 'Object.assign(revealConfig, {transition:"});' not in html
