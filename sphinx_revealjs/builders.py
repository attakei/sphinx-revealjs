"""Definition for sphinx custom builder."""
import copy
from typing import Any, Dict, List, Tuple

from sphinx.builders.html import StandaloneHTMLBuilder

from sphinx_revealjs.directives import raw_json
from sphinx_revealjs.writers import RevealjsSlideTranslator

from .contexts import GoogleFonts, RevealjsPlugin, RevealjsProjectContext
from .utils import static_resource_uri


class RevealjsHTMLBuilder(StandaloneHTMLBuilder):
    """Sphinx builder class to generate Reveal.js presentation HTML.

    This manage theme path and configure default options.
    """

    name = "revealjs"
    default_translator_class = RevealjsSlideTranslator

    def __init__(self, app):  # noqa: D107
        super().__init__(app)
        self.revealjs_slide = None
        self.google_fonts = GoogleFonts(self.config.revealjs_generic_font)

    def init(self):  # noqa
        if hasattr(self.config, "revealjs_google_fonts"):
            self.google_fonts = self.google_fonts.extend(
                self.config.revealjs_google_fonts
            )
        # Create RevealjsProjectContext
        self.revealjs_context = RevealjsProjectContext(
            4,
            [  # noqa: W503
                static_resource_uri(src)
                for src in getattr(self.config, "revealjs_script_files", [])
            ],
            getattr(self.config, "revealjs_script_conf", None),
            [
                RevealjsPlugin(
                    static_resource_uri(plugin["src"]),
                    plugin.get("name", ""),
                    plugin.get("options", "{}").strip(),
                )
                for plugin in getattr(self.config, "revealjs_script_plugins", [])
            ],
        )
        # Hand over builder configs to html builder.
        setattr(self.config, "html_static_path", self.config.revealjs_static_path)
        super().init()

    def init_css_files(self) -> None:  # noqa
        self.add_css_file(self.revealjs_context.engine.css_path)
        for filename in self.get_builder_config("css_files", "revealjs"):
            self.add_css_file(filename)

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
        ctx["css_files"] = copy.copy(self.css_files)
        ctx["revealjs"] = self.revealjs_context
        return ctx

    def update_page_context(
        self, pagename: str, templatename: str, ctx: Dict, event_arg: Any
    ) -> None:  # noqa
        self.configure_theme(ctx)
        self.configure_fonts(ctx)
        ctx["revealjs_page_confs"] = self.configure_page_script_conf()

    def configure_theme(self, ctx: Dict):
        """Find and add theme css from conf and directive."""
        # Use directive or conf
        if self.revealjs_slide and "theme" in self.revealjs_slide.attributes:
            theme = self.revealjs_slide.attributes["theme"]
        else:
            theme = self.config.revealjs_style_theme
        # Build path of stylesheet
        if theme.startswith("http://") or theme.startswith("https://"):
            pass
        elif theme.endswith(".css"):
            theme = f"_static/{theme}"
        else:
            theme = f"_static/{self.revealjs_context.engine.theme_dir}/{theme}.css"
        # index 0: "_static/revealjs4/dist/reveal.css"
        # index 1: theme css file path
        # index 2 or later: other css files
        ctx["css_files"].insert(1, theme)

    def configure_fonts(self, ctx: Dict):
        """Find and add google-fonts settins from conf and directive."""
        # Injection Google Font css
        fonts = self.google_fonts
        if self.revealjs_slide and "google_font" in self.revealjs_slide.attributes:
            fonts = fonts.extend(
                self.revealjs_slide.attributes["google_font"].split(",")
            )
        ctx["google_fonts"] = fonts
        ctx["css_files"] += fonts.css_files

    def configure_page_script_conf(self) -> List[str]:  # noqa
        if not self.revealjs_slide:
            return []
        configs = []
        if "conf" in self.revealjs_slide.attributes:
            configs.append(self.revealjs_slide.attributes["conf"])
        if self.revealjs_slide.content:
            configs.append(self.revealjs_slide.content)
        return configs
