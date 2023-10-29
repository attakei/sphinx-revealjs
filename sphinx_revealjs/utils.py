"""Util as functions for some modules."""
from typing import Optional


def static_resource_uri(src: str, prefix: Optional[str] = None) -> str:
    """Build static path of resource."""
    local_prefix = "_static" if prefix is None else prefix
    if src.startswith("http://") or src.startswith("https://"):
        return src
    return f"{local_prefix}/{src}"


def deprecated_message(version: str, frm: str, to: str) -> str:  # noqa: D103
    return f"DEPRECATED: {frm} will drop by {version}, pleas use {to}"
