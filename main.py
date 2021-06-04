# simple application to run the search from preprocessing to the returned query
# author: Lars Kasüschke
# import sys
import time
import utilities
from data import database
from search import searching_algorithm
from tf_idf import tf_idf_main
from evaluation import evaluation_functions
from preprocessing import main as preprocessing_main
from matrix import inverted_matrix
algorithm = searching_algorithm.and_search


def main_search(taskstring):
    qry_dicts = database.load_object(taskstring + "_pp_" + "CISI.QRY")
    doc_dicts = database.load_object(taskstring + "_pp_" + "CISI.ALL")
    tf_idf_main.main(doc_dicts, qry_dicts)



def main_evaluate(taskstring):
        query_dict = database.load_object(taskstring + "_pp_" + "CISI.QRY")
        doc_dict = database.load_object(taskstring + "_pp_" + "CISI.ALL")
        rel_dict = database.load_object(taskstring + "_pp" + "_CISI.REL")
        print((query_dict, doc_dict, rel_dict))
        result = evaluation_functions.evaluate_tf_idf(query_dict, doc_dict, rel_dict)
        evaluation_functions.save_eval_tf_idf(result, taskstring)
        database.save_object(result, taskstring + "_evaluation")
        return result


def main_preprocess() -> None:
    pair_of_list_taskstrings_filenames = preprocessing_main.run_preprocessing()
    taskstrings = pair_of_list_taskstrings_filenames[0]
    filenames = pair_of_list_taskstrings_filenames[1]
    time.sleep(.1)
    for filename in filenames:
        if filename.endswith(".ALL"):
            for i in range(1, len(pair_of_list_taskstrings_filenames)):
                # i = 1: with stemming, i = 2: without stemming
                taskstring = taskstrings[i]
                try:
                    collection_of_pp_output = database.load_object(taskstring + "_pp_" + filename)
                    matrix = inverted_matrix.InvertedMatrix(taskstring, collection_of_pp_output)
                    database.save_object(matrix, taskstring + "_matrix")
                    time.sleep(.1)
                except():
                    print("nothing saved yet. rerun!")
                    exit()
                finally:
                    print("pp_output and inverted matrix created")





def main():
    print("----------------------")
    print("Simple IR System Setup")
    print("----------------------\n")
    print("Do you want to preprocess (y/n)?")
    i = input()
    if i == "y":
        main_preprocess()
    print("enter taskstring you want to work with: ")
    taskstring = input()
    print("\nDo you want to:")
    print("1: enter a search query")
    print("2: evaluate the current searching_algorithm")
    print("3: rerun")
    print("4: exit")
    i = input()
    if i == "1":
        main_search(taskstring)
    elif i == "2":
        main_evaluate(taskstring)
    elif i == "3":
        main()
    else:
        exit()


if __name__ == "__main__":
    main()
    # print(database.load_object("tnwp_pp_CISI.ALL"))
