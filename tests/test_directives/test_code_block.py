"""Test cases for ``revealjs-code-block`` directive."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from testutils import soup_html

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("revealjs", testroot="default")
def test_inherit_code_block(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-code-block.html")
    code_tag = soup.find_all("code")[0]
    assert "python" in code_tag.attrs["class"]


@pytest.mark.sphinx("revealjs", testroot="default")
def test_dataline(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-code-block.html")
    code_tag = soup.find_all("code")[1]
    assert "php" in code_tag.attrs["class"]
    assert "data-line-numbers" in code_tag.attrs


@pytest.mark.sphinx("revealjs", testroot="default")
def test_dataline_start_from(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-code-block.html")
    code_tag = soup.find_all("code")[2]
    assert "toml" in code_tag.attrs["class"]
    assert "data-line-numbers" in code_tag.attrs
    assert code_tag.attrs["data-ln-start-from"] == "5"
