=========
Changelog
=========

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
