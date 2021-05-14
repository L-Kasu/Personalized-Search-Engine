# preprocessing function container
# version: alpha1.11
# author: Niklas Munkes

import sys
import os
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from regex import search


def preprocessingUIwrapper():

    # init globals
    req_nltk_packages = set('punkt' 'stopwords')
    dir_containers = "./PP_Containers/"
    dir_archive = "./CISI_archive/"
    dir_output = "./PP_output/"

    print("----------------------")
    print("Simple IR System Setup")
    print("----------------------\n")
    print("place the files you wish to search here:")
    print(dir_archive + "\n")

    for dirname, _, filenames in os.walk(dir_archive):
        for filename in filenames:
            print("saving data as pp_container_" + filename + ".txt...", end='')
            saveTextAsTxt(filename, dir_containers, dir_archive)
            print("DONE")

    print("\nplease specify the file you wish to preprocess:")
    filename = "default, should not appear"
    for dirname, _, filenames in os.walk(dir_archive):
        file_counter = 1
        for filename in filenames:
            print(str(file_counter) + ". " + filename)
            file_counter += 1
        filename = "default 2, should also not appear"
        print('> ', end='')
        i = int(input())
        for j in range(0, file_counter):
            if i == j:
                filename = filenames[i-1]
        if filename == "default 2, should also not appear":
            tb = sys.exc_info()[2]
            raise Exception("Invalid input.").with_traceback(tb)

    print("downloading the necessary packages for preprocessing...", end='')
    downloadNLTKPackages(req_nltk_packages)
    print("DONE")

    print("please chose a stemming algorithm:")
    print("1. PorterStemmer")
    print("2. LancasterStemmer")
    print('> ', end='')
    i = input()
    if i == "1":
        stemmer = "porter"
    elif i == "2":
        stemmer = "lancaster"
    else:
        tb = sys.exc_info()[2]
        raise Exception("Invalid input. Type either '1' or '2'").with_traceback(tb)

    print("preprocessing...")

    # taskstring structure
    # t: tokenizing (required)
    # n: normalizing (required)
    # w: stop word removal
    # s: stemming
    # p or l: stemmer (required if s is set)
    # x: task not active

    taskstring_1 = "tnws"
    taskstring_2 = "tnxx"
    if stemmer == "porter":
        taskstring_1 = taskstring_1 + "p"
    elif stemmer == "lancaster":
        taskstring_1 = taskstring_1 + "l"
    else:
        tb = sys.exc_info()[2]
        raise Exception("Stemmer not recognized. Supported stemming algorithms are 'porter' and 'lancaster'").with_traceback(tb)

    preProcessor(taskstring_1, filename, dir_containers, dir_output)
    preProcessor(taskstring_2, filename, dir_containers, dir_output)


def preProcessor(taskstring, filename, dir_containers, dir_output):
    if search("p", taskstring):
        stemmer = "porter"
    elif search("l", taskstring):
        stemmer = "lancaster"

    pp_container = open(dir_output + "pp_output_" + taskstring + "_" + filename + ".txt", 'w')
    with open(dir_containers + "pp_container_" + filename + ".txt", 'r') as container:
        index = "default, should not appear"
        for line in container.readlines():
            if line.startswith(".I"):
                index = line[3:].rstrip("\n")
            elif line.startswith(".W"):
                reduced_line = line[3:]
                line_reduction = line[:3]
                for task in taskstring:
                    if task == "t":
                        print("tokenizing paragraph " + index + "...")
                        processing_list = tokenize(reduced_line)
                    elif task == "n":
                        print("normalizing paragraph " + index + "...")
                        processing_set = normalize(processing_list)
                    elif task == "w":
                        print("removing stop words from paragraph " + index + "...")
                        stopword = set(stopwords.words("english"))
                        processing_set = removeStopWords(processing_set, stopword)
                    elif task == "s" and (search("p", taskstring) or search("l", taskstring)):
                        print("stemming paragraph " + index + " with " + stemmer + " stemmer" + "...")
                        processing_set = stemming(processing_set, stemmer)
                    elif task not in "xpl":
                        throwExeptionInvalidTaskstring(taskstring)

                print("adding preprocessed paragraph " + index + " to output file...", end='')
                pp_container.write(line_reduction + str(processing_set))
                pp_container.write("\n")
                print("DONE\n")
            else:
                pp_container.write(line)
        container.close()
    pp_container.close()


def throwExeptionInvalidTaskstring(taskstring):
    tb = sys.exc_info()[2]
    raise Exception("'" + taskstring + "' is not a valid taskstring").with_traceback(tb)


def saveTextAsTxt(filename, dir_containers, dir_archive):
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


def downloadNLTKPackages(packages):
    for package in packages:
        nltk.download(package)

