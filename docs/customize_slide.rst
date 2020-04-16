=============================
Customize slide from document
=============================

Sphinx can manage multiple documents,
so that |THIS| can build multiple presentation slides.

If you want to configure one presentation from some,
write ``revealjs_slide`` directive into reST document.

Directive usage
===============

Write ``revealjs_slide`` directive on directly below of title header.

.. code-block:: rst

    Presentation title
    ==================

    .. revealjs_slide::
        :theme: moon

    Section
    -------

    Content


Directive attributes
====================

.. note::

    Directive based customize has options less than conf based
    because implementation restrict.

theme
-----

Override ``revealjs_style_theme``.

google_font
-----------

Override ``revealjs_google_fonts``, but it can specify only one.

conf
----

Override ``revealjs_script_conf``, but single line only.
