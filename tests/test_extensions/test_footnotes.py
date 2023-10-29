"""Test cases for sphix_revealjs.ext.footnotes."""
import pytest
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx(
    "revealjs",
    testroot="default",
    confoverrides={
        "extensions": ["sphinx_revealjs", "sphinx_revealjs.ext.footnotes"],
    },
)
def test_skip_included(app: SphinxTestApp, status, warning):  # noqa
    app.build()
    css_path = app.outdir / "_static/sphinx-revealjs/css/footnotes.css"
    assert css_path.exists()


@pytest.mark.sphinx(
    "dirrevealjs",
    testroot="default",
    freshenv=True,
    confoverrides={
        "extensions": ["sphinx_revealjs", "sphinx_revealjs.ext.footnotes"],
    },
)
def test_dirrevealjs(app: SphinxTestApp, status, warning):  # noqa
    app.build()
    css_path = app.outdir / "_static/sphinx-revealjs/css/footnotes.css"
    assert css_path.exists()
