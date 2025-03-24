"""Build tests for configuration parameters."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from testutils import soup_html

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx(
    "revealjs",
    testroot="for-config",
    confoverrides={
        "revealjs_use_section_ids": True,
    },
)
def test_inject_id_to_all_sections(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    for e in soup.find_all("section"):
        children = {c.name for c in e.children}
        if children & {"h1", "h2", "h3"}:
            assert "id" in e.attrs


@pytest.mark.sphinx(
    "revealjs",
    testroot="for-config",
    confoverrides={
        "revealjs_use_section_ids": True,
    },
)
def test_inject_id_to_all_sections_with_label(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-label.html")
    h2_section = soup.h2.parent
    assert "id" in h2_section.attrs
    assert h2_section["id"] == "override-label"
