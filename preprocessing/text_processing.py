# preprocessing function container
# authors: Niklas Munkes, Lars Kasüschke
import sys
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from preprocessing.sulyvahn import SulyvahnStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords as sw


def tokenize(raw_text: list) -> list:
    # picks only sequences of alphanumeric characters and removes everything else
    r = ""
    for item in raw_text:
        r += item
    tokenizer = RegexpTokenizer(r'[\w\\.]+')
    r = tokenizer.tokenize(r)
    return list(r)


def normalize(tokens: list) -> list:
    result = map(lambda word: word.replace(".", "").lower(), tokens)
    return list(result)


def remove_stop_words(words: list) -> list:
    stopwords = list(sw.words("english"))
    words_without_stopwords = [word for word in words if word not in stopwords]
    return words_without_stopwords


def stemming(words: list, stemmer: list) -> list:
    if stemmer == "porter":
        stem = PorterStemmer().stem
    elif stemmer == "lancaster":
        stem = LancasterStemmer().stem
    else:
        stem = SulyvahnStemmer().stem
    stemmed_words = [stem(word) for word in words]
    return stemmed_words
