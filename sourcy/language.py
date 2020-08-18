from sourcy.parser import Parser
from sourcy.tokens.doc import Document


class Language(object):
    """
    Class containing the processing pipelines to apply on a source code of a specific language
    """

    def __init__(self, lang):
        self.parser = Parser(lang)

    def __call__(self, text, *args, **kwargs) -> Document:
        doc = self.make_doc(text)
        return doc

    def make_doc(self, text) -> Document:
        return self.parser(text)
