"""Build tests for writing directives."""
import pytest
from testutils import soup_html


@pytest.mark.sphinx("revealjs", testroot="misc")
def test_write_to_aside_by_revealjs(app, status, warning):  # noqa
    soup = soup_html(app, "with_notes.html")
    notes = soup.find_all("aside", {"class": "notes"})
    assert len(notes) == 1


@pytest.mark.sphinx("dirrevealjs", testroot="misc")
def test_write_to_aside_by_dirrevealjs(app, status, warning):  # noqa
    soup = soup_html(app, "with_notes/index.html")
    notes = soup.find_all("aside", {"class": "notes"})
    assert len(notes) == 1


@pytest.mark.sphinx("html", testroot="misc")
def test_no_out_by_html(app, status, warning):  # noqa
    soup = soup_html(app, "with_notes.html")
    notes = soup.find_all("aside", {"class": "notes"})
    assert len(notes) == 0
