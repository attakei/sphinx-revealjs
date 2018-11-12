from sphinx.builders.html import StandaloneHTMLBuilder

from sphinx_revealjs.writers import RevealjsSlideTranslator


class RevealjsHTMLBuilder(StandaloneHTMLBuilder):
    name = 'revealjs'
    default_translator_class = RevealjsSlideTranslator
