"""Integrationaly test by demo
"""
import unittest
from html.parser import HTMLParser
from pathlib import Path
from typing import AnyStr, Tuple

from sphinx_testing import TestApp


PROJECT_ROOT = Path(__file__).parents[1] / 'demo'


class RevealjsParser(HTMLParser):
    def __init__(self, *, convert_charrefs=True):
        super().__init__(convert_charrefs=convert_charrefs)
        self.local_css_files = []
        self.remote_css_files = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        # Judge that local resource is exists
        if tag == 'link' and attrs_dict['href']:
            uri = attrs_dict['href']
            if uri.startswith('http://'):
                self.remote_css_files.append(uri)
            elif uri.startswith('https://'):
                self.remote_css_files.append(uri)
            else:
                self.local_css_files.append(attrs_dict['href'])
        return


class DemoMakeTesting(unittest.TestCase):
    testapp: TestApp
    html: AnyStr
    parser: RevealjsParser

    @classmethod
    def setUpClass(cls):
        cls.testapp = TestApp(srcdir=str(PROJECT_ROOT), buildername='revealjs', copy_srcdir_to_tmpdir=True)
        cls.html: AnyStr = (cls.testapp.outdir / 'index.html').read_text()
        cls.parser: RevealjsParser = RevealjsParser()
        cls.parser.feed(cls.html)

    def test_refs_all_exists(self):
        google_fonts = [f for f in self.parser.remote_css_files if f.startswith('https://fonts.googleapis.com')]
        self.assertEqual(len(google_fonts), 0)