"""Configuration is cases for default behavior."""

extensions = [
    "sphinx_revealjs",
    "sphinx_revealjs.ext.sass",
]

# To skip toctree
rst_prolog = """
:orphan:
"""

revealjs_static_path = ["_static"]
revealjs_sass_src_dir = "_static"
revealjs_sass_out_dir = "_static"
