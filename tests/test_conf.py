"""Build tests for configuration parameters."""
import unittest

from sphinx_testing import TestApp, with_app

from testutils import gen_app_conf, soup_html


class BuildHtmlTests(unittest.TestCase):  # noqa
    @with_app(
        **gen_app_conf(
            confoverrides={
                "revealjs_theme_options": {"revealjs_config": '{"transition":"none"}'}
            }
        )
    )
    def test_revealjs_config(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        self.assertIn(
            'Object.assign(revealConfig, {"transition":"none"});',
            soup.find_all("script")[-1].text,
        )

    @with_app(
        **gen_app_conf(
            confoverrides={
                "revealjs_theme_options": {"revealjs_config": '{transition:"}'}
            }
        )
    )
    def test_invalid_config(self, app, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        self.assertNotIn('Object.assign(revealConfig, {transition:"});', soup)

    @with_app(
        **gen_app_conf(
            confoverrides={"revealjs_theme_options": {"google_font": "Noto Sans JP"}}
        )
    )
    def test_google_fonts(self, app, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        self.assertNotIn("Noto Sans JP", soup)
        self.assertNotIn("Noto+Sans+JP", soup)

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
