"""Test cases for ``revealjs_fragments`` directive."""
import unittest

from sphinx_testing import TestApp, with_app

from testutils import gen_app_conf, soup_html


class BuildHtmlTests(unittest.TestCase):  # noqa
    @with_app(**gen_app_conf())
    def test_fragments_generate(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "has_fragments.html")
        self.assertEqual(len(soup.find_all(attrs={"fragment"})), 3)
