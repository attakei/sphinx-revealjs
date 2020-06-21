"""Contexts for passing between objects."""
from collections import namedtuple
from typing import List

RevealjsPlugin = namedtuple("RevealjsPlugin", ["src", "options"])


class GoogleFonts(object):
    """Google fonts tag generator."""

    def __init__(self, generic_font: str, fonts: List[str] = None):  # noqa
        self.generic_font = generic_font
        self.fonts = fonts or []

    @property
    def css_files(self) -> List[str]:
        """Return google fonts urls."""
        return [
            "https://fonts.googleapis.com/css2"
            f"?family={font.replace(' ', '+')}&display=swap"
            for font in self.fonts
        ]

    @property
    def font_family(self) -> str:
        """Return style value of 'font-family' to use fonts."""
        fonts = ",".join([f"'{f}'" for f in self.fonts])
        if fonts:
            fonts += ", "
        fonts += self.generic_font
        return fonts

    @property
    def has_fonts(self) -> bool:  # noqa
        return bool(self.fonts)

    def extend(self, fonts: List[str]) -> "GoogleFonts":  # noqa
        return GoogleFonts(self.generic_font, list(set(self.fonts + fonts)))


class RevealjsProjectContext(object):
    """Context object for Reveal.js (project-wide)."""

    def __init__(
        self,
        script_files: List[str] = None,
        script_conf: str = None,
        script_plugins: List[RevealjsPlugin] = None,
    ):  # noqa
        self.script_files = script_files or []
        self.script_conf = script_conf
        self.script_plugins = script_plugins or []
