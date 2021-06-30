from sklearn.cluster import KMeans
from kneed import KneeLocator
from data import database
import pandas as pd
import numpy as np

# TODO: what should  KMAX be?
KMAX = 8


class Clustering():
    def __init__(self, tf_obj):
        self.KMAX = 8
        self.tf_obj = tf_obj
        self.clustering = self.__kmeans(self.__find_optimal_k(self.KMAX))

    def __find_optimal_k(self, kmax):
        points = self.tf_obj.tfidf_mat
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
                curr_sse += (points[i, 0] - curr_center[0]) ** 2 + (points[i, 1] - curr_center[1]) ** 2

            sse.append(curr_sse)

        elbow_graph = KneeLocator(k_list, sse, S=1.0, curve="convex", direction="decreasing")
        optimal_k = elbow_graph.elbow
        # TODO: make plotting work
        elbow_graph.plot_knee()
        return optimal_k

    def __kmeans(self, k):
        clustering = KMeans(n_clusters=k).fit(self.tf_obj.tfidf_mat)
        return clustering

    def get_cluster_of_vector(self, vec):
        return self.clustering.predict(vec)

    def get_cluster_of_index(self, k):
        titles = []
        vecs = []
        for i in range(0, self.tf_obj.tfidf_mat.shape[0]):
            vec = self.tf_obj.tfidf_mat[i]
            if self.get_cluster_of_vector(vec) == k:
                titles.append(self.tf_obj.titles[i])
                vecs.append(self.tf_obj.tfidf_mat[i])
        vecs = np.array(vecs)
        return (titles, vecs)


    def get_all_clusters(self):
        return self.clustering

def process_example_clustering():
    tf_obj = database.load_object("doc_folder")
    clustering = Clustering(tf_obj)
    clustering_at_two = clustering.get_cluster_of_index(0)
    print("end")

process_example_clustering()

