==============
Configurations
==============

|THIS| can build multiple presentations.
You can configure in ``conf.py`` for all presentations.

Style Configurations
====================

revealjs_css_files
------------------

:Type: ``str``
:Optional:
:Default: ``[]`` (empty)
:Example: ``["custom.css"]``

List of using custom css (same of ``html_css_files`` ).

If you want to customize presentation by CSS, write external css and use it.

revealjs_style_theme
--------------------

:Type: ``str``
:Optional:
:Default: ``black``
:Example: ``moon``, ``custom.css``

Theme name of stylesheet for Reveal.js.

* | If value does not have suffix ``.css``,
  | use bundled Reveal.js theme(included ``revealjs/css/theme``).

revealjs_google_fonts
---------------------

:Type: ``dict``
:Optional:
:Default: ``[]``
:Example: ``[]``

List of using fonts from `Google Fonts <https://fonts.google.com/>`_.
If this value is set, render ``link`` and ``style`` tags into html.

revealjs_generic_font
---------------------

:Type: ``str``
:Optional:
:Default: ``sans-serif``
:Example: ``serif``, ``monospace``

If you use ``revealjs_google_fonts``, set last of ``font-family`` style.


Presentation Configurations
===========================

revealjs_script_files
---------------------

:Type: ``List[str]``
:Optional:
:Default: ``["revealjs/js/reveal.js"]``
:Example: ``["revealjs/js/reveal.js", "presentation.js"]``

List of sources that render as ``script`` tags.

There is bundled Reveal.js script at ``revealjs/js/reveal.js``.

Example:

  .. code-block:: html

      <div>
        <!-- Presentation body -->
      </div>
      <!-- here!! -->
      <script src="_static/revealjs/js/revealjs.js"></script>
      <script src="_static/presentation.js"></script>

revealjs_script_conf
--------------------

:Type: ``str``
:Optional:
:Default: ``None``

Raw JavaScript code for configuration of Reveal.js.

If this value is set, render ``script`` tag after source script tags.

Example:

  .. code-block:: py

      revealjs_script_conf = """
      {
          controls: false,
          transition: 'zoom',
      }
      """

  .. code-block:: html

      <div>
        <!-- Presentation body -->
      </div>
      <script src="_static/revealjs/js/revealjs.js"></script>
      <!-- here!! -->
      <script>
        let revealjsConfig = {};
        revealjsConfig = Object.assign(revealjsConfig, {
          controls: false,
          transition: 'zoom',
        });
        revealjs.initialize(revealjsConfig);
      </script>

revealjs_script_plugins
-----------------------

:Type: ``List[Dict]``
:Optional:
:Default: ``[]``

List of pulugin configurations.
If this value is set, render ``script`` tag after source script tags.

There are bundled Reveal.js plugins at ``revealjs/plugin``.

Example:

  .. code-block:: py

      revealjs_script_plugins = [
          "src": "revealjs/plugin/highlight/highlight.js"
          "options: """
            {async: true, callback: function() { hljs.initHighlightingOnLoad(); } }
          """
      ]

  .. code-block:: html

      <div>
        <!-- Presentation body -->
      </div>
      <script src="_static/revealjs/js/revealjs.js"></script>
      <!-- here!! -->
      <script>
        let revealjsConfig = {};
        plugin_0 = {async: true, callback: function() { hljs.initHighlightingOnLoad(); } };
        plugin_0.src = "_static/revealjs/plugin/highlight/highlight.js"
        revealjsConfig.dependencies.push(plugin_0);
        revealjs.initialize(revealjsConfig);
      </script>
