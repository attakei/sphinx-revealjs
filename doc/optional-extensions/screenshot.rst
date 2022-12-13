==============================
sphinx_revealjs.ext.screenshot
==============================

:Added: v2.5.0

Overview
========

Generate screenshot first section of presentations by Playwright.
Screenshots are used as OGP Image contents.

.. warning::

   This generates screenshots ALWAYS when it set in ``extensions``.
   If you are going to run multiple builder without ``revealjs`` and ``dirrevealjs``,
   you need configure to work only when builder is ``revealjs`` or ``dirrevealjs``.

Installation
============

This extension need Playwright and browser component.

.. code-block:: console

   pip install 'sphinx-revealjs[screenshot]'
   playwright install

Configuration
=============

All Configuration names are prefixed ``revealjs_screenshot_``.

.. confval:: revealjs_screenshot_url

   :Type: ``str``
   :Default: ``"http://localhost:8000"``
   :Example: ``"https://attakei.github.io/sphinx-revealjs"``

   Prefix of images' URL. This is used attribute of ``og:image`` meta-tag.

.. confval:: revealjs_screenshot_path

   :Type: ``str``
   :Default: ``"_images/ogp"``
   :Example: ``"_static/images"``

   Output directory for generated screenshots.
   This must be releative path for outdir of Sphinx.

.. confval:: revealjs_screenshot_excludes

   :Type: ``List[str]``
   :Default: ``[]`` (empty)
   :Example: ``["index"]``

   List of docnames to exclude for target of screenshots.
   Valuese must be docname format that does not need extension of files.

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
