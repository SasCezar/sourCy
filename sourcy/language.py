from sourcy.parser import Parser


class Language(object):
    """
    Class containing the processing pipelines to apply on a source code of a specific language
    """

    def __init__(self, lang):
        self.parser = Parser(lang)

    def __call__(self, text, *args, **kwargs):
        doc = self.make_doc(text)
        return doc

    def make_doc(self, text):
        return self.parser(text)
