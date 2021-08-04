from abc import ABC, abstractmethod

import nltk
from nltk import PorterStemmer, LancasterStemmer
from nltk.corpus import stopwords
from nltk.stem import snowball
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from nltk.tokenize import word_tokenize

from gui.builder_toolbox.settings_util import get_config

class SearchMethod(ABC):
    
    @abstractmethod
    def get_matrix(self):
        pass
    
    @abstractmethod    
    def txt_to_vec(self, txt):
        pass 
    

class WordEmbeddingMethod(SearchMethod):
    def __init__(self,word_embedding, corpus):
        self.word_embedding = word_embedding
        doc_embedding_matrix = []
        
        for doc in corpus:
            doc_embedding_matrix.append(self.txt_to_vec(doc))
        
        self.doc_embedding_matrix = np.array(doc_embedding_matrix)
        
    def get_matrix(self):
        return self.doc_embedding_matrix
    
    def txt_to_vec(self, txt):
        split_str = word_tokenize(txt.lower())
        stop_words = set(stopwords.words(get_config("stopword_language")))
        split_str_tmp = []
        [split_str_tmp.append(word) for word in split_str if word not in stop_words]
        split_str = split_str_tmp
        vector = np.mean([self.word_embedding[word] for word in split_str if word in self.word_embedding], axis=0)
        normalized_vector = vector/np.linalg.norm(vector)
        return normalized_vector

    
class FasttextMethod(WordEmbeddingMethod):
    def __init__(self,corpus):
        super().__init__(pickle.load(open("wiki-news-300d-1M.p", "rb")), corpus)
        
        
class GloveMethod(WordEmbeddingMethod):
    def __init__(self,corpus):
        super().__init__(pickle.load(open("glove.6B.200d.pickle", "rb")), corpus)
        

class TfidfMethod(SearchMethod):
    # corpus and titles should be lists of str
    def __init__(self, corpus: list):

        # TODO THIS BREAKS THE AUTOMATIC RELOAD OF THE APPLICATION, NEED TO FIND A WORKAROUND
        # for package in ['punkt']:
        #     nltk.download(package)
        
        self.tfidfVectorizer = TfidfVectorizer(tokenizer=get_stems, analyzer='word', stop_words=get_config("stopword_language"))
        self.tfidf_mat = self.tfidfVectorizer.fit_transform(corpus)
    
    def get_matrix(self):
        return self.tfidf_mat
    
    def txt_to_vec(self, txt):
        return self.tfidfVectorizer.transform([txt])


# '''
def get_stems(text,
              snowball_language=get_config("snowballstemmer_language"),
              configstemmer=get_config("stemmer")):
    snowball_language = snowball_language
    stemmerdict = {"porter": PorterStemmer(),
                   "lancaster": LancasterStemmer(),
                   "snowball": snowball.SnowballStemmer(snowball_language)}
    stemmer = stemmerdict[configstemmer]
    tokens = [word for word in nltk.word_tokenize(text) if len(word) > 1]
    stems = [stemmer.stem(item) for item in tokens]
    return stems

# '''