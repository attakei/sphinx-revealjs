"""Test cases for sphix_revealjs.ext.design."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx(
    "revealjs",
    testroot="default",
    confoverrides={
        "extensions": ["sphinx_revealjs", "sphinx_revealjs.ext.design"],
    },
)
def test_build(app: SphinxTestApp, status, warning):  # noqa
    app.build()
