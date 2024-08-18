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
  * Have big changes of generated contents by new Reveal.js
  * Breaking changes for setup-level requirements

* Update minor version with:

  * Update marks for deprecated (warning level)
  * Add new features (include inner extensions)
  * Add supporting dependencies
  * Drop supporting dependencies (not change setup-level)
  * Change major version of Reveal.js, but it need not update as major version
  * Change minor version of Reveal.js
  * Change components by misc reasons

* Update patch version with:

  * Mark deprecated notice
  * Fixed bugs
  * Change patch version of Reveal.js

Following dependencies
======================

CPython
-------

|THIS| supports only "Living" versions for as of first of year.

**"Living"** means that it have not published last security-only releases.
**"Not living"** means that it is finished to published security-only releases.

#. When some version of CPython released "last security-only release",
   |THIS| will release with marks deprecated notice-level at upcoming (patch version).
#. When |THIS| releases new minor version after 2 month from version with marked deprecated notice,
   this will drop old versions from everywhere and deprecated warning (minor version).
#. If |THIS| must only use specify version,
   this will set ``python_requires`` and release new version (major or minor version).

Sphinx
------

(TBD)

Reveal.js
---------

|THIS| bundles stable version.

#. When Reveal.js is released as patch version,
   |THIS| bundles new version and releases as patch version at upcoming.
#. When Reveal.js is released as minor version,
   |THIS| bundles new version and releases as minor version at upcoming.
   It is possibility to include adding options for new version.
#. When Reveal.js is released as major version,
   I will check compatibility for configuration of extension.

  * If I have decided to need breaking change, |THIS| will release as major version.
  * if it need not change or only add configuration, |THIS| will release as minor version.
    |THIS| bundles new version and releases as patch version at upcoming.
