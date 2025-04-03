"""Util as functions for some modules."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional


def get_internal_static_path() -> Path:  # noqa: D103
    return Path(__file__).parent / "_static"


def get_revealjs_path() -> Path:
    """Return path-object of bundled Reveal.js files."""
    return get_internal_static_path() / "revealjs"


def static_resource_uri(src: str, prefix: Optional[str] = None) -> str:
    """Build static path of resource."""
    local_prefix = "_static" if prefix is None else prefix
    if src.startswith("http://") or src.startswith("https://"):
        return src
    return f"{local_prefix}/{src}"


def deprecated_message(version: str, frm: str, to: str) -> str:  # noqa: D103
    return f"DEPRECATED: {frm} will drop by {version}, pleas use {to}"
