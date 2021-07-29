from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import random, pickle, os
import numpy as np
from evaluation import file_reader
from nltk.tokenize import word_tokenize
from data import  database

class Model():
    def __init__(self, feature_creating_functions, documents, query_dict, rel_dict):
        self.training_data, self.test_data, self.validation_data = self.create_datasets(documents, query_dict, rel_dict)
        self.feature_generator = feature_creating_functions
        self.model = LogisticRegression()

    def train(self):
        X, y = self.training_data
        self.model.fit(X, y)

    def validate(self) -> int:
        X, y = self.validation_data
        return self.model.score(self.validation_data)

    def test(self):
        pass

    def score(self, doc1, doc2):
        doc_features = [func(doc1, doc2) for func in self.feature_generator]
        return self.model.predict_proba(doc_features)[0][0]

# return the matrix of features, by applying every function by the list for one feature, and the corresponding labels
    def create_datasets(self, documents, query_dict, rel_dict):
        train = ([], [])
        test = ([], [], [], [])
        validate = ([], [])
        for j in range(0, len(documents)):
            for i in range(0, len(query_dict)):
                sample = [func(query_dict[i], documents[j]) for func in self.feature_generator]
                label = 1 if j in rel_dict[str(i)] else 0
                query_number, doc_number = str(i + 1) + str(j + 1)
                rnd = random.uniform(0,1)
                if rnd <= .6:
                    train[0].append(sample)
                    train[1].append(label)
                elif rnd <= .8:
                    test[0].append(sample)
                    test[1].append(label)
                    test[2].append(doc_number)
                    test[3].append(query_number)
                else:
                    validate[0].append(sample)
                    validate[1].append(label)
        return train, test, validate

def main():
    # create list of features we want to take into consideration
    function_list = [lambda doc1: lambda doc2: np.numpy_ml.utils.distance_metrics.euclidean(txt_to_vec(doc1), txt_to_vec(doc2))]
    documents = file_reader.load_all()[2]
    query_dict = file_reader.load_qry()
    rel_dict = database.load_object("tn_pp" + "_CISI.REL")
    model = Model(function_list, documents, query_dict, rel_dict)
    score = model.validate()
    print(score)

def txt_to_vec(txt:str):
    # load embedding
    name = "glove.6B.300d.p"
    for root, dirs, files in os.walk(".\\data\\"):
        if name in files:
            path = os.path.join(root, name)
    word_embedding = pickle.load(open(path, "rb"))
    split_str = word_tokenize(txt.lower())
    vector = np.mean([word_embedding[word] for word in split_str if word in word_embedding], axis=0)
    return vector


if __name__ == "__main__":
    main()
