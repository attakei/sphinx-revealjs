# --------------------------------------
# Bump post version writer
# --------------------------------------
import argparse
from datetime import datetime
from pathlib import Path
import configparser


def calc_pre():
    cur = datetime.now()
    return f'post{int(cur.timestamp())}'


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
    # Find bump files and bumpversion
    for sec in setup_cfg.sections():
        if not sec.startswith("bumpversion:file:"):
            continue
        bump_file(
            Path(sec[17:]), current_version, next_version)


if __name__ == '__main__':
    main()
