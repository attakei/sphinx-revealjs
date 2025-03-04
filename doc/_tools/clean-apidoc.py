import shutil
import sys
from pathlib import Path


def main(argv: list[str]):
    targets = [Path(a).resolve() for a in argv]
    for t in targets:
        shutil.rmtree(t)


if __name__ == "__main__":
    main(sys.argv[1:])
