"""Test cases for builtin theme."""
from urllib.parse import urlparse

import pytest
from sphinx.testing.util import SphinxTestApp
from testutils import soup_html


@pytest.mark.sphinx("revealjs", testroot="default")
def test_has_revealcss(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    reveal_css = [
        d
        for d in soup.find_all("link", rel="stylesheet")
        if urlparse(d["href"]).path.endswith("dist/reveal.css")
    ]
    assert len(reveal_css) == 1


@pytest.mark.sphinx("revealjs", testroot="default")
def test_script_conf(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    script = soup.find_all("script")[-1]
    assert "Reveal.initialize(revealjsConfig);" in str(script)


@pytest.mark.sphinx("revealjs", testroot="default")
def test_script_sources(app, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    scripts = [s["src"] for s in soup.find_all("script") if "src" in s.attrs]
    assert "_static/revealjs4/dist/reveal.js" in scripts


@pytest.mark.sphinx("revealjs", testroot="default")
def test_stylesheet(app, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    links = [link["href"] for link in soup.find_all("link", rel="stylesheet")]
    assert "_static/revealjs4/dist/theme/black.css" in links
