# draft function container for preprocessing_draft.py
# author: Niklas Munkes

import sys
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')


dir_containers = "./PP_Containers/"
dir_archive = "./CISI_archive/"
dir_output = "./PP_output/"


def saveTextAsTxt(filename):
    container = open(dir_containers+"pp_container_"+filename+".txt", 'w')
    with open(dir_archive+filename) as file:
        lines = ""
        for line in file.readlines():
            lines += "\n" + line.strip() if line.startswith(".") else " " + line.strip()
        lines = lines.lstrip("\n").split("\n")
        for line in lines:
            container.write(line)
            container.write("\n")
        container.close()


def masterProcessor(filename):
    pp_container = open(dir_output+"pp_container_preprocessed_" + filename + ".txt", 'w')
    with open(dir_containers+"pp_container_" + filename + ".txt", 'r') as container:
        print("please chose a stemming algorithm:")
        print("1. PorterStemmer")
        print("2. LancasterStemmer")
        i = input()
        if i == "1":
            stemmer = "porter"
        elif i == "2":
            stemmer = "lancaster"
        else:
            tb = sys.exc_info()[2]
            raise Exception("Invalid input. Type either '1' or '2'").with_traceback(tb)
        print("\n")
        for line in container.readlines():
            if line.startswith(".T")\
                or line.startswith(".A")\
                or line.startswith(".W"):
                reduced_line = line[3:]
                line_reduction = line[:3]

                processing_list = tokenize(reduced_line)
                processing_set = normalize(processing_list)
                stopword = set(stopwords.words("english"))
                processing_set = removeStopWords(processing_set, stopword)
                processing_set = stemming(processing_set, stemmer)

                pp_container.write(line_reduction+str(processing_set))
                pp_container.write("\n")
            else:
                pp_container.write(line)
        container.close()
    pp_container.close()

def tokenize(raw_text):
    return word_tokenize(raw_text)


def normalize(tokens):
    normalized = []
    tokens_filtered = filter(lambda x: len(x) > 2 or x.isalpha() or x.isdigit(),
                             tokens)
    normalized += tokens_filtered
    normalized = ["".join(word.lower().split(".")) for word in normalized]
    return set(normalized)


def removeStopWords(pp_set, stopwords):
    new_pp_set = set()
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
        else:
            tb = sys.exc_info()[2]
            raise Exception("Stemmer not recognized. Supported stemming algorithms are 'porter' and 'lancaster'").with_traceback(tb)
    return new_pp_set
