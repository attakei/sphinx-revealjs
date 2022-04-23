"""Build tests for writing directives."""
import pytest
from testutils import soup_html


@pytest.mark.sphinx("revealjs", testroot="misc")
def test_write_to_aside_by_revealjs(app, status, warning):  # noqa
    soup = soup_html(app, "with_notes.html")
    notes = soup.find_all("aside", {"class": "notes"})
    assert len(notes) == 1
    assert len(notes[0]) == 1


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


@pytest.mark.sphinx(
    "revealjs", testroot="misc", confoverrides={"revealjs_notes_from_comments": True}
)
def test_write_with_comments(app, status, warning):  # noqa
    soup = soup_html(app, "with_notes.html")
    notes = soup.find_all("aside", {"class": "notes"})
    assert len(notes) == 2
