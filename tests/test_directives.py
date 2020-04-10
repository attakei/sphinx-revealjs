"""Testing with test docs

Use generated html from test documents
"""
import unittest

import bs4
from sphinx_testing import with_app

from testutils import gen_testdoc_conf


class RegularOutputTesting(unittest.TestCase):
    """Simple output content test"""

    @with_app(**gen_testdoc_conf())
    def test_generated_fragment(self, app, status, warning):
        app.build()
        html = (app.outdir / "has_fragments.html").read_text()
        assert "Test for fragments" in html
        soup = bs4.BeautifulSoup(html, "html.parser")
        self.assertEqual(len(soup.find_all(attrs={"fragment"})), 3)


class ConfigByContentTesting(unittest.TestCase):
    """Simple output content test"""

    @with_app(**gen_testdoc_conf())
    def test_generated_fragment(self, app, status, warning):
        app.build()
        html = (app.outdir / "config_by_content.html").read_text()
        soup = bs4.BeautifulSoup(html, "html.parser")
        script = soup.find_all("script")[-1]
        self.assertIn("dependencies: [],", script.text)
