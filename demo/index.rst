===============
sphinx-revealjs
===============

What is this?
=============

Sphinx extension to build Revealjs presentation

Features
========

* Convert sections from reStructuredText directly
* Select revealjs version
* Select theme from default themes

Usage
=====

Installation
------------

This project is not registered to PyPI.
User need to install from GitHub

.. code-block:: bash

    $ pip install git+https://github.com/attakei/sphinx-revealjs


Configure
---------

Edit `conf.py` to use this extension

.. code-block:: python

    extensions = [
        'sphinx_revealjs',
    ]

    html_theme = 'revealjs'

Build
-----

This extension has custom builder name ``revealjs`` .
If you make docs as Reveal.js presentation, you call ``make revealjs`` 

.. code-block:: bash

    $ make revealjs

This presentation is made from ``https://github.com/attakei/sphinx-revealjs/blob/demo/docs/index.rst``


Thank you
=========

Please star!

.. raw:: html

    <!-- Place this tag where you want the button to render. -->
    <a class="github-button" href="https://github.com/attakei/sphinx-revealjs" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star attakei/sphinx-revealjs on GitHub">Star</a>
    <!-- Place this tag in your head or just before your close body tag. -->
    <script async defer src="https://buttons.github.io/buttons.js"></script>