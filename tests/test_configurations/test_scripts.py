"""Build tests for configuration parameters."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from testutils import soup_html

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


class TestForRevealjsScriptFiles:  # noqa
    @pytest.mark.sphinx(
        "revealjs",
        testroot="for-config",
        freshenv=True,
        confoverrides={"revealjs_script_files": ["js/test.js"]},
    )
    def test_adding_localfile(self, app: SphinxTestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        elements = [
            e for e in soup.find_all("script") if e.get("src") == "_static/js/test.js"
        ]
        assert len(elements) == 1

    @pytest.mark.sphinx(
        "revealjs",
        testroot="for-config",
        freshenv=True,
        confoverrides={"revealjs_script_files": ["https://example.com/test.js"]},
    )
    def test_adding_url(self, app: SphinxTestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        elements = [
            e
            for e in soup.find_all("script")
            if e.get("src") == "https://example.com/test.js"
        ]
        assert len(elements) == 1


class TestForRevealjsScriptConfig:  # noqa
    @pytest.mark.sphinx(
        "revealjs",
        testroot="for-config",
        confoverrides={"revealjs_script_conf": '{transition:"none"}'},
    )
    def test_using_as_text(self, app: SphinxTestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        assert 'Object.assign(revealjsConfig, {transition:"none"});' in str(
            soup.find_all("script")[-1]
        )

    @pytest.mark.sphinx(
        "revealjs",
        testroot="for-config",
        confoverrides={"revealjs_script_conf": {"transition": "none"}},
    )
    def test_using_as_dict(self, app: SphinxTestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        assert (
            'Object.assign(revealjsConfig, {"transition": "none", "scrollActivationWidth": null});'  # noqa: E501
            in str(soup.find_all("script")[-1])
        )

    @pytest.mark.sphinx(
        "revealjs",
        testroot="for-config",
    )
    def test_not_use(self, app: SphinxTestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        assert 'Object.assign(revealjsConfig, {"scrollActivationWidth": null});' in str(
            soup.find_all("script")[-1]
        )

    @pytest.mark.sphinx(
        "revealjs",
        testroot="for-config",
        confoverrides={"revealjs_script_conf": {"param": "This is 'one'"}},
    )
    def test_with_quotes(self, app: SphinxTestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        assert (
            'Object.assign(revealjsConfig, {"param": "This is \'one\'", "scrollActivationWidth": null});'  # noqa: E501
            in str(soup.find_all("script")[-1])
        )

    @pytest.mark.sphinx(
        "revealjs",
        testroot="for-config",
        confoverrides={"revealjs_script_conf": {"param": 'This is "one"'}},
    )
    def test_with_double_quotes(self, app: SphinxTestApp, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        assert (
            r'Object.assign(revealjsConfig, {"param": "This is \"one\"", "scrollActivationWidth": null});'  # noqa: E501
            in str(soup.find_all("script")[-1])
        )


@pytest.mark.sphinx(
    "revealjs",
    testroot="for-config",
    confoverrides={
        "revealjs_script_plugins": [
            {
                "name": "RevealNotes",
                "src": "revealjs/plugin/notes/notes.js",
            }
        ]
    },
)
def test_revealjs_script_plugins(app: SphinxTestApp, status, warning):  # noqa
    soup = soup_html(app, "index.html")
    script = str(soup.find_all("script")[-1])
    assert "RevealNotes" in script
    for d in soup.find_all("script"):
        print(d)
    scripts = [d["src"] for d in soup.find_all("script") if "src" in d.attrs]
    assert "_static/revealjs/plugin/notes/notes.js" in scripts
    assert "RevealNotes" in str(soup)
