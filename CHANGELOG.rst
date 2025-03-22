ver 3.1.4
=========

:Release date: 2025-03-22 (Asia/Tokyo)
:Reveal.js version: 5.1.0

Fixes
-----

* Remove unnecessary deps for core.

ver 3.1.3
=========

:Release date: 2025-03-10 (Asia/Tokyo)
:Reveal.js version: 5.1.0

Fixes
-----

* Fix to set local files for background item.

  * It is same of fixes on ver 3.1.2.
  * This version includes for ``revaljs-vertical`` and ``revealjs-break``.

ver 3.1.2
=========

:Release date: 2025-03-09 (Asia/Tokyo)
:Reveal.js version: 5.1.0

Fixes
-----

* Fix to set local files for background item.

  * Target are ``data-background-image`` , ``data-background-video`` and ``data-background-iframe`` .

Others
------

* Update translation of demo.
* Use latest actions in GitHub Actions.
* Use renovate to sync versions of actions.

ver 3.1.1
=========

:Release date: 2025-03-01 (Asia/Manila)
:Reveal.js version: 5.1.0

Fixes
-----

* Fallback when ``literal_block`` and inherits does not have ``language`` attribute.

ver 3.1.0
=========

:Release date: 2025-02-27 (JST)
:Reveal.js version: 5.1.0

Dependencies
------------

* Drop Python 3.7 and 3.8 from supported version.

Fixes
-----

* Keep all attributes of project's nodes. ( `#189 <https://github.com/attakei/sphinx-revealjs/issues/189>`_ )

Others
------

* Refactor by Ruff and MyPy.
* Update type hintings.
* Use uv and go-task for wrokspace management.
* Use lefthook for hooks management instead of pre-commit.

ver 3.0.5
=========

:Release date: 2024-10-20 (JST)
:Reveal.js version: 5.1.0

Fixes
-----

* Do not render stray end-tag (``</section>``) - `GH#180 <https://github.com/attakei/sphinx-revealjs/issues/180>`_.

Others
------

* Update contents of demo for latest features.
* Mark python version of author workspace by mise.

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
