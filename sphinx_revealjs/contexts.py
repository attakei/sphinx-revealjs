"""Contexts for passing between objects."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

from sphinx.util import logging

from .utils import static_resource_uri

if TYPE_CHECKING:
    from typing import Optional, Union

logger = logging.getLogger(__name__)


class RevealjsEngine:
    """Reveal.js core metadata."""

    def __init__(self, version: int, js_path: str, css_path: str, theme_dir: str):  # noqa
        self.version = version
        self.js_path = js_path
        self.css_path = css_path
        self.theme_dir = theme_dir

    @classmethod
    def from_version(cls, version: int = 4):  # noqa
        return cls(
            version,
            "revealjs/dist/reveal.js",
            "revealjs/dist/reveal.css",
            "revealjs/dist/theme",
        )


class RevealjsPlugin:
    """Plugin metadata."""

    def __init__(
        self, src: str, name: Optional[str] = None, options: Optional[str] = None
    ):  # noqa
        self.src = src
        self.name = name
        self.options = options


class RevealjsProjectContext:
    """Context object for Reveal.js (project-wide)."""

    def __init__(
        self,
        engine_version: int,
        script_files: Optional[list[str]] = None,
        script_conf: Optional[Union[str, dict]] = None,
        script_plugins: Optional[list[RevealjsPlugin]] = None,
    ):  # noqa
        self.engine = RevealjsEngine.from_version(engine_version)
        if isinstance(script_conf, str):
            """.. noe::
               This need to keep as specs until found better implements to handle JavaScript code.

               :refs: #229
            """
            self.script_conf = script_conf
        else:
            self.script_conf = json.dumps(script_conf)
        self.script_plugins = script_plugins or []
        self._script_files = script_files or []

    @property
    def script_files(self):  # noqa
        return [static_resource_uri(self.engine.js_path)] + self._script_files
