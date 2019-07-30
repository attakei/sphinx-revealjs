.. |THIS| replace:: ``sphinx-revealjs``

=======================
Customize presentations
=======================

To customize presentations, you can configure by some approach.

Global configuration
====================

To customize all presentations, edit your ``conf.py`` .

Usage
-----

|THIS| is accept themes and theme options.
If you want set parameters,
write ``revealjs_theme`` and ``revealjs_theme_options``.

.. code-block:: python

    revealjs_theme_options = {
        'revealjs_config': '{"transition": "cube"}'
    }

Parameters
----------

revealjs_theme_options
    Options for default theme.
    Use to override from template default parameters.

revealjs_theme
    Theme name to use. (default is **sphinx_revealjs**)

    If you want customize template, change it.


Slide configuration
===================

For editing settings for specify presentation,
you write custom directive at source reST.

Usage
-----

Write ``revealjs_slide`` directive directly after first section.

.. code-block:: rst

    Slide title
    ===========

    .. revealjs_slide::
        :theme: solarized
        :config: {"transition": "none"}


Parameters
----------

theme
    Change Reveal.js theme for only slide

config
    Override parameter to initialize Reveal.js


Section configuration
=====================

To change behavior per section, write directive per section.

Usage
-----

Write ``revealjs_section`` directive directly after subsections.

.. code-block:: rest

    Title
    =====

    Section
    -------

    .. revealjs_section::
        :data-background-color: #009900

Parameters
----------

.. todo:: write after
