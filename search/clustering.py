import timeit

from sklearn.cluster import KMeans
from kneed import KneeLocator
import math
import numpy as np
import scipy.sparse.csr as csr
#from search.preprocessing_parameter import get_stems, get_stopword_value

# sensitivity of the elbow finder
default_sensitivity = 1.0


def cos_sim_func(query_vec, tfidf_mat):
    return tfidf_mat @ query_vec.T


class Clustering:
    # only works if vectors are normalized
    def __init__(self, matrix: csr):
        self.matrix = matrix # this breaks everything if matrix too big: /np.linalg.norm(matrix, axis = 1, keepdims=True)
        self.KMAX = max(round(math.log2(self.matrix.shape[0])), 1)
        self.optimal_k = self.__find_optimal_k(self.KMAX)
        self.clustering = self.__kmeans(self.optimal_k)

    def __find_optimal_k(self, kmax, sensitivity=default_sensitivity, counter=0):
        points = self.matrix
        # TODO: find better check for unqiue vectors
        # a = np.unique(points, axis=0).shape[0]
        #kmax = min(kmax, a)
        if kmax == 1:
            return 1
        sse = []
        k_list = list(range(1, min(kmax, points.shape[0]) + 1))
        for k in k_list:
            kmeans = KMeans(n_clusters=k).fit(points)
            centroids = kmeans.cluster_centers_
            pred_clusters = kmeans.predict(points)
            curr_sse = 0

            # calculate cosine similiraity from its cluster center and add to current WSS
            for i in range(points.shape[0]):
                curr_center = centroids[pred_clusters[i]]
                vec = points[i]
                curr_sse += float(cos_sim_func(vec, curr_center))

            curr_sse = curr_sse/k
            sse.append(curr_sse)

        elbow_graph = KneeLocator(k_list, sse, S=sensitivity, curve="convex", direction="decreasing")

        optimal_k = elbow_graph.elbow
        if not optimal_k:
            counter += 1
            optimal_k = self.__find_optimal_k(self.KMAX, sensitivity=sensitivity/2, counter=counter)
        if optimal_k == 1:
            if counter < 10:
                counter += 1
                optimal_k = self.__find_optimal_k(self.KMAX, sensitivity=sensitivity + 1, counter=counter)

        # TODO: make plotting work
        print("we use: " + str(optimal_k) + "clusters and KMAX is: " + str(self.KMAX))
        return optimal_k

    def __kmeans(self, k):
        clustering = KMeans(n_clusters=k).fit(self.matrix)
        return clustering

    # returns the index of the cluster
    def predict_the_cluster_of_vector(self, vec) -> int:
        result = self.clustering.predict(vec)
        if vec.shape[0] == 1:
            result = int(result)
        return result

    # returns a 3_tuple of:
    # - index_to_keep: indices of vectors in the original matrix that belong to Cluster Nr. k
    # - index_to_drop: indices of the vectors in the original matrix that belong to a different cluster
    # - vecs: Matrix containing all the vectors of cluster Nr. k.
    # Use index_to_keep to map vecs back on to the original matrix.
    def get_cluster_of_index(self, k):
        index_to_keep = [] # list of indeces to keep
        index_to_drop = []
        clustering_labels = self.clustering.labels_
        for i in range(0, len(clustering_labels)):
            if clustering_labels[i] == k:
                index_to_keep.append(i)
            else:
                index_to_drop.append(i)
        vecs = self.matrix[index_to_keep,:]
        return (index_to_keep, index_to_drop, vecs)






