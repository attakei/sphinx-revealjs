=============================
Customize slide from document
=============================

Sphinx can manage multiple documents,
so that |THIS| can build multiple presentation slides.

If you want to configure one presentation from some,
write ``revealjs-slide`` directive into reST document.

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

