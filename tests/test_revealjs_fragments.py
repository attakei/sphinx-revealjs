"""Test cases for ``revealjs_fragments`` directive."""
import pytest

from testutils import soup_html


class Test_BuildHtml:  # noqa
    @pytest.mark.sphinx("revealjs", testroot="misc")
    def test_list_fragments(self, app, status, warning):  # noqa
        soup = soup_html(app, "has_fragments.html")
        target = soup.find_all("h3")[0].parent
        assert len(target.find_all(attrs={"fragment"})) == 3

    @pytest.mark.sphinx("revealjs", testroot="misc")
    def test_paragraph_fragments(self, app, status, warning):  # noqa
        soup = soup_html(app, "has_fragments.html")
        target = soup.find_all("h3")[1].parent
        assert len(target.find_all(attrs={"fragment"})) == 2
