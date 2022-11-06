"""Test cases for comment block."""
import pytest
from sphinx.testing.util import SphinxTestApp
from testutils import soup_html


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
