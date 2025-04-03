"""Test cases for ``revealjs-notes`` directive."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from testutils import soup_html

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("revealjs", testroot="default")
def test_simple_notes(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-notes/simple.html")
    assert len(soup.find_all("aside")) == 1
    notes = soup.find_all("aside", {"class": "notes"})
    assert len(notes) == 1
    assert len(notes[0]) == 1


@pytest.mark.sphinx("revealjs", testroot="default")
def test_html_included_notes(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-notes/has-html.html")
    assert len(soup.find_all("aside")) == 1
    notes = soup.find_all("aside", {"class": "notes"})
    assert len(notes) == 1
    assert len(notes[0]) == 1


@pytest.mark.sphinx("html", testroot="default")
def test_no_out_by_html(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-notes/simple.html")
    notes = soup.find_all("aside", {"class": "notes"})
    assert len(notes) == 0
