Customize section behavior
==========================

Description
-----------

``sphinx-revealjs`` provides custom directives to customize behavior of sections.

* ``revealjs-section``
* ``revealjs-break``

Showing part of examples.

Change background color
-----------------------

.. revealjs-section::
   :data-background-color: #009900

.. code-block:: rst

   .. revealjs-section::
      :data-background-color: #009900

.. revealjs-break::
   :data-background-gradient: linear-gradient(to bottom, #283b95, #17b2c3)

.. code-block:: rst

   .. revealjs-section::
      :data-background-gradient: linear-gradient(to bottom, #283b95, #17b2c3)

Set background image
--------------------

.. revealjs-section::
   :data-background-image: _static/icon-attakei.jpg
   :data-background-size: contain

.. code-block:: rst

   .. revealjs-section::
      :data-background-image: _static/icon-attakei.jpg
      :data-background-size: contain

Change transition(before)
-------------------------

.. revealjs-section::
   :data-transition: none

.. code-block:: rst

   .. revealjs-section::
      :data-transition: none

Change transition(after)
------------------------

.. revealjs-section::
   :data-transition: concave

.. code-block:: rst

   .. revealjs-section::
      :data-transition: concave

Non-title section
-----------------

First

.. code-block:: rst

   Keep title without duplicated written
   -------------------------------------

   First

   .. revealjs-break::
      :notitle:

   Second

.. revealjs-break::
   :notitle:

Second

.. code-block:: rst

   Keep title without duplicated written
   -------------------------------------

   First

   .. revealjs-break::
      :notitle:

   Second
