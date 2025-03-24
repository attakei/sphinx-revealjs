"""Test cases for generating giles."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx(
    "revealjs", testroot="for-config", confoverrides={"revealjs_use_index": True}
)
def test_generating_genindex(app: SphinxTestApp, status, warning):  # noqa
    app.build()
    assert (app.outdir / "genindex.html").exists()
