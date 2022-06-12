"""Test cases for ``revealjs-break`` directive."""
import pytest
from sphinx.testing.util import SphinxTestApp
from testutils import soup_html


@pytest.mark.sphinx("revealjs", testroot="default")
def test_on_revealjs_builder(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-break.html")
    sec2 = soup.find_all("section")[1]
    # title, content1, content2 (splitted)
    assert len(sec2.find_all("section")) == 3
