"""Build tests for configuration parameters."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from testutils import soup_html

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


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
        if "_static/revealjs/dist/theme/moon.css" in e["href"]
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
