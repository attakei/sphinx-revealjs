========================
sphinx_revealjs.ext.sass
========================

.. versionadded:: 3.2.0

Overview
========

This extension compile Sass/SCSS source into CSS files using Dart Sass.
This is same feature of :pypi:`sphinxcontrib-sass`,
but it includes tuning for ``sphinx-revealjs``.

Installation
============

You need not install extra, you can use it immediately after installing |THIS|.

Usage
=====

Add extension module into ``extensions`` of your ``conf.py``.

.. code-block:: python
   :caption: conf.py

   extensions = [
       "sphinx_revealjs",
       "sphinx_revealjs.ext.sass",
   ]

Configuration
=============

All Configuration names are prefixed ``revealjs_sass_``.

.. confval:: revealjs_sass_src_dir

   :Type: ``str``
   :Default: ``None``
   :Example: ``"_static"``

   Root directory of source files fo ``revealjs_sass_targets`` and ``revealjs_sass_auto_targets``.

.. confval:: revealjs_sass_out_dir

   :Type: ``str``
   :Default: ``None``
   :Example: ``"_static"``

   Root directory of destination fo ``revealjs_sass_targets`` and ``revealjs_sass_auto_targets``.

.. confval:: revealjs_sass_targets

   :Type: ``dict[str, str]``
   :Default: ``{}`` (empty dict)
   :Example: ``{"style.scss": "style.css"}``

   Dict of targets to compile.

   - Dict key is target filepath.
   - Dict value is destination filepath.

.. confval:: revealjs_sass_include_paths

   :Type: ``list[str|Path]``
   :Default: ``[]`` (empty list)
   :Example: ``["_sass/modules"]``

   List of paths to load as external module.

   You need not to append revaljs theme resources because it is added automately in internal proccess.

.. confval:: revealjs_sass_output_style

   :Type: ``str``
   :Default: ``"expanded"``
   :Example: ``"compressed"``

   Style of generated CSS files. You can select one of ``expanded`` or ``compressed``.

   - ``expanded`` : Default style
   - ``compressed`` : Minified style

.. confval:: revealjs_sass_auto_targets

   :Type: ``bool``
   :Default: ``False``
   :Example: ``True``

   When it is set ``True``, extension works for all files matched these conditions

   - Managed files on ``revealjs_sass_src_dir``.
   - Files having extension either ``.sass`` or ``.scss``.
   - File name do not begin underscore.
