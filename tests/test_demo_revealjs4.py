"""Integrationaly tests by demo-revealjs4."""
import unittest

from sphinx_testing import TestApp

from testutils import PROJECT_ROOT, soup_html


class DemoMakeTesting(unittest.TestCase):  # noqa
    @classmethod
    def setUpClass(cls):  # noqa
        cls.app = TestApp(
            srcdir=str(PROJECT_ROOT / "demo-revealjs4"),
            buildername="revealjs",
            copy_srcdir_to_tmpdir=True,
        )
        cls.soup = soup_html(cls.app, "index.html")

    def test_has_revealcss(self):  # noqa
        reveal_css = [
            d
            for d in self.soup.find_all("link", rel="stylesheet")
            if d["href"].endswith("revealjs4/dist/reveal.css")
        ]
        self.assertEqual(len(reveal_css), 1)

    def test_refs_all_exists(self):  # noqa
        google_fonts = [
            d
            for d in self.soup.find_all("link", rel="stylesheet")
            if d["href"].startswith("https://fonts.googleapis.com")
        ]
        self.assertEqual(len(google_fonts), 1)

    def test_script_conf(self):  # noqa
        script = self.soup.find_all("script")[-1]
        self.assertIn("Reveal.initialize(revealjsConfig);", script.text)

    def test_script_sources(self):  # noqa
        scripts = [s for s in self.soup.find_all("script") if "src" in s.attrs]
        self.assertEqual(scripts[-1]["src"], "_static/revealjs4/dist/reveal.js")

    def test_stylesheet(self):  # noqa
        links = [l["href"] for l in self.soup.find_all("link", rel="stylesheet")]
        self.assertIn("_static/revealjs4/dist/theme/black.css", links)

    def test_title(self):  # noqa
        self.assertEqual("sphinx-revealjs", self.soup.title.text)

    def test_has_highlightjs_theme(self):  # noqa
        links = [
            d
            for d in self.soup.find_all("link", rel="stylesheet")
            if d["href"].endswith("revealjs4/plugin/highlight/zenburn.css")
        ]
        self.assertEqual(len(links), 1)
