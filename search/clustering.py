from sklearn.cluster import KMeans
from kneed import KneeLocator

from search import tf
import numpy as np
from search.tf import tfidf
import scipy.sparse.csr as csr

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
        a = np.unique(points)[0].shape[0]
        b = len(self.titles)
        kmax = min(kmax, len(self.titles), np.unique(points)[0].shape[0])
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
        result = self.clustering.predict(vec)
        if vec.shape[0] == 1:
            result = int(result)
        return result

    def get_cluster_of_index(self, k):
        titles = []
        corpus = []
        vecs = []
        index_to_keep = [] # list of indeces to keep
        index_to_drop = []
        original_indices = []
        for i in range(0, self.tfidf_mat.shape[0]):
            vec = self.tfidf_mat[i]
            if self.get_cluster_of_vector(vec) == k:
                titles.append(self.titles[i])
                corpus.append(self.corpus[i])
                original_indices.append(i)
                index_to_keep.append(i)
            else:
                index_to_drop.append(i)
        vecs = self.tfidf_mat[index_to_keep,:]
        return (corpus, titles, original_indices, index_to_drop, vecs)

    # predict cluster of query and search in the corresponding cluster, return indices of documents soreted by relevance
    def search_in_cluster(self, query):
        query_vec = self.tfidfVectorizer.transform([query])
        cluster_index = self.get_cluster_of_vector(query_vec)
        corpus, titles, original_indices, index_to_drop, vecs = self.get_cluster_of_index(cluster_index)
        query_vec = self.tfidfVectorizer.transform([query])

        # matrix multiplicatin to calculate cosine similarity
        cos_sim = tf.cos_sim_func(query_vec, vecs)

        # result_list will be filled with (index, cos-sim) tuples
        result_list = []

        for i in range(cos_sim.shape[0]):
            # map index of vector to index in the original matrix
            k = original_indices[i]
            result_list.append((k, cos_sim[i, 0]))
        for x in index_to_drop:
            result_list.append((x, -1))

        # sorts from large to small based on cos-sim value
        result_list.sort(key=lambda x: x[1], reverse=True)

        only_indicies = []
        for i in range(len(result_list)):
            only_indicies.append(result_list[i][0])

        return only_indicies

# drop columns of an csr matrix
def dropcols(M, idx_to_drop):
    idx_to_drop = np.unique(idx_to_drop)
    C = M.tocoo()
    keep = ~np.in1d(C.col, idx_to_drop)
    C.data, C.row, C.col = C.data[keep], C.row[keep], C.col[keep]
    C.col -= idx_to_drop.searchsorted(C.col)    # decrement column indices
    C._shape = (C.shape[0], C.shape[1] - len(idx_to_drop))
    return C.tocsr()

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