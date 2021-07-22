import timeit

from sklearn.cluster import KMeans
from kneed import KneeLocator

from search import tf
import numpy as np
from search.tf import tfidf
import scipy.sparse.csr as csr
from search.preprocessing_parameter import get_stems, get_stopword_value

# sensitivity of the elbow finder
default_sensitivity = 1.0
# max number of k to be considered for the k-means algorithm


class Clustering:
    def __init__(self, matrix: csr):
        self.matrix = matrix
        self.KMAX = max(round(self.matrix.shape[0]/50), 1)
        self.optimal_k = self.__find_optimal_k(self.KMAX)
        self.clustering = self.__kmeans(self.optimal_k)

    def __find_optimal_k(self, kmax, sensitivity=default_sensitivity):
        points = self.matrix
        a = np.unique(points)[0].shape[0]
        kmax = min(kmax, a)
        if kmax == 1:
            return 1
        sse = []
        k_list = range(1, min(kmax, points.shape[0]) + 1)
        for k in k_list:
            kmeans = KMeans(n_clusters=k).fit(points)
            centroids = kmeans.cluster_centers_
            pred_clusters = kmeans.predict(points)
            curr_sse = 0

            # calculate cosine similiraity from its cluster center and add to current WSS
            for i in range(points.shape[0]):
                curr_center = centroids[pred_clusters[i]]
                vec = points[i]
                curr_sse += tf.cos_sim_func(vec, curr_center)[0]

            curr_sse = curr_sse/k
            sse.append(curr_sse)

        elbow_graph = KneeLocator(k_list, sse, S=sensitivity, curve="convex", direction="decreasing")

        optimal_k = elbow_graph.elbow
        if not optimal_k:
            optimal_k = self.__find_optimal_k(self.KMAX, senitivity=sensitivity/2)
        if optimal_k == 1:
            optimal_k = self.__find_optimal_k(self.KMAX, sensitivity=sensitivity + 1)

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

'''
    # predict cluster of query and search in the corresponding cluster, return indices of documents soreted by relevance
    def search(self, query, with_clustering=True):
        query_vec = self.tfidfVectorizer.transform([query])
        vecs = self.tfidf_mat
        if with_clustering:
            cluster_index = self.predict_the_cluster_of_vector(query_vec)
            start = timeit.default_timer()
            corpus, titles, original_indices, index_to_drop, vecs = self.get_cluster_of_index(cluster_index)
            stop = timeit.default_timer()
            print("uff:", stop - start)

        # matrix multiplicatin to calculate cosine similarity
        cos_sim = tf.cos_sim_func(query_vec, vecs)

        # result_list will be filled with (index, cos-sim) tuples
        result_list = []

        for i in range(cos_sim.shape[0]):
            # map index of vector to index in the original matrix
            if with_clustering:
                k = original_indices[i]
            else:
                k = i
            result_list.append((k, cos_sim[i, 0]))
        # sorts from large to small based on cos-sim value
        result_list.sort(key=lambda x: x[1], reverse=True)

        only_indicies = []

        for i in range(len(result_list)):
            only_indicies.append(result_list[i][0])

        return only_indicies
'''




