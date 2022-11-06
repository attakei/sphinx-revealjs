=================
Versioning policy
=================

:date: 2022-11-06

.. note:: This is possibility to change without announces.

Base rules
==========

|THIS| releases based from `Semantic Versioning 2.0.0 <https://semver.org/spec/v2.0.0.html>`_.

* Update major version with:

  * Drop or changed configuration variables
  * Drop supporing dependencies
  * Change major version of Reveal.js

* Update minor version with:

  * Mark deprecated warning
  * Add features (include inner extensions)
  * Add supporing dependencies

* Update patch version with:

  * Mark deprecated notice
  * Fixed bugs
  * Change minor or patch version of Reveal.js
  * Change dependent packages without breaking-changes of itself

Following dependencies
======================

CPython
-------

|THIS| supports only "Living" versions for as of first of year.

**"Living"** means that it have not published last security-only releases.
**"Not living"** means that it is finished to published security-only releases.

At first of every year, I release major version with:

* Remove "Not living" version from matrix of GitHub Actions
* Add mark deprecated warning

Sphinx
------

Reveal.js
---------
