from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import random, pickle, os
import numpy as np
from evaluation import file_reader
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import LancasterStemmer
import pickle


class Model:
    def __init__(self, feature_creating_functions, class_weight="balanced"):
        self.training_data, self.test_data, self.validation_data = ((), (), ())
        self.feature_generator = feature_creating_functions
        self.model = LogisticRegression(solver='saga', random_state=0, class_weight=class_weight)

    def intialise_data(self, documents, query_dict, rel_dict):
        self.training_data, self.test_data, self.validation_data = self.create_datasets(documents, query_dict, rel_dict)

    def train(self):
        X, y = self.training_data
        self.model.fit(X, y)

    def validate(self) -> int:
        X, y = self.validation_data
        return self.model.score(X, y)

    def test(self):
        wrong_unrelated = []
        right_unrelated = []
        wrong_related = []
        right_related = []

        test_data = self.test_data
        for i in range(len(test_data[0])):
            item = test_data[0][i]
            predicted = self.score(np.array(item).reshape(1, -1))
            actual = test_data[1][i]
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
              "wrong unrelated: ", len(wrong_unrelated),)



    def score(self, doc_features):
        return self.model.predict_proba(doc_features)[0]

    # return the matrix of features, by applying every function by the list for one feature, and the corresponding labels
    def create_datasets(self, documents, query_dict, rel_dict):
        train = ([], [])
        test = ([], [], [], [])
        validate = ([], [])
        for i in range(0, len(query_dict)):
            for j in range(0, len(documents)):
                if i in rel_dict:
                    label = 1 if j in rel_dict[i] else 0
                else:
                    label = 0
                sample = [func(query_dict[i])(documents[j]) for func in self.feature_generator]
                query_number, doc_number = (str(i + 1), str(j + 1))
                rnd = random.uniform(0, 1)
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
        print("the share of related documents: sum(train[1])/len(train[1])")
        return train, test, validate


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
    stemmer = LancasterStemmer()
    tokens = [word for word in word_tokenize(doc.lower()) if len(word) > 1]
    result = [stemmer.stem(item) for item in tokens]
    return result

def load_embedding():
    name = "glove.6B.300d.p"
    path = ""
    for root, dirs, files in os.walk("..\\data\\"):
        if name in files:
            path = os.path.join(root, name)
    word_embedding = pickle.load(open(path, "rb"))
    return word_embedding

def main():
    Vectorizer = TfidfVectorizer(analyzer='word', stop_words="english")
    embedding = load_embedding()
    # specify document number to take into consideration(for performance)
    documents_to_use = 1
    load = False
    scores = []
    # create list of features we want to take into consideration
    embedding_vectors_distance = lambda doc1: lambda doc2: \
        1/(np.linalg.norm(document_to_embedding_vector(embedding, doc1) - document_to_embedding_vector(embedding, doc2)))
    embedding_vectors_cosine = lambda doc1: lambda doc2: \
        cosine_similarity(document_to_embedding_vector(embedding, doc1).reshape(1, -1),
                          document_to_embedding_vector(embedding, doc2).reshape(1, -1))[0][0]
    rnd = lambda _: lambda _: random.uniform(0, 1)
    tfidf_cosine = lambda doc1: lambda doc2: tfidf_cos_sim(Vectorizer, doc1, doc2)
    # making sure the validation runs correctly, by using a random funcition for testing and we should get back .5
    function_list = [embedding_vectors_distance, embedding_vectors_cosine, tfidf_cosine]
    documents = file_reader.load_all()[2][:documents_to_use]
    query_dict = file_reader.load_qry()
    rel_dict = {}
    my_model = None
    with open("../data/tn_pp_CISI.REL.pickle", "rb") as f:
        rel_dict = pickle.load(f)
    if load:
        with open("./my_model.pickle", "rb") as f:
            my_model = pickle.load(f)
    else:
        with open("./my_model.pickle", "wb") as f:
            my_model = Model(function_list)
            my_model.intialise_data(documents, query_dict, rel_dict)
            pickle.dump(my_model, f, protocol=pickle.HIGHEST_PROTOCOL)
    my_model.train()
    score = my_model.validate()
    my_model.test()
    print(score)
    scores.append(score)

if __name__ == "__main__":
    main()
