"""Setup module
"""
import re
from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).parent

with (here / 'README.rst').open(encoding='utf-8') as f:
    long_description = f.read()

install_requires = [
    'docutils',
    'Sphinx'
]

extra_requires = {
    'linting': [
        'flake8',
        'flake8-docstrings',
        'flake8-isort',
        'doc8',
    ],
    'testing': [
        'nose',
        'sphinx-testing',
    ]
}


def fetch_version_string(target: Path) -> str:
    line_re = re.compile(r"__version__ = '(.*?)'", re.S)
    return line_re.search(target.open().read()).group(1)


setup(
    name='sphinx-revealjs',
    version=fetch_version_string(here / 'sphinx_revealjs' / '__init__.py'),
    description='Sphinx extention with theme to generate Reveal.js presentation',
    long_description=long_description,
    url='https://github.com/attakei/sphinx-revealjs',
    author='attakei',
    author_email='attakei@gmail.com',
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'Framework :: Sphinx :: Theme',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'Topic :: Multimedia :: Graphics :: Presentation',
    ],
    packages=find_packages(exclude=['docs', 'demo', 'tools']),
    install_requires=install_requires,
    extras_require=extra_requires,
    include_package_data=True,
)
