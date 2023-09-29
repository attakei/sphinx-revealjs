"""Configuration for pytest."""
import inspect

import pytest
from _pytest.config import Config
from sphinx import deprecation
from sphinx.testing.path import path

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
    return path(__file__).parent.abspath() / "roots"
