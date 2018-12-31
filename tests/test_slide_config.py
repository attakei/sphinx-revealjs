import unittest
from pathlib import Path

from sphinx_testing import with_app

PROJECT_ROOT = Path(__file__).parents[1]
SPHINX_TESTAPP_CONF = {
    'buildername': 'revealjs',
    'srcdir': str(PROJECT_ROOT / 'tests' / 'testdocs' / 'default'),
    'copy_srcdir_to_tmpdir': True,
}
SPHINX_TESTAPP_INVALIDCONF = {
    'buildername': 'revealjs',
    'srcdir': str(PROJECT_ROOT / 'tests' / 'testdocs' / 'invalid-conf'),
    'copy_srcdir_to_tmpdir': True,
}
SPHINX_TESTAPP_VALIDCONF = {
    'buildername': 'revealjs',
    'srcdir': str(PROJECT_ROOT / 'tests' / 'testdocs' / 'valid-conf'),
    'copy_srcdir_to_tmpdir': True,
}


class SlideConfigTesting(unittest.TestCase):
    @with_app(**SPHINX_TESTAPP_CONF)
    def test_valid_conf_in_rst(self, app, status, warning):
        app.build()
        html = (app.outdir / 'config_override.html').read_text()
        assert '<h1>Test for override config</h1>' in html
        assert 'Object.assign(revealConfig, {"transition": "none"});' in html

    @with_app(**SPHINX_TESTAPP_VALIDCONF)
    def test_valid_conf_in_confpy(self, app, status, warning):
        app.build()
        html = (app.outdir / 'index.html').read_text()
        print(html)
        assert 'Object.assign(revealConfig, {"transition":"none"});' in html

    @with_app(**SPHINX_TESTAPP_CONF)
    def test_invalid_config_in_rst(self, app, status, warning):
        app.build()
        html = (app.outdir / 'config_invalid.html').read_text()
        assert '<h1>Test for invalid config</h1>' in html
        assert 'Object.assign(revealConfig, {transition:"});' not in html

    @with_app(**SPHINX_TESTAPP_INVALIDCONF)
    def test_invalid_conf_in_confpy(self, app, status, warning):
        app.build()
        html = (app.outdir / 'index.html').read_text()
        assert 'Object.assign(revealConfig, {transition:"});' not in html
