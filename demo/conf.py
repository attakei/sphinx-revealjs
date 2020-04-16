# -*- coding: utf-8 -*-

# -- Path setup --------------------------------------------------------------
import os

# -- Project information -----------------------------------------------------
project = "sphinx-revealjs"
copyright = "2018, Kazuya Takei"
author = "Kazuya Takei"
version = ""
release = "2018.10"

# -- General configuration ---------------------------------------------------
extensions = ["sphinx_revealjs", "sphinxcontrib.gtagjs"]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
language = None
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = None

# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"
html_theme_options = {
    "revealjs_theme": "league",
}
html_static_path = ["_static"]

# -- Options for Reveal.js output ---------------------------------------------
revealjs_style_theme = "black"
revealjs_script_conf = """
    {
        controls: true,
        progress: true,
        history: true,
        center: true,
        transition: "slide",
    }
"""
revealjs_script_plugins = [
    {
        "src": "revealjs/plugin/notes/notes.js",
        "options": "{async: true}",
    },
    {
        "src": "revealjs/plugin/highlight/highlight.js",
        "options": "{async: true, callback: function() { hljs.initHighlightingOnLoad(); }}",
    },
]

# -- Options for HTMLHelp output ---------------------------------------------
htmlhelp_basename = "sphinx-revealjsdoc"

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {}
latex_documents = [
    (
        master_doc,
        "sphinx-revealjs.tex",
        "sphinx-revealjs Documentation",
        "Kazuya Takei",
        "manual",
    ),
]

# -- Options for manual page output ------------------------------------------
man_pages = [
    (master_doc, "sphinx-revealjs", "sphinx-revealjs Documentation", [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------
texinfo_documents = [
    (
        master_doc,
        "sphinx-revealjs",
        "sphinx-revealjs Documentation",
        author,
        "sphinx-revealjs",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# -- Options for Epub output -------------------------------------------------
epub_title = project
epub_exclude_files = ["search.html"]

# -- Options for extensions --------------------------------------------------
if "GTAGJS_IDS" in os.environ:
    gtagjs_ids = os.environ["GTAGJS_IDS"].split(",")
