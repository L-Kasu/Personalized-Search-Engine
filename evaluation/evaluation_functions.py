from _ctypes_test import func
from search import searching_algorithm as search_algo
from matrix import inverted_matrix as im
from tf_idf import tf_idf_functions as tf
from sklearn import metrics
from numpy import ndarray


# gets the results of querrys for the evalutation
# returns a dicitonary of querry index and the results
def get_results_for_evaluation(query_dicts: list, doc_dicts: list) -> dict:
    None


# calculates for every querrry precision and recal
# returns a dictionary: dict[querry_index] = [precission, recall]
# special case: evaluation[-1] = average_precision
def evaluate_querrys(query_results: dict, rel_dict: dict) -> dict:
    y_true = get_relation_labels(query_results, rel_dict)
    y_pred = get_result_labels(query_results, rel_dict)
    evaluation = {}
    for i in query_results:
        i_true = y_true[i]
        i_pred = y_pred[i]
        precision = metrics.precision_score(i_true, i_pred)
        recall = metrics.recall_score(i_true, i_pred)
        evaluation[i] = [precision, recall]
    average = metrics.average_precision_score(y_true, y_pred)
    evaluation[-1] = average
    return evaluation


# saves the results of the evaluation in txt file
def save_evaluation(evaluation: dict, algo: str, taskstring: str):
    file = open('eval_output/' + algo + '_evaluation_' + taskstring + '.txt', "w")
    for i in evaluation:
        file.write("Querry " + str(i) + ":")
        file.write("\t\tprecission: " + str(evaluation[i][0]))
        file.write("\t\trecall: " + str(evaluation[i][1]) + "\n")
    file.write("\n\n\nwithout stemming: \n")


# compares to evaluations
def comp_evaluations(evaluation1: dict, evaluation2: dict):
    None


# labes the documents if they are expected for a querry
# returns a ndarray: result[i] = expected for querry i
def get_relation_labels(query_results: dict, rel_dict: dict) -> ndarray:
    result = ndarray((len(query_results), len(query_results[1])))
    for i in rel_dict:
        for x in range(0, len(query_results)):
            if x in rel_dict[i]:
                result[i][x] = True
            else:
                result[i][x] = False
    return result


def get_result_labels(query_results: dict, rel_dict: dict) -> ndarray:
    result = ndarray((len(query_results), len(query_results[1])))
    for i in rel_dict:
        k = len(rel_dict[i])
        count = 0
        for x in query_results[i]:
            if count < k:
                result[i][x] = True
                count = count + 1
            else:
                result[i][x] = False
                count = count + 1
    return result




#########################################################################################################
# old functions
# going to delete them
##########################################################################################################


# evaluates the search, that uses the preprocessing with stemming
# returns a dictionary that associates the query index with the precision and recall

# parameters:
# querys: dictionary of (preprocessed) querys
# rel: dictionary of relations
# matrix: matrix object
# algorithm: function of the search algorithm (two arguments: query, Matrix)
def evaluate(query: dict, rel: list, matrix: im.InvertedMatrix, algorithm: func) -> dict:
    evaluation = {}
    for i in rel:
        searched = algorithm(query[i], matrix)
        print(searched)
        found_wanted_documents = len(search_algo.intersect(searched, rel[i])) # number of the documents that were wanted and foud
        found_documents = len(searched)   # number of documents that were found
        wanted_documents = len(rel[i])  # number of wanted documents
        precision = get_precision(found_wanted_documents, found_documents)
        recall = get_recall(found_wanted_documents, wanted_documents)
        evaluation[i] = [precision, recall]
    return evaluation


# parameters:
# qry_dicts: dictionary of preprocessed querries
# doc_dicts: dictionary of preprocessed documents
# output: dictionary, that maps the querry index to the recall
def evaluate_tf_idf_alt(qry_dicts: list, doc_dicts: list, related) -> dict:
    evaluation = {}
    for i in range(0, len(qry_dicts)):
        wanted_documents = len(related[i])
        searched = tf.get_k_documents_for_query_i_lightweight(doc_dicts, qry_dicts, wanted_documents, i)
        found_wanted_documents = len(search_algo.intersect(searched, related[i]))
        recall = get_recall(found_wanted_documents, wanted_documents)
        evaluation[i] = recall
    return evaluation


def evaluate_tf_idf(doc_dicts: list, query_dicts: list, rel_dict: dict) -> dict:
    vocab_dict = tf.df_dict(doc_dicts, query_dicts)
    weight_matrix_doc = tf.weight_matrix_doc_tf_idf(doc_dicts, query_dicts, vocab_dict)
    evaluation = {}
    # workaround because query:dict is broken
    for i in range(0, 111):
    #for i in range(0, len(query_dicts)):
        weight_vec_qry = tf.weight_vec_qry_tf_idf(doc_dicts, query_dicts, i, vocab_dict)
        rank_matrix = tf.document_rank_matrix(weight_matrix_doc, weight_vec_qry)
        sorted_rank_matrix = tf.sort_document_rank_matrix_for_qry_i(rank_matrix, 0)
        wanted_documents = len(rel_dict)
        float_list = tf.get_k_documents(sorted_rank_matrix, wanted_documents)
        # cast to int
        int_list = list()
        for j in range(0, len(float_list)):
            int_list.append(int(float_list[j]))
        searched = int_list
        if i in rel_dict:
            found_wanted_documents = len(search_algo.intersect(searched, rel_dict[i]))
            recall = get_recall(found_wanted_documents, wanted_documents)
        else:
            # if no expected documents given, then recall = 10
            recall = 10
        evaluation[i] = recall
    return evaluation



def get_precision(found_wanted_documents: int, found_documents: int) -> float:
    if found_documents == 0 :
        return 0
    return found_wanted_documents/found_documents


def get_recall(found_wanted_documents: int, wanted_documents: int) -> float:
    if wanted_documents == 0:
        return 0
    return found_wanted_documents/wanted_documents


# get a list of mappings of a query to a single document and
# return a list of list of expected documents for each query
def rel_mapping_to_list_of_expected_results(data: list) -> dict:
    result = {}
    for item in data:
        if item:
            if item[0] in result:
                result[item[0]].append(item[1])
            else:
                result[item[0]] = [item[1]]
    return result


def query_list_to_dic(data: list) -> dict:
    result = {}
    for item in data:
        if item and type(item) == type({}):
            result[int(item["I"])] = item["W"]
    return result


def read_qry_list(filename: str) -> dict:
    qry_list = {}
    file = open(filename, "r")
    i = 0
    for line in file:
        if line.startswith('.W {'):
            line_without_prefix = line[3:].strip()
            content = set()
            for element in line_without_prefix[1:-1].split(","):
                content.add(element[1:-1].replace("'", ""))
            qry_list[i] = list(content)
            i = i +1
    file.close()
    return qry_list


# maps the related documents to a querry index
def read_related_documents(filename: str) -> dict:
    relation = {}
    file = open(filename, "r")
    for line in file:
        i = 1
        for element in line.split():
            if i == 1:
                key = int(element) - 1 # adjusrting index
                i = 2
            elif i == 2:
                value = int(element) - 1 # adjusting index
                i = 3
            elif i == 3:
                if key in relation:
                    relation[key].append(value)
                else :
                    relation[key] = [value]
                i = 4
            else:
                i = 1
    file.close()
    return relation

def save_eval_tf_idf(evaluation: dict, taskstring):
    file = open("eval_output/tf_idf_evaluation_" + taskstring + ".txt", "w")
    file.write("Evaluation tf_idf: \n")
    file.write("If recall = 10, then there were no expected documents given\n")
    for i in evaluation:
        file.write("Querry"+str(i)+": ")
        file.write("\t\trecall: "+str(evaluation[i]) + "\n")
    file.close()



# saves the evaluation in txt file
def save_eval() -> None:
    evaluation_with_stemming = evaluate_with_stemming()
    file = open('eval_output/evaluation.txt', "w")
    file.write("with stemminng: \n")
    for i in evaluation_with_stemming:
        file.write("Querry " + str(i) + ":")
        file.write("\t\tprecission: "+ str(evaluation_with_stemming[i][0]))
        file.write("\t\trecall: " + str(evaluation_with_stemming[i][1]) + "\n")
    file.write("\n\n\nwithout stemming: \n")
    evaluation_without_stemming = evaluate_without_stemming()
    for i in evaluation_without_stemming:
        file.write("Querry " + str(i) + ":")
        file.write("\t\tprecission: "+ str(evaluation_without_stemming[i][0]))
        file.write("\t\trecall: " + str(evaluation_without_stemming[i][1]) + "\n")
    file.close()

