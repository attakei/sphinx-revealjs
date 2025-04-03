"""Test cases for ``revealjs-section`` directive."""

from __future__ import annotations

import io
from pathlib import Path
from textwrap import dedent
from typing import TYPE_CHECKING

import pytest
from sphinx.testing import restructuredtext
from testutils import soup_html

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


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


@pytest.mark.sphinx("revealjs", testroot="default")
def test_render_local_photo_global(app: SphinxTestApp):  # noqa
    soup = soup_html(app, "with-section-directives/with-background-image.html")
    section_tag = soup.h2.parent
    assert "data-background-image" in section_tag.attrs
    assert (
        section_tag["data-background-image"]
        == "https://www.attakei.net/_static/images/icon-attakei@2x.png"
    )


@pytest.mark.sphinx("revealjs", testroot="default")
def test_render_local_photo(app: SphinxTestApp):  # noqa
    soup = soup_html(app, "with-section-directives/with-background-image-local.html")
    assert (Path(app.outdir) / "_images/photo.jpg").exists()
    section_tag = soup.h2.parent
    assert "data-background-image" in section_tag.attrs
    assert section_tag["data-background-image"] == "../_images/photo.jpg"


@pytest.mark.sphinx("revealjs", testroot="default")
def test_render_local_video_global(app: SphinxTestApp):  # noqa
    soup = soup_html(app, "with-section-directives/with-background-video.html")
    section_tag = soup.h2.parent
    assert "data-background-video" in section_tag.attrs
    assert (
        section_tag["data-background-video"]
        == "https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4"
    )


@pytest.mark.sphinx("revealjs", testroot="default")
def test_render_local_video_localfile(app: SphinxTestApp):  # noqa
    soup = soup_html(app, "with-section-directives/with-background-video-local.html")
    assert (Path(app.outdir) / "_images/sample.mp4").exists()
    section_tag = soup.h2.parent
    assert "data-background-video" in section_tag.attrs
    assert section_tag["data-background-video"] == "../_images/sample.mp4"


@pytest.mark.sphinx("revealjs", testroot="default")
def test_render_local_iframe_localfile(app: SphinxTestApp):  # noqa
    soup = soup_html(app, "with-section-directives/with-background-iframe-local.html")
    assert (Path(app.outdir) / "_images/sample.html").exists()
    section_tag = soup.h2.parent
    assert "data-background-iframe" in section_tag.attrs
    assert section_tag["data-background-iframe"] == "../_images/sample.html"


@pytest.mark.sphinx("revealjs", testroot="default")
def test_render_local_iframe_localfile_from_vertical(app: SphinxTestApp):  # noqa
    soup = soup_html(
        app, "with-section-directives/with-vertical-background-iframe-local.html"
    )
    assert (Path(app.outdir) / "_images/sample.html").exists()
    section_tag = soup.h2.parent.parent
    assert "data-background-iframe" in section_tag.attrs
    assert section_tag["data-background-iframe"] == "../_images/sample.html"


@pytest.mark.sphinx("revealjs", testroot="default")
def test_render_local_iframe_localfile_from_break(app: SphinxTestApp):  # noqa
    soup = soup_html(
        app, "with-section-directives/with-break-background-iframe-local.html"
    )
    assert (Path(app.outdir) / "_images/sample.html").exists()
    section_tag = soup.h2.parent.parent.find_all("section")[-1]
    assert "data-background-iframe" in section_tag.attrs
    assert section_tag["data-background-iframe"] == "../_images/sample.html"


@pytest.mark.sphinx("revealjs", testroot="default")
def test_render_local_iframe(app: SphinxTestApp):  # noqa
    soup = soup_html(app, "with-section-directives/with-background-iframe.html")
    section_tag = soup.h2.parent
    assert "data-background-iframe" in section_tag.attrs
    assert section_tag["data-background-iframe"] == "https://example.com"


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
