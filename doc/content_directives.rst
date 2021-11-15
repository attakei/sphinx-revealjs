==================
Content directives
==================

|THIS| provides features for contents of section.

.. rst:directive:: revealjs-code-block

   This is extends of :rst:dir:`code-block` direcrive for presentation.

   If you want to use ``data-line-number`` attributes in code-block.

   .. rst:directive:option:: data-line-numbers
      :type: string or no value

      Code highlighting pattern. See `Reveal.js document <https://revealjs.com/code/#line-numbers-%26-highlights>`_

   Example:

   .. code-block:: rst

      .. revealjs-code-block:: python
         :data-line-numbers: 1

         def hello():
             print("world")

.. rst:directive:: revealjs-fragments

   .. note::

      There are cases not working regular.

   Inject ``fragment`` attribute into objects.
   Referer to `"Fragments" from Reveal.js <https://revealjs.com/fragments/>`_

   Example:

   Write block as directive that you want to present as fragments.

   .. code-block:: rst

      .. revealjs-fragments::

         * First
         * Second
         * Third

   See `demo <https://attakei.github.io/sphinx-revealjs/#/5/1>`_

.. rst:directive:: revealjs_fragments

   Alias of ``revealjs-fragments`` for backward compatibility.

