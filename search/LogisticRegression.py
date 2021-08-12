from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import random, os
import dill
import numpy as np
from evaluation import file_reader
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import LancasterStemmer
import pickle
import timeit
import marshal, types


# global dictionary for saving the functions

# turns list of names of function to actual list of functions
def lookup_functions(func_list):
    result = []
    Vectorizer = TfidfVectorizer(analyzer='word', stop_words="english", tokenizer=tokenize)
    embedding = load_embedding()
    function_dict = {"tfidf_cosine": lambda doc1, doc2: tfidf_cos_sim(Vectorizer, doc1, doc2),
                     "embedding_vectors_distance": lambda doc1, doc2: 0 - np.linalg.norm(
                        document_to_embedding_vector(embedding, doc1) -
                        document_to_embedding_vector(embedding, doc2)),
                     "embedding_vectors_cosine": lambda doc1, doc2: \
        cosine_similarity(document_to_embedding_vector(embedding, doc1).reshape(1, -1),
                          document_to_embedding_vector(embedding, doc2).reshape(1, -1))[0][0]}
    for item in func_list:
        if item in function_dict:
            result.append(function_dict[item])
    return result


# for loading feature generator
def deserialize_feature_generator(func_list):
    result = []
    for code in func_list:
        func = dill.loads(code)
        result.append(func)
    return result


class Model:
    def __init__(self, function_name_list=[], class_weight="balanced"):
        self.training_data, self.validation_data = ((), ())
        self.function_name_list = function_name_list
        self.feature_generator = lookup_functions(function_name_list)
        self.model = LogisticRegression(solver="lbfgs", penalty="l2", class_weight=class_weight)

    def set_model(self, model):
        self.model = model

    # prepares datasets to train the model:
    # - docs_1: first list of documents
    # - docs_2: second list of documets
    # - rel_dicts: mapping from indeces of docs_1 to docs_2 if they are related
    def intialise_data(self, docs_1, docs_2, rel_dict):
        self.training_data, self.validation_data = self.create_datasets(docs_1, docs_2, rel_dict)

    def train(self):
        X, y = self.training_data
        self.model.fit(X, y)

    def get_train_data(self):
        return self.training_data

    def set_train_data(self, data):
        self.training_data = data

    def validate(self) -> int:
        X, y = self.validation_data
        wrong_unrelated = []
        right_unrelated = []
        wrong_related = []
        right_related = []
        for i in range(len(X)):
            item = X[i]
            predicted = self.model.predict_proba(np.array(item).reshape(1, -1))[0]
            actual = y[i]
            if actual == 1:
                if predicted[1] > .5:
                    right_related.append(predicted[1])
                else:
                    wrong_unrelated.append(predicted[1])
            else:
                if predicted[1] > .5:
                    wrong_related.append(predicted[1])
                else:
                    right_unrelated.append(predicted[1])

        print("right related: ", len(right_related),
              "wrong related: ", len(wrong_related),
              "right unrelated: ", len(right_unrelated),
              "wrong unrelated: ", len(wrong_unrelated), )
        return self.model.score(X, y)

    def get_validation_data(self):
        return self.training_data

    def set_validation_data(self, data):
        self.validation_data = data

    def score(self, query, doc):
        feature = [func(query,doc) for func in self.feature_generator]
        feature = np.array(feature)
        feature = feature[:, np.newaxis].T
        predicted = self.model.predict_proba(feature)[0]
        return predicted

    # return the matrix of features, by applying every function by the list for one feature, and the corresponding labels
    def create_datasets(self, docs_1, query_dict, rel_dict):
        X = []
        y = []
        time = timeit.default_timer()
        for i in range(0, len(query_dict)):
            for j in range(0, len(docs_1)):
                if i in rel_dict:
                    if j in rel_dict[i]:
                        label = 1
                    else:
                        label = 0
                else:
                    label = 0
                if i in query_dict:
                    sample = [func(query_dict[i], docs_1[j]) for func in self.feature_generator]
                    X.append(sample)
                    y.append(label)
            time_now = timeit.default_timer() - time
            print(i, " time: ", time_now)
        print("the share of related documents:", sum(y) / max(1, len(y)))
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2)
        return ((X_train, y_train), (X_test, y_test))


def document_to_embedding_vector(embedding, txt: str):
    word_embedding = embedding
    split_str = word_tokenize(txt.lower())
    vector = np.mean([word_embedding[word] for word in split_str if word in word_embedding], axis=0)
    return vector


def tfidf_cos_sim(Vectorizer, doc1, doc2):
    vectorized = Vectorizer.fit_transform([doc1, doc2])
    similarity = cosine_similarity(vectorized[0], vectorized[1])
    return similarity[0][0]


def tokenize(doc):
    # stemmer = LancasterStemmer()
    stemmerdict = {"porter": PorterStemmer(),
                   "lancaster": LancasterStemmer(),
                   "snowball": snowball.SnowballStemmer(get_config("snowballstemmer_language"))}
    stemmer = stemmerdict[get_config("stemmer")]
    tokens = [word for word in word_tokenize(doc.lower())]
    result = [stemmer.stem(item) for item in tokens]
    return result


def load_embedding():
    name = "glove.6B.300d.p"
    path = ""
    try:
        for root, dirs, files in os.walk(".\\data\\"):
            if name in files:
                path = os.path.join(root, name)
        word_embedding = pickle.load(open(path, "rb"))
    except FileNotFoundError:
        for root, dirs, files in os.walk("..\\data\\"):
            if name in files:
                path = os.path.join(root, name)
        word_embedding = pickle.load(open(path, "rb"))
    return word_embedding


def save(filename, model):
    with open(filename, "wb") as f:
        dill.settings['recurse'] = True
        dill.dump(model, f, protocol=dill.HIGHEST_PROTOCOL)


def load(filename):
    with open(filename, "rb") as f:
        value = dill.load(f)
        return value


def main():
    # specify document number to take into consideration(for performance)
    is_saved = False
    # making sure the validation runs correctly, by using a random funcition for testing and we should get back .5
    function_list = ["tfidf_cosine", "embedding_vectors_cosine"]
    docs_1 = file_reader.load_all()[2]
    query_dict = file_reader.load_qry()
    # remove query 1-30
    for i in range(0, 30):
        if i in query_dict:
            del query_dict[i]
    rel_dict = file_reader.load_rel()
    my_model = Model(function_list)
    if is_saved:
        training_data, validation_data = load("./training_data.pickle")
        my_model.set_train_data(training_data)
        my_model.set_validation_data(validation_data)

    else:
        my_model.intialise_data(docs_1, query_dict, rel_dict)
        save("./training_data_2.pickle", (my_model.training_data, my_model.validation_data))
    my_model.train()
    score = my_model.validate()
    save("./my_model_2.pickle", my_model.model)
    print("x")
    save("./feature_generator_2.pickle", my_model.function_name_list)
    print(score)


if __name__ == "__main__":
    main()
