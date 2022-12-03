#!/usr/bin/env python
"""Fetch and sync reveal.js resources.

This script need to run these case.

* After editable install
* Before build package archibves
"""
import json
import logging
import shutil
import sys
import tarfile
import tempfile
from pathlib import Path
from typing import Dict
from urllib.request import urlretrieve

ROOT_DIR = Path(__file__).parent.parent.absolute()

RULE = {
    "name": "reveal.js",
    "targets": {
        "package/css": "css",
        "package/dist": "dist",
        "package/plugin": "plugin",
        "package/LICENSE": "LICENSE",
    },
    "dest": "sphinx_revealjs/themes/sphinx_revealjs/static/revealjs4",
}


def find_package(src: Path, name: str) -> dict:
    """Pick package file URL from package-lock.json."""
    package_lock = json.loads(src.read_text())
    deps = [m for n, m in package_lock.get("dependencies", {}).items() if n == name]
    if len(deps) == 0:
        raise ValueError(f"Invalid name: ({name})")
    return deps[0]


def extract_archive(source: Path, dest: Path, targets: Dict[str, str]):  # noqa: D103
    extract_dir = Path(tempfile.mkdtemp())
    with tarfile.open(str(source)) as tr:
        for trf in tr.getmembers():
            is_target = False
            for name in targets.keys():
                if trf.name.startswith(f"{name}"):
                    is_target = True
                    continue
            if not is_target:
                continue
            tr.extract(trf, extract_dir)
    for s, d in targets.items():
        func = shutil.copytree if (extract_dir / s).is_dir() else shutil.copyfile
        func(extract_dir / s, dest / d)


def main():  # noqa: D103
    package_lock_json = ROOT_DIR / "package-lock.json"
    package = find_package(package_lock_json, RULE["name"])
    local_archive = ROOT_DIR / "var" / f"{RULE['name']}-{package['version']}.tgz"
    if not local_archive.exists():
        urlretrieve(package["resolved"], local_archive)
    extract_archive(local_archive, Path() / RULE["dest"], RULE["targets"])


if __name__ == "__main__":
    if Path.cwd() != ROOT_DIR:
        logging.error("This script can run only project root.")
        sys.exit(1)
    (ROOT_DIR / "var").mkdir(exist_ok=True)
    main()
