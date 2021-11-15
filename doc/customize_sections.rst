==================
Customize sections
==================

To change behavior of sections, |THIS| provide some directives.

.. rst:directive:: revealjs-section

   To change behavior per section, write directive per section.

   .. rst:directive:option:: data-XXX

      This directive can accept attribute as same as Reveal.js ``section`` tags.

   Usage:

   Write ``revealjs-slide`` directive on directly below of section title header.

   .. code-block:: rst

      Title
      =====

      Section
      -------

      .. revealjs-section::
         :data-background-color: #009900

.. rst:directive:: revealjs_section

   Alias of ``revealjs-section`` for backward compatibility.


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

.. rst:directive:: revealjs_break

   Alias of ``revealjs-breaK`` For backward compatibility.
