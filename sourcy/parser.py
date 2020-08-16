from collections import deque

import tree_sitter

from sourcy.tokens.doc import Document
from sourcy.tokens.token import Token


class Parser(object):
    def __init__(self, lang, *args, **kwargs):
        self.lang = lang
        self.language = tree_sitter.Language("grammars/languages.so", f"{lang}")
        self.parser = tree_sitter.Parser()
        self.parser.set_language(self.language)

    def _create_tree(self, code):
        tree = self.parser.parse(bytes(code, "utf8"))
        return tree

    def __call__(self, code, *args, **kwargs):
        tree = self._create_tree(code)
        tokens = self._traverse(code, tree)

        return Document(code, tokens)

    def _traverse(self, code, tree):
        root = tree.root_node
        stack = deque()
        stack.append((root, None))

        tokens = []
        while len(stack):
            current, parent = stack.pop()

            if current.type != tree.root_node.type and len(current.children) == 0:
                token, annotation = self._extract_token_annotation(code, current)
                _, block_annotation = self._extract_token_annotation(code, parent)
                tokens.append(Token(token, annotation, block_annotation))
            for child in current.children:
                stack.append((child, current))

        return tokens[::-1]

    def _extract_token_annotation(self, code, node):
        token = code[node.start_byte:node.end_byte]
        annotations = node.type
        return token, annotations
