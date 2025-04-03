"""Test cases for ``revealjs-break`` directive."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from testutils import soup_html

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("revealjs", testroot="default")
def test_on_revealjs_builder(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-break.html")
    section_tag = soup.h2.parent.parent
    assert len(section_tag.find_all("section")) == 3
    # title, content1, content2 (splitted)


@pytest.mark.sphinx("revealjs", testroot="default")
def test_top_of_section(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-break-top.html")
    section_tag = soup.h1.parent.parent
    print(section_tag)
    assert len(section_tag.find_all("section")) == 2


@pytest.mark.sphinx("revealjs", testroot="default")
def test_render_all_items_of_head(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-break-decorated.html")
    head = soup.find_all("h3")[-1]
    assert head.text == "Decorated Head"
