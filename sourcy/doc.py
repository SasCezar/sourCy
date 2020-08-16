class Document(object):
    def __init__(self, code, tokens, annotations, *args, **kwargs):
        self.code = code
        self.tokens = tokens

    @property
    def tokens(self):
        return self.tokens

    @property
    def code(self):
        return self.code

    @tokens.setter
    def tokens(self, value):
        self._language = value

    @code.setter
    def code(self, value):
        self._code = value
