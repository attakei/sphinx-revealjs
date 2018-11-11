from docutils import nodes


class revealjs_section(nodes.Structural, nodes.Element):
    def attributes_str(self):
        return ' '.join([
            f'{k}="{v}"'
            for k, v in self['meta'].items()])
