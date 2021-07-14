import unittest
class TestAndSearch(unittest.TestCase):
    def test_list_init(self):
        for i in range(0, len(query_dicts)):
            print(i)
            query_vec = tf_obj.tfidfVectorizer.transform([query_dicts[i]])
            cluster_index = tf_obj.get_cluster_of_vector(query_vec)
            corpus, titles, vecs = tf_obj.get_cluster_of_index(cluster_index)
            tf_copy = tf.tfidf(corpus, titles)
            if tf_copy:
                result = tf_copy.query_indicies(query_dicts[i])
                searched[i] = result[:10]
        return searched