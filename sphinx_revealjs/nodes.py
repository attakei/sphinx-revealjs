from docutils import nodes


class FlagAttribute(object):
    pass


class revealjs_section(nodes.Structural, nodes.Element):
    def attributes_str(self):
        pair = []
        for k, v in self.attributes.items():
            if isinstance(v, FlagAttribute):
                pair.append(k)
                continue
            pair.append(f'{k}="{v}"')
        return ' '.join(pair)


class revealjs_break(nodes.Structural, nodes.Element):
    def attributes_str(self):
        pair = []
        for k, v in self.attributes.items():
            if isinstance(v, FlagAttribute):
                pair.append(k)
                continue
            pair.append(f'{k}="{v}"')
        return ' '.join(pair)


class revealjs_slide(nodes.Structural, nodes.Element):
    pass
