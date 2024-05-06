"""Deprecated notes."""

import sys
import textwrap

from packaging import version
from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util import logging

logger = logging.getLogger(__name__)


def _get_python_version() -> version.Version:
    """Retrieve version object of Python."""
    text = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    return version.parse(text)


def _get_sphinx_version() -> version.Version:
    """Retrieve version object of Sphinx."""
    from sphinx import __version__

    return version.parse(__version__)


def _to_single_message(msg: str) -> str:
    """Re-format from triple-quoted string to single-line string."""
    return textwrap.dedent(msg).strip().replace("\n", " ")


def handle(app: Sphinx, config: Config):
    """Monitor dependencies and log deprecated messages."""
    python_version = _get_python_version()
    sphinx_version = _get_sphinx_version()
    # For python supportings
    if python_version < version.parse("3.8"):
        msg = f"""
            2024-05-06 - All Python <3.8 is already dropped in supporting.
            {__name__} will supports only python 3.8 and newer using `requires-python` metadata with minor version up.
            Please update python to keep using it.
            """  # noqa: E501
        logger.warning(_to_single_message(msg))

    if sphinx_version.major < 5:
        msg = f"""
            2024-05-06 - In near future,
            {__name__} will drop supports for Sphinx of version less than 5 with minor version up.
            Please update dependencies to keep using it.
            """  # noqa: E501
        logger.warning(_to_single_message(msg))
