"""SASS compile bridge.

Some features of this are copied from https://github.com/attakei-lab/sphinxcontrib-sass/blob/main/sphinxcontrib/sass.py
"""

from __future__ import annotations

import subprocess
from os import PathLike
from pathlib import Path
from typing import TYPE_CHECKING

from sphinx.util import logging

from .dart_sass import setup_dart_sass

if TYPE_CHECKING:
    from typing import Optional, Union

    from sphinx.application import Sphinx
    from sphinx.environment import BuildEnvironment

SUB_ROOT = Path(__file__).parent

Targets = dict[PathLike, PathLike]


logger = logging.getLogger(__name__)


def configure_path(conf_dir: PathLike, src: Optional[Union[PathLike, Path]]) -> Path:
    if src is None:
        target = Path(conf_dir)
    elif isinstance(src, Path):
        target = src
    else:
        target = Path(src)
    if not target.is_absolute():
        target = Path(conf_dir) / target
    return target


def build_sass_sources(app: Sphinx, env: BuildEnvironment):
    sass_bin = setup_dart_sass("1.86.0", SUB_ROOT)
    logger.debug("Building stylesheet files")
    src_dir = configure_path(app.confdir, app.config.sass_src_dir)
    out_dir = configure_path(app.confdir, app.config.sass_out_dir)

    options = [f"--style={app.config.sass_output_style}"]
    if app.config.sass_include_paths:
        options += [f"--load-path={p}" for p in app.config.sass_include_paths]

    targets: Targets = app.config.sass_targets
    if app.config.sass_auto_targets:
        for s in src_dir.glob("*.s[ac]ss"):
            if s.name.startswith("_"):
                continue
            rel_src = s.relative_to(src_dir)
            rel_dst = rel_src.parent / f"{rel_src.stem}.css"
            targets[rel_src] = rel_dst

    for src, dst in targets.items():
        src_ = src_dir / src
        out_path = out_dir / dst
        out_path.parent.mkdir(exist_ok=True, parents=True)
        subprocess.run([str(sass_bin), *options, f"{src_}:{out_path}"])


def setup(app: Sphinx):
    app.add_config_value("sass_include_paths", [], "html")
    app.add_config_value("sass_src_dir", None, "html")
    app.add_config_value("sass_out_dir", None, "html")
    app.add_config_value("sass_targets", {}, "html")
    app.add_config_value("sass_output_style", "expanded", "html")
    app.add_config_value("sass_auto_targets", False, "html")
    app.connect("env-updated", build_sass_sources)
