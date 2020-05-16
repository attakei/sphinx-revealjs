"""Integrationaly tests by demo."""
import unittest

from sphinx_testing import TestApp

from testutils import PROJECT_ROOT, soup_html


class DemoMakeTesting(unittest.TestCase):  # noqa
    @classmethod
    def setUpClass(cls):  # noqa
        cls.app = TestApp(
            srcdir=str(PROJECT_ROOT / "demo"),
            buildername="revealjs",
            copy_srcdir_to_tmpdir=True,
        )
        cls.soup = soup_html(cls.app, "index.html")

    def test_no_refs_sphinx_based(self):  # noqa
        sphinx_basic_css = [
            d
            for d in self.soup.find_all("link", rel="stylesheet")
            if d["href"] == "_static/basic.css"
        ]
        self.assertEqual(len(sphinx_basic_css), 0)
        self.assertEqual(len([
            d
            for d in self.soup.find_all("link", rel="stylesheet")
            if d["href"] == "_static/"
        ]), 0)

    def test_refs_all_exists(self):  # noqa
        google_fonts = [
            d
            for d in self.soup.find_all("link", rel="stylesheet")
            if d["href"].startswith("https://fonts.googleapis.com")
        ]
        self.assertEqual(len(google_fonts), 0)

    def test_script_conf(self):  # noqa
        script = self.soup.find_all("script")[-1]
        self.assertIn("Reveal.initialize(revealjsConfig);", script.text)

    def test_script_sources(self):  # noqa
        scripts = [s for s in self.soup.find_all("script") if "src" in s.attrs]
        self.assertEqual(scripts[-1]["src"], "_static/revealjs/js/reveal.js")

    def test_stylesheet(self):  # noqa
        links = [l["href"] for l in self.soup.find_all("link", rel="stylesheet")]
        self.assertIn("_static/revealjs/css/theme/black.css", links)

    def test_title(self):  # noqa
        self.assertEqual("sphinx-revealjs", self.soup.title.text)
