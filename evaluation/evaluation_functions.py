from _ctypes_test import func
from sklearn import metrics
import numpy
from numpy import  ndarray


# gets the results of querrys for the evalutation
# using the tf_idf algorithm
# returns a dicitonary of querry index and the results
from search import tf, clustering


def get_results_for_evaluation_tf_idf(query_dict: dict, tf_search) -> dict:
    searched = {}
    for i in query_dict:
        docs = tf_search.query_indicies(query_dict[i])
        searched[i] = docs[:10]
    return searched


# gets the results of querrys for the evalutation
# using the and_search algorithm
# returns a dicitonary of querry index and the results
def get_results_for_evaluation_and_search(query_dicts: list, matrix) -> dict:
    searched = {}
    for i in range(0, len(query_dicts)):
        words = query_dicts[i]["W"]
        docs = search_algo.and_search(words, matrix)
        searched[i] = docs
    return searched


def get_results_for_evaluation_clustering(doc_dicts, query_dicts: list) -> dict:
    searched = {}
    corpus_list = doc_dicts[2]
    titles_list = doc_dicts[1]
    tf_obj = clustering.Clustering(corpus_list, titles_list)
    for i in range(0, len(query_dicts)):
        print(i)
        query = query_dicts[i]
        searched[i] = tf_obj.search(query)[:10]
    return searched


# calculates for every querry precision and recal
# parameter ndarrays with labels true and false
# returns a dictionary: dict[querry_index] = [precission, recall]
# special case: evaluation[-1] = average_precision
def evaluate_querrys(query_labels_f: list, rel_labels_f: list, query_labels_p: list, rel_labels_p: list) -> dict:
    evaluation = {}
    sum_f = 0
    sum_p = 0
    for i in range(0, len(query_labels_f)-1):
        i_true = rel_labels_f[i]
        i_pred = query_labels_f[i]
        f_score = metrics.f1_score(i_true, i_pred)
        p_true = rel_labels_p[i]
        p_pred = query_labels_p[i]
        mean_precission = mean_average_precission(p_pred, p_true)
        evaluation[i] = [f_score, mean_precission]
        sum_f += f_score
        sum_p += mean_precission
    average_f = sum_f / (len(query_labels_f))
    evaluation[-2] = average_f
    average_p = sum_p / (len(query_labels_f))
    evaluation[-1] = average_p
    return evaluation


def mean_average_precission(query_labels: ndarray, rel_labels: ndarray):
    sum = 0
    counter = 0
    for i in range(1,len(query_labels)):
        average_precision = metrics.average_precision_score(rel_labels[:i], query_labels[:i])
        if not numpy.isnan(average_precision):
            sum = sum + average_precision
            counter = counter+1
    if counter == 0: counter = 1
    return sum/counter


# saves the results of the evaluation in txt file
def save_evaluation(evaluation: dict, name: str):
    file = open('eval_output/' + name + '.txt', "w")
    file.write("average precision: " + str(evaluation[-1]) + "\n")
    file.write("average f_score: " + str(evaluation[-2]) + "\n")
    for i in evaluation:
        file.write("Querry " + str(i) + ":")
        file.write("\t\tf-score/average precission: " + str(evaluation[i])  + "\n")
    file.close()


# compares to evaluations
def comp_evaluations(evaluation1: dict, evaluation2: dict, name1: str, name2: str):
    name = "comp_" + name1 + "_and_" + name2
    file = open('eval_output/' + name + '.txt', "w")

    file.write("\t\t\t\t\t\t" + name1 + "\t\t\t" + name2 + "\n")
    file.write("average precission:\t" + str(evaluation1[-1]) + "\t\t" + str(evaluation2[-1]) + "\n")
    file.write("average f1-score:\t" +  str(evaluation1[-2]) + "\t\t" + str(evaluation2[-2]) + "\n")

    file.close()


def get_result_labels_average_precission(query_results: dict, rel_dict: dict) -> list:
    result = []
    rel = []
    for i in range(0, len(query_results)):
        pred = numpy.ones(10)
        true = numpy.zeros(10)
        for j in range(0, len(query_results[i])):
            if i in rel_dict:
                if query_results[i][j] in rel_dict[i]:
                    true[j] = 1
        result.append(pred)
        rel.append(true)
    return  [result, rel]


def get_result_labels_f1(doc_dicts: list, query_results: dict, rel_dict: dict) -> list:
    result = []
    rel = []
    n = len(doc_dicts)
    print("doc_dicts: " + str(n))
    for i in query_results:
        pred = numpy.zeros(n)
        true = numpy.zeros(n)
        for x in query_results[i]:
            pred[x] = 1
        if i in rel_dict:
            for y in rel_dict[i]:
                true[y] = 1
        result.append(pred)
        rel.append(true)
    return [result, rel]
