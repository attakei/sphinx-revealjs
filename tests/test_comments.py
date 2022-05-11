"""comment block."""
import pytest
from testutils import soup_html


@pytest.mark.sphinx("revealjs", testroot="misc")
def test_ignore_comment_at_default_config(app, status, warning):  # noqa
    soup = soup_html(app, "with_commented_notes.html")
    assert len(soup.find_all("aside")) == 0


@pytest.mark.sphinx(
    "revealjs", testroot="misc", confoverrides={"revealjs_notes_from_comments": True}
)
def test_comment_as_notes(app, status, warning):  # noqa
    soup = soup_html(app, "with_commented_notes.html")
    assert len(soup.find_all("aside")) == 1


@pytest.mark.sphinx("revealjs", testroot="misc")
def test_content_escape(app, status, warning):  # noqa
    soup = soup_html(app, "with_notes_include_html.html")
    assert len(soup.find_all("aside")) == 1
