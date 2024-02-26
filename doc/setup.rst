=====
Setup
=====

Requirements
============

|THIS| requires Python 3.7+ and Sphinx 4.0+.

Current development environment
-------------------------------

* Python: ``3.11.x``
* Sphinx: ``5.3.0``


Installation
============

You can install |THIS| from PyPI.

.. code-block:: shell

   $ pip install sphinx-revealjs

|THIS| specify ``Sphinx`` and ``docutils`` expressly as dependencies.
You get ``Sphinx`` by this command only.

Configuration
=============

|THIS| does not provide ``revealjs`` builder instead of ``html`` builder.
To use builder, edit your ``conf.py``.

.. code-block:: python

   extensions = [
       "sphinx_revealjs",
   ]

if you want to configure more,
edit conf.py with seeing :doc:`./configurations`.

Build
=====

Run ``make`` command to build presentations.
Files are generated to **revealjs** folder.

.. code-block:: shell

   $ make revealjs

You can generate all pages as ``index.html`` to use ``dirrevealjs``.

.. code-block:: console

   make dirrevealjs
