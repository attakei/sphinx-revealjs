"""Build tests for core behaviors of presentation(sections)."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from testutils import soup_html

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("revealjs", testroot="default")
def test_valid_html(app: SphinxTestApp):  # noqa
    app.build()
    content = (app.outdir / "index.html").read_text()
    assert content.count("<section >") == content.count("</section>")
    content = (app.outdir / "simple.html").read_text()
    assert content.count("<section >") == content.count("</section>")


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
    section = main.find_all("section", recursive=False)[1]
    assert len(section.find_all("section", recursive=False)) == 3


@pytest.mark.sphinx("revealjs", testroot="default")
def test_lv4_section(app, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    h4 = soup.h4
    assert h4 is not None
    # Lv4 content is sibling pf Lv3 content (not splitted as other slides)
    assert h4.parent.h3 is not None
