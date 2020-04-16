==================
Customize sections
==================

To change behavior of sections, |THIS| provide some directives.

revealjs_section
================

To change behavior per section, write directive per section.

Usage
-----

Write ``revealjs_slide`` directive on directly below of section title header.

.. code-block:: rst

    Title
    =====

    Section
    -------

    .. revealjs_section::
        :data-background-color: #009900

Attributes
----------

This direcvite can accept attribute as same as Reveal.js ``section`` tags.

revealjs_break
==============

If you want to transition section with keeping title,
``revealjs_break`` can use.

Usage
-----

Write ``revealjs_break`` to point of want to split section.

.. code-block:: rst

    Title
    =====

    Section
    -------

    Content 1

    .. revealjs_break::

    Content 2(next slide)

Attributes
----------

It accepts attributes as same as ``revealjs_section``.

And it accepts ``notitle`` as unique feature.

notitle
  If it is set in directive, next section page does not display title.
