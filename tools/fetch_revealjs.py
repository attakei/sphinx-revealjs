#!/use/bin/env python
"""Fetch and sync reveal.js resources.

This script need to run these case.

* After editable install
* Before build package archibves
"""
import logging
import shutil
import sys
import tarfile
from pathlib import Path
from urllib.request import urlretrieve

ROOT_DIR = Path(__file__).parent.parent.absolute()

RULES = [
    {
        "version": "4.0.2",
        "src": ["dist", "plugin", "LICENSE"],
        "dest": "sphinx_revealjs/themes/sphinx_revealjs/static/revealjs4",
    }
]


def download_release(target: Path, version: str) -> Path:  # noqa: D103
    target.mkdir(exist_ok=True)
    url = f"https://github.com/hakimel/reveal.js/archive/{version}.tar.gz"
    dest = target / f"revealjs-{version}.tgz"
    if not dest.exists():
        urlretrieve(url, str(dest))
    return dest


def extract_archive(target: Path) -> Path:  # noqa: D103
    with tarfile.open(str(target)) as tr:
        dir_name = tr.getmembers()[0].name
        tr.extractall(str(target.parent))
        return target.parent / dir_name


def main():  # noqa: D103
    for rule in RULES:
        downloaded = download_release(ROOT_DIR / "var", rule["version"])
        extracted = extract_archive(downloaded)
        dest_base = ROOT_DIR / rule["dest"]
        dest_base.mkdir(parents=True, exist_ok=True)
        for src_ in rule["src"]:
            src = extracted / src_
            dest = ROOT_DIR / rule["dest"] / src_
            if dest.exists():
                shutil.rmtree(dest)
            if src.is_dir():
                shutil.copytree(src, dest)
            else:
                shutil.copy2(src, dest)


if __name__ == "__main__":
    if Path.cwd() != ROOT_DIR:
        logging.error("This script can run only project root.")
        sys.exit(1)
    main()
