===============
sphinx-revealjs
===============

.. This toctree is only to link examples.

.. toctree::
   :glob:
   :hidden:

   *

:Based version: 1.0.0
:Released: 2020-12-27

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
    </section>

code-block as reveal.js code block
----------------------------------


Directive for meta of section
=============================

Inject background color
-----------------------

.. revealjs_section::
    :data-background-color: #009900

.. code-block:: rest

    .. revealjs_section::
        :data-background-color: #009900

Inject background image
-----------------------

.. revealjs_section::
    :data-background-image: _static/icon-attakei.jpg
    :data-background-size: contain

.. code-block:: rest

    .. revealjs_section::
        :data-background-image: _static/icon-attakei.jpg
        :data-background-size: contain

Inject background video
-----------------------

.. revealjs_section::
    :data-background-video: https://s3.amazonaws.com/static.slid.es/site/homepage/v1/homepage-video-editor.mp4,https://s3.amazonaws.com/static.slid.es/site/homepage/v1/homepage-video-editor.webm

.. code-block:: rest

    .. revealjs_section::
        :data-background-video: https://s3.amazonaws.com/static.slid.es/site/homepage/v1/homepage-video-editor.mp4,https://s3.amazonaws.com/static.slid.es/site/homepage/v1/homepage-video-editor.webm

Inject background iframe
------------------------

.. revealjs_section::
    :data-background-iframe: https://slides.com
    :data-background-interactive:

.. code-block:: rest

    .. revealjs_section::
        :data-background-iframe: https://slides.com
        :data-background-interactive:


Transition settings(before)
---------------------------

.. revealjs_section::
    :data-transition: none

.. code-block:: rest

    .. revealjs_section::
        :data-transition: none

Transition settings(after)
--------------------------

.. revealjs_section::
    :data-transition: fade

.. code-block:: rest

    .. revealjs_section::
        :data-transition: fade

Background image transition
---------------------------

.. revealjs_section::
    :data-background-image: _static/icon-attakei.jpg
    :data-background-size: contain
    :data-background-transition: zoom

.. code-block:: rest

    .. revealjs_section::
        :data-background-image: _static/icon-attakei.jpg
        :data-background-size: contain
        :data-background-transition: zoom


Keep title without duplicated written
-------------------------------------

First section

.. revealjs_break::

Second section

.. code-block:: rest

    .. revealjs_break::


.. revealjs_break::
    :notitle:

Third section.

You can hide section title

.. code-block:: rest

    .. revealjs_break::
        :notitle:

Support features
================

Fragments
---------

This is support fragment with groups.

.. revealjs_fragments::

   * First
   * Second
   * Third

Plugins
-------

bundled plugins can use just write ``conf.py``

.. code-block:: python

    revealjs_script_plugins = [
        {
            "name": "RevealNotes",
            "src": "revealjs4/plugin/notes/notes.js",
        },
    ]

This is used `RevealNotes` plugin, Please press `S` key to try it!

Usage
=====

Installation
------------

You can install from PyPI.

.. code-block:: bash

    $ pip install sphinx-revealjs

Configure
---------

Edit `conf.py` to use this extension

.. code-block:: python

    extensions = [
        "sphinx_revealjs",
    ]

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
If you make docs as Reveal.js presentation, you call ``make revealjs``.

.. code-block:: bash

    $ make revealjs

This presentation is made from `source <https://github.com/attakei/sphinx-revealjs/blob/master/demo/revealjs4/index.rst>`_.

Other examples
==============

Within this pages
-----------------

* :doc:`example-background-only-section`

Enjoy writing reST as presentation
==================================

Please star!

.. raw:: html

    <!-- Place this tag where you want the button to render. -->
    <a class="github-button" href="https://github.com/attakei/sphinx-revealjs" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star attakei/sphinx-revealjs on GitHub">Star</a>
    <!-- Place this tag in your head or just before your close body tag. -->
    <script async defer src="https://buttons.github.io/buttons.js"></script>
