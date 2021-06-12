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

#class TestTfIdfEvaluation(unittest.TestCase)


if __name__ == '__main__':
    unittest.main()
