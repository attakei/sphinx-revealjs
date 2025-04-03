===============
sphinx-revealjs
===============

|THIS| is Sphinx extension
to generate Reveal.js presentation documents
from **standard** reStructuredText.

Basic Features
==============

* Nested sections
* Speaker note
* Syntax highlight for Reveal.js (not used pygments)
* Customize slides and sections by conf.py or source reST

Demo
====

* Source: `Sphinx document <https://github.com/attakei/sphinx-revealjs/tree/master/demo>`_
* Created: `Reveal.js presentation <https://attakei.github.io/sphinx-revealjs/>`_

.. container:: flex

  .. container:: half

    .. figure:: _static/screenshot-sphinx.png
        :alt: Screenshot of source Sphinx doc

  .. container:: half

    .. figure:: _static/screenshot-revealjs.png
        :alt: Screenshot of Reveal.js slide

.. only:: not latex

   .. container:: presentation

      .. oembed:: https://attakei.github.io/sphinx-revealjs/en/

Concept and motivation
======================

Goal of this library is to provide presentation platform
for self-branding of engineer using Sphinx.
Using static site hosting service, you can show own presentations to anyone.

Core motivation is that I want to play presentation by this library.

Contents
========

.. toctree::
   :maxdepth: 2

   setup
   upgrade
   configurations
   directives
   optional-extensions
   tips
   local-workspace
   contributing
   changes
   versioning-policy

Licenses
========

This library is licensed Apache License version 2.0.

About license of directly dependencies,
please see each software projects or documentations.

* docutils:

  * https://docutils.sourceforge.io/

* Sphinx:

  * https://www.sphinx-doc.org/
  * https://github.com/sphinx-doc/sphinx

* Reveal.js:

  * https://revealjs.com/#/
  * https://github.com/hakimel/reveal.js

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
