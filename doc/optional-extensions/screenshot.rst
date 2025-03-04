==============================
sphinx_revealjs.ext.screenshot
==============================

:Added: v2.5.0

Overview
========

Generate screenshot first section of presentations by Playwright.
Screenshots can use as OGP Image contents.

.. note::

   This extension generates screenshots only when your running builder is ``revealjs`` or ``dirrevealjs``.
   Even if you run other builder with this in extensions, any screenshot are not generated.

Installation
============

This extension need Playwright and browser component.

.. code-block:: console

   pip install 'sphinx-revealjs[screenshot]'
   playwright install chromium

Usage
=====

When adding extension into your ``conf.py``, this generates screenshots per pages.
You can set image path into ``:og:image:`` field of sphinxext-opengraph_ in advance.

Example
-------

.. code-block:: python
   :caption: conf.py

   extensions = [
       "sphinx_revealjs",
       "sphinx_revealjs.ext.screenshot",
       "sphinxext.opengraph",
   ]

.. code-block:: rst
   :caption: sample-slide.rst

   :og:image: ./_images/ogp/sample-slide.png

   Sample title
   ============

Configuration
=============

All Configuration names are prefixed ``revealjs_screenshot_``.

.. confval:: revealjs_screenshot_outdir

   :Type: ``str``
   :Default: ``"_images/ogp"``
   :Example: ``"_static/images"``

   Output directory for generated screenshots.
   This must be relative path for outdir of Sphinx.

.. confval:: revealjs_screenshot_excludes

   :Type: ``List[str]``
   :Default: ``[]`` (empty)
   :Example: ``["index"]``

   List of docnames to exclude for target of screenshots.
   Values must be docname format that does not need extension of files.

Works
=====

After build all documents, launch headless-browser by Playwright.

Browser captures screenshots any document pages for these rule.

* Targets are generating files. If it runs incremental build and document is not changed, document is not target.
* If docname contains are :confval:`revealjs_screenshot_excludes`, document is not target.

When browser capture screenshots, this sets image size from ``Reveal`` config (with and height).
This values are used viewport of presentation.

* If you want to change all sizes, you can set :confval:`revealjs_script_conf`.
* If you want to change per docs, you can set :rst:dir:`revealjs-slide` directive.

Note
====

Currently, I recommend using sphinxext-opengraph_ to add ogp metatags (it is useful).
I delegate behavior about opengraph, and |THIS| does not have feature to generate ogp tags.


.. _sphinxext-opengraph: https://pypi.org/project/sphinxext-opengraph/
