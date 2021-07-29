from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from evaluation import file_reader
from data import *
from search import search_class
import random


class Model():
    def __init__(self, feature_creating_functions, documents, query_dict, rel_dict):
        self.train, self.test, self.validate = self.createDatasets(documents, query_dict, rel_dict)
        self.feature_generator = feature_creating_functions
        self.model = LogisticRegression()

    def train(self):
        self.model.fit(self.train[0], self.train[1])

    def validate(self):
        pass

    def test(self):
        pass

    def score(self, doc1, doc2):
        doc_features = [func(doc1, doc2) for func in self.feature_generator]
        return self.model.predict_proba(doc_features)[0][0]

# return the matrix of features, by applying every function by the list for one feature, and the corresponding labels
    def create_datasets(documents, query_dict, rel_dict):
        train = ([], [])
        test = ([], [])
        validate = ([], [])
        for j in range(0, len(documents)):
            for i in range(0, len(query_dict)):
                sample = [func(query_dict[i], documents[j]) for func in self.feature_generator]
                label = 1 if j in rel_dict[str(i)] else 0
                rnd = random.uniform(0,1)
                if rnd <= .6:
                    train[0].append(sample)
                    train[1].append(label)
                elif rnd <= .8:
                    test[0].append(sample)
                    test[1].append(label)
                else:
                    validate[0].append(sample)
                    validate[1].append(label)
        return train, test, validate








