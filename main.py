# simple application to run the search from preprocessing to the returned query
# import sys


# to evaluate the wordembedding there is the file glove.6B.200d.pickle needed in the database
import search.LogisticRegression
from data import database
from evaluation import evaluation_main, file_reader
from search import search_class
from gui.builder_toolbox import settings_util


# initialise the tf algorithm
documents = file_reader.load_all()
titles = documents[1]
corpus = documents[2]
#tf_search = tf.tfidf(corpus, titles)
#search_algo = search_class.Search(corpus, titles)


def main_evaluate():
    rel_dict = database.load_object("tn_pp" + "_CISI.REL")
    query_dict = file_reader.load_qry()
    config = settings_util.get_configdict()
    print("What algorithm do you want to evaluate?")
    print("1: tf_idf")
    print("2: tf_idf with clustering")
    print("3: word-embedding")
    print("4: word-embedding with clustering")
    print("5: logistic regression")
    i = input()
    if i == "1":
        algo = "tf_idf"
        config["search_mode"] = "tfidf"
        config["clustering"] = False
    elif i == "2":
        algo = "tf_idf_clustering"
        config["search_mode"] = "tfidf"
        config["clustering"] = True
    elif i == "3":
        algo = "word-embedding"
        config["search_mode"] = "GloVe"
        config["clustering"] = False
    elif i == "4":
        algo = "word-embedding_clustering"
        config["search_mode"] = "GloVe"
        config["clustering"] = True
    elif i == "5":
        algo = "logistic-regression"
        config["search_mode"] = "GloVe"
        config["clustering"] = False
    else:
        algo = ""
        query_dict = {}
    settings_util.edit_config(config)
    search_algo = search_class.Search(corpus, titles)
    print("1: evaluate the first 30 queries")
    print("2: evaluate all queries")
    j = input()
    query_dict_ = {}
    if j == "1":
        for i in range(0, 30):
            query_dict_[i] = query_dict[i]
        algo = algo + "_30"
    else:
        query_dict_ = query_dict
    evaluation_main.run_evaluation(query_dict_, search_algo, algo, rel_dict, corpus)

def main_LR():
    search.LogisticRegression.main()



def main_compare():
    print("1: all queries")
    print("2: the first 30 queries")
    i = input()
    if i == "1":
        n1 = "tf_idf"
        n2 = "word-embedding"
        n3 = "logistic-regression"
        e1 = database.load_object("tf_idf_evaluation")
        e1c = database.load_object("tf_idf_clustering_evaluation")
        e2 = database.load_object("word-embedding_evaluation")
        e2c = database.load_object("word-embedding_clustering_evaluation")
        e3 = database.load_object("logistic-regression_evaluation")
        all = True
    else:
        n1 = "tf_idf"
        n2 = "word-embedding"
        n3 = "logistic-regression"
        e1 = database.load_object("tf_idf_30_evaluation")
        e1c = database.load_object("tf_idf_clustering_30_evaluation")
        e2 = database.load_object("word-embedding_30_evaluation")
        e2c = database.load_object("word-embedding_clustering_30_evaluation")
        e3 = database.load_object("logistic-regression_30_evaluation")
        all = False

    evaluation_main.run_compare(e1, e1c, e2, e2c, e3, n1, n2, n3, all)

def special():
    eval_1 = database.load_object("word-embedding-30_evaluation")
    eval_2 = database.load_object("word-embedding_evaluation")
    evaluation_main.run_compare(eval_1, eval_2, "we30", "we")


def main():
    print("----------------------")
    print("Simple IR System Setup")
    print("----------------------\n")
    print("\nDo you want to:")
    print("1: evaluate the search engine")
    print("2: compare two systems")
    print("3: run linear regression")
    i = input()
    if i == "1":
        main_evaluate()
    elif i == "2":
        main_compare()
        #special()
    elif i == "3":
        main_LR()
    else:
        exit()




if __name__ == "__main__":
    main()
