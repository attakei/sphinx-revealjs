"""Build tests for configuration parameters."""
import unittest

from sphinx_testing import TestApp, with_app

from testutils import gen_app_conf, soup_html


class BuildHtmlTests(unittest.TestCase):  # noqa
    @with_app(**gen_app_conf(confoverrides={"revealjs_script_files": ["js/test.js"]}))
    def test_script_tags(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        elements = [
            e for e in soup.find_all("script") if e.get("src") == "_static/js/test.js"
        ]
        self.assertEqual(len(elements), 1)

    @with_app(**gen_app_conf(confoverrides={"revealjs_google_fonts": ["Noto Sans JP"]}))
    def test_google_fonts(self, app, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        link = [
            e
            for e in soup.find_all("link", rel="stylesheet")
            if e["href"].startswith("https://fonts.googleapis.com/css2")
        ]
        self.assertEqual(len(link), 1)
        style = soup.find_all("style")[-1]
        self.assertIn(".reveal", style.text)
        self.assertIn("Noto Sans JP", style.text)
        self.assertIn("sans-serif;", style.text)

    @with_app(
        **gen_app_conf(
            confoverrides={
                "revealjs_google_fonts": ["Noto Sans JP"],
                "revealjs_generic_font": "cursive",
            }
        )
    )
    def test_google_fonts_with_generic(self, app, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        link = [
            e
            for e in soup.find_all("link", rel="stylesheet")
            if e["href"].startswith("https://fonts.googleapi")
        ]
        self.assertEqual(len(link), 1)
        style = soup.find_all("style")[-1]
        self.assertIn("Noto Sans JP", style.text)
        self.assertIn("cursive", style.text)

    @with_app(**gen_app_conf(confoverrides={"revealjs_generic_font": "cursive"}))
    def test_generic_font_only(self, app, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        styles = soup.find_all("style")
        self.assertEqual(len(styles), 0)

    @with_app(**gen_app_conf(confoverrides={"revealjs_script_files": ["js/test.js"]}))
    def test_script_tags(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        elements = [
            e for e in soup.find_all("script") if e.get("src") == "_static/js/test.js"
        ]
        self.assertEqual(len(elements), 1)

    @with_app(
        **gen_app_conf(
            confoverrides={"revealjs_script_files": ["https://example.com/test.js"]}
        )
    )
    def test_script_tags_https(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        elements = [
            e
            for e in soup.find_all("script")
            if e.get("src") == "https://example.com/test.js"
        ]
        self.assertEqual(len(elements), 1)

    @with_app(
        **gen_app_conf(confoverrides={"revealjs_script_conf": '{transition:"none"}'})
    )
    def test_revealjs_script_conf(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        self.assertIn(
            'Object.assign(revealjsConfig, {transition:"none"});',
            soup.find_all("script")[-1].text,
        )

    @with_app(
        **gen_app_conf(
            confoverrides={
                "revealjs_script_plugins": [
                    {"name": "RevealNotes", "src": "revealjs4/plugin/notes/notes.js",}
                ]
            }
        )
    )
    def test_revealjs_script_plugins(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        script = soup.find_all("script")[-1].text
        self.assertIn("RevealNotes", script)
        for d in soup.find_all("script"):
            print(d)
        scripts = [d["src"] for d in soup.find_all("script") if "src" in d.attrs]
        self.assertIn("_static/revealjs4/plugin/notes/notes.js", scripts)

    @with_app(**gen_app_conf(confoverrides={"revealjs_style_theme": "moon"}))
    def test_revealjs_style_theme(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        links = [
            e
            for e in soup.find_all("link", rel="stylesheet")
            if "_static/revealjs/css/theme/moon.css" in e["href"]
        ]
        self.assertEqual(len(links), 1)

    @with_app(**gen_app_conf(confoverrides={"revealjs_style_theme": "custom.css"}))
    def test_revealjs_style_theme(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        links = [
            e
            for e in soup.find_all("link", rel="stylesheet")
            if "_static/custom.css" in e["href"]
        ]
        self.assertEqual(len(links), 1)

    @with_app(
        **gen_app_conf(
            confoverrides={"revealjs_css_files": ["https://example.com/example.css"]}
        )
    )
    def test_revealjs_css_files(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        links = [
            e
            for e in soup.find_all("link", rel="stylesheet")
            if "https://example.com/example.css" in e["href"]
        ]
        self.assertEqual(len(links), 1)

    @with_app(
        **gen_app_conf(
            confoverrides={
                "revealjs_static_path": ["_static"],
                "revealjs_css_files": ["custom.css"],
            }
        )
    )
    def test_revealjs_css_files_local(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        links = [
            e
            for e in soup.find_all("link", rel="stylesheet")
            if "_static/custom.css" in e["href"]
        ]
        self.assertEqual(len(links), 1)
        self.assertTrue((app.outdir / "_static/custom.css").exists())

    @with_app(
        **gen_app_conf(
            confoverrides={
                "revealjs_static_path": ["_static"],
                "revealjs_css_files": ["custom.css"],
            }
        )
    )
    def test_default_theme_css_comes_before_custom_css(
        self, app: TestApp, status, warning
    ):
        soup = soup_html(app, "index.html")
        stylesheet_href_list = [
            e["href"] for e in soup.find_all("link", rel="stylesheet")
        ]
        default_theme_index = stylesheet_href_list.index(
            "_static/revealjs4/dist/theme/black.css"
        )
        custom_css_index = stylesheet_href_list.index("_static/custom.css")
        self.assertTrue(default_theme_index < custom_css_index)

    @with_app(
        **gen_app_conf(
            confoverrides={
                "revealjs_style_theme": "moon",
                "revealjs_static_path": ["_static"],
                "revealjs_css_files": ["other_custom.css"],
            }
        )
    )
    def test_specified_theme_css_comes_before_custom_css(
        self, app: TestApp, status, warning
    ):
        soup = soup_html(app, "index.html")
        stylesheet_href_list = [
            e["href"] for e in soup.find_all("link", rel="stylesheet")
        ]
        specified_theme_index = stylesheet_href_list.index(
            "_static/revealjs4/dist/theme/moon.css"
        )
        custom_css_index = stylesheet_href_list.index("_static/other_custom.css")
        self.assertTrue(specified_theme_index < custom_css_index)
