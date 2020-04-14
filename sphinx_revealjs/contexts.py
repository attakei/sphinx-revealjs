"""Contexts for passing between objects."""
from collections import namedtuple
from typing import List

RevealjsPlugin = namedtuple("RevealjsPlugin", ["src", "options"])


class GoogleFonts(object):
    """Google fonts tag generator."""

    def __init__(self, fonts: List[str]):  # noqa
        self.fonts = fonts

    @property
    def css_files(self) -> List[str]:
        """Return google fonts urls."""
        return [
            "https://fonts.googleapis.com/css"
            f"?family={font.replace(' ', '+')}&display=swap"
            for font in self.fonts
        ]

    @property
    def font_family(self) -> str:
        """Return style value of 'font-family' to use fonts."""
        fonts = ",".join([f"'{f}'" for f in self.fonts])
        return fonts


class RevealjsProjectContext(object):
    """Context object for Reveal.js (project-wide)."""

    def __init__(
        self,
        google_fonts: GoogleFonts = None,
        script_files: List[str] = None,
        script_conf: str = None,
        script_plugins: List[RevealjsPlugin] = None,
    ):  # noqa
        self.google_fonts = google_fonts
        self.script_files = script_files or []
        self.script_conf = script_conf
        self.script_plugins = script_plugins or []
