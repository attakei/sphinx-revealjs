"""Test cases for deprecated messages from Sphinx."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("revealjs", testroot="default")
@pytest.mark.skipif(
    sys.version_info.major == 3 and sys.version_info.minor >= 7,
    reason="Run only deprecated python version",
)
def test_not_notice(app: SphinxTestApp, status, warning, capsys):  # noqa
    app.build()
    # Left is return warning text if exists.
    assert warning.getvalue() != ""
