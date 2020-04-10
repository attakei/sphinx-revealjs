import unittest
from pathlib import Path

from sphinx_testing import with_app, TestApp
from testutils import RevealjsParser


PROJECT_ROOT = Path(__file__).parents[1]


class DemoMakeTesting(unittest.TestCase):
    @with_app(
        buildername="revealjs",
        srcdir=str(PROJECT_ROOT / "demo"),
        copy_srcdir_to_tmpdir=True,
    )
    def test_build_ok(self, app, status, warning):
        app.build()

    @with_app(
        buildername="revealjs",
        srcdir=str(PROJECT_ROOT / "demo"),
        copy_srcdir_to_tmpdir=True,
    )
    def test_refs_all_exists(self, app: TestApp, status, warning):
        app.build()
        html = (app.outdir / "index.html").read_text()
        parser = RevealjsParser()
        parser.feed(html)
        for src in parser.local_css_files:
            self.assertTrue((Path(app.outdir) / src).exists())
        for src in parser.local_js_files:
            self.assertTrue((Path(app.outdir) / src).exists())
        assert "_static/revealjs/css/reveal.css" in parser.local_css_files
        assert "_static/revealjs/lib/css/zenburn.css" in parser.local_css_files

    @with_app(
        buildername="html",
        srcdir=str(PROJECT_ROOT / "demo"),
        copy_srcdir_to_tmpdir=True,
    )
    def test_css_skipped_in_html_build(self, app: TestApp, status, warning):
        app.build()
        html = (app.outdir / "index.html").read_text()
        parser = RevealjsParser()
        parser.feed(html)
        assert "_static/revealjs/css/reveal.css" not in parser.local_css_files
        assert "_static/revealjs/lib/css/zenburn.css" not in parser.local_css_files
