class Document(object):
    """
    A sequence of :class: 'tokens.token.Token' containing the annotations for the source code
    """

    def __init__(self, code, tokens, *args, **kwargs):
        """

        :param code:
        :param tokens:
        :param args:
        :param kwargs:
        """
        self._code = code
        self._tokens = tokens

    @property
    def tokens(self):
        return self._tokens

    @property
    def code(self):
        return self._code

    @tokens.setter
    def tokens(self, value):
        self._language = value

    @code.setter
    def code(self, value):
        self._code = value

    def __getitem__(self, item):
        yield self.tokens[item]

    def __iter__(self):
        for token in self.tokens:
            yield token

    def __len__(self):
        return len(self.tokens)