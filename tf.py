from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
import pandas as pd
import numpy as np
import os


# currently not used
def same_len(corpus, titles):
    if len(new_corpus) != len(new_titles):
        print("not for each doc a title was given")
        print("number of docs:", len(corpus))
        print("number of titels:", len(titles))
        return False
    else:
        return True
    

class tfidf:
    # corpus and titles should be lists of str
    def __init__(self, corpus:list, titles:list):
        
        self.tfidfVectorizer = TfidfVectorizer(analyzer='word',stop_words= 'english')
        self.corpus = corpus
        self.titles = titles
        self.tfidf_mat = self.tfidfVectorizer.fit_transform(self.corpus)
       
    # corpus and titles should be lists of str
    def add_to_corpus(self, new_corpus:list, new_titles:list):
        
        self.corpus += new_corpus
        self.titles += new_titels
        
        self.tfidf_mat = self.tfidfVectorizer.fit_transform(self.corpus)
    
    # returns a list of indicies sorted by relevance
    def query_indicies(self, query: str):
        
        voc = self.tfidfVectorizer.get_feature_names()
        tfidfvectorizer_query = TfidfVectorizer(analyzer='word',stop_words= 'english',vocabulary=voc)
        
        query_tfidf = tfidfvectorizer_query.fit_transform([query])
        
        # matrix multiplicatin to calculate cosine similarity
        query_result_matrix = self.tfidf_mat @ query_tfidf.reshape(-1,1)
        
        # result_list will be filled with (index, idf-value) tuples
        result_list =[]
        
        for i in range(query_result_matrix.shape[0]):
            result_list.append((i,query_result_matrix[i,0]))
        
        #sorts from large to small based on idf-value
        result_list.sort(key=lambda x:x[1], reverse=True)
        
        only_indices = []
        for i in range(len(result_list)):
            only_indices.append(result_list[i][0])

        return only_indices
    
    # returns a list of all titles sorted by relevance
    def query_titles(self, query:str):
        
        indicies = self.query_indicies(query)
        titles = []
        for i in indicies:
            titles.append(self.titles[i])
        
        return titles
    
    # returns a list of the top k titles for a query
    def query_k_titles(self, query:str, k=10):
        
        return self.query_titles(query)[:k]
