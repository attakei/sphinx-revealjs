"""Test cases for ``revealjs-section`` directive."""
import io
from textwrap import dedent

import pytest
from sphinx.testing import restructuredtext
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


@pytest.mark.sphinx("revealjs", testroot="default")
def test_render_vertical_bg_vslide1(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-vertical-1.html")
    section_tag = soup.h1.parent.parent
    assert "data-background-color" in section_tag.attrs
    assert section_tag["data-background-color"] == "#000001"


@pytest.mark.sphinx("revealjs", testroot="default")
def test_render_vertical_bg_vslide2(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-vertical-2.html")
    section_tag = soup.h2.parent.parent
    assert "data-background-color" in section_tag.attrs
    assert section_tag["data-background-color"] == "#000001"


@pytest.mark.sphinx("revealjs", testroot="default")
def test_render_custom_attributes(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-section-having-custom-attributes.html")
    section_tag = soup.h2.parent
    assert "data-markdown" in section_tag.attrs
    assert section_tag["data-markdown"] == ""


class TestForRevealjsSection:
    @pytest.mark.sphinx("revealjs", testroot="default")
    def test_csutom_params(self, app: SphinxTestApp, warning: io.StringIO):
        text = dedent(
            """
        .. revealjs-section::
           :data-x:
        """
        )
        doctree = restructuredtext.parse(app, text)
        assert 'ERROR: Error in "revealjs-section" directive:' not in warning.getvalue()
        assert "data-x" in doctree.children[0].attributes

    @pytest.mark.sphinx("revealjs", testroot="default")
    def test_invalid_section_params(self, app: SphinxTestApp, warning: io.StringIO):
        text = dedent(
            """
        .. revealjs-section::
           :x-data:
        """
        )
        doctree = restructuredtext.parse(app, text)
        assert 'ERROR: Error in "revealjs-section" directive:' in warning.getvalue()
        assert 'unknown option: "x-data"' in warning.getvalue()
        assert "x-data" not in doctree.attributes


class TestForRevealjsBreak:
    @pytest.mark.sphinx("revealjs", testroot="default")
    def test_csutom_params(self, app: SphinxTestApp, warning: io.StringIO):
        text = dedent(
            """
        .. revealjs-break::
           :data-x:
        """
        )
        doctree = restructuredtext.parse(app, text)
        assert 'ERROR: Error in "revealjs-break" directive:' not in warning.getvalue()
        assert "data-x" in doctree.children[0].attributes

    @pytest.mark.sphinx("revealjs", testroot="default")
    def test_invalid_section_params(self, app: SphinxTestApp, warning: io.StringIO):
        text = dedent(
            """
        .. revealjs-break::
           :x-data:
        """
        )
        doctree = restructuredtext.parse(app, text)
        assert 'ERROR: Error in "revealjs-break" directive:' in warning.getvalue()
        assert 'unknown option: "x-data"' in warning.getvalue()
        assert "x-data" not in doctree.attributes


class TestForRevealjsVertical:
    @pytest.mark.sphinx("revealjs", testroot="default")
    def test_csutom_params(self, app: SphinxTestApp, warning: io.StringIO):
        text = dedent(
            """
        .. revealjs-vertical::
           :data-x:
        """
        )
        doctree = restructuredtext.parse(app, text)
        assert (
            'ERROR: Error in "revealjs-vertical" directive:' not in warning.getvalue()
        )
        assert "data-x" in doctree.children[0].attributes

    @pytest.mark.sphinx("revealjs", testroot="default")
    def test_invalid_section_params(self, app: SphinxTestApp, warning: io.StringIO):
        text = dedent(
            """
        .. revealjs-vertical::
           :x-data:
        """
        )
        doctree = restructuredtext.parse(app, text)
        assert 'ERROR: Error in "revealjs-vertical" directive:' in warning.getvalue()
        assert 'unknown option: "x-data"' in warning.getvalue()
        assert "x-data" not in doctree.attributes
