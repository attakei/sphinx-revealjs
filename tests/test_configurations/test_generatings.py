"""Test cases for generating giles."""
import pytest
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx(
    "revealjs", testroot="default", confoverrides={"revealjs_use_index": True}
)
def test_generating_genindex(app: SphinxTestApp, status, warning):  # noqa
    app.build()
    assert (app.outdir / "genindex.html").exists()
