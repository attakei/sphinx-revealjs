Standard usage
==============

Installation
------------

You can install stable version of ``sphinx-revealjs`` from PyPI.

.. code-block:: console

   pip install sphinx-revealjs

Set up
------

Edit ``conf.py`` to use this extension.

.. code-block:: python

   extensions = [
       "sphinx_revealjs",
   ]

You can customize behavior. Please see `documentation <https://sphinx-revealjs.readthedocs.io/en/stable/configurations/>`_.

Write source
------------

Write plain reStructuredText.

.. code-block:: rst

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

Build presentation
------------------

This extension has custom builder name ``revealjs``.
If you make docs as Reveal.js presentation, you call ``make revealjs``.

.. code-block:: console

   make revealjs

This presentation is made from `source <https://github.com/attakei/sphinx-revealjs/blob/master/demo/index.rst>`_.

Footnotes
---------

You can set footnotes. footnotes are rendered on tail of slide by using internal-extension. [#]_

.. [#] This is footnote.
