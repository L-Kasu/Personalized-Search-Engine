from abc import ABC, abstractmethod
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from nltk.tokenize import word_tokenize

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
        split_str = word_tokenize(txt)
        vector = np.mean([self.word_embedding[word] for word in split_str if word in self.word_embedding],axis=0)
        normalized_vector = vector/np.linalg.norm(vector)
        return normalized_vector

    
class FasttextMethod(WordEmbeddingMethod):
    def __init__(self,corpus):
        super().__init__(pickle.load(open("wiki-news-300d-1M.p", "rb")), corpus)
        
        
class GloveMethod(WordEmbeddingMethod):
    def __init__(self,corpus):
        super().__init__(pickle.load(open("glove.6B.200d.p", "rb")), corpus)
        

class TfidfMethod(SearchMethod):
    # corpus and titles should be lists of str
    def __init__(self, corpus: list):#, tokenize=get_stems, swv=get_stopword_value()):

        # TODO THIS BREAKS THE AUTOMATIC RELOAD OF THE APPLICATION, NEED TO FIND A WORKAROUND
        # for package in ['punkt']:
        #     nltk.download(package)
        
        self.tfidfVectorizer = TfidfVectorizer(analyzer='word',stop_words= "english") #TfidfVectorizer(tokenizer=tokenize, analyzer='word', stop_words=swv)
        self.tfidf_mat = self.tfidfVectorizer.fit_transform(corpus)
    
    def get_matrix(self):
        return self.tfidf_mat
    
    def txt_to_vec(self, txt):
        return self.tfidfVectorizer.transform([txt])