"""Test cases for comment block."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from testutils import soup_html

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("revealjs", testroot="for-commented-notes")
def test_ignore_comment_at_default_config(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    assert len(soup.find_all("aside")) == 0


@pytest.mark.sphinx(
    "revealjs",
    testroot="for-commented-notes",
    confoverrides={"revealjs_notes_from_comments": True},
)
def test_comment_as_notes(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    assert len(soup.find_all("aside")) == 1
