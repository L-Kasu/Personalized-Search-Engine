from sklearn.cluster import kmeans_plusplus as km
from sklearn.cluster import KMeans
from kneed import KneeLocator

class Clustering():
    def __init__(self, tf_mat):
       #  self.clustering = evaluate_optimal_k(self)
         self.matrix = tf_mat

    def kmeans(self, k):
         print(km(self.matrix, k))

    def evaluate_optimal_k(self):
         pass

    # function returns WSS score for k values from 1 to kmax
    def calculate_WSS(points, kmax):
        sse = []
        k_list = list(range(1, kmax + 1))
        for k in k_list:
            kmeans = KMeans(n_clusters=k).fit(points)
            centroids = kmeans.cluster_centers_
            pred_clusters = kmeans.predict(points)
            curr_sse = 0

            # calculate square of Euclidean distance of each point from its cluster center and add to current WSS
            for i in range(len(points)):
                curr_center = centroids[pred_clusters[i]]
                curr_sse += (points[i, 0] - curr_center[0]) ** 2 + (points[i, 1] - curr_center[1]) ** 2

            sse.append(curr_sse)

        elbow_graph = KneeLocator(k_list, sse, S=1.0, curve="convex", direction="decreasing")

        return elbow_graph.elbow
