"""Build tests for core behaviors of presentation(sections)."""
import pytest
from sphinx.testing.util import SphinxTestApp
from testutils import soup_html


@pytest.mark.sphinx("revealjs", testroot="default")
def test_render_title(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    assert soup.h1.text == "Test presentation"


@pytest.mark.sphinx("revealjs", testroot="default")
def test_count_horizontal_sections(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    main = soup.find("div", {"role": "main"})
    assert len(main.find_all("section", recursive=False)) == 3


@pytest.mark.sphinx("revealjs", testroot="default")
def test_count_vertical_sections(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    main = soup.find("div", {"role": "main"})
    section = main.find_all("section", reccursive=False)[1]
    assert len(section.find_all("section", recursive=False)) == 3
