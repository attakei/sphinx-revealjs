"""Contexts for passing between objects."""
import json
from typing import Dict, List, Optional, Union

from sphinx.util import logging

from .utils import static_resource_uri

logger = logging.getLogger(__name__)


class RevealjsEngine:
    """Reveal.js core metadata."""

    def __init__(
        self, version: int, js_path: str, css_path: str, theme_dir: str
    ):  # noqa
        self.version = version
        self.js_path = js_path
        self.css_path = css_path
        self.theme_dir = theme_dir

    @classmethod
    def from_version(cls, version: int = 4):  # noqa
        return cls(
            version,
            "revealjs4/dist/reveal.js",
            "revealjs4/dist/reveal.css",
            "revealjs4/dist/theme",
        )


class RevealjsPlugin:
    """Plugin metadata."""

    def __init__(
        self, src: str, name: Optional[str] = None, options: Optional[str] = None
    ):  # noqa
        self.src = src
        self.name = name
        self.options = options


class RevealjsProjectContext(object):
    """Context object for Reveal.js (project-wide)."""

    def __init__(
        self,
        engine_version: int,
        script_files: Optional[List[str]] = None,
        script_conf: Optional[Union[str, Dict]] = None,
        script_plugins: Optional[List[RevealjsPlugin]] = None,
    ):  # noqa
        self.engine = RevealjsEngine.from_version(engine_version)
        if isinstance(script_conf, str):
            logger.warning(
                "For next major version, revealjs_script_conf accepts only dict",
            )
            self.script_conf = script_conf
        else:
            self.script_conf = f"JSON.parse('{json.dumps(script_conf)}')"
        self.script_plugins = script_plugins or []
        self._script_files = script_files or []

    @property
    def script_files(self):  # noqa
        return [static_resource_uri(self.engine.js_path)] + self._script_files
