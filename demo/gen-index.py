#!/usr/bin/env python
import argparse
from pathlib import Path

from jinja2 import Template

here = Path(__file__).parent

parser = argparse.ArgumentParser()
parser.add_argument("outdir", type=Path)


def main(args: argparse.Namespace):
    languages = ["en"] + [v.name for v in (here / "_locales").glob("*")]
    for tmpl_path in here.glob("*.html.j2"):
        tmpl = Template(tmpl_path.read_text())
        out_path: Path = args.outdir / tmpl_path.stem
        out_path.write_text(tmpl.render(languages=languages))


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
