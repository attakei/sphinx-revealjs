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

Enable animations for each ``revealjs-section`` and ``revealjs-break``:

.. code-block:: console
   :linenos:

   echo 'First part of my command'

.. revealjs-break::
   :data-auto-animate:

Enable animations for each ``revealjs-section`` and ``revealjs-break``:

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

.. revealjs-break::

You can customize behavior of fragments.

.. code-block:: rst

   .. revealjs-fragments::
      :custom-effect: blur

      * First
      * Second
      * Third

.. code-block:: css

   // For custom effect of fragments
   .fragment.blur {
     filter: blur(5px);
   }
   .fragment.blur.visible {
     filter: none;
   }

.. revealjs-break::

You can customize behavior of fragments.

.. code-block:: rst

   .. revealjs-fragments::
      :custom-effect: blur

      * First
      * Second
      * Third

.. revealjs-fragments::
   :custom-effect: blur

   * First
   * Second
   * Third

.. revealjs-break::

Using ``container`` directive, you can work stack layouting.

.. code-block:: rst

   .. container:: r-stack

      .. revealjs-fragments::

         .. image:: https://picsum.photos/450/300

         .. image:: https://picsum.photos/300/450

         .. image:: https://picsum.photos/400/400

.. revealjs-break::

Using ``container`` directive, you can work stack layouting.

.. container:: r-stack

   .. revealjs-fragments::

      .. image:: https://picsum.photos/450/300

      .. image:: https://picsum.photos/300/450

      .. image:: https://picsum.photos/400/400
