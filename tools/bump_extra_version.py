#!/usr/bin/env python
"""Bump post version writer."""

import argparse
import configparser
from datetime import datetime
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("release_type", choices=["post", "dev"], default="post")


def calc_pre(release_type: str) -> str:
    """Generate post version number from timestamp."""
    cur = datetime.now()
    return f"{release_type}{int(cur.timestamp())}"


def bump_file(fpath: Path, current_version: str, next_version: str):
    """Change version string not using bump2version."""
    with fpath.open() as fp:
        raw = fp.read()
    with fpath.open("w") as fp:
        fp.write(raw.replace(current_version, next_version))


def main(args):  # noqa
    setup_cfg = configparser.ConfigParser()
    setup_cfg.read("setup.cfg")
    current_version = setup_cfg.get("bumpversion", "current_version")
    next_version = f"{current_version}.{calc_pre(args.release_type)}"
    # Find bump files and bumpversion
    for sec in setup_cfg.sections():
        if not sec.startswith("bumpversion:file:"):
            continue
        bump_file(Path(sec[17:]), current_version, next_version)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
