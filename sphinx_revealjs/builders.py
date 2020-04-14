"""Definition for sphinx custom builder."""
from typing import Any, Dict, Tuple

from sphinx.builders.html import StandaloneHTMLBuilder

from sphinx_revealjs.directives import raw_json
from sphinx_revealjs.writers import RevealjsSlideTranslator

from .contexts import GoogleFonts, RevealjsPlugin, RevealjsProjectContext


def static_resource_uri(src: str, prefix: str = None) -> str:
    """Build static path of resource."""
    local_prefix = "_static" if prefix is None else prefix
    if src.startswith("http://") or src.startswith("https://"):
        return src
    return f"{local_prefix}/{src}"


class RevealjsHTMLBuilder(StandaloneHTMLBuilder):
    """Sphinx builder class to generate Reveal.js presentation HTML.

    This manage theme path and configure default options.
    """

    name = "revealjs"
    default_translator_class = RevealjsSlideTranslator

    def __init__(self, app):  # noqa: D107
        super().__init__(app)
        self.revealjs_slide = None
        self.css_files = [
            "_static/revealjs/css/reveal.css",
            "_static/revealjs/lib/css/zenburn.css",
        ]
        self.google_fonts = GoogleFonts()

    def init(self):  # noqa
        super().init()
        if hasattr(self.config, "revealjs_google_fonts"):
            self.google_fonts = self.google_fonts.extend(
                self.config.revealjs_google_fonts
            )
        # Create RevealjsProjectContext
        self.revealjs_context = RevealjsProjectContext(
            [
                static_resource_uri(src)
                for src in getattr(self.config, "revealjs_script_files", [])
            ],
            getattr(self.config, "revealjs_script_conf", None),
            [
                RevealjsPlugin(
                    static_resource_uri(plugin["src"]),
                    plugin.get("options", "{}").strip(),
                )
                for plugin in getattr(self.config, "revealjs_script_plugins", [])
            ],
        )

    def get_theme_config(self) -> Tuple[str, Dict]:
        """Find and return configuration about theme (name and option params).

        Find theme and merge options.
        """
        theme_name = getattr(self.config, "revealjs_theme", "sphinx_revealjs")
        theme_options = getattr(self.config, "revealjs_theme_options", {})
        config = raw_json(theme_options.get("revealjs_config", ""))
        theme_options["revealjs_config"] = config
        return theme_name, theme_options

    def get_doc_context(self, docname, body, metatags):
        """Return customized context.

        if source has ``revealjs_slide`` property, add configures.
        """
        ctx = super().get_doc_context(docname, body, metatags)
        if self.revealjs_slide:
            ctx["revealjs_slide"] = self.revealjs_slide.attributes
            ctx["revealjs_config"] = self.revealjs_slide.content
        ctx["revealjs"] = self.revealjs_context
        return ctx

    def update_page_context(
        self, pagename: str, templatename: str, ctx: Dict, event_arg: Any
    ) -> None:  # noqa
        # Injection Google Font css
        fonts = self.google_fonts
        if self.revealjs_slide and "google_font" in self.revealjs_slide.attributes:
            fonts = fonts.extend(
                self.revealjs_slide.attributes["google_font"].split(",")
            )
        ctx["google_fonts"] = fonts
        ctx["css_files"] = self.css_files + fonts.css_files
