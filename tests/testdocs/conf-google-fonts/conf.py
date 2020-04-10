# -*- coding: utf-8 -*-

# -- Project information -----------------------------------------------------

project = "Test docs for sphinx-revealjs"
copyright = "2018, Kazuya Takei"
author = "Kazuya Takei"

version = ""
release = ""
extensions = [
    "sphinx_revealjs",
]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

language = None

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

pygments_style = None

revealjs_theme_options = {
    "google_font": "Noto Sans JP",
    "revealjs_config": '{"transition":"none"}',
}
