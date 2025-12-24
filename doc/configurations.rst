==============
Configurations
==============

|THIS| can build multiple presentations.
You can configure in ``conf.py`` for all presentations.

Basic configurations
====================

.. confval:: revealjs_static_path

   :Type: ``list``
   :Default: ``[]`` (empty)
   :Example: ``["_static"]``

   List of static files directory ( same as :confval:`sphinx:html_static_path` )

.. confval:: revealjs_js_files

   :Type: ``list``
   :Default: ``[]`` (empty)
   :Example: ``["custom.js"]``

   List of using custom css (same as :confval:`sphinx:html_js_files` ).

   When you want to use JS that does not related revealjs, can use this.

.. confval:: revealjs_css_files

   :Type: ``list``
   :Default: ``[]`` (empty)
   :Example: ``["custom.css"]``

   List of using custom css (same as :confval:`sphinx:html_css_files` ).

   If you want to customize presentation by CSS, write external css and use it.

.. confval:: revealjs_use_index

   :Type: ``bool``
   :Default: ``False``

   Flag that does builder generate ``genindex.html`` (same as :confval:`sphinx:html_use_index` ).

.. confval:: revealjs_html_theme

   :Type: ``str``
   :Default: ``revealjs-basic``
   :Example: ``revealjs-simple``

   Using HTML Theme for output contents.
   It can set any html theme, but it should set theme made for revealjs.

   Bundled themes are:

   * ``revealjs-basic`` : Inherit style from basic html theme.
   * ``revealjs-simple`` : Minimal defined style.

Style Configurations
====================

.. confval:: revealjs_style_theme

   :Type: ``str``
   :Default: ``black``
   :Example: ``moon``, ``custom.css``

   Theme name of stylesheet for Reveal.js.

   * | If value does not have suffix ``.css``,
     | use bundled Reveal.js theme(included ``revealjs/css/theme``).

Presentation Configurations
===========================

.. confval:: revealjs_use_section_ids

   :Type: ``boolean``
   :Default: ``False``

   If this is set ``True``,
   inject ``id`` attribute into ``section`` element (parent of headings).
   This means that change format of internal links (default is numbering style).

.. confval:: revealjs_script_files

   :Type: ``List[str]``
   :Default: ``[]``
   :Example: ``["presentation.js"]``

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

.. confval:: revealjs_script_conf

   :Type: ``str or dict``
   :Default: ``None``

   Configuration of Reveal.js presentation.
   This value is used as options of ``Reveal.initialize`` in output files.

   * If value is string type, handle as raw javascript code.
   * If value is dict object, convert to json string at internal.

   .. note::

      For behavior compatibility,
      it appends ``{"scrollActivationWidth": None}`` as default configuration
      when value is dict object or is not set.

      See it: https://github.com/hakimel/reveal.js/releases/tag/5.0.0

   .. hint::

      If you want to initialze plugins with custom arguments,
      you should use "string type" configuration.

      "dict object" does not work correctly because it convert to JSON string into script.

   Example 1: case of str

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

   Example 2: case of dict

   .. code-block:: py

      revealjs_script_conf = {
          "controls": False,
          "transition": "zoom",
      }

   .. code-block:: html

      <div>
        <!-- Presentation body -->
      </div>
      <script src="_static/revealjs/js/revealjs.js"></script>
      <!-- here!! -->
      <script>
        let revealjsConfig = {};
        revealjsConfig = Object.assign(revealjsConfig, JSON.parse('{"controls": false, "transition": "zoom", "scrollActivationWidth": null}'));
        revealjs.initialize(revealjsConfig);
      </script>

   example 1 and 2 are behaving same.

   Example 3: Using Highligt plugin with ``beforeHighlight`` hook.

   .. code-block:: python

      revealjs_script_conf = """
      {
          highlight: {
              beforeHighlight: (hljs) => hljs.registerLanguage(/*...*/),
          }
      }

.. confval:: revealjs_script_plugins

   :Type: ``List[Dict]``
   :Default: ``[]``

   List of plugin configurations.
   If this value is set, render ``script`` tag after source script tags.

   There are bundled Reveal.js plugins at ``revealjs/plugin``.

   Example:

   .. code-block:: py

      revealjs_script_plugins = [
          {
              "src": "revealjs/plugin/highlight/highlight.js",
              "name": "RevealHighlight",
          },
      ]

   .. code-block:: html

      <div>
        <!-- Presentation body -->
      </div>
      <script src="_static/revealjs/js/revealjs.js"></script>
      <script src="_static/revealjs/plugin/highlight/highlight.js"></script>
      <!-- here!! -->
      <script>
        let revealjsConfig = {};
        revealjsConfig.plugins = [RevealHighlight,];
        revealjs.initialize(revealjsConfig);
      </script>

.. confval:: revealjs_notes_from_comments

   :Type: boolean
   :Default: False

   If this is set `True`, builder writes notes section from comment block.
