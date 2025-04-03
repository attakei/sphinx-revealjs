==========================
sphinx_revealjs.ext.oembed
==========================

.. versionadded:: 3.2.0

Overview
========

This extension provide oEmbed content for presentation.
You can embed presentation used this into your document by ``oembed`` directive of :pypi:`oEmbedPy`.

Installation
============

You need not install extra, you can use it immediately after installing |THIS|.

Usage
=====

Add extension module into ``extensions`` of your ``conf.py``.

.. code-block:: python
   :caption: conf.py

   extensions = [
       "sphinx_revealjs",
       "sphinx_revealjs.ext.oembed",
   ]

Configuration
=============

All Configuration names are prefixed ``revealjs_oembed_``.

.. confval:: revealjs_oembed_url

   :Type: ``str``
   :Default: ``"http://localhost:8000"``
   :Example: ``"https://example.com"``

   Base part of URL for presentations and oEmbed contents.

   Default value is to test in localmachine.
   We recommend to set for your environment.

.. confval:: revealjs_oembed_out_dir

   :Type: ``str``
   :Default: ``"_files/oembed"``
   :Example: ``"_static/oembed"``

   Root directory of destination for oEmbed contents.

.. confval:: revealjs_oembed_excludes

   :Type: ``list[str]``
   :Default: ``[]`` (empty list)
   :Example: ``["index"]``

   List of docname that you don't want to generate oEmbed contents.
