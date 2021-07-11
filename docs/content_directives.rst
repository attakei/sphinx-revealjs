==================
Content directives
==================

|THIS| provides features for contents of section.

revealjs-code-block
===================

This is extends of ``code-block`` direcrive for presentation.

If you want to use ``data-line-number`` attributes in code-block.

Usage
-----

Set it instead of ``code-block``.

.. code-block:: rst

   .. revealjs-code-block: python
      :data-line-numbers: 1

      def hello():
          print("world")

Reference
---------

* https://revealjs.com/code/#line-numbers-%26-highlights

revealjs-frabments / revealjs_fragments
=======================================

.. note::
    There are cases not working regular.

Inject ``fragment`` attribute into objects.

Usage
-----

Write block as directive that you want to present as fragments.

.. code-block:: rst

    .. revealjs-fragments::

        * First
        * Second
        * Third

See `demo <https://attakei.github.io/sphinx-revealjs/#/5/1>`_

Reference
---------

* https://github.com/hakimel/reveal.js/#fragments
