==========
Directives
==========

|THIS| provides some directives to customize presence and behaviors.

For customize presentation
==========================

Sphinx can manage multiple documents,
so that |THIS| can build multiple presentation slides.

If you want to configure one presentation from some,
use this directive into your source.

.. rst:directive:: revealjs-slide

   Write ``revealjs-slide`` directive on directly below of title header.

   .. note::

      Directive based customize has options less than conf based
      because implementation restrict.

   .. rst:directive:option:: theme
      :type: string

      Override ``revealjs_style_theme``.

   .. rst:directive:option:: google_font
      :type: string

      Override ``revealjs_google_fonts``, but it can specify only one.

      .. warning:: This option is not work in v2.x. It will removed in v3.x

   .. rst:directive:option:: conf
      :type: JSON-string or no-value

      Override ``revealjs_script_conf``, but single line only.

   Usage:

   .. code-block:: rst

      Presentation title
      ==================

      .. revealjs-slide::
         :theme: moon

      Section
      -------

      Content

For customize sections
======================

If you want to change behavior of sections, use these directives.

.. rst:directive:: revealjs-section

   To change behavior per section, write directive per section.

   .. rst:directive:option:: data-XXX

      This directive can accept any ``data-`` attributes included options of section element for Reveal.js [#]_.
      For more information, please see `Reveal.js documentation <https://revealjs.com/>`_.

      .. [#] Reveal.js plugins use ``data-`` attributes often to customize behavior.

      .. note::

         This may be not completed all attributes for Reveal.js.
         If you find missing attribute, pleas post issues or pull-requests into GitHub.

   Usage:

   Write ``revealjs-slide`` directive on directly below of section title header.

   .. code-block:: rst

      Title
      =====

      Section
      -------

      .. revealjs-section::
         :data-background-color: #009900

.. rst:directive:: revealjs-break

   If you want to transition section with keeping title,
   ``revealjs-break`` can use.

   Usage:

   Write ``revealjs-break`` to point of want to split section.

   .. code-block:: rst

       Title
       =====

       Section
       -------

       Content 1

       .. revealjs-break::

       Content 2(next slide)

   .. rst:directive:option:: data-XXX

      It accepts attributes as same as ``revealjs-section``.

   .. rst:directive:option:: notitle

      If it is set in directive, next section page does not display title.

.. rst:directive:: revealjs-vertical

   To change behavior of sections rendered vertical (called as vertical slides [#]_).

   .. [#] Pleas see `Reveal.js document <https://revealjs.com/vertical-slides/>`_ to know about this.

   .. rst:directive:option:: data-XXX

      It accepts attributes as same as :rst:dir:`revealjs-section`.
      There are affected on all slides vertical from declared section.

   Usage:

   Write ``revealjs-vertical`` to point of want to split section (second level).

   .. code-block:: rst

      Title
      =====

      .. revaeljs-vertical::
         :data-background-color: #009900

For interactive contents
========================

.. rst:directive:: revealjs-code-block

   This is extends of :rst:dir:`code-block` directive for presentation.

   If you want to use custom attributes in code-block.

   .. rst:directive:option:: data-line-numbers
      :type: string or no value

      Code highlighting pattern. See `Reveal.js document <https://revealjs.com/code/#line-numbers-%26-highlights>`_

   Example:

   .. code-block:: rst

      .. revealjs-code-block:: python
         :data-line-numbers: 1

         def hello():
             print("world")

   .. rst:directive:option:: data-ln-start-from
      :type: integer

      Set number of first-line in code block.
      When this is assigned, display line numbers even if ``data-line-numbers`` is not set.

   .. code-block:: rst

      .. revealjs-code-block:: python
         :data-ln-start-from: 3

         print(datetime.datetime.now())

      Please see `Reveal.js document <https://revealjs.com/code/#line-number-offset-4.2.0>`_.

.. rst:directive:: revealjs-literalinclude

   This is extends of :rst:dir:`literalinclude` directive for presentation.

   If you want to use custom attributes in literalinclude.

   External attributes are same from :rst:dir:`revealjs-code-block`.

.. rst:directive:: revealjs-fragments

   .. note::

      There are cases not working regular.

   Inject ``fragment`` attribute into objects.
   Referer to `"Fragments" from Reveal.js <https://revealjs.com/fragments/>`_

   You can see `demo <https://attakei.github.io/sphinx-revealjs/en/#/5/1>`_ to know usage.

   .. rst:directive:option:: custom-effect
      :type: string

      When it is set, inject as custom class.
      You can customize behavior of fragments transitions with CSS.

   Example:

   Write block as directive that you want to present as fragments.

   .. code-block:: rst

      .. revealjs-fragments::

         * First
         * Second
         * Third

.. rst:directive:: revealjs-notes

   When you write this section, inner text are as content of `Speaker View <https://revealjs.com/speaker-view/>`_.

   If you write some directives on same-level, Reveal.js uses first directive only.

   .. note::

      You must be careful for comment block when you set :confval:`revealjs_notes_from_comments` in ``conf.py``.
      Reveal.js recognizes first ``<aside>`` element as content of speaker-view,
      so you may not see directive content as notes.

   Example:

   .. code-block:: rst

      .. revealjs-notes::

         This content output into <aside> element on <section>.
