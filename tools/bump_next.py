# --------------------------------------
# Bump next preversion writer
# --------------------------------------
import argparse
from datetime import datetime
from pathlib import Path
import configparser


def calc_pre():
    cur = datetime.now()
    return f'next{int(cur.timestamp())}'


def bump_file(fpath, current_version, next_version):
    with fpath.open() as fp:
        raw = fp.read()
    with fpath.open('w') as fp:
        fp.write(raw.replace(current_version, next_version))


def main():
    setup_cfg = configparser.ConfigParser()
    setup_cfg.read('setup.cfg')
    current_version = setup_cfg.get('bumpversion', 'current_version')
    next_version = f'{current_version}-{calc_pre()}'
    bump_file(
        Path('setup.py'), current_version, next_version)
    bump_file(
        Path('sphinx_revealjs/__init__.py'), current_version, next_version)


if __name__ == '__main__':
    main()
