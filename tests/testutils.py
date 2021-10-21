"""Test support functions."""
from typing import AnyStr

from bs4 import BeautifulSoup
from sphinx.testing.util import SphinxTestApp


def soup_html(app: SphinxTestApp, path: str) -> BeautifulSoup:
    """Build application and parse content."""
    app.build()
    html: AnyStr = (app.outdir / path).read_text()
    return BeautifulSoup(html, "html.parser")
