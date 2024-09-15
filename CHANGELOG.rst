ver 3.0.4
=========

:Release date: 2024-09-15 (JST)
:Reveal.js version: 5.1.0

Fixes
-----

* Render all heading content by ``revealjs-break``.

Others
------

* Update version of workflow.

ver 3.0.3
=========

:Release date: 2024-08-18 (JST)
:Reveal.js version: 5.1.0

Fixes
-----

* Change accessing property in builder for compatibility.

Others
------

* Fix broken links in documents.
* Fix typo in documents and comments.
* Use Ruff for lint and format sources instead of flake8 and black.
* Use latest patterns from GitignoreIO.
* Adjust compatibility of dependencies.

ver 3.0.2
=========

:Release date: 2024-05-06 (JST)
:Reveal.js version: 5.1.0

Fixes
-----

* Enable to use ``metatags`` variable in ``revealjs-simple`` theme.

Others
------

* Add message for deprecated: Sphinx<5.0 and Python<3.8.
* Use oEmbedPy in demo (instead of sphinxcontrib-oembed).

ver 3.0.1
=========

:Release date: 2024-04-14 (JST)
:Reveal.js version: 5.1.0 (updated)

(None updates for features)

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
  (``revealjs-section``, ``revealjs-break`` and ``revealjs-vertical``)
* Add wrapper function to get bundled revealjs path.
* Add new html-theme ``revealjs-simple`` that render minimum style reveal.js
  (Default theme is named ``revealjs-basic`` )

Fixes
-----

* ``revealjs-break`` splits pages in vertical slides when it is added to top of section.
