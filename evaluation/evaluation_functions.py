from _ctypes_test import func
from search import searching_algorithm as search_algo
from sklearn import metrics
import numpy
from numpy import  ndarray
import clustering
from gui.builder_toolbox import  search_util
from gui import ui_builder
import tkinter


# gets the results of querrys for the evalutation
# using the tf_idf algorithm
# returns a dicitonary of querry index and the results
def get_results_for_evaluation_tf_idf(query_dict: dict, tf_search) -> dict:
    searched = {}
    for i in query_dict:
        docs = tf_search.query_indicies(query_dict[i])
        searched[i] = docs
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


def get_results_for_evaluation_clustering(query_dicts: list) -> dict:
    searched = {}
    for i in range(0, len(query_dicts)):
        print(str(i) + '\n')
        root = tkinter.Tk()
        app = ui_builder.Application(master=root)
        app.dir_selected = 'DOCUMENTS/doc_folder'
        search_util.search(app, query_dicts[i], use_case="eval")
        searched[i] = app.result
    return searched


# calculates for every querrry precision and recal
# parameter ndarrays with labels true and false
# returns a dictionary: dict[querry_index] = [precission, recall]
# special case: evaluation[-1] = average_precision
def evaluate_querrys(query_labels: ndarray, rel_labels: ndarray) -> dict:
    evaluation = {}
    for i in range(0, len(query_labels)-1):
        i_true = rel_labels[i]
        i_pred = query_labels[i]
        f_score = metrics.f1_score(i_true, i_pred, zero_division=1)
        evaluation[i] = f_score
    sum = 0
    c = 0
    for i in evaluation:
        sum += evaluation[i]
        c += 1
    average_f = sum / c
    evaluation[-2] = average_f
    average = metrics.average_precision_score(rel_labels, query_labels, average='micro')
    evaluation[-1] = average
    return evaluation


# saves the results of the evaluation in txt file
def save_evaluation(evaluation: dict, name: str):
    file = open('eval_output/' + name + '.txt', "w")
    file.write("average precision: " + str(evaluation[-1]) + "\n")
    file.write("average f_score: " + str(evaluation[-2]) + "\n")
    for i in evaluation:
        file.write("Querry " + str(i) + ":")
        file.write("\t\tf-score: " + str(evaluation[i]) + "\n")
    file.close()


# compares to evaluations
def comp_evaluations(evaluation1: dict, evaluation2: dict, name1: str, name2: str):
    name = "comp_" + name1 + "_and_" + name2
    file = open('eval_output/' + name + '.txt', "w")

    file.write("\t\t\t\t\t\t" + name1 + "\t\t\t" + name2 + "\n")
    file.write("average precission:\t" + str(evaluation1[-1]) + "\t\t" + str(evaluation2[-1]) + "\n")
    file.write("average f1-score:\t" +  str(evaluation1[-2]) + "\t\t" + str(evaluation2[-2]) + "\n")

    file.close()


# labes the documents if they are expected for a querry
# returns a ndarray: result[i] = expected for querry i
def get_relation_labels(doc_dicts: list, query_results: dict, rel_dict: dict) -> ndarray:
    result = numpy.zeros((len(query_results), len(doc_dicts)))
    for i in rel_dict:
        for x in range(0, len(doc_dicts)):
            if x in rel_dict[i]:
                result[i][x] = 1
    return result

def get_result_labels_tf_idf(doc_dicts: list, query_results: dict, rel_dict: dict) -> ndarray:
    result = numpy.zeros((len(query_results), len(doc_dicts)))
    for i in rel_dict:
        count = 0
        k = len(rel_dict[i])
        for x in query_results[i]:
            if count < k:
                result[i][x] = 1
                count = count + 1
    return result


def get_result_labels_and_search(doc_dicts: list, query_results: dict) -> ndarray:
    result = numpy.zeros((len(query_results), len(doc_dicts)))
    for i in query_results:
        for x in query_results[i]:
            result[i][x]=1
    return result
