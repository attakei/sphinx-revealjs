"""Setup module
"""
from pathlib import Path

from setuptools import find_packages, setup

from sphinx_revealjs import __version__ as sphinx_revealjs_version

here = Path(__file__).parent

with (here / 'README.rst').open(encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sphinx-revealjs',
    version=sphinx_revealjs_version,
    description='',
    long_description=long_description,
    url='https://gitlab.com/attakei/sphinx-revealjs',
    author='attakei',
    author_email='attakei@gmail.com',
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['docs']),
    extras_require={
    },
    include_package_data=True,
)
