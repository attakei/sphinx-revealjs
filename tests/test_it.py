import unittest
from html.parser import HTMLParser
from pathlib import Path

from sphinx_testing import with_app, TestApp

PROJECT_ROOT = Path(__file__).parents[1]


class RevealjsParser(HTMLParser):
    def __init__(self, *, convert_charrefs=True):
        super().__init__(convert_charrefs=convert_charrefs)
        self.css_static_files = []
        self.js_static_files = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        # Judge that local resource is exists
        if tag == 'script' and 'src' in attrs_dict:
            if not attrs_dict['src'].startswith('_static'):
                return
            self.js_static_files.append(attrs_dict['src'])
            # script_src = Path(app.outdir) / attrs_dict['src']
            # assert script_src.exists()
        if tag == 'link' and  attrs_dict['rel'] == 'stylesheet':
            if not attrs_dict['href'].startswith('_static'):
                return
            self.css_static_files.append(attrs_dict['href'])
        return


class DemoMakeTesting(unittest.TestCase):
    @with_app(
        buildername='revealjs',
        srcdir=str(PROJECT_ROOT / 'demo'),
        copy_srcdir_to_tmpdir=True)
    def test_build_ok(self, app, status, warning):
        app.build()

    @with_app(
        buildername='revealjs',
        srcdir=str(PROJECT_ROOT / 'demo'),
        copy_srcdir_to_tmpdir=True)
    def test_refs_all_exists(self, app: TestApp, status, warning):
        app.build()
        html = (app.outdir / 'index.html').read_text()
        parser = RevealjsParser()
        parser.feed(html)
        for src in parser.css_static_files:
            self.assertTrue((Path(app.outdir) / src).exists())
        for src in parser.js_static_files:
            self.assertTrue((Path(app.outdir) / src).exists())
        assert '_static/revealjs/css/reveal.css' in parser.css_static_files
        assert '_static/revealjs/lib/css/zenburn.css' in parser.css_static_files

    @with_app(
        buildername='html',
        srcdir=str(PROJECT_ROOT / 'demo'),
        copy_srcdir_to_tmpdir=True)
    def test_css_skipped_in_html_build(self, app: TestApp, status, warning):
        app.build()
        html = (app.outdir / 'index.html').read_text()
        parser = RevealjsParser()
        parser.feed(html)
        assert '_static/revealjs/css/reveal.css' not in parser.css_static_files
        assert '_static/revealjs/lib/css/zenburn.css' not in parser.css_static_files