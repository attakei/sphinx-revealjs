"""Test cases for not revealjs builders."""
import pytest
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html", testroot="default")
def test_for_html_build(app: SphinxTestApp, status, warning):  # noqa
    app.build()


@pytest.mark.sphinx("text", testroot="default")
def test_for_text_build(app: SphinxTestApp, status, warning):  # noqa
    app.build()


@pytest.mark.sphinx("man", testroot="default")
def test_for_man_build(app: SphinxTestApp, status, warning):  # noqa
    app.build()


@pytest.mark.sphinx("texinfo", testroot="default")
def test_for_texinfo_build(app: SphinxTestApp, status, warning):  # noqa
    app.build()


@pytest.mark.sphinx("latex", testroot="default")
def test_for_latex_build(app: SphinxTestApp, status, warning):  # noqa
    app.build()
