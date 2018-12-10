from sphinx.builders.html import StandaloneHTMLBuilder

from sphinx_revealjs.writers import RevealjsSlideTranslator


class RevealjsHTMLBuilder(StandaloneHTMLBuilder):
    name = 'revealjs'
    default_translator_class = RevealjsSlideTranslator

    def __init__(self, app):
        super().__init__(app)
        self.revealjs_slide = None

    def get_theme_config(self):
        # type: () -> Tuple[unicode, Dict]
        theme_name = getattr(self.config, 'revealjs_theme', 'sphinx_revealjs')
        theme_options = getattr(self.config, 'revealjs_theme_options', {})
        return theme_name, theme_options

    def get_doc_context(self, docname, body, metatags):
        ctx = super().get_doc_context(docname, body, metatags)
        if self.revealjs_slide:
            ctx['revealjs_slide'] = self.revealjs_slide.attributes
        return ctx
