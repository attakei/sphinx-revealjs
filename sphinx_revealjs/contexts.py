"""Contexts for passing between objects."""
from typing import List


class RevealjsProjectContext(object):
    """Context object for Reveal.js (project-wide)."""

    def __init__(self, script_files: List[str], script_conf: str = None):  # noqa
        self.script_files = script_files
        self.script_conf = script_conf
