# preprocessing function container
# authors: Niklas Munkes, Lars Kasüschke
import re
import sys
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from preprocessing.sulyvahn import SulyvahnStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords as sw


def tokenize(raw_text: list) -> list:
    # picks only sequences of alphanumeric characters and removes everything else
    r = ""
    for item in raw_text:
        r += item
    r = word_tokenize(r)
    return list(r)


# return a list of words
def __normalize_word(word: str) -> list:
    result = []
    words = word.split("-")
    for word in words:
        item = re.sub('\\W', "", word)
        item = item.lower()
        result.append(item)
    return result


def normalize(tokens: list) -> list:
    result = []
    for word in tokens:
        normalized_words =__normalize_word(word)
        for part_word in normalized_words:
            if part_word:
                result.append(part_word)
    return result


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
