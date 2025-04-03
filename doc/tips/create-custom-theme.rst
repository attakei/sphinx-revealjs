===================
Create custom theme
===================

.. versionadded:: 2.1.0

.. versionchanged:: 3.2.0

``sphinx-revealjs`` includes SCSS sources of bundled themes.
You can write custom theme from theme template of reveal.js using ``sphinx_revealjs.ext.sass``.

Example 1: Using ``sphinx_revealjs.ext.sass`` (recommended)
===========================================================

.. code-block:: python

   extensions = [
       # .. Your extensions
       # Add
       "sphinx_revealjs.ext.sass",
   ]

   revealjs_style_theme = "custom.css"

   revealjs_sass_src_dir = "_sass"
   revealjs_sass_out_dir = "_static"
   revealjs_sass_auto_targets = True

When you build document with ``/_sass/custom.scss``,
it compile SCSS to CSS and you can use ``_static/custom.css`` as theme style of presentation.

Old examples
============

.. versionremoved:: 3.2.0

   This does not works since Reveal.js v5.2.0.

Example 1: Using `libsass`_
---------------------------

First, install `libsass`_ to compile SASS/SCSS on your environment.

.. code-block:: console

   pip install libsass

Write SCSS source for your theme.

.. code-block:: SCSS

   // Use template sources from Reveal.js
   @import "template/mixins";
   @import "template/settings";

   // Write your settings
   $base03: #002b36;

   // ...


   @import "template/theme";

   // You can write custom style too.
   .reveal {
     h1, h2, h3 {
       text-transform: none;
     }
   }

Compile source.

.. code-block:: python

   from pathlib import Path

   import sass
   from sphinx_revealjs.utils import get_revealjs_path

   source = Path("_sass/custom.scss").read_text()
   css = sass.compile(
       string=source,
       include_paths=[str(get_revealjs_path() / "css/theme")]
   )
   Path("_static/custom.css").write_text(css)

Use compiled CSS as your theme.

.. code-block:: python

   # conf.py
   # If option has extension, find from static files.
   revealjs_style_theme = "custom.css"
   revealjs_static_path = ["_static"]

Example 2: `sphinxcontrib-sass`_
--------------------------------

You can use `sphinxcontrib-sass`_ to simplify.

.. code-block:: console

   pip install --find-links=https://github.com/attakei-lab/sphinxcontrib-sass/releases sphinxcontrib-sass

.. code-block:: python

   # conf.py
   from sphinx_revealjs.utils import get_revealjs_path

   extensions = [
       # .. Your extensions
       # Add
       "sphinxcontrib.sass",
   ]

   sass_src_dir = "_sass"
   sass_out_dir = "_static"
   sass_targets = {"custom.scss": "custom.css"}
   sass_include_paths = [
       get_revealjs_path() / "css" / "theme",
   ]

When document updated, it compile scss to css.

.. _libsass: https://pypi.org/project/libsass/
.. _sphinxcontrib-sass: https://github.com/attakei-lab/sphinxcontrib-sass
