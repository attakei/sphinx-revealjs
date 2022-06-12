Interactive content
===================

Description
-----------

``sphinx-revealjs`` provides directives to show some interactive contents.

* ``revealjs-section``
* ``revealjs-break``
* ``revealjs-fragments``

Showing part of examples.

Animate source code transitions
-------------------------------

.. revealjs-section::
   :data-auto-animate:

Enable animations for each `revealjs-section` and `revealjs-break`:

.. code-block:: console
   :linenos:

   echo 'First part of my command'

.. revealjs-break::
   :data-auto-animate:

Enable animations for each `revealjs-section` and `revealjs-break`:

.. code-block:: console
   :linenos:

   echo 'First part of my command'
   echo 'Second part of my command'

Fragments
---------

This is support fragment with groups.

.. code-block:: rst

   .. revealjs-fragments::

      * First
      * Second
      * Third

.. revealjs-fragments::

   * First
   * Second
   * Third
