from sphinx.builders.html import StandaloneHTMLBuilder


class RevealjsHTMLBuilder(StandaloneHTMLBuilder):
    name = 'revealjs'
    revealjs = {}
