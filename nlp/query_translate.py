from googletrans import Translator


class QueryTranslator(object):
    translator = Translator()

    def translate_input(self, query):
        translations = self.translator.translate(query, dest='en')
        return translations.text

    def translate_output(self, query):
        translations = self.translator.translate(query, dest='am')
        return translations.text
