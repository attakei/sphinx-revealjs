"""Deprecated notes."""

import textwrap

from packaging import version
from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util import logging

logger = logging.getLogger(__name__)


def _get_sphinx_version() -> version.Version:
    """Retrieve version object of Sphinx."""
    from sphinx import __version__

    return version.parse(__version__)


def _to_single_message(msg: str) -> str:
    """Re-format from triple-quoted string to single-line string."""
    return textwrap.dedent(msg).strip().replace("\n", " ")


def handle(app: Sphinx, config: Config):
    """Monitor dependencies and log deprecated messages."""
    sphinx_version = _get_sphinx_version()
    if sphinx_version.major < 5:
        msg = f"""
            2024-05-06 - In near future,
            {__name__} will drop supports for Sphinx of version less than 5 with minor version up.
            Please update dependencies to keep using it.
            """  # noqa: E501
        logger.warning(_to_single_message(msg))
