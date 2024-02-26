ver 3.0.0
=========

:Release date: 2024-02-27
:Reveal.js version: 5.0.5 (updated)

Breaking changes
----------------

* Dropped old Python and Sphinx versions.
* Change path of bundled revealjs path.
* The builder outputs everything in the "vertical slide" format.
* Builder does not generate ``section`` element for level-4 sections.

Features
--------

* Add new directive ``revealjs-vertical``.
* Section directives accepts any ``data-`` attributes.
  (``revealjs-secion``, ``revealjs-break`` and ``revealjs-vertical``)
* Add wrapper function to get bundled revealjs path.
* Add new html-theme ``revealjs-simple`` that render minimum style reveal.js
  (Default theme is named ``revealjs-basic`` )

Fixes
-----

* ``revealjs-break`` splits pages in vertical slides when it is added to top of section.
