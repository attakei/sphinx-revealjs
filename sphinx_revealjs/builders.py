from sphinx.builders.html import StandaloneHTMLBuilder

from sphinx_revealjs.writers import RevealjsSlideTranslator


class RevealjsHTMLBuilder(StandaloneHTMLBuilder):
    name = 'revealjs'
    default_translator_class = RevealjsSlideTranslator

    def get_theme_config(self):
        # type: () -> Tuple[unicode, Dict]
        theme_name = getattr(self.config, 'revealjs_theme', 'sphinx_revealjs')
        theme_options = getattr(self.config, 'revealjs_theme_options', {})
        print(theme_name, theme_options)
        return theme_name, theme_options
