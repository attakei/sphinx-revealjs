sphinx-revealjs
===============

.. image:: https://img.shields.io/pypi/v/sphinx-revealjs.svg
    :target: https://pypi.org/project/sphinx-revealjs/

.. image:: https://github.com/attakei/sphinx-revealjs/workflows/Testings/badge.svg
    :target: https://github.com/attakei/sphinx-revealjs/actions

.. image:: https://travis-ci.org/attakei/sphinx-revealjs.svg?branch=master
    :target: https://travis-ci.org/attakei/sphinx-revealjs


Sphinx extention with theme to generate Reveal.js presentation

Orverview
---------

This extension generate Reveal.js presentation
from **standard** reStructuredText.

It include theses features.

* Custom builder to translate from reST to reveal.js style HTML
* Template to be enable to render presentation local imdependent

Installation
------------

.. code-block:: bash

    $ pip install sphinx-revealjs


Usage
-----

1. Create your sphinx documentation
2. Edit `conf.py` to use this extension

    .. code-block:: python

        extensions = [
            'sphinx_revealjs',
        ]

3. Write source for standard document style

4. Build sources as Reveal.js presentation

    .. code-block:: bash

        $ make revealjs

Change logs
-----------

See `it <./CHANGES.rst>`_

Futures
-------

* Index template as none presentation
* CDN support

Contributings
-------------

GitHub repository does not have reveal.js library.

If you use from GitHub and editable mode, Run ``tools/fetch_revealjs.py`` after install.

.. code-block:: bash

    $ git clone https://github.com/attakei/sphinx-revealjs
    $ cd sphinx-revealjs
    $ poetry install
    $ poetry run python tools/fetch_revealjs.py

Copyright
---------

Apache-2.0 license. Please see `LICENSE <./LICENSE>`_.
