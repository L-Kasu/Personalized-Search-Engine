# preprocessing function container
# version: alpha1.4
# authors: Niklas Munkes, Lars Kasüschke


import sys
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from pp_sulyvahn import SulyvahnStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords as sw


def tokenize(raw_text):
    return word_tokenize(raw_text)


def normalize(tokens):
    normalized = []
    tokens_filtered = filter(lambda x: len(x) > 2 or x.isalpha() or x.isdigit(),
                             tokens)
    normalized += tokens_filtered
    normalized = ["".join(word.lower().split(".")) for word in normalized]
    return set(normalized)


def remove_stop_words(pp_set):
    new_pp_set = set()
    stopwords = set(sw.words("english"))
    for item in pp_set:
        if item not in stopwords:
            new_pp_set.add(item)
    return new_pp_set


def stemming(pp_set, stemmer):
    new_pp_set = set()
    for item in pp_set:
        if stemmer == "porter":
            new_pp_set.add(PorterStemmer().stem(item))
        elif stemmer == "lancaster":
            new_pp_set.add(LancasterStemmer().stem(item))
        elif stemmer == "sulyvahn":
            new_pp_set.add(SulyvahnStemmer().stem(item))
        else:
            tb = sys.exc_info()[2]
            raise Exception("Stemmer not recognized. Supported stemming algorithms are 'porter' and 'lancaster'").with_traceback(tb)
    return new_pp_set
