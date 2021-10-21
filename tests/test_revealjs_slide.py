"""Test cases for ``revealjs_slide`` directive."""
import pytest

from testutils import soup_html


@pytest.mark.sphinx("revealjs", testroot="misc")
def test_override_theme(app, status, warning):  # noqa
    soup = soup_html(app, "with_theme.html")
    css_hrefs = [elm["href"] for elm in soup.find_all("link", rel="stylesheet")]
    assert "_static/custom.css" in css_hrefs


@pytest.mark.sphinx("revealjs", testroot="misc")
def test_override_font(app, status, warning):  # noqa
    soup = soup_html(app, "with_googlefont.html")
    css_hrefs = [
        elm["href"]
        for elm in soup.find_all("link", rel="stylesheet")
        if elm["href"].startswith("https://fonts.googleapis.com")
    ]
    assert len(css_hrefs) == 1
    styles = "\n".join([str(e) for e in soup.find_all("style")])
    assert "'M PLUS 1p'" in styles


@pytest.mark.sphinx("revealjs", testroot="misc")
def test_config(app, status, warning):  # noqa
    soup = soup_html(app, "with_conf.html")
    assert 'Object.assign(revealjsConfig, {"transition": "none"});' in str(
        soup.find_all("script")[-1]
    )


@pytest.mark.sphinx("revealjs", testroot="misc")
def test_config_as_content(app, status, warning):  # noqa
    soup = soup_html(app, "with_conf_content.html")
    assert "Object.assign(revealjsConfig, {\n" in str(soup.find_all("script")[-1])
    assert '"transition": "none"\n' in str(soup.find_all("script")[-1])
    assert "});" in str(soup.find_all("script")[-1])
