import evaluation_functions as ev
from data import database


def run_evaluation(query_dicts: list, doc_dicts: list, rel_dict: dict, taskstring: str, algo: str):
    try:
        evaluation = database.load_object(algo + "_evaluation_" + taskstring)
        name = algo + "_evaluation_" + taskstring
    except:
        if algo == "tf_idf":
            evaluation = evaluate_tf_idf(query_dicts, doc_dicts, rel_dict)
        elif algo == "and_search":
            evaluation = evaluate_and_search(query_dicts, doc_dicts, rel_dict)
        else:
            evaluation = {}
        name = algo + "_evaluation_" + taskstring
        database.save_object(evaluation, name)
    ev.save_evaluation(evaluation, name)


def evaluate_tf_idf(query_dicts: list, doc_dicts: list, rel_dict: dict) -> dict:
    search_result = ev.get_results_for_evaluation_tf_idf(query_dicts, doc_dicts)
    query_labels = ev.get_result_labels(search_result, rel_dict)
    rel_labels = ev.get_relation_labels(search_result, rel_dict)
    evaluation = ev.evaluate_querrys(query_labels, rel_labels)
    return evaluation


def evaluate_and_search(query_dicts: list, doc_dicts: list, rel_dict: dict) -> dict:
    search_result = ev.get_results_for_evaluation_and_search(query_dicts, doc_dicts)
    query_labels = ev.get_result_labels(search_result, rel_dict)
    rel_labels = ev.get_relation_labels(search_result, rel_dict)
    evaluation = ev.evaluate_querrys(query_labels, rel_labels)
    return evaluation