"""Test cases for generating files."""

from pathlib import Path

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


@pytest.mark.sphinx("revealjs", testroot="default")
def test_contains_scss(app: SphinxTestApp, status, warning):  # noqa
    app.build()
    assert Path(app.outdir / "_static/revealjs/css").exists()
    assert Path(
        app.outdir / "_static/revealjs/css/theme/template/settings.scss"
    ).exists()
