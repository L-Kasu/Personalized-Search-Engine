# preprocessing function container
# version: alpha1.23
# author: Niklas Munkes

import sys
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from regex import search


def pre_processor(taskstring, filename, dir_containers, dir_output):
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
                pp_container.write(".I " + str(int(line.lstrip(".I ").rstrip("\n")) - 1))
                pp_container.write("\n")
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
                        processing_set = remove_stop_words(processing_set, stopword)
                    elif task == "s" and (search("p", taskstring) or search("l", taskstring)):
                        print("stemming paragraph " + index + " with " + stemmer + " stemmer" + "...")
                        processing_set = stemming(processing_set, stemmer)
                    elif task not in "xpl":
                        throw_exception_invalid_taskstring(taskstring)

                print("adding preprocessed paragraph " + index + " to output file...", end='')
                pp_container.write(line_reduction + str(processing_set))
                pp_container.write("\n")
                print("DONE\n")
            else:
                pp_container.write(line)
        container.close()
    pp_container.close()


def throw_exception_invalid_taskstring(taskstring):
    tb = sys.exc_info()[2]
    raise Exception("'" + taskstring + "' is not a valid taskstring").with_traceback(tb)


def save_text_as_txt(filename, dir_containers, dir_archive):
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


def remove_stop_words(pp_set, stopwords):
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


def download_NLTK_packages(packages):
    for package in packages:
        nltk.download(package)

