from pathlib import Path

import pytest
from sphinx.testing.fixtures import SphinxTestApp
from sphinx.util.docutils import nodes

from sphinx_revealjs import directives
from sphinx_revealjs import nodes as rj_nodes
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


@pytest.mark.sphinx("html", testroot="dummy")
class TestFor_append_section_attributes:
    @pytest.fixture(autouse=True)
    def _fixture(self, app: SphinxTestApp):
        self._app = app
        self._app.add_directive("revealjs-section", directives.RevealjsSection)
        self._app.builder.read()

    def get_doctree(self, docname: str) -> nodes.document:
        return transforms.remap_sections(self._app.env.get_doctree(docname))

    def test__index(self):
        doctree = self.get_doctree("index")
        assert len(list(doctree.findall(rj_nodes.revealjs_section))) == 0
        doctree = transforms.append_section_attributes(doctree)
        assert len(list(doctree.findall(rj_nodes.revealjs_section))) == 0

    def test__has_revealjs_section(self):
        doctree = self.get_doctree("with-revealjs-section")
        assert len(list(doctree.findall(rj_nodes.revealjs_section))) == 2
        doctree = transforms.append_section_attributes(doctree)
        assert len(list(doctree.findall(rj_nodes.revealjs_section))) == 0
        assert "revealjs" in doctree.children[0].children[0].attributes


@pytest.mark.sphinx("html", testroot="dummy")
class TestFor_append_vertical_attributes:
    @pytest.fixture(autouse=True)
    def _fixture(self, app: SphinxTestApp):
        self._app = app
        self._app.add_directive("revealjs-section", directives.RevealjsSection)
        self._app.add_directive("revealjs-vertical", directives.RevealjsVertical)
        self._app.builder.read()

    def get_doctree(self, docname: str) -> nodes.document:
        return transforms.remap_sections(self._app.env.get_doctree(docname))

    def test__index(self):
        doctree = self.get_doctree("index")
        assert len(list(doctree.findall(rj_nodes.revealjs_vertical))) == 0
        doctree = transforms.append_vertical_attributes(doctree)
        assert len(list(doctree.findall(rj_nodes.revealjs_vertical))) == 0

    def test__has_revealjs_vertical(self):
        doctree = self.get_doctree("with-revealjs-vertical-1")
        assert len(list(doctree.findall(rj_nodes.revealjs_vertical))) == 1
        doctree = transforms.append_vertical_attributes(doctree)
        assert len(list(doctree.findall(rj_nodes.revealjs_vertical))) == 0
        assert "revealjs" in doctree.children[0].attributes
        assert "revealjs" not in doctree.children[0].children[0].attributes


@pytest.mark.sphinx("html", testroot="dummy")
class TestFor_break_sections:
    @pytest.fixture(autouse=True)
    def _fixture(self, app: SphinxTestApp):
        self._app = app
        self._app.add_directive("revealjs-break", directives.RevealjsBreak)
        self._app.builder.read()

    def get_doctree(self, docname: str) -> nodes.document:
        return transforms.remap_sections(self._app.env.get_doctree(docname))

    def test__index(self):
        doctree = self.get_doctree("index")
        assert len(list(doctree.findall(rj_nodes.revealjs_break))) == 0
        doctree = transforms.break_sections(doctree)
        assert len(list(doctree.findall(rj_nodes.revealjs_break))) == 0

    def test__on_top(self):
        doctree = self.get_doctree("with-revealjs-break-top")
        assert len(list(doctree.findall(rj_nodes.revealjs_break))) == 1
        doctree = transforms.break_sections(doctree)
        assert len(list(doctree.findall(rj_nodes.revealjs_break))) == 0
        assert len(doctree.children[0].children) == 2

    def test__single(self):
        doctree = self.get_doctree("with-revealjs-break")
        assert len(list(doctree.findall(rj_nodes.revealjs_break))) == 1
        doctree = transforms.break_sections(doctree)
        assert len(list(doctree.findall(rj_nodes.revealjs_break))) == 0
        assert len(doctree.children[1].children) == 3
        assert len(list(doctree.children[1].children[-1].findall(nodes.title))) == 1

    def test__chain(self):
        doctree = self.get_doctree("with-revealjs-break-chain")
        assert len(list(doctree.findall(rj_nodes.revealjs_break))) == 2
        doctree = transforms.break_sections(doctree)
        assert len(list(doctree.findall(rj_nodes.revealjs_break))) == 0
        assert len(doctree.children[1].children) == 4
        assert doctree.children[1].children[1].astext() == "Head\n\ncontent 1"
        assert doctree.children[1].children[3].astext() == "content 3"
        # For attributes_str
        assert "revealjs" not in doctree.children[1].children[0].attributes
        assert "revealjs" in doctree.children[1].children[2].attributes
        assert "revealjs" in doctree.children[1].children[3].attributes
        assert doctree.children[1].children[3].attributes["revealjs"] == ""
        # For notitle
        assert not list(doctree.children[1].children[3].findall(nodes.title))
