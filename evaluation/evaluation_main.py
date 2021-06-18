from evaluation import evaluation_functions as ev
from data import database
from matrix import inverted_matrix
import os.path


def run_evaluation(query_dicts: list, doc_dicts: list, rel_dict: dict, tf_search, taskstring: str, algo: str):
    name = algo + "_evaluation_" + taskstring
    if os.path.exists('data/' + name):
        evaluation = database.load_object(algo + "_evaluation_" + taskstring)
    else:
        if algo == "tf_idf":
            evaluation = evaluate_tf_idf(query_dicts, doc_dicts, rel_dict, tf_search)
        elif algo == "and_search":
            matrix = inverted_matrix.InvertedMatrix(taskstring, doc_dicts)
            evaluation = evaluate_and_search(query_dicts, matrix, rel_dict, doc_dicts)
        else:
            evaluation = {}
        database.save_object(evaluation, name)
    ev.save_evaluation(evaluation, name)


def evaluate_tf_idf(query_dicts: list, doc_dicts: list, rel_dict: dict, tf_search) -> dict:
    search_result = ev.get_results_for_evaluation_tf_idf(query_dicts, tf_search)
    query_labels = ev.get_result_labels_tf_idf(doc_dicts, search_result, rel_dict)
    rel_labels = ev.get_relation_labels(doc_dicts, search_result, rel_dict)
    evaluation = ev.evaluate_querrys(query_labels, rel_labels)
    return evaluation


def evaluate_and_search(query_dicts: list, matrix, rel_dict: dict, doc_dicts: list) -> dict:
    search_result = ev.get_results_for_evaluation_and_search(query_dicts, matrix)
    query_labels = ev.get_result_labels_and_search(doc_dicts, search_result)
    rel_labels = ev.get_relation_labels(doc_dicts, search_result, rel_dict)
    evaluation = ev.evaluate_querrys(query_labels, rel_labels)
    return evaluation


def run_compare(eval1: dict, eval2: dict, name1, name2):
    ev.comp_evaluations(eval1, eval2, name1, name2)