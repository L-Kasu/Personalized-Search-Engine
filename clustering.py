from sklearn.cluster import kmeans_plusplus as km
from sklearn.cluster import KMeans
from kneed import KneeLocator
import os
from data import database

import tf
from DOCUMENTS import extract_docs

KMAX = 8


class Clustering():
    def __init__(self, tf_mat):
         self.matrix = tf_mat
         self.clustering = self.kmeans(self.find_optimal_k(self.matrix, KMAX))

    def kmeans(self, k):
        clustering = km(self.matrix, k)
        return clustering

    # uses elbow method
    def find_optimal_k(self, points, kmax):
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
        elbow_graph.plot_knee()
        return optimal_k



tf_obj = database.load_object("doc_folder")
clustering = Clustering(tf_obj.tfidf_mat)
print("end")


