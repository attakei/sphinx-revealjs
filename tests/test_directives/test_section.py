"""Test cases for ``revealjs-section`` directive."""
import pytest
from sphinx.testing.util import SphinxTestApp
from testutils import soup_html


@pytest.mark.sphinx("revealjs", testroot="default")
def test_render_section1_bg(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-section.html")
    section_tag = soup.h1.parent
    assert "data-background-color" in section_tag.attrs
    assert section_tag["data-background-color"] == "#000001"


@pytest.mark.sphinx("revealjs", testroot="default")
def test_render_section2_bg(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-section.html")
    section_tag = soup.h2.parent
    assert "data-background-color" in section_tag.attrs
    assert section_tag["data-background-color"] == "#000101"


@pytest.mark.sphinx("revealjs", testroot="default")
def test_no_render_parent_bg(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-section.html")
    section_tag = soup.h2.parent.parent
    assert "data-background-color" not in section_tag.attrs
