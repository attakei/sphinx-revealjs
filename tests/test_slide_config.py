import unittest
from pathlib import Path

from sphinx_testing import with_app

PROJECT_ROOT = Path(__file__).parents[1]
SPHINX_TESTAPP_CONF = {
    'buildername': 'revealjs',
    'srcdir': str(PROJECT_ROOT / 'tests' / 'testdocs'),
    'copy_srcdir_to_tmpdir': True,
}


class SlideConfigTesting(unittest.TestCase):
    @with_app(**SPHINX_TESTAPP_CONF)
    def test_conf_in_directive(self, app, status, warning):
        app.build()
        html = (app.outdir / 'override_config.html').read_text()
        assert '<h1>Test for override config</h1>' in html
        assert 'Object.assign(revealConfig, {transition: "none"});' in html

    @with_app(**SPHINX_TESTAPP_CONF)
    def test_theme_invalid_config(self, app, status, warning):
        app.build()
        html = (app.outdir / 'config_invalid.html').read_text()
        assert '<h1>Test for invalid config</h1>' in html
        assert 'Object.assign(revealConfig, {transition:"});' not in html
