from docutils.nodes import Element, section, comment, literal_block
from sphinx.writers.html5 import HTML5Translator


def has_child_sections(node: Element, name: str):
    nodes = set([n.tagname for n in node.children])
    return name in nodes


def find_child_section(node: Element, name: str):
    for n in node.children:
        if n.tagname == name:
            return n
    return None


class RevealjsSlideTranslator(HTML5Translator):
    permalink_text = False

    def __init__(self, builder, *args, **kwds):
        super().__init__(builder, *args, **kwds)
        self.builder.add_permalinks = False
        self._proc_first_on_section = False

    def visit_section(self, node: section):
        self.section_level += 1
        meta = find_child_section(node, 'revealjs_section')
        if meta is not None:
            attrs = meta.attributes_str()
        else:
            attrs = ''
        if self.section_level == 1:
            slide_meta = find_child_section(node, 'revealjs_slide')
            if slide_meta:
                print('koko')
                self.builder.revealjs_slide = slide_meta
            self._proc_first_on_section = True
            self.body.append('<section>\n')
            return
        if self._proc_first_on_section:
            self._proc_first_on_section = False
            self.body.append('</section>\n')
        self.body.append(f"<section {attrs}>\n")
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

    def visit_literal_block(self, node: literal_block):
        lang = node['language']
        self.body.append(
            f'<pre><code data-trim data-noescape class="{lang}">\n')

    def depart_literal_block(self, node: literal_block):
        self.body.append('</code></pre>\n')


def not_write(self, node):
    """visit/depart function for declare "no write"
    """
    pass
