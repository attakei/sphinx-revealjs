"""Test cases for ``revealjs_slide`` directive."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from testutils import soup_html

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("revealjs", testroot="default")
def test_override_theme(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-slide/has-theme.html")
    css_hrefs = [elm["href"] for elm in soup.find_all("link", rel="stylesheet")]
    assert "../_static/custom.css" in css_hrefs


@pytest.mark.sphinx("revealjs", testroot="default")
def test_config(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-slide/has-conf.html")
    assert 'Object.assign(revealjsConfig, {"transition": "none"});' in str(
        soup.find_all("script")[-1]
    )


@pytest.mark.sphinx("revealjs", testroot="default")
def test_config_as_content(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "with-revealjs-slide/has-content.html")
    assert "Object.assign(revealjsConfig, {\n" in str(soup.find_all("script")[-1])
    assert '"transition": "none"\n' in str(soup.find_all("script")[-1])
    assert "});" in str(soup.find_all("script")[-1])
