# preprocessing function container
# authors: Niklas Munkes, Lars Kasüschke


import sys
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from preprocessing.sulyvahn import SulyvahnStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords as sw


def tokenize(raw_text: list) -> list:
    r = []
    if raw_text:
        r = raw_text[0]
    if type(r) == str:
        r = word_tokenize(r)
    return r


def normalize(tokens: list) -> list:
    tokens = list(tokens)
    normalized = []
    tokens_filtered = filter(lambda x: len(x) > 2 or x.isalpha() or x.isdigit(),
                             tokens)
    normalized += tokens_filtered
    normalized = ["".join(word.lower().split(".")) for word in normalized]
    return list(normalized)


def remove_stop_words(pp_set: list) -> list:
    new_pp_set = list()
    stopwords = list(sw.words("english"))
    for item in pp_set:
        if item not in stopwords:
            new_pp_set.append(item)
    return new_pp_set


def stemming(pp_set: list, stemmer: list) -> list:
    new_pp_set = list()
    for item in pp_set:
        if stemmer == "porter":
            new_pp_set.append(PorterStemmer().stem(item))
        elif stemmer == "lancaster":
            new_pp_set.append(LancasterStemmer().stem(item))
        elif stemmer == "sulyvahn":
            new_pp_set.append(SulyvahnStemmer().stem(item))
        else:
            tb = sys.exc_info()[2]
            raise Exception("Stemmer not recognized. Supported stemming algorithms are 'porter' and 'lancaster'").with_traceback(tb)
    return new_pp_set


# lightweight preprocessing for the query0
def preprocessing_pipeline(raw_text: list, stemmer: list) -> list:
    preprocessed_text = remove_stop_words(normalize(tokenize(raw_text)))
    try:
        preprocecessed_text = stemming(preprocessed_text, stemmer)
    finally:
        return preprocessed_text