"""Build tests for writing directives."""
import pytest
from testutils import soup_html


class Test_RevealjsSection:  # noqa
    @pytest.mark.sphinx("revealjs", testroot="misc")
    def test_render_section1_bg(self, app, status, warning):  # noqa
        soup = soup_html(app, "has_section_directive.html")
        section_tag = soup.h1.parent
        assert "data-background-color" in section_tag.attrs
        assert section_tag["data-background-color"] == "#000001"

    @pytest.mark.sphinx("revealjs", testroot="misc")
    def test_render_section2_bg(self, app, status, warning):  # noqa
        soup = soup_html(app, "has_section_directive.html")
        section_tag = soup.h2.parent
        assert "data-background-color" in section_tag.attrs
        assert section_tag["data-background-color"] == "#000101"

    @pytest.mark.sphinx("revealjs", testroot="misc")
    def test_no_render_parent_bg(self, app, status, warning):  # noqa
        soup = soup_html(app, "has_section_directive.html")
        section_tag = soup.h2.parent.parent
        assert "data-background-color" not in section_tag.attrs


class Test_RevealjsCode:  # noqa
    @pytest.mark.sphinx("revealjs", testroot="misc")
    def test_inherit_code_block(self, app, status, warning):  # noqa
        soup = soup_html(app, "has_revealjs_code_block.html")
        code_tag = soup.find_all("code")[0]
        assert "python" in code_tag.attrs["class"]

    @pytest.mark.sphinx("revealjs", testroot="misc")
    def test_dataline(self, app, status, warning):  # noqa
        soup = soup_html(app, "has_revealjs_code_block.html")
        code_tag = soup.find_all("code")[1]
        assert "php" in code_tag.attrs["class"]
        assert "data-line-numbers" in code_tag.attrs
