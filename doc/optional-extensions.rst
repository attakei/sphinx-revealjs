===================
Optional extensions
===================

|THIS| includes optional extensions.
These are not core features for presentation, but supporting features to get for more values.

Why these are optional ?
========================

These require extra packages to work, but them do not need for standard features.
However, required packages are large (example: playwright is 27MB to only create screenshot).

Therefore, I split core features and optional features as "package extra".

Usage
=====

With install |THIS|, append extras by ``[]``.

.. code-block:: console

   pip install 'sphinx-revealjs[OPT1]'

You can install multiple extras with comma.

.. code-block:: console

   pip install 'sphinx-revealjs[OPT1,OPT2]'

Edit ``conf.py`` to work extensions.

For details, please see extension's page.

Features
========

.. toctree::
   :glob:
   :maxdepth: 1

   optional-extensions/*
