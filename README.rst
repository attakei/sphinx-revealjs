sphinx-revealjs
===============

Sphinx extention for generating Reveal.js presentation.

Orverview
---------

This extension generate Reveal.js presentation from **standard** reStructuredText.

It include theses features.

* Custom builder to translate from reST to reveal.js style HTML
* Template to be enable to render presentation local imdependent

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

3. Write source for standard document style

4. Build sources as Reveal.js presentation

    .. code-block:: bash

        $ make revealjs

Futures
-------

* Index template as none presentation
* Theme select per presentations
* CDN support