"""Package entrypoint that fetch archive."""
import argparse
import tempfile
from pathlib import Path
from urllib.request import urlretrieve

from .themes import extract_package, get_default_revealjs, get_theme_path

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--force", action="store_true", default=False)
parser.add_argument("--workdir", default=None)
parser.add_argument("--theme", default="sphinx_revealjs")
parser.add_argument("--static-name", default="revealjs4")

args = parser.parse_args()

if args.workdir is None:
    args.workdir = tempfile.mkdtemp()
args.workdir = Path(args.workdir)

package = get_default_revealjs()
print(f"Fetch Reveal.js v{package['version']}")

local_archive = args.workdir / f"reveal.js-{package['version']}.tgz"
urlretrieve(package["resolved"], local_archive)

dest = get_theme_path(args.theme) / "static" / args.static_name
print(f"Extract into {dest}")
extract_package(local_archive, dest, args.force)
