"""Build tests for configuration parameters."""
import pytest

from testutils import soup_html


class Test_BuildHtmlTests:  # noqa
    @pytest.mark.sphinx("revealjs", testroot="misc")
    def test_defaults(self, app, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        for e in soup.find_all("section"):
            assert "id" not in e.attrs

    @pytest.mark.sphinx(
        "revealjs",
        testroot="misc",
        freshenv=True,
        confoverrides={"revealjs_script_files": ["js/test.js"]},
    )
    def test_script_tags(self, app, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        elements = [
            e for e in soup.find_all("script") if e.get("src") == "_static/js/test.js"
        ]
        assert len(elements) == 1

    @pytest.mark.sphinx(
        "revealjs",
        testroot="misc",
        freshenv=True,
        confoverrides={"revealjs_google_fonts": ["Noto Sans JP"]},
    )
    def test_google_fonts(self, app, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        link = [
            e
            for e in soup.find_all("link", rel="stylesheet")
            if e["href"].startswith("https://fonts.googleapis.com/css2")
        ]
        assert len(link) == 1
        style = soup.find_all("style")[-1]
        assert ".reveal" in str(style)
        assert "Noto Sans JP" in str(style)
        assert "sans-serif;" in str(style)

    @pytest.mark.sphinx(
        "revealjs",
        testroot="misc",
        freshenv=True,
        confoverrides={
            "revealjs_google_fonts": ["Noto Sans JP"],
            "revealjs_generic_font": "cursive",
        },
    )
    def test_google_fonts_with_generic(self, app, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        link = [
            e
            for e in soup.find_all("link", rel="stylesheet")
            if e["href"].startswith("https://fonts.googleapi")
        ]
        assert len(link) == 1
        style = soup.find_all("style")[-1]
        assert "Noto Sans JP" in str(style)
        assert "cursive" in str(style)

    @pytest.mark.sphinx(
        "revealjs",
        testroot="misc",
        freshenv=True,
        confoverrides={"revealjs_generic_font": "cursive"},
    )
    def test_generic_font_only(self, app, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        styles = soup.find_all("style")
        assert len(styles) == 0

    @pytest.mark.sphinx(
        "revealjs",
        testroot="misc",
        freshenv=True,
        confoverrides={"revealjs_script_files": ["js/test.js"]},
    )
    def test_script_tags(self, app, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        elements = [
            e for e in soup.find_all("script") if e.get("src") == "_static/js/test.js"
        ]
        assert len(elements) == 1

    @pytest.mark.sphinx(
        "revealjs",
        testroot="misc",
        freshenv=True,
        confoverrides={"revealjs_script_files": ["https://example.com/test.js"]},
    )
    def test_script_tags_https(self, app, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        elements = [
            e
            for e in soup.find_all("script")
            if e.get("src") == "https://example.com/test.js"
        ]
        assert len(elements) == 1

    @pytest.mark.sphinx(
        "revealjs",
        testroot="misc",
        freshenv=True,
        confoverrides={"revealjs_script_conf": '{transition:"none"}'},
    )
    def test_revealjs_script_conf(self, app, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        assert 'Object.assign(revealjsConfig, {transition:"none"});' in str(
            soup.find_all("script")[-1]
        )

    @pytest.mark.sphinx(
        "revealjs",
        testroot="misc",
        freshenv=True,
        confoverrides={
            "revealjs_script_plugins": [
                {
                    "name": "RevealNotes",
                    "src": "revealjs4/plugin/notes/notes.js",
                }
            ]
        },
    )
    def test_revealjs_script_plugins(self, app, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        script = str(soup.find_all("script")[-1])
        assert "RevealNotes" in script
        for d in soup.find_all("script"):
            print(d)
        scripts = [d["src"] for d in soup.find_all("script") if "src" in d.attrs]
        assert "_static/revealjs4/plugin/notes/notes.js" in scripts

    @pytest.mark.sphinx(
        "revealjs",
        testroot="misc",
        freshenv=True,
        confoverrides={"revealjs_style_theme": "moon"},
    )
    def test_revealjs_style_theme_builtin(self, app, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        links = [
            e
            for e in soup.find_all("link", rel="stylesheet")
            if "_static/revealjs4/dist/theme/moon.css" in e["href"]
        ]
        assert len(links) == 1

    @pytest.mark.sphinx(
        "revealjs",
        testroot="misc",
        freshenv=True,
        confoverrides={"revealjs_style_theme": "custom.css"},
    )
    def test_revealjs_style_theme_custom(self, app, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        links = [
            e
            for e in soup.find_all("link", rel="stylesheet")
            if "_static/custom.css" in e["href"]
        ]
        assert len(links) == 1

    @pytest.mark.sphinx(
        "revealjs",
        testroot="misc",
        freshenv=True,
        confoverrides={"revealjs_css_files": ["https://example.com/example.css"]},
    )
    def test_revealjs_css_files(self, app, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        links = [
            e
            for e in soup.find_all("link", rel="stylesheet")
            if "https://example.com/example.css" in e["href"]
        ]
        assert len(links) == 1

    @pytest.mark.sphinx(
        "revealjs",
        testroot="misc",
        freshenv=True,
        confoverrides={
            "revealjs_static_path": ["_static"],
            "revealjs_css_files": ["custom.css"],
        },
    )
    def test_revealjs_css_files_local(self, app, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        links = [
            e
            for e in soup.find_all("link", rel="stylesheet")
            if "_static/custom.css" in e["href"]
        ]
        assert len(links) == 1
        assert (app.outdir / "_static/custom.css").exists()

    @pytest.mark.sphinx(
        "revealjs",
        testroot="misc",
        freshenv=True,
        confoverrides={
            "revealjs_static_path": ["_static"],
            "revealjs_css_files": ["custom.css"],
        },
    )
    def test_default_theme_css_comes_before_custom_css(self, app, status, warning):
        soup = soup_html(app, "index.html")
        stylesheet_href_list = [
            e["href"] for e in soup.find_all("link", rel="stylesheet")
        ]
        default_theme_index = stylesheet_href_list.index(
            "_static/revealjs4/dist/theme/black.css"
        )
        custom_css_index = stylesheet_href_list.index("_static/custom.css")
        assert default_theme_index < custom_css_index

    @pytest.mark.sphinx(
        "revealjs",
        testroot="misc",
        freshenv=True,
        confoverrides={
            "revealjs_style_theme": "moon",
            "revealjs_static_path": ["_static"],
            "revealjs_css_files": ["other_custom.css"],
        },
    )
    def test_specified_theme_css_comes_before_custom_css(self, app, status, warning):
        soup = soup_html(app, "index.html")
        stylesheet_href_list = [
            e["href"] for e in soup.find_all("link", rel="stylesheet")
        ]
        specified_theme_index = stylesheet_href_list.index(
            "_static/revealjs4/dist/theme/moon.css"
        )
        custom_css_index = stylesheet_href_list.index("_static/other_custom.css")
        assert specified_theme_index < custom_css_index

    @pytest.mark.sphinx(
        "revealjs",
        testroot="misc",
        freshenv=True,
        confoverrides={
            "revealjs_use_section_ids": True,
        },
    )
    def test_inject_id_to_all_sections(self, app, status, warning):  # noqa
        soup = soup_html(app, "index.html")
        for e in soup.find_all("section"):
            children = set([c.name for c in e.children])
            if children & {"h1", "h2", "h3"}:
                assert "id" in e.attrs

    @pytest.mark.sphinx(
        "revealjs",
        testroot="misc",
        freshenv=True,
        confoverrides={
            "revealjs_use_section_ids": True,
        },
    )
    def test_inject_id_to_all_sections_with_label(self, app, status, warning):  # noqa
        soup = soup_html(app, "with_label.html")
        h2_section = soup.h2.parent
        assert "id" in h2_section.attrs
        assert h2_section["id"] == "override-label"
