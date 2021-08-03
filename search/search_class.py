from search import search_methods, loading_and_saving_embeddings, clustering
import pickle
import os
import sys
from gui.builder_toolbox.settings_util import get_config
from gui.builder_toolbox.tkinter_objects.listboxes import print_to_ui_console

def check_len(corpus, titles):
    
    tb = sys.exc_info()[2]
    if(len(corpus) != len(titles)): raise Exception("Length of corpus doesn't match the length of titles.\n len(corpus) =", len(corpus),"len(titles) =", len(titles)).with_traceback(tb)


class Search:
    def __init__(self, corpus, titles, app=None):

        check_len(corpus, titles)
        
        self.corpus = corpus
        self.titles = titles
        
        self.search_method = None
        search_name = get_config("search_mode")

        if search_name == "tfidf":
            self.search_method = search_methods.TfidfMethod(corpus)

        elif search_name == "GloVe":
            name = "glove.6B.300d.p"
            for root, dirs, files in os.walk(".\\data\\"):
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
        
        self.clustering = None
        clustering_flag = get_config("clustering")
        
        if clustering_flag:
            self.clustering = clustering.Clustering(self.search_method.get_matrix(), app=app)

        print_to_ui_console(app, "Search class initialized with search mode: "+search_name+", clustering: "+str(clustering_flag))
        print("Search class initialized with search mode: ", search_name, ", clustering: ", clustering_flag)
            
    
    def search_indicies(self, query):
        
        query_vector = self.search_method.txt_to_vec(query)
        
        relevant_indicies = list(range(len(self.titles)))
        relevant_matrix = self.search_method.get_matrix()
        
        if self.clustering is not None:
            query_vector = query_vector.reshape(1, -1)
            index = self.clustering.predict_the_cluster_of_vector(query_vector)
            relevant_indicies, _, relevant_matrix = self.clustering.get_cluster_of_index(index)
        
        # cosine similarity
        cos_sim = relevant_matrix @ query_vector.T
        
        combination = list(zip(relevant_indicies, cos_sim))
        
        combination.sort(key=lambda x: x[1], reverse=True)
        
        return [c[0] for c in combination]
        
        
    def search_titles(self, query):
        indicies = self.search_indicies(query)
        return list(map(lambda index: self.titles[index], indicies))
