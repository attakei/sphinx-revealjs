"""Doctree transformer functions."""

from sphinx.util.docutils import nodes

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
