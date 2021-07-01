from sklearn.cluster import KMeans
from kneed import KneeLocator

import tf
from data import database
import pandas as pd
import numpy as np
from tf import tfidf

# TODO: what should  KMAX be?
S = 1
KMAX = 20


class Clustering(tfidf):
    def __init__(self, corpus: list, titles: list):
        super().__init__(corpus, titles)
        self.KMAX = KMAX
        self.clustering = self.__kmeans(self.__find_optimal_k(self.KMAX))

    def __find_optimal_k(self, kmax):
        points = self.tfidf_mat
        sse = []
        k_list = list(range(1, kmax + 1))
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

        elbow_graph = KneeLocator(k_list, sse, S=S, curve="convex", direction="decreasing")
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
        vecs = []
        for i in range(0, self.tfidf_mat.shape[0]):
            vec = self.tfidf_mat[i]
            if self.get_cluster_of_vector(vec) == k:
                titles.append(self.titles[i])
                vecs.append(self.tfidf_mat[i])
        vecs = np.array(vecs)
        return (titles, vecs)


    def get_all_clusters(self):
        return self.clustering

def process_example_clustering():
    tf_obj = database.load_object("doc_folder")
    titles = tf_obj.titles
    corpus = tf_obj.corpus
    clustering = Clustering(corpus, titles)
    clustering_at_two = clustering.get_cluster_of_index(0)
    print("end")

process_example_clustering()

