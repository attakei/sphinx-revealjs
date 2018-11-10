===============
sphinx-revealjs
===============

:Version: 0.2
:Released: 2018-11-09

Overview
========

What is this?
-------------

Sphinx extension to build Revealjs presentation

Features
--------

.. This is reST comment. Render into speaker note section

* Convert sections from reStructuredText directly
* Select theme from default themes


Convert sections from reStructuredText directly
===============================================

Adjust section structure 
------------------------

From:

.. code-block:: rest

    Title
    =====

    First section
    -------------

        Content 1
        ^^^^^^^^^

        Content 2
        ^^^^^^^^^

To:

.. code-block:: html

    <section>
        <h1>Title</h1>
    </section>
    <section>
        <section>
            <h2>First section</h2>
        </section>
        <section>
            <h3>Content 1</h3>
        </section>    
        <section>
            <h3>Content 2</h3>
        </section>    
    </section>


reStructuredText comments are used as speaker notes
---------------------------------------------------


From:

.. code-block:: rest

    .. This is comment in reStructuredText


To:

.. code-block:: html

    <section>
        <aside class="notes">
        This is comment in reStructuredText
        </aside>


code-block as reveal.js code block
----------------------------------



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

Write source
------------

Write plain reStructuredText

.. code-block:: rest

    My Reveal.js presentation
    =========================

    Agenda
    ------

    * Author
    * Feature


    Author: Who am I
    ================

    Own self promotion

    Content
    =======


Build
-----

This extension has custom builder name ``revealjs`` .
If you make docs as Reveal.js presentation, you call ``make revealjs`` 

.. code-block:: bash

    $ make revealjs

This presentation is made from ``https://github.com/attakei/sphinx-revealjs/blob/demo/docs/index.rst``


Enjoy writing reST as presentation
==================================

Please star!

.. raw:: html

    <!-- Place this tag where you want the button to render. -->
    <a class="github-button" href="https://github.com/attakei/sphinx-revealjs" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star attakei/sphinx-revealjs on GitHub">Star</a>
    <!-- Place this tag in your head or just before your close body tag. -->
    <script async defer src="https://buttons.github.io/buttons.js"></script>