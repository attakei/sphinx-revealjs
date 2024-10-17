Using Reveal.js plugins
=======================

Description
-----------

``sphinx-revealjs`` can use Reveal.js plugins by ``revealjs_script_plugins`` in ``conf.py``

.. code-block:: python

   revealjs_script_plugins = [
       {
           "name": "RevealMath",
           "src": "revealjs/plugin/math/math.js",
       },
   ]

Code highlighting
-----------------

.. code-block:: python

   revealjs_script_plugins = [
       {
           "name": "RevealHighlight",
           "src": "revealjs/plugin/highlight/highlight.js",
       },
   ]

These codes are highlighting by ``RevealHighlight`` plugin.

.. revealjs-break::

.. code-block:: rst

   .. code-block:: python

      print("hello world")

You can use ``code-block`` and ``literalinclude`` for code highlighting.

.. revealjs-break::

.. revealjs-code-block:: rst
   :data-line-numbers: 1|2

   .. revealjs-code-block:: rst
      :data-line-numbers: 1|2

      print("hello world")

Using ``revealjs-code-block``, line-level highlighting works.

.. revealjs-break::

.. revealjs-literalinclude:: ./conf.py
   :language: python
   :lines: 45-58
   :data-line-numbers: 2-5|6-7|10-13

You can include other file with step-by-step highlighting by ``revealjs-literalinclude``.

.. revealjs-break::

.. code-block:: rst

   .. revealjs-code-block:: python
      :data-ln-start-from: 47

.. revealjs-code-block:: python
   :data-ln-start-from: 47

   revealjs_script_plugins = [
       {
           "name": "RevealHighlight",
           "src": "revealjs/plugin/highlight/highlight.js",
       },
   ]

You can use ``data-ln-start-from`` for display line numbers from specify value.

.. revealjs-break::

.. revealjs-literalinclude:: ./conf.py
   :data-ln-start-from: 47
   :lines: 47-60

``revealjs-literalinclude`` can use it too.

Speaker notes
-------------

.. code-block:: python

   revealjs_script_plugins = [
       {
           "name": "RevealNotes",
           "src": "revealjs/plugin/notes/notes.js",
       },
   ]

This is used ``RevealNotes`` plugin, Please press ``S`` key to try it!

.. revealjs-break::

.. revealjs-notes::

   In this section, showing message from notes.

.. code-block:: rst

   .. revealjs-notes::

      In this section, showing message from notes.
