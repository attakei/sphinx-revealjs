"""Integrationaly tests by demo."""
import unittest

from sphinx_testing import TestApp, with_app

from testutils import PROJECT_ROOT, soup_html

APP_CONF = {
    "buildername": "revealjs",
    "srcdir": str(PROJECT_ROOT / "demo"),
    "copy_srcdir_to_tmpdir": True,
}


class DemoMakeTesting(unittest.TestCase):  # noqa
    @with_app(**APP_CONF)
    def test_refs_all_exists(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        google_fonts = [
            d
            for d in soup.find_all("link", rel="stylesheet")
            if d["href"].startswith("https://fonts.googleapis.com")
        ]
        self.assertEqual(len(google_fonts), 0)
