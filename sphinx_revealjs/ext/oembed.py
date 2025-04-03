"""Extension to inject oEmbed items for presentations.

This is optional extension.
You need install extra and configure to use it.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING

from docutils import nodes
from sphinx.util.logging import getLogger

if TYPE_CHECKING:
    from typing import Any, Optional

    from sphinx.application import Sphinx

from .. import __version__ as core_version

logger = getLogger(__name__)
_targets: dict[str, dict[str, str]] = dict()


def create_oembed_content(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: Optional[nodes.document],
) -> None:
    if not doctree:
        return

    def _get_title(doctree: nodes.document) -> str:
        s_idx = doctree.first_child_matching_class(nodes.section)
        section = doctree.children[s_idx]  # type: ignore[index]
        t_idx = section.first_child_matching_class(nodes.title)  # type: ignore[attr-defined]
        title = section.children[t_idx]
        return title.astext()

    def _calc_size(context: dict[str, Any]) -> tuple[int, int]:
        width = 960
        height = 700

        if "revealjs" in context:
            conf = json.loads(context["revealjs"].script_conf)
            width = conf.get("width", width)
            height = conf.get("height", height)
        if "revealjs_page_confs" in context:
            for conf_json in context["revealjs_page_confs"]:
                conf = json.loads(conf_json)
                width = conf.get("width", width)
                height = conf.get("height", height)

        return width, height

    content_path = f"{app.config.revealjs_oembed_outdir}/{pagename}.json"
    content_fullpath = Path(app.outdir) / content_path
    content_url = f"{app.config.revealjs_oembed_urlbase}/{content_path}"

    title = _get_title(doctree)
    width, height = _calc_size(context)
    url = f"{app.config.revealjs_oembed_urlbase}/{pagename}.html"
    html = f'<iframe src="{url}" title="{title}" width="{width}" height="{height}"></iframe>'
    data = {
        "type": "rich",
        "version": "1.0",
        "title": title,
        "width": width,
        "height": height,
        "html": html,
    }

    content_fullpath.parent.mkdir(parents=True, exist_ok=True)
    content_fullpath.write_text(json.dumps(data))

    metatags = context.get("metatags", "")
    metatags += f'<link rel="alternate" type="application/json+oembed" href="{content_url}?url=self" title="{title}" />'
    context["metatags"] = metatags


def setup(app: Sphinx):
    """Entrypoint."""
    app.add_config_value("revealjs_oembed_urlbase", "http://localhost:8000", "env")
    app.add_config_value("revealjs_oembed_outdir", "_files/oembed", "env")
    app.add_config_value("revealjs_oembed_excludes", [], "env")
    app.connect("html-page-context", create_oembed_content)
    return {
        "version": core_version,
        "env_version": 1,
        "parallel_read_safe": True,
    }
