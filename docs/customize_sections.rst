==================
Customize sections
==================

To change behavior of sections, |THIS| provide some directives.

revealjs-section / revealjs_section
===================================

To change behavior per section, write directive per section.

Usage
-----

Write ``revealjs-slide`` directive on directly below of section title header.

.. code-block:: rst

    Title
    =====

    Section
    -------

    .. revealjs-section::
        :data-background-color: #009900

Attributes
----------

This directive can accept attribute as same as Reveal.js ``section`` tags.

revealjs-break / revealjs_break
===============================

If you want to transition section with keeping title,
``revealjs-break`` can use.

Usage
-----

Write ``revealjs-break`` to point of want to split section.

.. code-block:: rst

    Title
    =====

    Section
    -------

    Content 1

    .. revealjs-break::

    Content 2(next slide)

Attributes
----------

It accepts attributes as same as ``revealjs-section``.

And it accepts ``notitle`` as unique feature.

notitle
  If it is set in directive, next section page does not display title.
