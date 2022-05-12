===============
sphinx-revealjs
===============

.. This toctree is only to link examples.

.. toctree::
   :glob:
   :hidden:

   *

:Based version: 2.0.0.dev1
:Demo updated: 2022-01-09

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

.. container:: adjust-section-structure

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

.. container:: adjust-section-structure

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

.. This is comment in reStructuredText

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

**NOTE:** You must set revealjs_notes_from_comments

Use directive for speaker notes
-------------------------------

.. revealjs-notes::

   Content outputs into <aside> element,
   and you can see as speaker-notes.

From:

.. code-block:: rest

    .. revealjs-notes::

       Content outputs into <aside> element,
       and you can see as speaker-notes.

To:

.. code-block:: html

    <section>
      <aside class="notes">
        Content outputs into <aside> element, and you can see as speaker-notes.
      </aside>
    </section>

code-block as reveal.js code block
----------------------------------

From:

.. code-block:: rst

   .. code-block:: php

      <?php

      phpinfo();

To:

.. code-block:: php

   <?php

   phpinfo();


Directive for meta of section
=============================

Inject background color
-----------------------

.. revealjs-section::
    :data-background-color: #009900

.. code-block:: rest

    .. revealjs-section::
        :data-background-color: #009900

Inject background image
-----------------------

.. revealjs-section::
    :data-background-image: _static/icon-attakei.jpg
    :data-background-size: contain

.. code-block:: rest

    .. revealjs-section::
        :data-background-image: _static/icon-attakei.jpg
        :data-background-size: contain

Inject background video
-----------------------

.. revealjs-section::
    :data-background-video: https://s3.amazonaws.com/static.slid.es/site/homepage/v1/homepage-video-editor.mp4,https://s3.amazonaws.com/static.slid.es/site/homepage/v1/homepage-video-editor.webm

.. code-block:: rest

    .. revealjs-section::
        :data-background-video: https://s3.amazonaws.com/static.slid.es/site/homepage/v1/homepage-video-editor.mp4,https://s3.amazonaws.com/static.slid.es/site/homepage/v1/homepage-video-editor.webm

Inject background iframe
------------------------

.. revealjs-section::
    :data-background-iframe: https://slides.com
    :data-background-interactive:

.. code-block:: rest

    .. revealjs-section::
        :data-background-iframe: https://slides.com
        :data-background-interactive:


Transition settings(before)
---------------------------

.. revealjs-section::
    :data-transition: none

.. code-block:: rest

    .. revealjs-section::
        :data-transition: none

Transition settings(after)
--------------------------

.. revealjs-section::
    :data-transition: fade

.. code-block:: rest

    .. revealjs-section::
        :data-transition: fade

Background image transition
---------------------------

.. revealjs-section::
    :data-background-image: _static/icon-attakei.jpg
    :data-background-size: contain
    :data-background-transition: zoom

.. code-block:: rest

    .. revealjs-section::
        :data-background-image: _static/icon-attakei.jpg
        :data-background-size: contain
        :data-background-transition: zoom


Keep title without duplicated written
-------------------------------------

First section

.. revealjs-break::

Second section

.. code-block:: rest

    .. revealjs-break::


.. revealjs-break::
    :notitle:

Third section.

You can hide section title

.. code-block:: rest

    .. revealjs-break::
        :notitle:


Animate source code transitions
-------------------------------

.. revealjs-section::
   :data-auto-animate:

Enable animations for each `revealjs-section` and `revealjs-break`:

.. code-block:: console
   :linenos:

   echo 'First part of my command'

.. revealjs-break::
   :data-auto-animate:

Enable animations for each `revealjs-section` and `revealjs-break`:

.. code-block:: console
   :linenos:

   echo 'First part of my command'
   echo 'Second part of my command'


Animate source code highlighting
--------------------------------

.. revealjs-section::
   :data-auto-animate:

Highlight source code per line, using the `revealjs-code-block` directive:

.. code-block:: rst

   .. revealjs-code-block:: console
      :linenos:
      :data-line-numbers: 1|2|3,4

      echo 'First part of my command'
      echo 'Second part of my command'
      echo 'Third part of my command'
      echo 'Forth part of my command'

.. revealjs-code-block:: console
   :linenos:
   :data-line-numbers: 1|2|3,4

   echo 'First part of my command'
   echo 'Second part of my command'
   echo 'Third part of my command'
   echo 'Forth part of my command'

Support features
================

Fragments(reveal.js)
--------------------

This is support fragment with groups.

.. code-block:: rst

   .. revealjs-fragments::

      * First
      * Second
      * Third

.. revealjs-fragments::

   * First
   * Second
   * Third

Plugins(reveal.js)
------------------

bundled plugins can use just write ``conf.py``

.. code-block:: python

    revealjs_script_plugins = [
        {
            "name": "RevealNotes",
            "src": "revealjs4/plugin/notes/notes.js",
        },
    ]

This is used `RevealNotes` plugin, Please press `S` key to try it!

Math
----

Supporting math renderer from sphinx.

Example to use ``sphinx.ext.mathjax`` (recommended)

.. code-block:: rst

    .. math::

        \begin{aligned}
          \dot{x} & = \sigma(y-x) \\
          \dot{y} & = \rho x - y - xz \\
          \dot{z} & = -\beta z + xy
        \end{aligned}

.. math::

    \begin{aligned}
      \dot{x} & = \sigma(y-x) \\
      \dot{y} & = \rho x - y - xz \\
      \dot{z} & = -\beta z + xy     
    \end{aligned}

.. revealjs-break::

You can use math plugin of Reveal.js

Source:

.. code-block:: python

    revealjs_script_plugins = [
        {
            "name": "RevealMath",
            "src": "revealjs4/plugin/math/math.js",
        }
    ]

.. code-block:: rst

    .. raw:: html

        \[\begin{aligned}
        \dot{x} &amp; = \sigma(y-x) \\
        \dot{y} &amp; = \rho x - y - xz \\
        \dot{z} &amp; = -\beta z + xy
        \end{aligned} \]

.. revealjs-break::

You can use math plugin of Reveal.js

Output:

.. raw:: html

    \[\begin{aligned}
    \dot{x} &amp; = \sigma(y-x) \\
    \dot{y} &amp; = \rho x - y - xz \\
    \dot{z} &amp; = -\beta z + xy
    \end{aligned} \]

Use other sphinx extensions
---------------------------

You can use other extensions to render html.

.. todo:: This is example todo by ``sphinx.ext.todo`` . render at presentation.

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
