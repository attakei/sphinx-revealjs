===========
Change logs
===========

ver 0.10.0
==========

:data: 2020-03-25

Features
--------

* Change bundle Reveal.js (3.8.0 -> 3.9.1)
* Add support version (3.8, author's default)

Fixes
-----

* In development, depend by ``sphinxcontrib-gtagjs``. (use in demo)

Extra
-----

* Change license (MIT -> Apache-2.0)
* Use poetry as build environment

ver 0.9.0
=========

:date: 2019-12-22

Fixes
-----

* google-fonts default options is changed for not to render in template.
* Adjusting templates based by sphinx basic theme. (short breaking)

  * Enable ``metatags`` , ``scripts`` and more template values.

ver 0.8.0
=========

:date: 2019-11-11

Features
--------

* Add new config option ``google_font`` to set google-font style.

ver 0.7.0
=========

:date: 2019-10-28

Features
--------

* Add new directive ``revealjs_fragments`` to use Fragment.

ver 0.6.1
=========

:date: 2019-09-12

Fixes
-----

* Remove tag that refer source not exits

ver 0.6.0
=========

:date: 2019-07-31

Features
--------

* Add new directive ``revealjs_break`` to split sections.

  * Updated demo

Extra
-----

* Add docstrings any sources. (ignore tests)
* Remove Pipenv.
* Migrate metadata and options from ``setup.py`` into ``setup.cfg`` .
* Use bumpversion for versioning

ver 0.5.1
=========

:date: 2019-06-30

Extra
-----

* Update Reveal.js from 3.7.0 to 3.8.0


ver 0.5.0
=========

:date: 2018-12-31

Features
--------

* Revealjs initialize config accept from sphinx document config
* Revealjs initialize config accept from ``revealjs_slide`` directive


ver 0.4.1
=========

:date: 2018-12-21

Fixes
-----

* ``revealjs_section`` directive of source apply for itself only

ver 0.4.0
=========

:date: 2018-12-10

Features
--------

* It can select theme per presentations.


ver 0.3.1
=========

First public release on PyPI.
