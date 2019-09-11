import unittest
from html.parser import HTMLParser
from pathlib import Path

from sphinx_testing import with_app, TestApp

PROJECT_ROOT = Path(__file__).parents[1]


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
        class RevealjsParser(HTMLParser):
            def handle_starttag(self_, tag, attrs):
                attrs_dict = dict(attrs)
                # Judge that local resource is exists
                if tag == 'script' and 'src' in attrs_dict:
                    if not attrs_dict['src'].startswith('_static'):
                        return
                    script_src = Path(app.outdir) / attrs_dict['src']
                    assert script_src.exists()
                return

        app.build()
        html = (app.outdir / 'index.html').read_text()
        parser = RevealjsParser()
        parser.feed(html)