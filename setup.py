"""Setup module."""
import re
from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).parent

install_requires = [
    'docutils',
    'Sphinx'
]

extra_requires = {
    'linting': [
        'flake8',
        'flake8-docstrings',
        'flake8-isort',
        'pydocstyle<4.0.0',
        'doc8',
    ],
    'testing': [
        'nose',
        'sphinx-testing',
    ]
}


def fetch_version_string(target: Path) -> str:
    """Fetch version string from module."""
    line_re = re.compile(r"__version__ = '(.*?)'", re.S)
    return line_re.search(target.open().read()).group(1)


setup(
    version=fetch_version_string(here / 'sphinx_revealjs' / '__init__.py'),
    packages=find_packages(exclude=['docs', 'demo', 'tools']),
    install_requires=install_requires,
    extras_require=extra_requires,
    include_package_data=True,
)
