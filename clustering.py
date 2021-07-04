from sklearn.cluster import KMeans
from kneed import KneeLocator

import tf
from data import database
import pandas as pd
import numpy as np
from tf import tfidf

# sensitivity of the elbow finder
sensitivity = 1.0
# max number of k to be considered for the k-means algorithm
KMAX = 10

class Clustering(tfidf):
    def __init__(self, corpus: list, titles: list):
        super().__init__(corpus, titles)
        self.KMAX = KMAX
        self.clustering = self.__kmeans(self.__find_optimal_k(self.KMAX))

    def __find_optimal_k(self, kmax):
        points = self.tfidf_mat
        kmax = min(kmax, len(self.titles), np.unique(points).shape[0])
        if kmax == 1:
            return 1
        sse = []
        k_list = range(1, min(kmax, len(self.titles)) + 1)
        for k in k_list:
            kmeans = KMeans(n_clusters=k).fit(points)
            centroids = kmeans.cluster_centers_
            pred_clusters = kmeans.predict(points)
            curr_sse = 0

            # calculate square of Euclidean distance of each point from its cluster center and add to current WSS
            for i in range(points.shape[0]):
                curr_center = centroids[pred_clusters[i]]
                vec = points[i,:]
                curr_sse += tf.cos_sim_func(vec, curr_center)[0]

            curr_sse = curr_sse/k
            sse.append(curr_sse)

        elbow_graph = KneeLocator(k_list, sse, S=sensitivity, curve="convex", direction="decreasing")

        optimal_k = elbow_graph.elbow
        if not optimal_k:
            optimal_k = 1

        # TODO: make plotting work
        return optimal_k

    def __kmeans(self, k):
        clustering = KMeans(n_clusters=k).fit(self.tfidf_mat)
        return clustering

    def get_cluster_of_vector(self, vec):
        return self.clustering.predict(vec)

    def get_cluster_of_index(self, k):
        titles = []
        corpus = []
        vecs = []
        for i in range(0, self.tfidf_mat.shape[0]):
            vec = self.tfidf_mat[i]
            if self.get_cluster_of_vector(vec) == k:
                titles.append(self.titles[i])
                corpus.append(self.corpus[i])
                vecs.append(self.tfidf_mat[i])
        vecs = np.array(vecs)
        return (corpus, titles, vecs)


    def get_all_clusters(self):
        return self.clustering

'''
    def search_with_clustering(self):
            __preprocess(self)
            tf_obj = self.tf_object
            query_vec = tf_obj.tfidfVectorizer.transform([query])
            cluster_index = tf_obj.get_cluster_of_vector(query_vec)
            corpus, titles, vecs = tf_obj.get_cluster_of_index(cluster_index)
            tf_copy = clustering.Clustering(corpus, titles)
            return_docs_num = len(corpus)

            if tf_copy:
                result = tf_copy.query_k_titles(query, return_docs_num)
                for x in range(0, len(result)):
                    self.result_text.insert(x, result[x])

    def __preprocess(self, dir_selected):
        corpus_list = []
        titles = []
        tf_object = None
        for _, _, filenames in os.walk(dir_selected):
            titles = filenames
            dir = os.path.basename(dir_selected)
            for filename in filenames:
                path = dir_selected + "/" + filename
                text = search_util.file_to_list_of_string(path)
                corpus_list.append(text)
            # TODO: implement saving to databases

            if titles and corpus_list:
                tf_object = Clustering(corpus_list, titles)
            break
        return tf_object

        :


'''

'''
    def search_with_clustering(self):
            __preprocess(self)
            tf_obj = self.tf_object
            query_vec = tf_obj.tfidfVectorizer.transform([query])
            cluster_index = tf_obj.get_cluster_of_vector(query_vec)
            corpus, titles, vecs = tf_obj.get_cluster_of_index(cluster_index)
            tf_copy = clustering.Clustering(corpus, titles)
            return_docs_num = len(corpus)

            if tf_copy:
                result = tf_copy.query_k_titles(query, return_docs_num)
                for x in range(0, len(result)):
                    self.result_text.insert(x, result[x])

    def __preprocess(self, dir_selected):
        corpus_list = []
        titles = []
        tf_object = None
        for _, _, filenames in os.walk(dir_selected):
            titles = filenames
            dir = os.path.basename(dir_selected)
            for filename in filenames:
                path = dir_selected + "/" + filename
                text = search_util.file_to_list_of_string(path)
                corpus_list.append(text)
            # TODO: implement saving to databases

            if titles and corpus_list:
                tf_object = Clustering(corpus_list, titles)
            break
        return tf_object

        :


'''