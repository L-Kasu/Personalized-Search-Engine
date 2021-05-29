# implementation of the tf-idf algorithm (ranked retrieval)
# version: alpha0.1
# author: Niklas Munkes


import numpy as np


def log_weighted_term_frequency(term: str, document: list) -> float:
    raw_tf = 0
    for item in document:
        if item == term:
            raw_tf += 1
    if raw_tf > 0:
        return 1 + np.log10(raw_tf)
    return 0


def terms_not_in_document(document: list, query: list) -> bool:
    for term in query:
        if term in document:
            return True
    return False


def score_document_query(document: list, query: list) -> float:
    if terms_not_in_document(document, query):
        return 0
    score = 0
    for term in list(set(document) & set(query)):
        score = score + (1 + log_weighted_term_frequency(term, document))
    return score
