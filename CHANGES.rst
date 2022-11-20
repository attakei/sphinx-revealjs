=========
Changelog
=========

ver 2.4.1
=========

:date: 2022-11-20
:base: Reveal.js 4.4.0

(None updates for features)

Extra
-----

* Fix badge of readme

ver 2.4.0
=========

:date: 2022-11-13
:base: Reveal.js 4.4.0

Added features
--------------

* Add ``data-ln-start-from`` into ``revealjs-code-block`` and ``revealjs-literalinclude``.

Changes
-------

* Demo documentation are changed from ``demo/revealjs4`` to ``demo``.

Deprecated
----------

* Output warning when using it by Python 3.6
* Mark notice level deprecated

  * Change directory for contents of Reveal.js

Change supportings
------------------

* Add Python 3.11 into supportings
* Drop Python 3.6 from supportings

Develoment environment
----------------------

* Hooks of ``pre-commit`` are using as standard lintings.
  In GitHub Actions, ``lint`` is running ``pre-commit``.
* Use Flit as building library instead of Poetry.

ver 2.3.0
=========

:date: 2022-10-23
:base: Reveal.js 4.4.0 (updated)

Updated Features
----------------

* Support data-background-gradient correctly (already defined, but not working at older Reveal.js)

ver 2.2.0
=========

:date: 2022-10-01
:base: Reveal.js 4.3.1

Added features
--------------

* Add ``revealjs-literalinclude`` that is extends of ``literalinclude`` for ``data-line-numbers``.
  It is likely ``revealjs-code-block``.

ver 2.1.0
=========

:date: 2022-08-28
:base: Reveal.js 4.3.1

Added Features
--------------

* Package includes SCSS sources of revealjs bundled-themes

Extra
-----

* Use pre-commit

ver 2.0.1
=========

:date: 2022-08-02
:base: Reveal.js 4.3.1

Fixes
-----

* Custom builders accept ``app`` and ``env`` (optional) in initialize function

ver 2.0.0
=========

:date: 2022-05-31
:base: Reveal.js 4.3.1

Added Features
--------------

* Directive ``revealjs-notes`` writes speaker-view content into presentation

* Config ``reveajs_notes_from_comments`` toggle if it creates speaker-view content from comment-block

  * BREAKING CHANGE: Default value is False. You must set ``True`` explicitly to use as same as ver 1.x
* Config ``reveajs_use_index`` toggle if it creates ``genindex.html``

  * BREAKING CHANGE: Default value is False. You must set ``True`` explicitly to use as same as ver 1.x

Fixes
-----

* Register ``data-XXX`` attributes into ``revealjs-section`` and ``revealjs-break`` from https://revealjs.com/

Deleted feaures
---------------

* Remove snake-cesed directives
* Does not generate ``search.html``
