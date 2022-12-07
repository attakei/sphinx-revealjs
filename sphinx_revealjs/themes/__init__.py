"""Theme handle module."""
import json
import shutil
import tarfile
import tempfile
from pathlib import Path
from typing import Optional

here = Path(__file__).parent


def get_theme_path(name: str) -> Path:
    """Return directory real path of itself."""
    return here / name


def get_default_revealjs(src: Optional[Path] = None) -> dict:
    """Pick package file URL from package-lock.json."""
    if src is None:
        src = here / "package-lock.json"
    pkg = json.loads(src.read_text())
    deps = [m for n, m in pkg.get("dependencies", {}).items() if n == "reveal.js"]
    if len(deps) == 0:
        raise ValueError("Source file does not manage Reveal.js")
    return deps[0]


def extract_package(src: Path, dest: Path, replace: False):
    if dest.exists():
        if not replace:
            raise ValueError("Dest directry is already exists.")
        shutil.rmtree(dest)
    targets = {
        "package/css": "css",
        "package/dist": "dist",
        "package/plugin": "plugin",
        "package/LICENSE": "LICENSE",
    }
    extract_dir = Path(tempfile.mkdtemp())
    with tarfile.open(str(src)) as tr:
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
