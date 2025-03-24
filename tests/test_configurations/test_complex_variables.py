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
    confoverrides={
        "revealjs_static_path": ["_static"],
        "revealjs_css_files": ["custom.css"],
    },
)
def test_default_theme_css_comes_before_custom_css(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    stylesheet_href_list = [e["href"] for e in soup.find_all("link", rel="stylesheet")]
    default_theme_index = stylesheet_href_list.index(
        "_static/revealjs/dist/theme/black.css"
    )
    custom_css_index = stylesheet_href_list.index("_static/custom.css")
    assert default_theme_index < custom_css_index


@pytest.mark.sphinx(
    "revealjs",
    testroot="for-config",
    confoverrides={
        "revealjs_style_theme": "moon",
        "revealjs_static_path": ["_static"],
        "revealjs_css_files": ["other_custom.css"],
    },
)
def test_specified_theme_css_comes_before_custom_css(
    app: SphinxTestApp, status, warning
):  # noqa
    soup = soup_html(app, "index.html")
    stylesheet_href_list = [e["href"] for e in soup.find_all("link", rel="stylesheet")]
    specified_theme_index = stylesheet_href_list.index(
        "_static/revealjs/dist/theme/moon.css"
    )
    custom_css_index = stylesheet_href_list.index("_static/other_custom.css")
    assert specified_theme_index < custom_css_index
