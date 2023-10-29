=============================
sphinx_revealjs.ext.footnotes
=============================

:Added: v2.8.0

Overview
========

This extension updates position of footnotes.

Installation
============

You need not install extra, you can use it immediately after installing |THIS|.

Usage
=====

WHen adding extension into your ``conf.py``, insert CSS file to customize layout of footnotes.

Example
-------

.. code-block:: python
   :caption: conf.py

   extensions = [
       "sphinx_revealjs",
       "sphinx_revealjs.ext.footnotes",
   ]

.. code-block:: rst
   :caption: sample-slide.rst

   Sample title
   ============

   This sentence has footnotes [#f1]_

   .. [#f1] This is footnote.

Configuration
=============

All Configuration names are prefixed ``revealjs_footnotes_``.

.. confval:: revealjs_footnotes_font_size

   :Type: ``str``
   :Default: ``50%``
   :Example: ``60%``

   Font-size of rendered footnote contents.

.. confval:: revealjs_footnotes_ref_font_size

   :Type: ``str``
   :Default: ``70%``
   :Example: ``60%``

   Font-size of rendered footnote's referer text.
