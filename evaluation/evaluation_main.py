from evaluation import evaluation_functions as ev
from data import database
from matrix import inverted_matrix


def run_evaluation(query_dicts: list, doc_dicts: list, rel_dict: dict, tf_search, taskstring: str, algo: str):
    name = algo + "_evaluation"
    if algo == "tf_idf":
        search_results = ev.get_results_for_evaluation_tf_idf(query_dicts, tf_search)
    elif algo == "and_search":
        matrix = inverted_matrix.InvertedMatrix(taskstring, doc_dicts)
        search_results = ev.get_results_for_evaluation_and_search(query_dicts, matrix)
    elif algo == "clustering":
        search_results = ev.get_results_for_evaluation_clustering(doc_dicts, query_dicts)
        doc_dicts = doc_dicts[1]
    else:
        search_results = []
    labels_f1 = ev.get_result_labels_f1(doc_dicts, search_results, rel_dict)
    query_labels_f1 = labels_f1[0]
    rel_labels_f1 = labels_f1[1]
    labels_prec = ev.get_result_labels_average_precission(search_results,rel_dict)
    query_labels_prec = labels_prec[0]
    rel_labels_prec = labels_prec[1]
    evaluation = ev.evaluate_querrys(query_labels_f1, rel_labels_f1, query_labels_prec, rel_labels_prec)
    database.save_object(evaluation, name)
    ev.save_evaluation(evaluation, name)

def run_compare(eval1: dict, eval2: dict, name1, name2):
    ev.comp_evaluations(eval1, eval2, name1, name2)

