from docutils import nodes


class FlagAttribute(object):
    pass


class SectionTagRenderer(object):
    def attributes_str(self):
        pair = []
        for k, v in self.attributes.items():
            if not k.startswith('data-'):
                continue
            if isinstance(v, FlagAttribute):
                pair.append(k)
                continue
            pair.append(f'{k}="{v}"')
        return ' '.join(pair)


class revealjs_section(SectionTagRenderer, nodes.Structural, nodes.Element):
    pass


class revealjs_break(SectionTagRenderer, nodes.Structural, nodes.Element):
    pass


class revealjs_slide(nodes.Structural, nodes.Element):
    pass
