Multi column section
====================

Description
-----------

On one section, display multi-column layout.

Sources
-------

If you want to show multi-column contents in section,
need ``container`` directive and custom CSS.

``presentation.rst``

.. code-block:: rst

   Section title
   =============

   .. container:: flex

      .. container:: half

         Left side content

      .. container:: half

         Right side content

``custom.css``

.. code-block:: css

   div.flex {
     display: flex;
   }

   div.flex div.half {
     width: 50% !important;
     flex: 1;
   }

``conf.py``

.. code-block:: python

   revealjs_css_files = [
       "custom.css"
   ]

Outputs
-------

Generate section content like these(exclude borders)

+----------------------------------------+
| Section title                          |
+-------------------+--------------------+
| Left side content | Right side content |
+-------------------+--------------------+

if you want to see more real using example, see it.

* `RST source <https://gitlab.com/attakei.net/slides/pyconjp-2019/-/blob/master/_includes/whoami-201909-public.rst>`_
* `CSS(SASS) source <https://gitlab.com/attakei.net/slides/pyconjp-2019/-/blob/master/_sass/_layout.scss#L54>`_
* `Generated presentation <https://attakei.net/slides/pyconjp-2019/#/1/1>`_
