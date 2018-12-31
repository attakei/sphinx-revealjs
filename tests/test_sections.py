import unittest

from sphinx_testing import with_app

from testutils import gen_testdoc_conf


class DemoMakeTesting(unittest.TestCase):
    @with_app(**gen_testdoc_conf())
    def test_build_ok(self, app, status, warning):
        app.build()
