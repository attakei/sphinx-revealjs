"""Testing with test docs

Use generated html from test documents
"""
import unittest

from sphinx_testing import with_app

from testutils import gen_testdoc_conf


class RegularOutputTesting(unittest.TestCase):
    """Simple output content test"""

    @with_app(**gen_testdoc_conf())
    def test_theme_default(self, app, status, warning):
        app.build()
        html = (app.outdir / "index.html").read_text()
        assert "sphinx-revealjs test doc" in html


class SlideConfigTesting(unittest.TestCase):
    """Test case for Revealjs config parameters"""

    @with_app(**gen_testdoc_conf())
    def test_valid_conf_in_rst(self, app, status, warning):
        app.build()
        html = (app.outdir / "config_override.html").read_text()
        assert "<h1>Test for override config</h1>" in html
        assert 'Object.assign(revealConfig, {"transition": "none"});' in html

    @with_app(**gen_testdoc_conf("valid-conf"))
    def test_valid_conf_in_confpy(self, app, status, warning):
        app.build()
        html = (app.outdir / "index.html").read_text()
        assert 'Object.assign(revealConfig, {"transition":"none"});' in html

    @with_app(**gen_testdoc_conf())
    def test_invalid_config_in_rst(self, app, status, warning):
        app.build()
        html = (app.outdir / "config_invalid.html").read_text()
        assert "<h1>Test for invalid config</h1>" in html
        assert 'Object.assign(revealConfig, {transition:"});' not in html

    @with_app(**gen_testdoc_conf("invalid-conf"))
    def test_invalid_conf_in_confpy(self, app, status, warning):
        app.build()
        html = (app.outdir / "index.html").read_text()
        assert 'Object.assign(revealConfig, {transition:"});' not in html

    @with_app(**gen_testdoc_conf("conf-google-fonts"))
    def test_google_fonts_in_confpy(self, app, status, warning):
        app.build()
        html = (app.outdir / "index.html").read_text()
        assert "Noto Sans JP" in html
        assert "Noto+Sans+JP" in html


class SlideThemeTesting(unittest.TestCase):
    """Test case for Reveal.js theme settings"""

    @with_app(**gen_testdoc_conf())
    def test_theme_default(self, app, status, warning):
        app.build()
        html = (app.outdir / "index.html").read_text()
        theme_url_path = f"_static/black.css"
        assert theme_url_path in html

    @with_app(**gen_testdoc_conf())
    def test_theme_by_directive(self, app, status, warning):
        app.build()
        html = (app.outdir / "theme_changed.html").read_text()
        assert "<h1>Test for selecatable theme</h1>" in html
        theme_url_path = f"_static/solarized.css"
        assert theme_url_path in html


class SlideFontTesting(unittest.TestCase):
    """Test case for Reveal.js webfont settings"""

    @with_app(**gen_testdoc_conf())
    def test_theme_by_directive(self, app, status, warning):
        app.build()
        html = (app.outdir / "webfont_set.html").read_text()
        assert "<h1>Test for selecatable theme</h1>" in html
        assert "Noto Sans JP" in html
        assert "Noto+Sans+JP" in html
