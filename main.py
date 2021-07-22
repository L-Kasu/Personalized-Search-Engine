# simple application to run the search from preprocessing to the returned query
# import sys


# to evaluate the wordembedding there is the file glove.6B.200d.pickle needed in the database

from data import database
from evaluation import evaluation_main, file_reader
from search import search_class, search_methods, clustering


# initialise the tf algorithm
documents = file_reader.load_all()
titles = documents[1]
corpus = documents[2]
#tf_search = tf.tfidf(corpus, titles)
#search_algo = search_class.Search(corpus, titles)


'''def main_evaluate():
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
    evaluation_main.run_evaluation(query_dict, doc_dict, rel_dict, tf_search, algo)'''

'''def main_evaluate():
    rel_dict = database.load_object("tn_pp" + "_CISI.REL")
    query_dict = file_reader.load_qry()
    print("What algorithm do you want to evaluate?")
    print("1: tf_idf")
    print("2: word-embedding")
    i = input()
    if i == "1":
        algo = "tf_idf"
        search_algo.search_method = search_methods.TfidfMethod(corpus)

        print("With clustering? (y/n)")
        j = input()
        if j == "y":
            search_algo.clustering = clustering.Clustering(search_algo.search_method.get_matrix())
    elif i == "2":
        algo = "word-embedding"
        glove_embedding = database.load_object("glove.6B.200d")
        search_algo.search_method = search_methods.WordEmbeddingMethod(glove_embedding, corpus)

        print("With clustering? (y/n)")
        j = input()
        if j == "y":
            search_algo.clustering = clustering.Clustering(search_algo.search_methodgi.get_matrix())
    else:
        exit()

    evaluation_main.run_evaluation(query_dict, search_algo, algo, rel_dict, corpus)'''

def main_evaluate():
    rel_dict = database.load_object("tn_pp" + "_CISI.REL")
    query_dict = file_reader.load_qry()
    algo = "tf-idf"
    search_algo = search_class.Search(corpus, titles)
    evaluation_main.run_evaluation(query_dict, search_algo, algo, rel_dict, corpus)

def main_compare():
    print("Choose the first algorithm")
    print("1: tf_idf")
    print("2: tf_idf with clustering")
    print("3: word-embedding")
    print("4: word-embedding with clustering")
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
    elif i == "4":
        eval_1 = database.load_object("word-embedding_clustering_evaluation")
        name1 = "word-embedding_clustering"
    else:
        exit()

    print("Choose the second algorithm")
    print("1: tf_idf")
    print("2: tf_idf with clustering")
    print("3: word-embedding")
    print("4: word-embedding with clustering")
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
    elif i == "4":
        eval_2 = database.load_object("word-embedding_clustering_evaluation")
        name2 = "word-embedding_clustering"
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




if __name__ == "__main__":
    main()
