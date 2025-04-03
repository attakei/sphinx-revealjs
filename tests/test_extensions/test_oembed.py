from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from testutils import soup_html

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx(
    "revealjs",
    testroot="oembed",
)
def test_standard_behavior(app: SphinxTestApp):
    app.build()
    assert (app.outdir / "_files/oembed/index.json").exists()
    data = json.loads((app.outdir / "_files/oembed/index.json").read_text())
    assert "version" in data
    assert data["type"] == "rich"
    assert data["title"] == "Test presentation"
    assert data["width"] == 960
    assert data["height"] == 700
    assert data["html"].startswith("<iframe src")
    assert data["html"].endswith("</iframe>")
    soup = soup_html(app, "index.html")
    assert soup.find("link", {"rel": "alternate", "type": "application/json+oembed"})


@pytest.mark.sphinx(
    "revealjs",
    testroot="oembed",
)
def test_override_by_directive(app: SphinxTestApp):
    app.build()
    data = json.loads((app.outdir / "_files/oembed/with-directive.json").read_text())
    assert data["width"] == 1440
    assert data["height"] == 1080


@pytest.mark.sphinx(
    "revealjs",
    testroot="oembed",
    confoverrides={
        "revealjs_script_conf": {
            "width": 1280,
            "height": 960,
        }
    },
)
def test_override_by_conf(app: SphinxTestApp):
    app.build()
    data = json.loads((app.outdir / "_files/oembed/index.json").read_text())
    assert data["width"] == 1280
    assert data["height"] == 960


@pytest.mark.sphinx(
    "revealjs",
    testroot="oembed",
    confoverrides={
        "revealjs_script_conf": {
            "width": 1280,
            "height": 960,
        }
    },
)
def test_override_priority(app: SphinxTestApp):
    app.build()
    data = json.loads((app.outdir / "_files/oembed/with-directive.json").read_text())
    assert data["width"] == 1440
    assert data["height"] == 1080
