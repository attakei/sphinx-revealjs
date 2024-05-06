"""Configuration is cases for default behavior."""

extensions = [
    "sphinx_revealjs",
]

# To skip toctree
rst_prolog = """
:orphan:
"""

revealjs_html_theme = "revealjs-simple"


def setup(app):
    def _html_page_context(app, pagename, templatename, context, doctree):
        metatags = context.get("metatags", "")
        metatags += "<style></style>"
        context["metatags"] = metatags

    app.connect("html-page-context", _html_page_context)
