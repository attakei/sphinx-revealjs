"""Definition for sphinx custom builder."""

from __future__ import annotations

import copy
import logging
from typing import TYPE_CHECKING

from sphinx import version_info as sphinx_version
from sphinx.builders.dirhtml import DirectoryHTMLBuilder
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.locale import __

from sphinx_revealjs.directives import raw_json
from sphinx_revealjs.writers import RevealjsSlideTranslator

from .contexts import RevealjsPlugin, RevealjsProjectContext
from .utils import get_internal_static_path, static_resource_uri

if TYPE_CHECKING:
    from typing import Any, Optional

    from sphinx.application import Sphinx
    from sphinx.config import Config
    from sphinx.environment import BuildEnvironment

    from .nodes import revealjs_slide


logger = logging.getLogger(__name__)


class RevealjsHTMLBuilder(StandaloneHTMLBuilder):
    """Sphinx builder class to generate Reveal.js presentation HTML.

    This manage theme path and configure default options.
    """

    name = "revealjs"
    default_translator_class = RevealjsSlideTranslator
    search = False

    def __init__(self, app, env: BuildEnvironment):  # noqa: D107
        super().__init__(app, env)
        self.revealjs_slide: Optional[revealjs_slide] = None

    def init(self):  # noqa
        # Create RevealjsProjectContext
        script_conf = getattr(self.config, "revealjs_script_conf")
        if not script_conf:
            script_conf = {}
        if isinstance(script_conf, dict):
            script_conf.setdefault("scrollActivationWidth", None)
        self.revealjs_context = RevealjsProjectContext(
            4,
            [  # noqa: W503
                static_resource_uri(src)
                for src in getattr(self.config, "revealjs_script_files", [])
            ],
            script_conf,
            [
                RevealjsPlugin(
                    static_resource_uri(plugin["src"]),
                    plugin.get("name", ""),
                    plugin.get("options", "{}").strip(),
                )
                for plugin in getattr(self.config, "revealjs_script_plugins", [])
            ],
        )
        self.config.revealjs_static_path.append(str(get_internal_static_path()))
        # Hand over builder configs to html builder.
        setattr(self.config, "html_static_path", self.config.revealjs_static_path)
        super().init()
        self.use_index = self.get_builder_config("use_index", "revealjs")

    def init_css_files(self) -> None:  # noqa
        self.add_css_file(self.revealjs_context.engine.css_path)
        for filename in self.get_builder_config("css_files", "revealjs"):
            self.add_css_file(filename)

    def init_js_files(self) -> None:  # noqa
        for filename, attrs in self.app.registry.js_files:
            self.add_js_file(filename, **attrs)  # type: ignore[arg-type]

        for filename, attrs in self.get_builder_config("js_files", "revealjs"):
            self.add_js_file(filename, **attrs)  # type: ignore[arg-type]

    def get_theme_config(self) -> tuple[str, dict]:
        """Find and return configuration about theme (name and option params).

        Find theme and merge options.
        """
        theme_options = getattr(self.config, "revealjs_theme_options", {})
        config = raw_json(theme_options.get("revealjs_config", ""))
        theme_options["revealjs_config"] = config
        return self.config.revealjs_html_theme, theme_options

    def get_doc_context(self, docname, body, metatags):
        """Return customized context.

        if source has ``revealjs_slide`` property, add configures.
        """
        ctx = super().get_doc_context(docname, body, metatags)
        # TODO: Add note it why it copies from properties
        if sphinx_version[0] >= 8:
            ctx["css_files"] = copy.copy(self._css_files)
        else:
            ctx["css_files"] = copy.copy(self.css_files)
        ctx["revealjs"] = self.revealjs_context
        return ctx

    def update_page_context(
        self, pagename: str, templatename: str, ctx: dict, event_arg: Any
    ) -> None:  # noqa
        self.configure_theme(ctx)
        ctx["revealjs_page_confs"] = self.configure_page_script_conf()

    def configure_theme(self, ctx: dict):
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

    def configure_page_script_conf(self) -> list[str]:  # noqa
        if not self.revealjs_slide:
            return []
        configs = []
        if "conf" in self.revealjs_slide.attributes:
            configs.append(self.revealjs_slide.attributes["conf"])
        if self.revealjs_slide.content:
            configs.append(self.revealjs_slide.content)
        return configs

    def prepare_writing(self, docnames: set[str]):
        super().prepare_writing(docnames)
        self.events.emit("revealjs:ready-for-writing", self.globalcontext)


class DirectoryRevealjsHTMLBuilder(DirectoryHTMLBuilder, RevealjsHTMLBuilder):
    """Custom RevealjsHTMLBuilder to generate all HTML pages as ``index.html``.

    This does not have specific features, only inherit base builders.
    """

    name = "dirrevealjs"


def convert_reveal_js_files(app: Sphinx, config: Config) -> None:
    """Convert string styled html_js_files to tuple styled one.

    Original is :py:func:`sphinx.builders.html.convert_html_js_files`.
    """
    revealjs_js_files: list[tuple[str, dict]] = []
    for entry in config.revealjs_js_files:
        if isinstance(entry, str):
            revealjs_js_files.append((entry, {}))
        else:
            try:
                filename, attrs = entry
                revealjs_js_files.append((filename, attrs))
            except Exception:
                logger.warning(__("invalid js_file: %r, ignored"), entry)
                continue
    config.revealjs_js_files = revealjs_js_files
