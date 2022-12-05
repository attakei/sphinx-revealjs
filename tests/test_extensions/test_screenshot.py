"""Test cases for sphix_revealjs.ext.screenshot."""
import magic
import pytest
from sphinx.testing.util import SphinxTestApp
from testutils import soup_html


@pytest.mark.sphinx(
    "revealjs",
    testroot="default",
    confoverrides={"extensions": ["sphinx_revealjs", "sphinx_revealjs.ext.screenshot"]},
)
def test_generate_screenshot(app: SphinxTestApp, status, warning):  # noqa
    app.build()
    image_path = app.outdir / "_images/ogp/index.png"
    assert image_path.exists()
    assert magic.from_file(image_path, mime=True) == "image/png"
    soup = soup_html(app, "index.html")
    assert soup.find("meta", {"property": "og:image"})


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
