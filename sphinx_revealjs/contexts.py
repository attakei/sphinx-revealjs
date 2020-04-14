"""Contexts for passing between objects."""
from collections import namedtuple
from typing import List

RevealjsPlugin = namedtuple("RevealjsPlugin", ["src", "options"])


class RevealjsProjectContext(object):
    """Context object for Reveal.js (project-wide)."""

    def __init__(
        self,
        script_files: List[str],
        script_conf: str = None,
        script_plugins: List[RevealjsPlugin] = None,
    ):  # noqa
        self.script_files = script_files
        self.script_conf = script_conf
        self.script_plugins = script_plugins or []
