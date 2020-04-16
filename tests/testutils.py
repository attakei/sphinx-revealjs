"""Test supprto functions."""
from pathlib import Path
from typing import AnyStr

from bs4 import BeautifulSoup
from sphinx_testing import TestApp

TEST_ROOT = Path(__file__).parent

PROJECT_ROOT = TEST_ROOT.parent


def gen_app_conf(**kwargs: dict) -> dict:
    """Create TestApp configuration."""
    kwargs["buildername"] = "revealjs"
    kwargs["srcdir"] = str(TEST_ROOT / "testdocs")
    kwargs["copy_srcdir_to_tmpdir"] = True
    return kwargs


def soup_html(app: TestApp, path: str) -> BeautifulSoup:
    """Build application and parse content."""
    app.build()
    html: AnyStr = (app.outdir / path).read_text()
    return BeautifulSoup(html, "html.parser")
