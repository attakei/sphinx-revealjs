===============
Local workspace
===============

This is guide to setup as "source code install".
It is usefull to use with private patch by yourself.

When you will develop for bug fix or new features,
please setup local repository by this document.

Overview
========

.. todo:: TBD

Notice
------

This project uses ``uv`` to configure development environment.

But you cannot ``uv sync``,
because this has missmatch of ``requires-python`` of this and dependencies.

Development tools
=================

This project uses these tools to management.

* pre-commit (to manage git hooks)
* uv >= 0.6.0 (to manage inner of python project)

.. todo:: Future plans

   * Lefthook (to manage git hooks instead of pre-commit)
   * go-task (project workflow excluded GitHub Actions)

Use mise (reccomended)
----------------------

I use `mise <https://mise.jdx.dev/>`_ to manage tools outside of python.
If you use mise, you can setup by only ``mise install``.

Setup workspace
===============

.. note:: After ``git clone``.

#. Set up hooks by ``pre-commit install``.
#. Create virtualenv by ``uv venv``.
#. Get Reveal.js assets by ``uv run --no-sync tools/fetch_revealjs.py``.
#. Install dependencies by ``uv pip install -e .[doc,test]``.

   * If you want to develop for screenshot options,
     append ``screenshot`` optional and run ``uv run --no-sync playwright install``.

#. Verify workspace by ``uv run --no-sync pytest``.

   * If it runs on Windows and it does not install **libmagic**,
     append ``--ignore=tests/test_extensions/test_screenshot.py`` into pytest command.

When you are developing for pull-request,
Please keep green for pytest and pre-commit.
