import search_methods
import loading_and_saving

import sys
def check_len(corpus, titles):
    
    tb = sys.exc_info()[2]
    if(len(corpus) != len(titles)): raise Exception("Length of corpus doesn't match the length of titles.\n len(corpus) =", len(corpus),"len(titles) =", len(titles)).with_traceback(tb)


class Search:
    def __init__(self, corpus, titles):
        
        check_len(corpus, titles)
        
        self.corpus = corpus
        self.titles = titles
        
        self.search_method = None
        search_name = "tfidf" #get_config("algorithem")

        if search_name == "tfidf":
            self.search_method = TfidfMethod(corpus)

        elif search_name == "glove":
            glove_embedding = pickle.load(open("glove.6B.200d.p", "rb"))
            self.search_method = WordEmbeddingMethod(glove_embedding, corpus)

        elif search_name == "fasttext":
            fasttext_embedding = pickle.load(open("wiki-news-300d-1M.p", "rb"))
            self.search_method = WordEmbeddingMethod(fasttext_embedding, corpus)
        
        self.clustering = None
        clustering_flag = False #get_config("clustering")
        
        if clustering_flag:
            self.clustering = Clustering(search_method.get_matrix())
            
    
    def search_indicies(self, query):
        
        query_vector = self.search_method.txt_to_vec(query)
        
        relevant_indicies = list(range(len(titles)))
        relevant_matrix = self.search_method.get_matrix()
        
        if self.clustering != None:
            index = self.clustering.predict_the_cluster_of_vector(query_vector)
            relevant_indicies, _, relevant_matrix = self.clustering.get_cluster_of_index(index)
        
        # cosine similarity
        cos_sim = relevant_matrix @ query_vector.T
        
        combination = list(zip(relevant_indicies, cos_sim))
        
        combination.sort(key=lambda x: x[1], reverse=True)
        
        return [c[0] for c in combination]
        
        
    def search_titles(self, query):
        indicies = self.search_indicies(query)
        return list(map(lambda index: titles[index], indicies))
        
