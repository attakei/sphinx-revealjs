"""Test cases for sphix_revealjs.ext.screenshot."""
import magic
import pytest
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx(
    "revealjs",
    testroot="default",
    confoverrides={"extensions": ["sphinx_revealjs", "sphinx_revealjs.ext.screenshot"]},
)
def test_not_generate_screenshot(app: SphinxTestApp, status, warning):  # noqa
    app.build()
    image_path = app.outdir / "_images/ogp/index.png"
    assert image_path.exists()
    assert magic.from_file(image_path, mime=True) == "image/png"
