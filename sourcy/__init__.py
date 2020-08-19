from sourcy.language import Language

__author__ = """Cezar Sas"""
__email__ = 'cezar.sas@gmail.com'
__version__ = '__version__ = '0.1.2''


def load(lang: str, *args, **kwargs) -> Language:
    return Language(lang)
