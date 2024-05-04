from pathlib import Path

import pytest
from sphinx.testing.fixtures import SphinxTestApp
from sphinx.util.docutils import nodes

from sphinx_revealjs import transforms

here = Path(__file__).parent


@pytest.mark.parametrize("docname,cnt_before,cnt_after", [("index", 7, 10)])
@pytest.mark.sphinx("html", testroot="dummy")
def test__remap_sections(
    app: SphinxTestApp, docname: str, cnt_before: int, cnt_after: int
):
    app.builder.read()
    doctree = app.env.get_doctree(docname)
    assert len(list(doctree.findall(nodes.section))) == cnt_before
    doctree = transforms.remap_sections(doctree)
    assert len(list(doctree.findall(nodes.section))) == cnt_after
