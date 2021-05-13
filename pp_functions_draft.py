# draft function container for preprocessing_draft.py
# author: Niklas Munkes
import os
import sys
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
import nltk
# from nltk.corpus import stopwords
from typing import List


dir_containers = "./PP_Containers/"
dir_archive = "./CISI_archive/"
dir_output = "./PP_output/"

def printLines(n):
    with open(dir_archive+'CISI.ALL') as file:
        lines = ""
        for line in file.readlines():
            lines += "\n" + line.strip() if line.startswith(".") else " " + line.strip()
        lines = lines.lstrip("\n").split("\n")

        if n == "all":
            for l in lines:
                print(l)
        else:
            for l in lines[:n]:
                print(l)


# accepts the following str
# ".T" := title
# ".A" := author
# ".I" := index
# ".W" := writing (text body)
# ".X" := ??? (some numbers)
def extractLinesByType(selector):
    with open(dir_archive+'CISI.ALL') as file:
        lines = ""
        for line in file.readlines():
            lines += "\n" + line.strip() if line.startswith(".") else " " + line.strip()
        lines = lines.lstrip("\n").split("\n")
        for line in lines:
            if selector == ".T" or ".A" or ".I" or ".W" or ".X":
                if line.startswith(selector):
                    print(line)
            else:
                tb = sys.exc_info()[2]
                raise Exception("Invalid selector").with_traceback(tb)


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


# def createTAWContainer(filename):
#     taw_container = open(dir_containers+"pp_container_T-A-W_" + filename + ".txt", 'w')
#     with open(dir_containers+"pp_container_" + filename + ".txt", 'r') as container:
#         lines = ""
#         for line in container.readlines():
#             lines += "\n" + line.strip() if line.startswith(".") else " " + line.strip()
#         lines = lines.lstrip("\n").split("\n")
#         for line in lines:
#             if line.startswith(".T")\
#                 or line.startswith(".A")\
#                 or line.startswith(".W"):
#                 taw_container.write(line)
#                 taw_container.write("\n")
#         container.close()
#     taw_container.close()


# tokenizer


# normalizer



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

def masterProcesser(filename):
    pp_container = open(dir_output+"pp_container_preprocessed_" + filename + ".txt", 'w')
    with open(dir_containers+"pp_container_" + filename + ".txt", 'r') as container:
        # lines = ""
        for line in container.readlines():
        #     lines += "\n" + line.strip() if line.startswith(".") else " " + line.strip()
        # lines = lines.lstrip("\n").split("\n")
        # for line in lines:
            if line.startswith(".T")\
                or line.startswith(".A")\
                or line.startswith(".W"):
                # tokenizing
                print("tokenizing...")
                processing_set = tokenize("pp_container_T-A-W_CISI.ALL.txt")
                print("DONE")

                # normalization
                print("normalizing...pending")
                processing_set = processing_set
                # print("DONE")

                # stop word removal
                print("removing stop words...")
                nltk.download('stopwords')
                stopwords = set(stopwords.words("english"))
                removeStopWords(processing_set, stopwords)
                print("DONE")

                # stemming
                print("stemming with " + stemmer + " stemmer...")
                stemming(processing_set, stemmer)
                print("DONE")

                # export preprocessed file
                print("exporting processed set as 'preprocessed_set.txt' to '" + dir_output + "'...")
                with open(dir_output + "preprocessed_set.txt", "w") as outputfile:
                    outputfile.write(" ".join(processing_set))
                    outputfile.close()
                print("DONE")
                print(":)\n")

                print("1. Credits")
                print("2. Exit")
                i = input()
                if i == "1":
                    print("TODO: Credits")
                    exit()
                elif i == "2":
                    exit()
                else:
                    tb = sys.exc_info()[2]
                    raise Exception("Invalid input. Type either '1' or '2'").with_traceback(tb)

                pp_container.write(line)
                # pp_container.write("\n")
        container.close()
    pp_container.close()