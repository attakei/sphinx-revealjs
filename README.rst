sphinx-revealjs
===============

Sphinx extention with theme to generate Reveal.js presentation

Orverview
---------

This extension generate Reveal.js presentation from **standard** reStructuredText.

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

Futures
-------

* Index template as none presentation
* Theme select per presentations
* CDN support