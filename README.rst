sphinx-revealjs
===============

Sphinx extention for generating Revealjs presentation.

Installation
------------

This project is not registered to PyPI.

For installation, you need to install from GitHub.

.. code-block:: bash

    $ pip install git+https://github.com/attakei/sphinx-revealjs


Usage
-----

1. Create your sphinx documentation
2. Edit `conf.py` to use this extension

.. code-block:: python

    extensions = [
        'sphinx_revealjs',
    ]

    html_theme = 'revealjs'

3. Build revealjs sources

.. code-block:: bash

    $ make revealjs
