# simple application to run the search from preprocessing to the returned query
# author: Lars Kasüschke
# import sys
import time

import preprocessing.pp_main
import utilities
from data import database
from search import searching_algorithm
from tf_idf import tf_idf_main
from evaluation import evaluation_functions
from preprocessing import pp_main as preprocessing_main
from matrix import inverted_matrix

# the algorithm you want to use
algorithm = searching_algorithm.and_search
# only fill in if you want to preprocess a specific file again
filenames_for_preprocessing = []
# fill in all taskstrings to use for preprocessing
taskstrings_for_preprocessing = ["tnwl", "tnwp", "tn"]
# taskstring to work with
taskstring = "tnwl"


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
    print("Place the files you wish to preprocess: " + preprocessing.pp_main.dir_archive)
    print("endings: '.ALL' for documents, 'QRY' for querys, 'REL' for expected results.")
    print("press any key when you are finished")
    input()
    print("Let's go")
    if taskstrings_for_preprocessing:
        for taskstring in taskstrings_for_preprocessing:
            if filenames_for_preprocessing:
                preprocessing.pp_main.run_preprocessing(taskstring=taskstring, filenames=filenames_for_preprocessing)
            else:
                preprocessing.pp_main.run_preprocessing(taskstring=taskstring)
    else:
        preprocessing.pp_main.run_preprocessing()
    time.sleep(.5)








def main():
    print("----------------------")
    print("Simple IR System Setup")
    print("----------------------\n")
    print("\nDo you want to:")
    print("1: enter a search query")
    print("2: evaluate the current searching_algorithm")
    print("3: rerun")
    print("4: preprocess")
    print("5: exit")
    i = input()
    if i == "1":
        main_search(taskstring)
    elif i == "2":
        main_evaluate(taskstring)
    elif i == "3":
        main()
    elif i == "4":
        main_preprocess()
    else:
        exit()


if __name__ == "__main__":
    main()
    # print(database.load_object("tnwp_pp_CISI.ALL"))
