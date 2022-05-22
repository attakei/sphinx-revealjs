"""Build tests for configuration parameters."""
import pytest
from sphinx.testing.util import SphinxTestApp
from testutils import soup_html


@pytest.mark.sphinx(
    "revealjs",
    testroot="for-config",
    confoverrides={"revealjs_style_theme": "moon"},
)
def test_using_builtin_theme(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    links = [
        e
        for e in soup.find_all("link", rel="stylesheet")
        if "_static/revealjs4/dist/theme/moon.css" in e["href"]
    ]
    assert len(links) == 1


@pytest.mark.sphinx(
    "revealjs",
    testroot="for-config",
    confoverrides={"revealjs_style_theme": "custom.css"},
)
def test_using_custom_theme(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    links = [
        e
        for e in soup.find_all("link", rel="stylesheet")
        if "_static/custom.css" in e["href"]
    ]
    assert len(links) == 1
