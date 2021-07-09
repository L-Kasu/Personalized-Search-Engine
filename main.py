# simple application to run the search from preprocessing to the returned query
# author: Lars Kasüschke
# import sys
import time

from data import database
from evaluation import evaluation_main, file_reader
from search import tf


# initialise the tf algorithm
documents = file_reader.load_all()
titles = documents[1]
corpus = documents[2]
tf_search = tf.tfidf(corpus, titles)


def main_evaluate():
    rel_dict = database.load_object("tn_pp" + "_CISI.REL")
    print("What algorithm do you want to evaluate?")
    print("1: tf_idf")
    print("2: clustering")
    i = input()
    if i == "1":
        algo = "tf_idf"
        doc_dict = database.load_object("tnwl_pp_" + "CISI.ALL")
        query_dict = file_reader.load_qry()
    elif i == "2":
        algo = "clustering"
        doc_dict = file_reader.load_all()
        query_dict = file_reader.load_qry()
    else:
        algo = ""
        query_dict = {}
    evaluation_main.run_evaluation(query_dict, doc_dict, rel_dict, tf_search, algo)

def main_compare():
    eval_tf = database.load_object("tf_idf_evaluation")
    evl_and = database.load_object("clustering_evaluation")
    evaluation_main.run_compare(eval_tf, evl_and, "tf_idf", "clustering")


def main():
    print("----------------------")
    print("Simple IR System Setup")
    print("----------------------\n")
    print("\nDo you want to:")
    print("1: evaluate the search engine")
    print("2: compare tf_idf and clustering")
    i = input()
    if i == "1":
        main_evaluate()
    elif i == "2":
        main_compare()
    else:
        exit()


text = "Abstracting is a key segment of the information industry Opportunities are available for both full-time professionals and part-time orvolunteer workers.Many librarians find such activities pleasant and rewarding, for they knowthey are contributing to the more effective use of stored information.One chapter is devoted to career opportunities for abstractors."


if __name__ == "__main__":
    main()
