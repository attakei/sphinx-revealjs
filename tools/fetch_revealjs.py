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
from pathlib import Path
from urllib.request import urlretrieve

ROOT_DIR = Path(__file__).parent.parent.absolute()

RULE = {
    "name": "reveal.js",
    "src": ["css", "dist", "plugin", "LICENSE"],
    "dest": "sphinx_revealjs/themes/sphinx_revealjs/static/revealjs4",
}


def find_package(src: Path, name: str) -> dict:
    """Pick package file URL from package-lock.json."""
    package_lock = json.loads(src.read_text())
    deps = [m for n, m in package_lock.get("dependencies", {}).items() if n == name]
    if len(deps) == 0:
        raise ValueError(f"Invalid name: ({name})")
    return deps[0]


def extract_archive(target: Path) -> Path:  # noqa: D103
    dest = target.parent / target.stem
    with tarfile.open(str(target)) as tr:
        tr.extractall(str(dest))
    return dest


def main():  # noqa: D103
    package_lock_json = ROOT_DIR / "package-lock.json"
    package = find_package(package_lock_json, RULE["name"])
    local_archive = ROOT_DIR / "var" / f"{RULE['name']}-{package['version']}.tgz"
    if not local_archive.exists():
        urlretrieve(package["resolved"], local_archive)
    extracted = extract_archive(local_archive) / "package"
    dest_base = ROOT_DIR / RULE["dest"]
    dest_base.mkdir(parents=True, exist_ok=True)
    for src_ in RULE["src"]:
        src = extracted / src_
        dest = ROOT_DIR / RULE["dest"] / src_
        if dest.exists():
            if dest.is_file():
                dest.unlink()
            else:
                shutil.rmtree(dest)
        if src.is_dir():
            shutil.copytree(src, dest)
        else:
            shutil.copy2(src, dest)


if __name__ == "__main__":
    if Path.cwd() != ROOT_DIR:
        logging.error("This script can run only project root.")
        sys.exit(1)
    (ROOT_DIR / "var").mkdir(exist_ok=True)
    main()
