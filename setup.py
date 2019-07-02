"""Setup module
"""
import re
from pathlib import Path
from setuptools import setup


here = Path(__file__).parent


def fetch_version_string(target: Path) -> str:
    line_re = re.compile(r"__version__ = '(.*?)'", re.S)
    return line_re.search(target.open().read()).group(1)


setup(
    version=fetch_version_string(here / 'sphinx_revealjs' / '__init__.py')
)
