"""Test cases for sphix_revealjs.ext.screenshot."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from PIL import Image

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx(
    "revealjs",
    testroot="default",
    freshenv=True,
    confoverrides={"extensions": ["sphinx_revealjs", "sphinx_revealjs.ext.screenshot"]},
)
def test_generate_screenshot(app: SphinxTestApp, status, warning):  # noqa
    try:
        import magic
    except ImportError as err:
        pytest.skip(reason=err.msg)

    app.build()
    image_path = app.outdir / "_images/ogp/index.png"
    assert image_path.exists()
    assert magic.from_file(image_path, mime=True) == "image/png"
    with Image.open(image_path) as img:
        width, height = img.size
        assert width == 960
        assert height == 700


@pytest.mark.sphinx(
    "revealjs",
    testroot="includes",
    confoverrides={
        "extensions": ["sphinx_revealjs", "sphinx_revealjs.ext.screenshot"],
        "revealjs_screenshot_excludes": ["content"],
    },
)
def test_skip_included(app: SphinxTestApp, status, warning):  # noqa
    app.build()
    image_path = app.outdir / "_images/ogp/content.png"
    assert not image_path.exists()


@pytest.mark.sphinx(
    "dirrevealjs",
    testroot="default",
    freshenv=True,
    confoverrides={
        "extensions": ["sphinx_revealjs", "sphinx_revealjs.ext.screenshot"],
    },
)
def test_dirrevealjs(app: SphinxTestApp, status, warning):  # noqa
    app.build()


@pytest.mark.sphinx(
    "revealjs",
    testroot="viewports",
)
def test_customize_size_by_directive(app: SphinxTestApp, status, warning):  # noqa
    app.build()
    with Image.open(app.outdir / "_images/ogp/index.png") as img:
        width, height = img.size
        assert width == 960
        assert height == 700
    with Image.open(app.outdir / "_images/ogp/custom.png") as img:
        width, height = img.size
        assert width == 1280
        assert height == 720


@pytest.mark.sphinx(
    "revealjs",
    testroot="viewports",
    confoverrides={"revealjs_script_conf": {"width": 960, "height": 720}},
)
def test_customize_size_by_conf(app: SphinxTestApp, status, warning):  # noqa
    app.build()
    with Image.open(app.outdir / "_images/ogp/index.png") as img:
        width, height = img.size
        assert width == 960
        assert height == 720
    with Image.open(app.outdir / "_images/ogp/custom.png") as img:
        width, height = img.size
        assert width == 1280
        assert height == 720


@pytest.mark.sphinx(
    "html",
    testroot="viewports",
)
def test_work_in_html_builder(app: SphinxTestApp, status, warning):  # noqa
    app.build()
    image_path = app.outdir / "_images/ogp/index.png"
    assert not image_path.exists()
