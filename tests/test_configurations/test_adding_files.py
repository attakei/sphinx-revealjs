"""Build tests for configuration parameters."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from testutils import soup_html

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


class TestForRevealjsCssFiles:  # noqa
    @pytest.mark.sphinx(
        "revealjs",
        testroot="for-config",
        confoverrides={"revealjs_css_files": ["https://example.com/example.css"]},
    )
    def test_url(self, app: SphinxTestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        links = [
            e
            for e in soup.find_all("link", rel="stylesheet")
            if "https://example.com/example.css" in e["href"]
        ]
        assert len(links) == 1

    @pytest.mark.sphinx(
        "revealjs",
        testroot="for-config",
        confoverrides={
            "revealjs_static_path": ["_static"],
            "revealjs_css_files": ["custom.css"],
        },
    )
    def test_localfile(self, app: SphinxTestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        links = [
            e
            for e in soup.find_all("link", rel="stylesheet")
            if "_static/custom.css" in e["href"]
        ]
        assert len(links) == 1
        assert (app.outdir / "_static/custom.css").exists()


class TestForRevealjsJsFiles:  # noqa
    @pytest.mark.sphinx(
        "revealjs",
        testroot="for-config",
        confoverrides={
            "revealjs_js_files": [
                "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.7/dayjs.min.js"
            ]
        },
    )
    def test_revealjs_js_files(self, app: SphinxTestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        elm = soup.find(
            "script",
            src="https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.7/dayjs.min.js",
        )
        assert elm is not None


# TODO: Unsupport 2.x (keep until 3.x)
@pytest.mark.sphinx(
    "revealjs",
    testroot="for-config",
    confoverrides={
        "html_js_files": [
            "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.7/dayjs.min.js"
        ]
    },
)
def test_unuse_html_js_files(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    elm = soup.find(
        "script", src="https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.7/dayjs.min.js"
    )
    assert elm is None
    assert soup.find("script", src="_static/jquery.js") is None
    assert soup.find("script", src="_static/underscore.js") is None
