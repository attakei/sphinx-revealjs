from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx(
    "revealjs",
    testroot="sass",
    confoverrides={
        "revealjs_sass_targets": {"style.scss": "style.css"},
    },
)
def test_sass_simple_build(app: SphinxTestApp):
    app.build()
    assert (app.outdir / "_static" / "style.css").exists()


@pytest.mark.sphinx(
    "revealjs",
    testroot="sass",
    confoverrides={
        "revealjs_sass_auto_targets": True,
    },
)
def test_sass_auto_build(app: SphinxTestApp):
    app.build()
    assert (app.outdir / "_static" / "style2.css").exists()
