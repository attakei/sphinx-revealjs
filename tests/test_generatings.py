"""Test cases for generating giles."""
import pytest
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("revealjs", testroot="default")
def test_not_generate_genindex(app: SphinxTestApp, status, warning):  # noqa
    app.build()
    assert not (app.outdir / "genindex.html").exists()


@pytest.mark.sphinx("revealjs", testroot="default")
def test_not_generate_search(app: SphinxTestApp, status, warning):  # noqa
    app.build()
    assert not (app.outdir / "search.html").exists()
