from search import search_methods, loading_and_saving_embeddings, clustering, LogisticRegression
import pickle, dill
import os
import sys
from gui.builder_toolbox.settings_util import get_config
def check_len(corpus, titles):
    
    tb = sys.exc_info()[2]
    if(len(corpus) != len(titles)): raise Exception("Length of corpus doesn't match the length of titles.\n len(corpus) =", len(corpus),"len(titles) =", len(titles)).with_traceback(tb)


class Search:
    def __init__(self, corpus, titles, app):

        check_len(corpus, titles)
        
        self.corpus = corpus
        self.titles = titles
        self.app = app
        
        self.search_method = None
        search_name = get_config("search_mode")

        if search_name == "tfidf":
            self.search_method = search_methods.TfidfMethod(corpus)

        elif search_name == "GloVe":
            name = "glove.6B.300d.p"
            for root, dirs, files in os.walk(os.sep.join([".", "data"])):
                if name in files:
                    path = os.path.join(root, name)
            glove_embedding = pickle.load(open(path, "rb"))
            self.search_method = search_methods.WordEmbeddingMethod(glove_embedding, corpus)

        elif search_name == "fasttext":
            name = "wiki-news-300d-1M.p"
            for root, dirs, files in os.walk(".\\data\\"):
                if name in files:
                    path = os.path.join(root, name)
            fasttext_embedding = pickle.load(open(path, "rb"))
            self.search_method = search_methods.WordEmbeddingMethod(fasttext_embedding, corpus)

        elif search_name == "logistic regression":
            model = "my_model.pickle"
            feat_gen = "feature_generator.pickle"
            for root, _, files in os.walk("./search/"):
                if model in files:
                    path_to_model = os.path.join(root, model)
                if feat_gen in files:
                    path_to_feature_generator =os.path.join(root, feat_gen)
            with open(path_to_model, "rb") as f:
                my_model = dill.load(f)
            with open(path_to_feature_generator, "rb") as f:
                function_name_list = dill.load(f)
                search_object = LogisticRegression.Model(function_name_list=function_name_list)
                search_object.set_model(my_model)
                self.search_method = search_object

        
        self.clustering = None
        clustering_flag = get_config("clustering")
        
        if clustering_flag:
            self.clustering = clustering.Clustering(self.search_method.get_matrix())

    def set_clustering(self, clustering):
        self.clustering = clustering

    def search_indicies(self, query):

        relevant_indicies = list(range(len(self.titles)))
        document_scores = []

        if type(self.search_method) == LogisticRegression.Model:
            my_model = self.search_method
            for item in self.corpus:
                score = my_model.score(query, item)
                document_scores.append(score[1])

        else:
            query_vector = self.search_method.txt_to_vec(query)
            relevant_matrix = self.search_method.get_matrix()

            if self.clustering is not None:
                query_vector = query_vector.reshape(1, -1)
                index = self.clustering.predict_the_cluster_of_vector(query_vector)
                relevant_indicies, _, relevant_matrix = self.clustering.get_cluster_of_index(index)

            # cosine similarity
            document_scores = relevant_matrix @ query_vector.T

        combination = list(zip(relevant_indicies, document_scores))
        
        combination.sort(key=lambda x: x[1], reverse=True)
        result = [c[0] for c in combination]
        return result
        
    def search_titles(self, query):
        indicies = self.search_indicies(query)
        return list(map(lambda index: self.titles[index], indicies))
