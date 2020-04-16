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

* Sourece: `Sphinx document <https://github.com/attakei/sphinx-revealjs/tree/master/demo>`_
* Created: `Reveal.js presentation <https://attakei.github.io/sphinx-revealjs/>`_

.. container:: flex

  .. container:: half

    .. figure:: _static/screenshot-sphinx.png
        :alt: Screenshot of source Sphinx doc

  .. container:: half

    .. figure:: _static/screenshot-revealjs.png
        :alt: Screenshot of Reveal.js slide

Contents
========

.. toctree::
   :maxdepth: 1

   setup
   configurations
   customize_slide
   customize_sections
   content_directives

Concept and motivation
======================

Goal of this library is to provide presentation platform
for self-branding of engineer using Sphinx.
Using static site hosting service, you can show own presentations to anyone.

Core motivation is that I want to play plesentation by this library.

Liceses
=======

This library is licensed Apache License verion 2.0.

About license of directly dependencies,
please see each software projects or documententions.

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
