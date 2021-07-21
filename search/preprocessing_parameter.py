import nltk
from nltk import PorterStemmer, LancasterStemmer
from nltk.stem import snowball
from gui.builder_toolbox.settings_util import get_config


def get_stopword_value(stop_word=get_config("stop_word"),
                       language=get_config("ID_lang")):
    stop_word = stop_word
    language = language
    stop_word_value = None
    if stop_word and language == "english":
        stop_word_value = language
    return stop_word_value


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
