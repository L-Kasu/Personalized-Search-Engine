import preprocessing.pp_preprocessing_functions as ppf
from utilities import *

# stemmed_matrix_f = open("./matrix_output/matrix_with_stemming.txt")
# unstemmed_matrix_f = open("./matrix_output/matrix_without_stemming.txt")
matrix= {

    "provide": [0, 3, 11, 14, 16, 22, 27, 29, 37, 41],
    "study": [0, 5, 6, 8, 9, 17, 22, 24, 26, 30, 31, 37],
    "eighteen": [0, 181, 487, 821, 853],
    "continu": [0, 16, 30, 91, 119, 121, 128, 135, 136, 137, 139, 164, 181, 187],
    "detail": [0, 5, 15, 16, 49, 58, 79, 83, 114, 133, 152, 157, 160, 201, 207, 218, 226, 242, 243, 246],
    "1876": [0, 19, 170],
    "nev": [0, 138, 169, 197, 241, 292, 358, 748, 893, 938, 1031, 1035, 1231, 1276, 1383],
    "attempt": [0, 6, 12, 17, 60, 63, 66, 83, 97, 109, 110, 119, 122, 132, 133, 135, 138, 150, 157, 175, 216, 217, 228, 233, 265],
    "usa": [0, 1, 3, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 19, 21, 22, 23, 30, 31, 32, 35, 45, 55, 63, 66, 71, 74, 79, 86, 89],
    "country": [0, 16, 39, 93, 141, 236, 241, 246, 259, 260, 268, 341, 353, 390, 399, 452, 558, 587, 606, 748, 774, 788, 872, 918],
    "unsuccessful": [2, 7800],
    "empty": [],

}


def and_search_curried(query):
    return sa.and_search(query, matrix)


query_empty = ""
query_simple = "eighteen provide continue attempt"
query_unsuccessful = "I studied unsuccessful in the u.s.a."
query_advanced = "I studied in the u.s.a., to study there as a state-of-the-art-solution."

expected_result_lancaster = [
set(),
{"eighteen", "provide", "continu", "attempt"},
{"study", "unsuccessful", "usa"},
{"study", "usa", "state", "of", "the", "art", "solution"}
]

# pp for preprocessed, stemmed with lancaster
query_list_lancaster = [
ppf.preprocessing_pipeline({query_empty}, "lancaster"),
ppf.preprocessing_pipeline({query_simple}, "lancaster"),
ppf.preprocessing_pipeline({query_unsuccessful}, "lancaster"),
ppf.preprocessing_pipeline({query_advanced}, "lancaster")
]

expected_results_and = [[], [0], [], [0, 5, 6, 8, 9, 17, 22, 30, 31]]


class TestPreprocessing(unittest.TestCase):
    def test_list_init(self):
        for i in range(0, 3):
            self.assertEqual(ppf.preprocessing_pipeline(query_list_lancaster[i], "lancaster"), expected_result_lancaster[i])


class TestAndSearch(unittest.TestCase):
    def test_list_init(self):
        for i in range(0, 3):
            self.assertEqual(and_search_curried(query_list_lancaster[i]), expected_results_and[i])


if __name__ == '__main__':
    unittest.main()


