import tree_sitter

from sourcy.doc import Document


class Parser(object):
    def __init__(self, lang, *args, **kwargs):
        self.lang = lang
        self.language = tree_sitter.Language("grammars/languages.so", f"{lang}")
        self.parser = tree_sitter.Parser()
        self.parser.set_language(self.language)
        pass

    def _create_tree(self, code):
        tree = self.parser.parse(bytes(code, "utf8"))
        return tree

    def _extract_tokens(self, code, tree):
        return self._traverse(code, tree)

    def __call__(self, code, *args, **kwargs):
        tree = self._create_tree(code)
        tokens, annotations = self._extract_tokens(code, tree)

        return Document(code, tokens, annotations)

    def _traverse(self, code, tree):
        tokens = []
        annotations = []

        def __traverse(code, node):
            if node.type != tree.root_node.type and len(node.children) == 0:
                token, annotation = self._extract_token_annotation(code, node)
                tokens.append(token)
                annotations.append(annotation)
            # if node.type in ["import_declaration", "package_declaration"]:
            #     token, annotation = self._extract_annotation(code, node.children[0])
            #     tokens.append(token)
            #     annotations.append(token)
            #
            #     token, annotation = self._extract_annotation(code, node.children[1])
            #     tokens.append(token)
            #     annotations.append(token)
            # else:
            for child in node.children:
                # if node.type != "program" and child.start_point == node.start_point \
                # and (child.start_point <= node.end_point or child.end_point <= node.end_point):
                #    continue
                __traverse(code, child)

        __traverse(code, tree.root_node)

        return tokens, annotations

    def _extract_token_annotation(self, code, node):
        token = code[node.start_byte:node.end_byte]
        annotations = node.type
        return token, annotations
