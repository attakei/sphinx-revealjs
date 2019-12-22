"""Integrationaly test by demo
"""
import unittest
from html.parser import HTMLParser
from pathlib import Path
from typing import AnyStr, Tuple

from sphinx_testing import with_app, TestApp

from testutils import RevealjsParser


PROJECT_ROOT = Path(__file__).parents[1] / 'demo'


class DemoMakeTesting(unittest.TestCase):
    @with_app(
        buildername='revealjs',
        srcdir=str(PROJECT_ROOT),
        copy_srcdir_to_tmpdir=True)
    def test_refs_all_exists(self, app: TestApp, status, warning):
        html: AnyStr = (app.outdir / 'index.html').read_text()
        parser = RevealjsParser()
        parser.feed(html)
        google_fonts = [f for f in parser.remote_css_files if f.startswith('https://fonts.googleapis.com')]
        self.assertEqual(len(google_fonts), 0)