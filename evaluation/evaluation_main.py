from evaluation import evaluation_functions as ev
from data import database


def run_evaluation(query_dicts: list, search, algo: str, rel_dict: dict, doc_dicts):
    name = algo + "_evaluation"
    search_results = ev.get_search_results(query_dicts, search)

    labels_f1 = ev.get_result_labels_f1(doc_dicts, search_results, rel_dict)
    query_labels_f1 = labels_f1[0]
    rel_labels_f1 = labels_f1[1]
    labels_prec = ev.get_result_labels_average_precission(search_results, rel_dict)
    query_labels_prec = labels_prec[0]
    rel_labels_prec = labels_prec[1]

    evaluation = ev.evaluate_querrys(query_labels_f1, rel_labels_f1, query_labels_prec, rel_labels_prec)
    database.save_object(evaluation, name)
    ev.save_evaluation(evaluation, name)

def run_compare(e1, e1c, e2, e2c, e3, n1, n2, n3, all):
    ev.comp_evaluations(e1, e1c, e2, e2c, e2, n1, n2, n3, all)

