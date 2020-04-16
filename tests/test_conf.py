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
            if e["href"].startswith("https://fonts.googleapi")
        ]
        self.assertEqual(len(link), 1)
        style = soup.find_all("style")[-1]
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
                    {
                        "src": "revealjs/plugin/notes/notes.js",
                        "options": """
                    {async: true}
                """,
                    }
                ]
            }
        )
    )
    def test_revealjs_script_plugins(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        script = soup.find_all("script")[-1].text
        self.assertIn("plugin_0 = {async: true}", script)
        self.assertIn('plugin_0.src = "_static/revealjs/plugin/notes/notes.js"', script)
        self.assertIn("revealjsConfig.dependencies.push(plugin_0);", script)

    @with_app(
        **gen_app_conf(
            confoverrides={
                "revealjs_script_plugins": [
                    {
                        "src": "revealjs/plugin/notes/notes.js",
                        "options": "{async: true}",
                    },
                    {"src": "revealjs/plugin/highlight/highlight.js"},
                ]
            }
        )
    )
    def test_revealjs_script_plugins(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        script = soup.find_all("script")[-1].text
        self.assertIn("plugin_1 = {};", script)
        self.assertIn(
            'plugin_1.src = "_static/revealjs/plugin/highlight/highlight.js"', script
        )

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
