# simple application to run the search from preprocessing to the returned query
# author: Lars Kasüschke
# import sys
import time

import preprocessing.pp_main
import utilities
from data import database
from search import searching_algorithm
from tf_idf import tf_idf_main
from evaluation import evaluation_main
from preprocessing import pp_main as preprocessing_main
from matrix import inverted_matrix
import file_reader
import tf

# the algorithm you want to use
algorithm = searching_algorithm.and_search
# only fill in if you want to preprocess a specific file again
filenames_for_preprocessing = ["CISI.ALL"]
# fill in all taskstrings to use for preprocessing
taskstrings_for_preprocessing = ["tn"]
# taskstring to work with
default_taskstring = "tn"
# initialise the tf algorithm
documents = file_reader.load_all()
titles = documents[1]
corpus = documents[2]
tf_search = tf.tfidf(corpus, titles)

def main_search():
    print("Enter your search:")
    i = input()
    tf_search.query_k_titles(i)


def main_evaluate(taskstring):
    doc_dict = database.load_object(taskstring + "_pp_" + "CISI.ALL")
    rel_dict = database.load_object("tn_pp" + "_CISI.REL")
    print("What algorithm do you want to evaluate?")
    print("1: tf_idf")
    print("2: and_search")
    i = input()
    if i == "1":
        algo = "tf_idf"
        query_dict = file_reader.load_qry()
    elif i == "2":
        algo = "and_search"
        query_dict = database.load_object(taskstring + "_pp_" + "CISI.QRY")
    else:
        algo = ""
        query_dict = {}
    evaluation_main.run_evaluation(query_dict, doc_dict, rel_dict, tf_search, taskstring, algo)


def main_preprocess() -> None:
    print("Place the files you wish to preprocess: " + preprocessing.pp_main.dir_archive)
    print("endings for indexed: '.ALL' for documents, 'QRY' for querys, 'REL' for expected results.")
    print("for indexed files every distint part starts with .[A-Z]")
    print("press any key when you are finished")
    input()
    print("Let's go...")
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
    print("2: evaluate the search engine")
    print("3: rerun")
    print("4: preprocess")
    print("5: exit")
    i = input()
    if i == "1":
        main_search()
    elif i == "2":
        main_evaluate(default_taskstring)
    elif i == "3":
        main()
    elif i == "4":
        main_preprocess()
    else:
        exit()


text = "Abstracting is a key segment of the information industry Opportunities are available for both full-time professionals and part-time orvolunteer workers.Many librarians find such activities pleasant and rewarding, for they knowthey are contributing to the more effective use of stored information.One chapter is devoted to career opportunities for abstractors."


if __name__ == "__main__":
    main()
    print(database.load_object("tn_pp_CISI.ALL"))
