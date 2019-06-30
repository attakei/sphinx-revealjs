#!/use/bin/env python
"""Fetch and sync reveal.js resources
"""
import shutil
import sys
from pathlib import Path
from urllib.request import urlretrieve
import tarfile


def validate_dir_state(target: Path) -> bool:
    expected = [
        'sphinx_revealjs',
    ]
    actually = all([(target / e).exists() for e in expected])
    return actually


def download_release(target: Path, version: str = '3.8.0') -> Path:
    target.mkdir(exist_ok=True)
    url = f"https://github.com/hakimel/reveal.js/archive/{version}.tar.gz"
    dest = target / f"revealjs-{version}.tgz"
    if not dest.exists():
        urlretrieve(url, str(dest))
    return dest


def extract_archive(target: Path) -> Path:
    with tarfile.open(str(target)) as tr:
        dir_name = tr.getmembers()[0].name
        tr.extractall(str(target.parent))
        return target.parent / dir_name


if __name__ == '__main__':
    base_dir = Path.cwd()
    valid = validate_dir_state(base_dir)
    if not valid:
        print('Nooo')
        sys.exit(1)
    downloaded = download_release(base_dir / 'var')
    extracted = extract_archive(downloaded)
    src_list = [
        'css',
        'js',
        'lib',
        'plugin',
        'LICENSE',
    ]
    dest_base = base_dir / 'sphinx_revealjs' \
        / 'themes' / 'sphinx_revealjs' / 'static' / 'revealjs'
    for src_ in src_list:
        src = extracted / src_
        dest = dest_base / src_
        if src.is_dir():
            shutil.rmtree(dest)
            shutil.copytree(src, dest)
        else:
            dest.unlink()
            shutil.copy2(src, dest)
