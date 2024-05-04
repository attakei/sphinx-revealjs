"""Doctree transformer functions."""

from sphinx.util.docutils import nodes


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

    return doctree
