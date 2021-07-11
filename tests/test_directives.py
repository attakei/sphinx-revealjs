"""Build tests for writing directives."""
import unittest

from sphinx_testing import TestApp, with_app

from testutils import gen_app_conf, soup_html


class RevealjsSectionTests(unittest.TestCase):  # noqa
    @with_app(**gen_app_conf())
    def test_render_section1_bg(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "has_section_directive.html")
        section_tag = soup.h1.parent
        self.assertIn("data-background-color", section_tag.attrs)
        self.assertEqual(section_tag["data-background-color"], "#000001")

    @with_app(**gen_app_conf())
    def test_render_section2_bg(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "has_section_directive.html")
        section_tag = soup.h2.parent
        self.assertIn("data-background-color", section_tag.attrs)
        self.assertEqual(section_tag["data-background-color"], "#000101")

    @with_app(**gen_app_conf())
    def test_no_render_parent_bg(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "has_section_directive.html")
        section_tag = soup.h2.parent.parent
        self.assertNotIn("data-background-color", section_tag.attrs)


class RevealjsCodeTests(unittest.TestCase):  # noqa
    @with_app(**gen_app_conf())
    def test_inherit_code_block(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "has_revealjs_code_block.html")
        code_tag = soup.find_all("code")[0]
        self.assertIn("python", code_tag.attrs["class"])

    @with_app(**gen_app_conf())
    def test_dataline(self, app: TestApp, status, warning):  # noqa
        soup = soup_html(app, "has_revealjs_code_block.html")
        code_tag = soup.find_all("code")[1]
        self.assertIn("php", code_tag.attrs["class"])
        self.assertIn("data-line-numbers", code_tag.attrs)
