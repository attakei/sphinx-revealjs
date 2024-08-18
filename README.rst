sphinx-revealjs
===============

.. image:: https://img.shields.io/pypi/v/sphinx-revealjs.svg
    :target: https://pypi.org/project/sphinx-revealjs/

.. image:: https://github.com/attakei/sphinx-revealjs/actions/workflows/main.yml/badge.svg
    :target: https://github.com/attakei/sphinx-revealjs/actions

.. image:: https://readthedocs.org/projects/sphinx-revealjs/badge/?version=latest
    :target: https://sphinx-revealjs.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Sphinx extension with theme to generate Reveal.js presentation

Overview
--------

This extension generate Reveal.js presentation
from **standard** reStructuredText.

It include theses features.

* Custom builder to translate from reST to reveal.js style HTML
* Template to be enable to render presentation local independent

For more information, refer to `the documentation <https://sphinx-revealjs.readthedocs.io/>`_.

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

See `it <./CHANGELOG.rst>`_

Policy for following to Reveal.js version
-----------------------------------------

This is implemented based Reveal.js.
I plan to update it at patch-version for catch up when new Reveal.js version released.

* If Reveal.js updated minor or patch version, sphinx-revealjs update patch version.
* If Reveal.js updated major version, sphinx-revealjs update minor version with compatible for two versions.

Contributing
------------

GitHub repository does not have reveal.js library.

If you use from GitHub and editable mode, Run ``tools/fetch_revealjs.py`` after install.

.. code-block:: bash

    $ git clone https://github.com/attakei/sphinx-revealjs
    $ cd sphinx-revealjs
    $ python tools/fetch_revealjs.py

For more information, See `CONTRIBUTING.rst <./CONTRIBUTING.rst>`_ and `"contributing" <https://sphinx-revealjs.readthedocs.io/en/stable/contributing/>`_ page in documentation.

Copyright
---------

Apache-2.0 license. Please see `LICENSE <./LICENSE>`_.
