import unittest
from pathlib import Path

from sphinx_testing import with_app

PROJECT_ROOT = Path(__file__).parents[1]


class DemoMakeTesting(unittest.TestCase):
    @with_app(
        buildername='revealjs',
        srcdir=str(PROJECT_ROOT / 'demo'),
        copy_srcdir_to_tmpdir=True)
    def test_build_ok(self, app, status, warning):
        app.build()
