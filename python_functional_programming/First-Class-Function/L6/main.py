import functools
from typing import List


def join(doc_so_far: str, sentence: str) -> str:
    return doc_so_far + "." + " " + sentence


def join_first_sentences(sentences: List[str], n: int) -> str:
    if n == 0:
        return ""
    joined_sentence = functools.reduce(join, sentences[:n])
    return joined_sentence + "."