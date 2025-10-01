"""Design root.

We can use this package.

* Import as package to use function.
* Load as Sphinx extension.

If you add as Sphinx extensions,
Sphinx will load all sub packages.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ... import __version__

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def setup(app: Sphinx):
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": False,
    }
