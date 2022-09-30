=========
Changelog
=========

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
