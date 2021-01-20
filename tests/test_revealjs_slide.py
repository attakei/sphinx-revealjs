"""Test cases for ``revealjs_slide`` directive."""
import unittest

from sphinx_testing import TestApp, with_app

from testutils import gen_app_conf, soup_html


class BuildHtmlTests(unittest.TestCase):  # noqa
    @with_app(**gen_app_conf())
    def test_override_theme(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "with_theme.html")
        css_hrefs = [elm["href"] for elm in soup.find_all("link", rel="stylesheet")]
        self.assertIn("_static/custom.css", css_hrefs)

    @with_app(**gen_app_conf())
    def test_override_font(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "with_googlefont.html")
        css_hrefs = [
            elm["href"]
            for elm in soup.find_all("link", rel="stylesheet")
            if elm["href"].startswith("https://fonts.googleapis.com")
        ]
        self.assertEqual(len(css_hrefs), 1)
        styles = "\n".join([e.text for e in soup.find_all("style")])
        self.assertIn("'M PLUS 1p'", styles)

    @with_app(**gen_app_conf())
    def test_config(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "with_conf.html")
        self.assertIn(
            'Object.assign(revealjsConfig, {"transition": "none"});',
            soup.find_all("script")[-1].text,
        )

    @with_app(**gen_app_conf())
    def test_config_as_content(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "with_conf_content.html")
        self.assertIn(
            "Object.assign(revealjsConfig, {\n", soup.find_all("script")[-1].text,
        )
        self.assertIn(
            '"transition": "none"\n', soup.find_all("script")[-1].text,
        )
        self.assertIn(
            "});", soup.find_all("script")[-1].text,
        )
