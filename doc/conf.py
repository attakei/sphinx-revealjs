# -*- coding: utf-8 -*-
from pathlib import Path

from sphinx_revealjs import __version__

PROJ_ROOT = Path(__file__).parents[1]

# -- Project information -----------------------------------------------------
project = "sphinx-revealjs"
copyright = "2018, Kazuya Takei"
author = "Kazuya Takei"
version = __version__
release = __version__

# -- General configuration ---------------------------------------------------
extensions = [
    "atsphinx.footnotes",
    "atsphinx.htmx_boost",
    "oembedpy.adapters.sphinx",
    "rst_package_refs.sphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
language = "en"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = None
rst_prolog = """
.. |THIS| replace:: ``sphinx-revealjs``
"""

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

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

# -- Options for Linkcheck output
linkcheck_ignore = [
    r"./docs/migrations",  # TODO: Fix after.
    # TODO: Migrate ``linkcheck_anchors_ignore_for_url``
    r"https://attakei.github.io/sphinx-revealjs/en/#/5/1",
    r"https://revealjs.com/#/",
    r"https://revealjs.com/code/#line-numbers-%26-highlights",
]

# -- Extension configuration -------------------------------------------------
# For sphinx.ext.intersphinx
intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}
# For sphinx.ext.todo
todo_include_todos = True
# For atsphinx.htmx_boost
htmx_boost_preload = "mouseover"


def setup(app):
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )
