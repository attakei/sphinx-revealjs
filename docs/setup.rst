.. |THIS| replace:: ``sphinx-revealjs``

=====
Setup
=====

Requirements
============

|THIS| requires Python 3.6+, Sphinx and make.

Latest development environment
------------------------------

* Python

  * 3.6.x
  * 3.7.x

* Sphinx

  * 1.8.2


Installation
============

Because |THIS| is registered in PyPI, you can install this by ``pip`` .

.. code-block:: shell

   $ pip install sphinx-revealjs

|THIS| specify ``Sphinx`` and ``docutils`` expressly as dependencies.
You get ``Sphinx`` by this command only.

Configuration
=============

|THIS| does not have ``html`` builder but ``revealjs`` builder.
To use builder, edit your ``conf.py``.

.. code-block:: python

   extensions = [
       'sphinx_revealjs',
   ]

if you want to configure more, edit conf.py with seeing settings page.

Build
=====

Run ``make`` command to build presentations.
Files are generated to **revealjs** folder.

.. code-block:: shell

   $ make revealjs

