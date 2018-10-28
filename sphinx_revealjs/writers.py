from docutils.nodes import Node
from sphinx.writers.html5 import HTML5Translator


class RevealjsSlideTranslator(HTML5Translator):
    def __init__(self, builder, *args, **kwds):
        super().__init__(builder, *args, **kwds)
        self._on_zero_section = True

    def visit_section(self, node: Node):
        self.section_level += 1
        if self.section_level == 1 and self._on_zero_section:
            self.body.append('<section>\n')
        if self.section_level == 2 and self._on_zero_section:
            self._on_zero_section = False
            self.body.append('</section>\n')
        self.body.append(
            self.starttag(node, 'section'))

    def depart_section(self, node: Node):
        self.section_level -= 1
        self.body.append('</section>\n')
