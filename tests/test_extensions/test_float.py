"""Tests for revealjs-float extension."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from testutils import soup_html

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx(
    "revealjs",
    testroot="float",
)
def test_float_basic(app: SphinxTestApp):
    """Test basic revealjs-float functionality."""
    app.build()
    soup = soup_html(app, "index.html")
    # Find all revealjs-float divs
    float_divs = soup.find_all("div", {"style": True})
    # Filter for our float divs (they have position: absolute)
    float_divs = [
        div for div in float_divs if "position: absolute" in div.get("style", "")
    ]
    assert len(float_divs) == 3


@pytest.mark.sphinx(
    "revealjs",
    testroot="float",
)
def test_float_drag_option(app: SphinxTestApp):
    """Test drag option sets width and height."""
    app.build()
    soup = soup_html(app, "index.html")
    float_divs = soup.find_all("div", {"style": True})
    float_divs = [
        div for div in float_divs if "position: absolute" in div.get("style", "")
    ]
    # First float has drag: 40 50
    assert "width: 40%" in float_divs[0].get("style", "")
    assert "height: 50%" in float_divs[0].get("style", "")


@pytest.mark.sphinx(
    "revealjs",
    testroot="float",
)
def test_float_drop_option_positive(app: SphinxTestApp):
    """Test drop option with positive values sets left and top."""
    app.build()
    soup = soup_html(app, "index.html")
    float_divs = soup.find_all("div", {"style": True})
    float_divs = [
        div for div in float_divs if "position: absolute" in div.get("style", "")
    ]
    # First float has drop: 10 15
    assert "left: 10%" in float_divs[0].get("style", "")
    assert "top: 15%" in float_divs[0].get("style", "")


@pytest.mark.sphinx(
    "revealjs",
    testroot="float",
)
def test_float_drop_option_negative(app: SphinxTestApp):
    """Test drop option with negative values sets right and bottom."""
    app.build()
    soup = soup_html(app, "index.html")
    float_divs = soup.find_all("div", {"style": True})
    float_divs = [
        div for div in float_divs if "position: absolute" in div.get("style", "")
    ]
    # Third float has drop: -5 -20
    assert "right: 5%" in float_divs[2].get("style", "")
    assert "bottom: 20%" in float_divs[2].get("style", "")


@pytest.mark.sphinx(
    "revealjs",
    testroot="float",
)
def test_float_bg_option(app: SphinxTestApp):
    """Test bg option sets background color."""
    app.build()
    soup = soup_html(app, "index.html")
    float_divs = soup.find_all("div", {"style": True})
    float_divs = [
        div for div in float_divs if "position: absolute" in div.get("style", "")
    ]
    assert "background-color: yellow" in float_divs[0].get("style", "")
    assert "background-color: red" in float_divs[1].get("style", "")
    assert "background-color: blue" in float_divs[2].get("style", "")


@pytest.mark.sphinx(
    "revealjs",
    testroot="float",
)
def test_float_with_units(app: SphinxTestApp):
    """Test float with specific units (px)."""
    app.build()
    soup = soup_html(app, "index.html")
    float_divs = soup.find_all("div", {"style": True})
    float_divs = [
        div for div in float_divs if "position: absolute" in div.get("style", "")
    ]
    # Second float has drop: -40px 40px
    assert "right: 40px" in float_divs[1].get("style", "")
    assert "top: 40px" in float_divs[1].get("style", "")
