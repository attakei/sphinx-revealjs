"""Configuration for pytest."""

from __future__ import annotations

import inspect
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from packaging import version
from sphinx import deprecation

from sphinx_revealjs.deprecated import _get_sphinx_version

if TYPE_CHECKING:
    from _pytest.config import Config


pytest_plugins = "sphinx.testing.fixtures"
collect_ignore = ["roots"]


def pytest_configure(config: Config):  # noqa
    for name, klass in inspect.getmembers(deprecation, inspect.isclass):
        if not issubclass(klass, DeprecationWarning):
            continue
        config.addinivalue_line(
            "filterwarnings", f"error::{klass.__module__}.{klass.__name__}"
        )


@pytest.fixture(scope="session")
def rootdir():
    """Set root directory to use testing sphinx project."""
    current_ver = _get_sphinx_version()
    delimter_ver = version.parse("7.2.0")
    if current_ver < delimter_ver:
        from sphinx.testing.path import path

        return path(__file__).parent.abspath() / "roots"
    return Path(__file__).parent.resolve() / "roots"
