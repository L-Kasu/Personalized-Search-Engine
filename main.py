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
    print("2: tf_idf with clustering")
    print("3: word-embedding")
    i = input()
    if i == "1":
        algo = "tf_idf"
        doc_dict = database.load_object("tnwl_pp_" + "CISI.ALL")
        query_dict = file_reader.load_qry()
    elif i == "2":
        algo = "tf_idf_clustering"
        doc_dict = file_reader.load_all()
        query_dict = file_reader.load_qry()
    elif i == "3":
        algo = "word-embedding"
        doc_dict = file_reader.load_all()
        query_dict = file_reader.load_qry()
    else:
        algo = ""
        query_dict = {}
    evaluation_main.run_evaluation(query_dict, tf_search, algo, doc_dict, rel_dict)

def main_compare():
    print("Choose the first algorithm")
    print("1: tf_idf")
    print("2: tf_idf with clustering")
    print("3: word-embedding")
    i = input()
    if i == "1":
        eval_1 = database.load_object("tf_idf_evaluation")
        name1 = "tf_idf"
    elif i == "2":
        eval_1 = database.load_object("clustering_evaluation")
        name1 = "tf_idf_clustering"
    elif i == "3":
        eval_1 = database.load_object("word-embedding_evaluation")
        name1 = "word-embedding"
    else:
        exit()

    print("Choose the second algorithm")
    print("1: tf_idf")
    print("2: tf_idf with clustering")
    print("3: word-embedding")
    i = input()
    if i == "1":
        eval_2 = database.load_object("tf_idf_evaluation")
        name2 = "tf_idf"
    elif i == "2":
        eval_2 = database.load_object("clustering_evaluation")
        name2 = "tf_idf_clustering"
    elif i == "3":
        eval_2 = database.load_object("word-embedding_evaluation")
        name2 = "word-embedding"
    else:
        exit()

    evaluation_main.run_compare(eval_1, eval_2, name1, name2)


def main():
    print("----------------------")
    print("Simple IR System Setup")
    print("----------------------\n")
    print("\nDo you want to:")
    print("1: evaluate the search engine")
    print("2: compare two systems")
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
