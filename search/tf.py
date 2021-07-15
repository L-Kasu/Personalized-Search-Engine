import sys
import nltk
from nltk import PorterStemmer, LancasterStemmer
from nltk.stem import snowball
from sklearn.feature_extraction.text import TfidfVectorizer
from gui.builder_toolbox.settings_util import get_config


def check_len(corpus, titles):
    
    tb = sys.exc_info()[2]
    if(len(corpus) != len(titles)): raise Exception("Length of corpus doesn't match the length of titles.\n len(corpus) =", len(corpus),"len(titles) =", len(titles)).with_traceback(tb)


def cos_sim_func(query_vec, tfidf_mat):
    return tfidf_mat @ query_vec.T


class tfidf:
    # corpus and titles should be lists of str
    def __init__(self, corpus: list, titles: list):
        
        check_len(corpus, titles)

        # TODO THIS BREAKS THE AUTOMATIC RELOAD OF THE APPLICATION, NEED TO FIND A WORKAROUND
        # for package in ['punkt']:
        #     nltk.download(package)

        # set stop word removal
        stop_word = get_config("stop_word")
        language = get_config("ID_lang")
        stop_word_value = None
        if stop_word and language == "english":
            stop_word_value = language

        # set stemmer
        def tokenize(text):
            stemmerdict = {"porter": PorterStemmer(),
                           "lancaster": LancasterStemmer(),
                           "snowball": snowball.SnowballStemmer(language)}
            stemmer = stemmerdict[get_config("stemmer")]
            tokens = [word for word in nltk.word_tokenize(text) if len(word) > 1]
            stems = [stemmer.stem(item) for item in tokens]
            return stems

        self.tfidfVectorizer = TfidfVectorizer(tokenizer=tokenize, analyzer='word', stop_words=stop_word_value)
        self.corpus = corpus
        self.titles = titles
        self.tfidf_mat = self.tfidfVectorizer.fit_transform(self.corpus)
       
    # corpus and titles should be lists of str
    def add_to_corpus(self, new_corpus: list, new_titles: list):
        
        check_len(new_corpus, new_titles)
        
        self.corpus += new_corpus
        self.titles += new_titles
        
        self.tfidf_mat = self.tfidfVectorizer.fit_transform(self.corpus)
    
    # returns a list of indicies sorted by relevance


    def query_indicies(self, query: str):
        
        query_vec = self.tfidfVectorizer.transform([query])
        
        # matrix multiplicatin to calculate cosine similarity
        cos_sim = cos_sim_func(query_vec, self.tfidf_mat)
        
        # result_list will be filled with (index, cos-sim) tuples
        result_list =[]
        
        for i in range(cos_sim.shape[0]):
            result_list.append((i,cos_sim[i,0]))
        
        #sorts from large to small based on cos-sim value
        result_list.sort(key=lambda x: x[1], reverse=True)
        
        only_indicies = []
        for i in range(len(result_list)):
            only_indicies.append(result_list[i][0])

        return only_indicies
    
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
