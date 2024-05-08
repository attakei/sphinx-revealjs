"""Doctree transformer functions."""

from sphinx.application import Sphinx
from sphinx.util.docutils import nodes

from . import builders
from . import nodes as rj_nodes


def _calc_section_level(section: nodes.section) -> int:
    """Count 'section-level' that is numbers of sections until upgoing for root."""
    level = 1
    pt = section
    while not isinstance(pt.parent, nodes.document):
        if isinstance(pt.parent, nodes.section):
            level += 1
        pt = pt.parent
    return level


def rebuild_revealjs_structure(app: Sphinx, doctree: nodes.document, docname: str):
    """Transform from standard doctree to optimized for Reveal.js.

    This works only with 'revealjs' type builders.
    """
    if not isinstance(app.builder, builders.RevealjsHTMLBuilder):
        return
    bind_title_level(doctree)
    remap_sections(doctree)
    append_vertical_attributes(doctree)
    append_section_attributes(doctree)
    break_sections(doctree)
    fill_section_ids(doctree)


def bind_title_level(doctree: nodes.document) -> nodes.document:
    """Set heading level of titles.

    It need preserve level of titles
    because library restructures section using ``remap_sections``.
    """
    for title in doctree.findall(nodes.title):
        section = title.parent
        level = _calc_section_level(section)
        title.attributes["heading"] = level
    return doctree


def remap_sections(doctree: nodes.document) -> nodes.document:
    """Change struct of sections.

    When source can expression nested sections,
    docutils map node-tree for these:

    .. code:: text

       <document>
         <section>
           <title>
           <section>
             <title>
             <section>
               ...

    This function remaps tree for reveal.js style.

    .. code:: text

       <document>
         <section>
           <section>
             <title>
         <section>
           <section>
             <title>
           <section>
             ...

    If section-nests are more than 3 layers, remove nested section.
    """
    root_section = next(doctree.findall(nodes.section))
    for child in root_section.children.copy():
        if isinstance(child, nodes.section):
            root_section.parent.append(child)
            root_section.remove(child)
    for idx, top_section in enumerate(doctree.children.copy()):
        if not isinstance(top_section, nodes.section):
            continue
        wrapper_section = nodes.section()
        for child in list(top_section.children):
            if isinstance(child, nodes.section):
                wrapper_section.append(child)
                top_section.remove(child)
        wrapper_section.insert(0, top_section)
        doctree.remove(top_section)
        doctree.insert(idx, wrapper_section)

    # Trim 3 layered sections.
    for section in list(doctree.findall(nodes.section)):
        level = _calc_section_level(section)
        if level < 3:
            continue
        parent = section.parent
        parent += section.children
        parent.remove(section)

    return doctree


def append_section_attributes(doctree: nodes.document) -> nodes.document:
    """Find <revealj-section> nodes and delegate attributes into parent section for customize Revealjs.

    In current implementation,
    ``<revealj-section>`` with revealjs-type builder are used to inherit attribute into ``<section``,
    and remove itself.
    """  # noqa: E501
    for node in list(doctree.findall(rj_nodes.revealjs_section)):
        section = node.parent
        section.attributes["revealjs"] = node.attributes_str()
        section.remove(node)

    return doctree


def append_vertical_attributes(doctree: nodes.document) -> nodes.document:
    """Find <revealj-vertical> nodes and delegate attributes into parent section for customize Revealjs.

    In current implementation,
    ``<revealj-section>`` with revealjs-type builder are used to inherit attribute into ``<section``,
    and remove itself.
    """  # noqa: E501
    for node in list(doctree.findall(rj_nodes.revealjs_vertical)):
        target = node.parent.parent
        target.attributes["revealjs"] = node.attributes_str()
        node.parent.remove(node)

    return doctree


def break_sections(doctree: nodes.document) -> nodes.document:
    """Find <revealjs-break> nodes and split sections by found nodes as delimiter."""
    for node in list(doctree.findall(rj_nodes.revealjs_break)):
        vsec = node.parent.parent
        base = node.parent
        new_section = nodes.section()
        new_section.attributes["revealjs"] = node.attributes_str()
        if "notitle" not in node.attributes:
            new_section.append(next(base.findall(nodes.title)).deepcopy())
        can_move = False
        for child in base.children.copy():
            if child is node:
                can_move = True
                continue
            if can_move:
                new_section.append(child)
                base.remove(child)
        base.remove(node)
        vsec.insert(vsec.index(base) + 1, new_section)

    return doctree


def fill_section_ids(doctree: nodes.document) -> nodes.document:
    """Set required attributes into all section nodes.

    This is to render in writer.
    This is skipped if section has attributes already.
    """
    for vsec in doctree.children:
        if not isinstance(vsec, nodes.section):
            continue
        if vsec.attributes["ids"]:
            continue
        idx = doctree.index(vsec)
        label = f"revealj-section-{idx + 1}"
        vsec["ids"].append(label)
        for section in vsec.children:
            if not isinstance(section, nodes.section):
                continue
            if section.attributes["ids"]:
                continue
            idx = vsec.index(section)
            section["ids"].append(f"{label}-{idx + 1}")
    return doctree