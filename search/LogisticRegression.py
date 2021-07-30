from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import random, pickle, os
import numpy as np
from evaluation import file_reader
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity


class Model():
    def __init__(self, feature_creating_functions):
        self.training_data, self.test_data, self.validation_data = ((), (), ())
        self.feature_generator = feature_creating_functions
        self.model = LogisticRegression()

    def intialise_data(self, documents, query_dict, rel_dict):
        self.training_data, self.test_data, self.validation_data = self.create_datasets(documents, query_dict, rel_dict)

    def train(self):
        X, y = self.training_data
        self.model.fit(X, y)

    def validate(self) -> int:
        X, y = self.validation_data
        return self.model.score(X, y)

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
        counter = 1
        for j in range(0, len(documents)):
            for i in range(0, len(query_dict)):
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
        print(sum(train[1])/len(train[1]))
        return train, test, validate


def main():
    Vectorizer = TfidfVectorizer(analyzer='word')
    embedding = load_embedding()
    scores = []
    for i in range(0,5):
        # create list of features we want to take into consideration
        embedding_vectors_distance = lambda doc1: lambda doc2: \
            np.linalg.norm(document_to_embedding_vector(embedding, doc1) - document_to_embedding_vector(embedding, doc2))
        embedding_vectors_cosine = lambda doc1: lambda doc2: \
            cosine_similarity(document_to_embedding_vector(embedding, doc1).reshape(1, -1),
                              document_to_embedding_vector(embedding, doc2).reshape(1, -1))[0][0]
        rnd = lambda _: lambda _: random.uniform(0, 1)
        tfidf_cosine = lambda doc1: lambda doc2: tfidf_cos_sim(Vectorizer, doc1, doc2)
        # making sure the validation runs correctly, by using a random funcition for testing and we should get back .5
        function_list = [tfidf_cosine, embedding_vectors_distance, embedding_vectors_cosine]
        documents = file_reader.load_all()[2]
        query_dict = file_reader.load_qry()
        rel_dict = {}
        with open("../data/tn_pp_CISI.REL.pickle", "rb") as f:
            rel_dict = pickle.load(f)
        model = Model(function_list)
        model.intialise_data(documents, query_dict, rel_dict)
        model.train()
        score = model.validate()
        print(score)
        scores.append(score)
    print(sum(scores)/len(scores))


def document_to_embedding_vector(embedding, txt: str):
    word_embedding = embedding
    split_str = word_tokenize(txt.lower())
    vector = np.mean([word_embedding[word] for word in split_str if word in word_embedding], axis=0)
    return vector

def tfidf_cos_sim(Vectorizer, doc1, doc2):
    vectorized = Vectorizer.fit_transform([doc1, doc2])
    similarity = cosine_similarity(vectorized[0], vectorized[1])
    return similarity[0][0]

def load_embedding():
    name = "glove.6B.300d.p"
    path = ""
    for root, dirs, files in os.walk("..\\data\\"):
        if name in files:
            path = os.path.join(root, name)
    word_embedding = pickle.load(open(path, "rb"))
    return word_embedding


if __name__ == "__main__":
    main()
