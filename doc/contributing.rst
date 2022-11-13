============
Contributing
============

Thank you for interested to ``sphinx-revealjs``.

.. todo:: Add USING, QUESTION and DOCUMENTATION

Conttribute code
================

Local development environment
-----------------------------

This is spec for development by author( ``attakei`` ) on 2022/08/27.

* Arch Linux
* Python 3.10.x
* Installed `pre-commit <https://pre-commit.com/>`_ globally

Setting up repo
---------------

After you clone forked Git repository, run commands to set up.

.. code-block:: console

   python tools/fetch_revealjs.py
   pre-commit install
   python -m venv venv
   venv/bin/pip install -e '.[test]'
