import re

from .parser import text2sqlParser

_VOCABULARY = [literal for literal in text2sqlParser.literalNames if literal != '<INVALID>']

def _word_is_allowed(word: str) -> bool:
    return ("'"+word+"'" in _VOCABULARY or
            re.match(r'\d+', word) is not None)

def filter_question_words(question: str) -> str: 
    return ' '.join([word.rstrip('.?!') for word in question.split() if _word_is_allowed(word)])
