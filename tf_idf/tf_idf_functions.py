# function container for the tf-idf algorithm
# version: alpha1.1
# author: Niklas Munkes


import numpy as np


def vocabulary(doc_dicts: list, query_dicts: list) -> list:
    all_dicts = list(doc_dicts)
    for i in range(0, len(query_dicts)):
        curr_qry_dict = query_dicts[i]
        all_dicts.append(curr_qry_dict)
    vocab = set()
    for j in range(0, len(doc_dicts) + len(query_dicts)):
        curr_dict = all_dicts[j]
        for item in curr_dict["W"]:
            vocab.add(item)
    return list(vocab)


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
                        continue
    return freq_of_term


def max_possible_df(doc_dicts: list) -> int:
    return len(doc_dicts)


def idf(term: str, doc_dicts: list) -> float:
    # custom edit to prevent div by zero
    return np.log10(max_possible_df(doc_dicts) / (1 + document_frequency(term, doc_dicts)))


def tf_idf(term: str, document: list, doc_dicts: list) -> float:
    return np.log(1 + term_frequency(term, document)) * idf(term, doc_dicts)


def score_tf_idf(document: list, query: list, doc_dicts: list) -> float:
    score = 0
    for term in list(set(document) & set(query)):
        score = score + tf_idf(term, document, doc_dicts)
    return score


# docs are lined up at axis m (doc with index i is at m=i)
# terms are lined up at axis n (term with vocab index i is at n=i)
# result matrix is A(m,n)
def weight_matrix_doc_tf_idf(doc_dicts: list, query_dicts: list) -> np.ndarray:
    vocab = vocabulary(doc_dicts, query_dicts)
    matrix = np.zeros((len(doc_dicts), len(vocab)))
    for m in range(0, len(doc_dicts)):
        doc_dict = doc_dicts[m]
        for n in range(0, len(vocab)):
            matrix[m][n] = tf_idf(vocab[n], doc_dict["W"], doc_dicts)
    return matrix


# queries are lined up at axis m (qry with index i is at m=i)
# terms are lined up at axis n (term with vocab index i is at n=i)
# result matrix is A(m,n)
def weight_matrix_qry_tf_idf(doc_dicts: list, query_dicts: list) -> np.ndarray:
    vocab = vocabulary(doc_dicts, query_dicts)
    matrix = np.zeros((len(query_dicts), len(vocab)))
    for m in range(0, len(query_dicts)):
        for n in range(0, len(vocab)):
            matrix[m][n] = tf_idf(vocab[n], query_dicts[m]["W"], doc_dicts)
    return matrix


def cosine_similarity(vec_query: np.ndarray, vec_document: np.ndarray) -> float:
    cos_sim = 0
    for i in range(0, len(vec_query)):
        cos_sim = cos_sim + (float(vec_query[i]) * float(vec_document[i]))
    return cos_sim


# returns A(m,n) with a_i,j = ['orig_index_of_doc','orig_index_of_qry',cos_sim(qry[j],doc[i])]
def document_rank_matrix(matrix_doc: np.ndarray, matrix_qry: np.ndarray) -> np.ndarray:
    matrix = np.zeros((len(matrix_doc[:, 0]), len(matrix_qry[:, 0]), 3))
    for m_doc in range(0, len(matrix_doc[:, 0])):
        for m_qry in range(0, len(matrix_qry[:, 0])):
            matrix[m_doc][m_qry] = [m_doc, m_qry, cosine_similarity(matrix_qry[m_qry, :], matrix_doc[m_doc, :])]
    return matrix


def sort_document_rank_matrix_for_qry_i(matrix: np.ndarray, index_qry: int) -> list:
    data_for_qry = np.zeros((len(matrix[:, 0, 0]), len(matrix[0, 0, :])))
    for doc in range(0, len(matrix[:, 0, 0])):
        data_doc = matrix[doc, index_qry, :]
        data_for_qry[doc, :] = data_doc  # A(all_docs, [doc_index, qry_index, cos_sim])
    return sorted(data_for_qry, key=(lambda x: x[2]), reverse=True)


def get_k_documents(list_of_vec: list, k: int) -> list:
    doc_list = list()
    for j in range(0, k):
        doc_vec = list_of_vec[j]
        doc_list.append(doc_vec[0])
    return doc_list


def get_k_documents_for_query_i(doc_dicts: list, query_dicts: list, k: int, i: int) -> list:
    weight_matrix_doc = weight_matrix_doc_tf_idf(doc_dicts, query_dicts)
    weight_matrix_qry = weight_matrix_qry_tf_idf(doc_dicts, query_dicts)
    rank_matrix = document_rank_matrix(weight_matrix_doc, weight_matrix_qry)
    sorted_rank_matrix = sort_document_rank_matrix_for_qry_i(rank_matrix, i)
    float_list = get_k_documents(sorted_rank_matrix, k)
    # cast to int
    int_list = list()
    for i in range(0, len(float_list)):
        int_list.append(int(float_list[i]))
    return int_list
