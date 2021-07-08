import unittest
import numpy
from evaluation import evaluation_functions as ev_f

doc_dicts = [{},{}]
rel_dict = {0:[0,1], 1:[], 2:[1],}

search_results = {0:[1], 1:[1,0], 2:[0,1],}

relation_labels = numpy.array([[1,1], [0,0], [0,1]])
result_label = numpy.array([[0,1], [1,1], [1,1]])

evaluation = {-1:0.8333333333333333, 0:[1.0, 0.5], 1:[0.0, 1.0], 2:[0.5, 1.0] }

class TestAndEvaluation(unittest.TestCase):
    def test_get_relation_labels(self):
        numpy.testing.assert_array_equal(relation_labels, ev_f.get_relation_labels(doc_dicts, search_results, rel_dict))


    def test_get_result_labels(self):
        numpy.testing.assert_array_equal(result_label, ev_f.get_result_labels_and_search(doc_dicts, search_results))

    def test_evaluation(self):
        self.assertEqual(evaluation, ev_f.evaluate_querrys(result_label, relation_labels))

tf_search_results = { 0:[1,2,3,4,5,6,7,8,9,10], 1:[3,5,6,11,2,7,13,5,8,15], 2:[3,2,7,5,13,7,9,5,3,7]}
tf_result_relation = {0:[1,2,3,4,5,6,7,8,9,10], 1:[1,2,3,4,5,6,7,8], 2:[5,6,7,8,9,10,11]}
tf_relation_labels = numpy.array([[1,1,1,1,1,1,1,1,1,1],[1,1,1,0,1,1,0,1,1,0],[0,0,1,1,0,1,1,1,0,1]])
tf_result_labels = numpy.array([[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]])

class TestTfIdfEvaluation(unittest.TestCase):
    def test_get_result_labels(self):
        x = ev_f.get_result_labels_tf_idf(tf_search_results, tf_result_relation)
        result = x[0]
        eval_l = x[1]
        numpy.testing.assert_array_equal(result, tf_result_labels)
        numpy.testing.assert_array_equal(eval_l, tf_relation_labels)


if __name__ == '__main__':
    unittest.main()