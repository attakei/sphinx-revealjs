"""Configuration for pytest."""
import pytest
from sphinx.testing.path import path

pytest_plugins = "sphinx.testing.fixtures"

collect_ignore = ["roots"]


@pytest.fixture(scope="session")
def rootdir():
    """Set root directory to use testing sphinx project."""
    return path(__file__).parent.abspath() / "roots"
