"""Integration tests by demo/revealjs4."""
from pathlib import Path

import pytest
from sphinx.testing.util import SphinxTestApp
from testutils import soup_html

PROJECT_ROOT = Path(__file__).parent.parent


@pytest.mark.sphinx("revealjs", testroot=PROJECT_ROOT / "demo/revealjs4")
def test_has_revealcss(app, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    reveal_css = [
        d
        for d in soup.find_all("link", rel="stylesheet")
        if d["href"].endswith("revealjs4/dist/reveal.css")
    ]
    assert len(reveal_css) == 1


@pytest.mark.sphinx("revealjs", testroot=PROJECT_ROOT / "demo/revealjs4")
def test_pdfcss_not_exists(app, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    assert "print/pdf.css" not in str(soup)
    assert "print/paper.css" not in str(soup)


@pytest.mark.sphinx("revealjs", testroot=PROJECT_ROOT / "demo/revealjs4")
def test_refs_all_exists(app, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    google_fonts = [
        d
        for d in soup.find_all("link", rel="stylesheet")
        if d["href"].startswith("https://fonts.googleapis.com")
    ]
    assert len(google_fonts) == 1


@pytest.mark.sphinx("revealjs", testroot=PROJECT_ROOT / "demo/revealjs4")
def test_script_conf(app, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    script = soup.find_all("script")[-1]
    assert "Reveal.initialize(revealjsConfig);" in str(script)


@pytest.mark.sphinx("revealjs", testroot=PROJECT_ROOT / "demo/revealjs4")
def test_script_sources(app, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    scripts = [s["src"] for s in soup.find_all("script") if "src" in s.attrs]
    assert "_static/revealjs4/dist/reveal.js" in scripts


@pytest.mark.sphinx("revealjs", testroot=PROJECT_ROOT / "demo/revealjs4")
def test_stylesheet(app, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    links = [link["href"] for link in soup.find_all("link", rel="stylesheet")]
    assert "_static/revealjs4/dist/theme/black.css" in links


@pytest.mark.sphinx("revealjs", testroot=PROJECT_ROOT / "demo/revealjs4")
def test_title(app, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    assert "sphinx-revealjs" == soup.title.string


@pytest.mark.sphinx("revealjs", testroot=PROJECT_ROOT / "demo/revealjs4")
def test_has_highlightjs_theme(app, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    links = [
        d
        for d in soup.find_all("link", rel="stylesheet")
        if d["href"].endswith("revealjs4/plugin/highlight/zenburn.css")
    ]
    assert len(links) == 1


@pytest.mark.sphinx("revealjs", testroot=PROJECT_ROOT / "demo/revealjs4")
def test_plugin_loaded(app, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    assert "RevealNotes,RevealHighlight" in str(soup)


@pytest.mark.sphinx("dirrevealjs", testroot=PROJECT_ROOT / "demo/revealjs4")
def test_dirrevealjs(app: SphinxTestApp, status, warning):  # noqa
    app.build()
    assert Path(app.outdir / "index.html").exists()
    assert not Path(app.outdir / "example-background-only-section.html").exists()
    assert Path(app.outdir / "example-background-only-section/index.html").exists()
