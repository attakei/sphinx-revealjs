import unittest
from pathlib import Path

from sphinx_testing import with_app

PROJECT_ROOT = Path(__file__).parents[1]
SPHINX_TESTAPP_CONF = {
    'buildername': 'revealjs',
    'srcdir': str(PROJECT_ROOT / 'tests' / 'testdocs' / 'default'),
    'copy_srcdir_to_tmpdir': True,
}


class DemoMakeTesting(unittest.TestCase):
    @with_app(**SPHINX_TESTAPP_CONF)
    def test_build_ok(self, app, status, warning):
        app.build()
