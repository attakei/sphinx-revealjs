"""Configuration for testing revealjs-float extension."""

extensions = [
    "sphinx_revealjs",
    "sphinx_revealjs.ext.float",
]

# To skip toctree
rst_prolog = """
:orphan:
"""
