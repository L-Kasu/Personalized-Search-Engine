# implementation of the tf-idf algorithm (ranked retrieval)
# version: alpha0.8
# author: Niklas Munkes
import sys

import numpy as np
from pp_file_reader import file_reader
# from pp_main import dir_output, taskstring_1, taskstring_2, filename

dir_output = "./PP_output/"
taskstring_1 = "tnwp"
taskstring_2 = "tn"
filename = "CISI.ALL"

document_dict_ts1 = file_reader(dir_output + "pp_output_" + taskstring_1 + "_" + filename + ".txt")
document_dict_ts2 = file_reader(dir_output + "pp_output_" + taskstring_2 + "_" + filename + ".txt")
# print(document_dict_ts1, flush='left')
print(document_dict_ts2, flush='left')
# searchterm = "literature"
# searchterm = "cat"
sample_qry = ["certificates", "literature", "the", "for"]


def term_frequency(term: str, document: list) -> float:
    tf = 0
    for item in document:
        if item == term:
            tf += 1
    return tf


def log_weighted_term_frequency(term: str, document: list) -> float:
    raw_tf = term_frequency(term, document)
    if raw_tf > 0:
        return 1 + np.log10(raw_tf)
    return 0


def terms_not_in_document(document: list, query: list) -> bool:
    for term in query:
        if term in document:
            return True
    return False


def score_dq_log_tf(document: list, query: list) -> float:
    if terms_not_in_document(document, query):
        return 0
    score = 0
    for term in list(set(document) & set(query)):
        score = score + (1 + log_weighted_term_frequency(term, document))
    return score


def document_frequency(term: str, doc_dicts: list) -> int:
    freq_of_term = 0
    for i in range(0, len(doc_dicts)):
        curr_doc_dict = doc_dicts[i]
        for key in curr_doc_dict:
            if key == 'W':
                for item in curr_doc_dict[key]:
                    if item == term:
                        freq_of_term += 1
    return freq_of_term

# print(document_frequency(searchterm, document_dict_ts1))
# print(document_frequency(searchterm, document_dict_ts2))


def max_possible_df(doc_dicts: list) -> int:
    return len(doc_dicts)

# print(max_possible_df(document_dict_ts1))
# print(max_possible_df(document_dict_ts2))


def idf(term: str, doc_dicts: list) -> float:
    if document_frequency(term, doc_dicts) == 0:
        tb = sys.exc_info()[2]
        raise Exception("idf: The term " + term + " appears in no document!").with_traceback(tb)
    return np.log10(max_possible_df(doc_dicts) / document_frequency(term, doc_dicts))

# print(idf(searchterm, document_dict_ts1))
# print(idf(searchterm, document_dict_ts2))


def tf_idf(term: str, document: list, doc_dicts: list) -> float:
    return np.log(1 + term_frequency(term, document)) * idf(term, doc_dicts)

# print(tf_idf(searchterm, document_dict_ts1[1459]["W"], document_dict_ts1))
# print(tf_idf(searchterm, document_dict_ts2[1459]["W"], document_dict_ts2))


def score_dq_tf_idf(document: list, query: list, doc_dicts: list) -> float:
    score = 0
    for term in list(set(document) & set(query)):
        score = score + tf_idf(term, document, doc_dicts)
    return score

# print(score_dq_tf_idf(document_dict_ts1[1459]["W"], sample_qry, document_dict_ts1))
# print(score_dq_tf_idf(document_dict_ts2[1459]["W"], sample_qry, document_dict_ts2))
# print(document_dict_ts2[1459]["W"])


def weight_matrix_tf_idf(doc_dicts: list, query: list) -> list:
    matrix = list()
    for doc_dict in doc_dicts:
        scores_query = list()
        for term in query:
            # print(term)
            score_term = tf_idf(term, doc_dict["W"], doc_dicts)
            # print(score_term)
            scores_query.append(score_term)
        # print(scores_query)
        matrix.append(scores_query)
    return matrix

# print(weight_matrix_tf_idf(document_dict_ts1, sample_qry))
print(weight_matrix_tf_idf(document_dict_ts2, sample_qry))
