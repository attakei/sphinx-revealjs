Using Reveal.js plugins
=======================

Description
-----------

``sphinx-revealjs`` can use Reveal.js plugins by ``revealjs_script_plugins`` in ``conf.py``

.. code-block:: python

   revealjs_script_plugins = [
       {
           "name": "RevealMath",
           "src": "revealjs4/plugin/math/math.js",
       },
   ]

Code highlighting
-----------------

.. code-block:: python

   revealjs_script_plugins = [
       {
           "name": "RevealHighlight",
           "src": "revealjs4/plugin/highlight/highlight.js",
       },
   ]

These codes are highlighting by ``RevealHighlight`` plugin.

.. revealjs-break::

.. revealjs-code-block:: rst
   :data-line-numbers: 1|2

   .. revealjs-code-block:: rst
      :data-line-numbers: 1|2

In this section, line-level highlighting works.

Speaker notes
-------------

.. code-block:: python

   revealjs_script_plugins = [
       {
           "name": "RevealNotes",
           "src": "revealjs4/plugin/notes/notes.js",
       },
   ]

This is used ``RevealNotes`` plugin, Please press ``S`` key to try it!

.. revealjs-break::

.. revealjs-notes::

   In this section, showing message from notes.

.. code-block:: rst

   .. revealjs-notes::

      In this section, showing message from notes.
