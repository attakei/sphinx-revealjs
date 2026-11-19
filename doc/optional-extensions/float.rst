===========================
sphinx_revealjs.ext.float
===========================

.. versionadded:: 3.3.0

Overview
========

This extension provides the ``revealjs-float`` directive for creating
absolutely positioned content boxes on slides.

This is similar to the "Grid Layouts" feature from GitPitch, allowing you
to place content anywhere on a slide using width, height, x, and y coordinates.

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
       "sphinx_revealjs.ext.float",
   ]

Directive
=========

.. rst:directive:: .. revealjs-float::

   Create a floating content box on the slide.

   .. rubric:: Options

   .. rst:option:: drag

      :Type: ``str``
      :Example: ``"40 50"``, ``"200px 100px"``

      Width and height of the float box.
      Values can be specified as percentages (default) or with units (px, em, etc.).
      Two values separated by space: ``width height``

   .. rst:option:: drop

      :Type: ``str``
      :Example: ``"10 15"``, ``"-40px 20%"``

      X and Y position of the float box.
      Positive values position from left/top.
      Negative values position from right/bottom.
      Two values separated by space: ``x y``

   .. rst:option:: bg

      :Type: ``str``
      :Example: ``"yellow"``, ``"#ff0000"``, ``"rgba(255,0,0,0.5)"``

      Background color of the float box.
      Any valid CSS color value is accepted.

   .. rubric:: Example

   .. code-block:: rst

      .. revealjs-float::
         :drag: 40 50
         :drop: 10 15
         :bg: yellow

         This content appears in a yellow box
         positioned at 10% from left, 15% from top,
         with 40% width and 50% height.

      .. revealjs-float::
         :drag: 30 30
         :drop: -40px 40px
         :bg: red

         This red box is positioned 40px from right
         and 40px from top, with 30% width and 30% height.

Notes
=====

- Float boxes are rendered only in revealjs and dirrevealjs builders.
  They are skipped in other builders (html, latex, etc.).
- The positioning is relative to the slide container.
- Multiple float boxes can be used on a single slide.
- Content inside float boxes is parsed as normal reStructuredText.
