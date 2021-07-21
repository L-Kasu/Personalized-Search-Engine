import numpy as np
import io

# example

# glove_50d = load_glove_model("search/word_embeddings/glove/glove.6B.50d.txt")
# glove_50d_search = WordEmbeddingSearch(glove_50d, corpus, titles)
#
# # search returning titles
# glove_50d_search.doc_titles("search str")
#
# # search returning indicies
# glove_50d_search.doc_indicies("search str")


def load_glove_model(File):
    print("Loading Glove Model")
    f = open(File,'r',encoding="utf-8")
    gloveModel = {}
    for line in f:
        splitLines = line.split()
        word = splitLines[0]
        wordEmbedding = np.array([float(value) for value in splitLines[1:]])
        gloveModel[word] = wordEmbedding
    print(len(gloveModel)," words loaded!")
    return gloveModel


def load_fasttext_model(fname):
    print("Loading fastText Model")
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    data = {}
    for line in fin:
        tokens = line.rstrip().split(' ')
        data[tokens[0]] = map(float, tokens[1:])
    print(len(data)," words loaded!")
    return data


class WordEmbeddingSearch:
    def __init__(self, word_embedding, corpus, titles):
        self.corpus = corpus
        self.titles = titles
        self.word_embedding = word_embedding

        doc_embedding_matrix = []

        for doc in corpus:
            doc_embedding_matrix.append(self.txt_to_embedding(doc))

        self.doc_embedding_matrix = np.array(doc_embedding_matrix)

    def txt_to_embedding(self, doc):
        split_str = doc.split()
        return np.mean([self.word_embedding[word] for word in split_str if word in self.word_embedding], axis=0)

    def cos_sim_query(self, query):
        query_vec = self.txt_to_embedding(query)
        return self.cos_sim(query_vec)

    def cos_sim(self, vector):
        return self.doc_embedding_matrix @ vector.T

    # gets: query as str
    # returns: a ordered list of indicies (from most relevant to least)
    def doc_indicies(self, query):
        cosine_sim = self.cos_sim_query(query)

        index_and_cos_sim = []

        for i in range(len(cosine_sim)):
            index_and_cos_sim.append((i, cosine_sim[i]))

        index_and_cos_sim.sort(key=lambda x: x[1], reverse=True)

        only_index = []

        for i in range(len(index_and_cos_sim)):
            only_index.append(index_and_cos_sim[i][0])

        return only_index

    # gets: query as str
    # returns: a ordered list of titles (from most relevant to least)
    def doc_titles(self, query):

        indicies = self.docs_orderd_by_relevance(query)

        ordered_titles = [self.titles[index] for index in indicies]
        return ordered_titles
