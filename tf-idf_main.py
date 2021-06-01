# implementation of the tf-idf algorithm (ranked retrieval)
# version: alpha0.9
# author: Niklas Munkes
import cProfile
import sys
import numpy as np
from pp_file_reader import file_reader
# from pp_main import dir_output, taskstring_1, taskstring_2, filename

dir_output = "./PP_output/"
taskstring_1 = "tnwp"
taskstring_2 = "tn"
filename = "CISI.ALL"
filename_qry = "CISI.QRY"

document_dict_ts1 = file_reader(dir_output + "pp_output_" + taskstring_1 + "_" + filename + ".txt")
document_dict_ts2 = file_reader(dir_output + "pp_output_" + taskstring_2 + "_" + filename + ".txt")
document_dict_ts1_tenALL = file_reader(dir_output + "pp_output_" + taskstring_1 + "_" + filename + "_tenALL.txt")
query_dict_ts1 = file_reader(dir_output + "pp_output_" + taskstring_1 + "_" + filename_qry + ".txt")
query_dict_ts2 = file_reader(dir_output + "pp_output_" + taskstring_2 + "_" + filename_qry + ".txt")
query_dict_ts1_oneQRY = file_reader(dir_output + "pp_output_" + taskstring_1 + "_" + filename_qry + "_oneQRY.txt")
# print(document_dict_ts1, flush='left')
# print(document_dict_ts2, flush='left')
# searchterm = "literature"
# searchterm = "cat"
sample_qry = ["certificates", "literature", "the", "for"]

def vocabulary(doc_dicts: list, query_dicts: list) -> list:
    all_dicts = doc_dicts
    for i in range(0, len(query_dicts)):
        all_dicts.append(query_dicts[i])
    vocabulary = set()
    for dict in all_dicts:
        for term in dict["W"]:
            vocabulary.add(term)
    return list(vocabulary)


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


def score_tf_idf(document: list, query: list, doc_dicts: list) -> float:
    score = 0
    for term in list(set(document) & set(query)):
        score = score + tf_idf(term, document, doc_dicts)
    return score

# print(score_tf_idf(document_dict_ts1[1459]["W"], sample_qry, document_dict_ts1))
# print(score_tf_idf(document_dict_ts2[1459]["W"], sample_qry, document_dict_ts2))
# print(document_dict_ts2[1459]["W"])


# docs are lined up at axis m (doc with index i is at m=i)
# queries are lined up at axis n (qry with index i is at n=i)
# result matrix is A(m,n)
# def weight_matrix_tf_idf(doc_dicts: list, query_dicts: list) -> np.ndarray:
#     matrix = np.zeros((len(doc_dicts), len(query_dicts)))
#     for m in range(0, len(doc_dicts)):
#         for n in range(0, len(query_dicts)):
#             # print("doc: " + str(doc_dicts[m]["W"]))
#             # print("qry: " + str(query_dicts[n]["W"]))
#             matrix[m][n] = score_tf_idf(doc_dicts[m]["W"], query_dicts[n]["W"], doc_dicts)
#             # print("matrix["+str(m)+"]["+str(n)+"]: " + str(matrix[m][n]))
#     return matrix

# docs are lined up at axis m (doc with index i is at m=i)
# terms are lined up at axis n (term with vocab index i is at n=i)
# result matrix is A(m,n)
def weight_matrix_doc_tf_idf(doc_dicts: list, query_dicts: list) -> np.ndarray:
    vocab = vocabulary(doc_dicts, query_dicts)
    matrix = np.zeros((len(doc_dicts), len(vocab)))
    for m in range(0, len(doc_dicts)):
        for n in range(0, len(vocab)):
            matrix[m][n] = tf_idf(vocab[n], doc_dicts[m]["W"], doc_dicts)
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


# print(weight_matrix_tf_idf(document_dict_ts1_tenALL, query_dict_ts1_oneQRY))
# print(weight_matrix_tf_idf(document_dict_ts2, query_dict_ts2))


def cosine_similarity(vec_query: np.ndarray, vec_document: np.ndarray) -> float:
    return np.dot(np.linalg.norm(vec_query), np.linalg.norm(vec_document))
    # return np.dot(vec_query, vec_document) / (np.abs(vec_query) * np.abs(vec_document))


# returns A(m,n) with a_i,j = ['orig_index_of_doc',cos_sim(qry[j],doc[i])]
def document_rank_matrix(matrix_doc: np.ndarray, matrix_qry: np.ndarray) -> np.ndarray:
    matrix = np.zeros((len(matrix_doc[:, 0]), len(matrix_qry[:, 0]), 2))
    for m_doc in range(0, len(matrix_doc[:, 0])):
        for m_qry in range(0, len(matrix_qry[:, 0])):
            matrix[m_doc][m_qry] = [m_doc, cosine_similarity(matrix_qry[m_qry, :], matrix_doc[m_doc, :])]
    return matrix


def sort_document_rank_matrix(matrix: np.ndarray) -> np.ndarray:
    data_sorted = np.zeros((len(matrix[:, 0]), len(matrix[0, :]), 2))
    for n in range(0, len(matrix[0, :])):
        data = matrix[:, n]
        # data_sorted[:, n] = data.sort(key=lambda tup: tup[1])
        data_sorted[:, n] = sorted(data, key=(lambda x: x[1]))
    return data_sorted


def get_k_documents_for_query_i_matrix(matrix: np.ndarray, k: int, i: int) -> list:
    doc_list = list()
    for j in range(0, k):
        doc_list.append(matrix[:, i][j][0])
    return doc_list


# alters the input of get_k_documents_for_query_i_matrix
def get_k_documents_for_query_i(doc_dicts: list, query_dicts: list, k: int, i: int) -> list:
    weight_matrix_doc = weight_matrix_doc_tf_idf(doc_dicts, query_dicts)
    weight_matrix_qry = weight_matrix_qry_tf_idf(doc_dicts, query_dicts)
    rank_matrix = document_rank_matrix(weight_matrix_doc, weight_matrix_qry)
    return get_k_documents_for_query_i_matrix(sort_document_rank_matrix(rank_matrix), k, i)


# print(get_k_documents_for_query_i(document_dict_ts1, query_dict_ts1, 5, 0))
# print(cProfile.run("get_k_documents_for_query_i(document_dict_ts1, query_dict_ts1, 5, 0)"))
print(get_k_documents_for_query_i(document_dict_ts1_tenALL, query_dict_ts1_oneQRY, 5, 0))
print(cProfile.run("get_k_documents_for_query_i(document_dict_ts1_tenALL, query_dict_ts1_oneQRY, 5, 0)"))
