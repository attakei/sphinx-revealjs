"""Test cases for ``revealjs-fragments`` directive."""
import pytest
from sphinx.testing.util import SphinxTestApp
from testutils import soup_html


@pytest.mark.sphinx("revealjs", testroot="default")
def test_list_fragments(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-fragments.html")
    target = soup.find_all("h3")[0].parent
    assert len(target.find_all(attrs={"fragment"})) == 3


@pytest.mark.sphinx("revealjs", testroot="default")
def test_paragraph_fragments(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-fragments.html")
    target = soup.find_all("h3")[1].parent
    assert len(target.find_all(attrs={"fragment"})) == 2


@pytest.mark.sphinx("revealjs", testroot="default")
def test_custom_fragments(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-fragments.html")
    target = soup.find_all("h3")[2].parent
    assert len(target.find_all(attrs={"class": "fragment custom blur"})) == 3
