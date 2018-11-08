from docutils.nodes import Element, section, comment
from sphinx.writers.html5 import HTML5Translator


def has_child_sections(node: Element, name: str):
    nodes = set([n.tagname for n in node.children])
    return name in nodes


class RevealjsSlideTranslator(HTML5Translator):
    permalink_text = False

    def __init__(self, builder, *args, **kwds):
        super().__init__(builder, *args, **kwds)
        self.builder.add_permalinks = False
        self._proc_first_on_section = False

    def visit_section(self, node: section):
        self.section_level += 1
        if self.section_level == 1:
            self._proc_first_on_section = True
            self.body.append('<section>\n')
            return
        if self._proc_first_on_section:
            self._proc_first_on_section = False
            self.body.append('</section>\n')
        self.body.append('<section>\n')
        if has_child_sections(node, 'section'):
            self._proc_first_on_section = True
            self.body.append('<section>\n')

    def depart_section(self, node: section):
        self.section_level -= 1
        if self.section_level >= 1:
            self.body.append('</section>\n')

    def visit_comment(self, node: comment):
        self.body.append('<aside class="notes">\n')

    def depart_comment(self, node: comment):
        self.body.append('</aside>\n')
