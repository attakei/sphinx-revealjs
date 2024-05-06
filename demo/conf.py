# -*- coding: utf-8 -*-

# -- Path setup --------------------------------------------------------------
import os
from urllib.parse import urljoin

from sphinx_revealjs.utils import get_revealjs_path

# -- Project information -----------------------------------------------------
project = "sphinx-revealjs"
copyright = "2018, Kazuya Takei"
author = "Kazuya Takei"
version = ""
release = "2018.10"

# -- General configuration ---------------------------------------------------
extensions = [
    "atsphinx.mini18n",
    "oembedpy.ext.sphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx_revealjs",
    "sphinx_revealjs.ext.footnotes",
    "sphinx_revealjs.ext.screenshot",
    "sphinxcontrib.budoux",
    "sphinxcontrib.gtagjs",
    "sphinxcontrib.sass",
    "sphinxext.opengraph",
]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
language = "en"
locale_dirs = ["_locales"]
exclude_patterns = [".venv", "_build", "Thumbs.db", ".DS_Store", "_sections"]
pygments_style = None

# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"
html_static_path = ["_static"]

# -- Options for Reveal.js output ---------------------------------------------
revealjs_html_theme = "revealjs-simple"
revealjs_static_path = ["_static"]
revealjs_style_theme = "custom.css"
revealjs_script_conf = {
    "controls": True,
    "progress": True,
    "hash": True,
    "center": True,
    "transition": "slide",
    "customcontrols": {
        "controls": [
            {
                "icon": "EN",
                "action": "location.href = '/en/';",
            },
            {
                "icon": "JA",
                "action": "location.href = '/ja/';",
            },
        ]
    },
}
revealjs_script_plugins = [
    {
        "name": "RevealNotes",
        "src": "revealjs/plugin/notes/notes.js",
    },
    {
        "name": "RevealHighlight",
        "src": "revealjs/plugin/highlight/highlight.js",
    },
    {
        "name": "RevealMath",
        "src": "revealjs/plugin/math/math.js",
    },
    {
        "name": "RevealCustomControls",
        "src": "https://cdn.jsdelivr.net/npm/reveal.js-plugins@latest/customcontrols/plugin.js",
    },
]
revealjs_css_files = [
    "revealjs/plugin/highlight/zenburn.css",
    "https://cdn.jsdelivr.net/npm/reveal.js-plugins@latest/customcontrols/style.css",
]
revealjs_notes_from_comments = True

# -- Options for extensions --------------------------------------------------
# - sphinx.ext.todo
todo_include_todos = True
# - sphinxcontrib.gtagjs
if "GTAGJS_IDS" in os.environ:
    gtagjs_ids = os.environ["GTAGJS_IDS"].split(",")
# - sphinxcontrib.budoux
budoux_targets = ["h1", "h2", "h3"]
# - sphinxcontrib.sass
sass_src_dir = "_sass"
sass_out_dir = "_static"
sass_targets = {"custom.scss": "custom.css"}
sass_include_paths = [
    get_revealjs_path() / "css" / "theme",
]
# sphinxext.opengraph
ogp_site_url = os.environ.get("DEMO_URL_BASE", "http://localhost:8000/")
ogp_custom_meta_tags = [
    '<meta name="twitter:card" content="summary_large_image" />',
    '<meta name="twitter:site" content="@attakei" />',
]

# atsphinx-mini18n
mini18n_default_language = "en"
mini18n_support_languages = ["en", "ja"]
mini18n_basepath = "/sphinx-revealjs/"


def update_ogp(app, config):
    print(config.ogp_site_url, config.language)
    config.ogp_site_url = urljoin(config.ogp_site_url, f"{config.language}/")


def _add_navigation_for_mini18n(app, config):
    config.revealjs_script_conf["customcontrols"] = {
        "controls": [
            {
                "icon": lang.upper(),
                "action": f"location.href = '{config.mini18n_basepath}{lang}/';",
            }
            for lang in config.mini18n_support_languages
        ]
    }


def setup(app):
    app.connect("config-inited", update_ogp)
    app.connect("config-inited", _add_navigation_for_mini18n)
