# draft file for PSE assignment 01, preprocessing
# author: Niklas Munkes

import nltk
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
import os
import sys
import pp_functions_draft as ppf
# from mpl_toolkits.mplot3d import Axes3D
# from sklearn.preprocessing import StandardScaler
# import matplotlib.pyplot as plt # plotting

####################
# Menu definitions #
####################

print("----------------------")
print("Simple IR System Setup")
print("----------------------\n")
print("place the files you wish to search here:")
print(ppf.dir_archive+"\n")

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


for dirname, _, filenames in os.walk(ppf.dir_archive):
    for filename in filenames:
        # print(os.path.join(dirname, filename))
        #
        # with open(os.path.join(dirname, filename)) as f:
        #     line_count = 0
        #     id_set = set()
        #
        #     for l in f.readlines():
        #         line_count += 1
        #         if filename == "CISI.REL":
        #             id_set.add(l.lstrip(" ").split(" ")[0])
        #         elif l.startswith(".I "):
        #             id_set.add(l.split(" ")[1].strip())
        #
        #     print(f"{filename} : {len(id_set)} items, over {line_count} lines.")

            # print("trying to load a raw document...")
            # file = open('document.txt')
            # file_raw = file.read()

            # ppf.printLines(5)
            # ppf.printLines("all")
            # ppf.extractLinesByType(".A")
            # ppf.extractLinesByType("italy")
        print("saving data as pp_container_"+filename+".txt...")
        ppf.saveTextAsTxt(filename)
        print("DONE")

filename = "CISI.ALL"
print("creating TAW container of " + filename)
ppf.createTAWContainer(filename)
print("DONE")


# tokenizing
print("tokenizing...")
processing_set = ppf.tokenize("pp_container_T-A-W_CISI.ALL.txt")
print("DONE")

# normalization
print("normalizing...pending")
processing_set = processing_set
# print("DONE")

# stop word removal
print("removing stop words...")
nltk.download('stopwords')
stopwords = set(stopwords.words("english"))
ppf.removeStopWords(processing_set, stopwords)
print("DONE")

# stemming
print("stemming with "+stemmer+" stemmer...")
ppf.stemming(processing_set, stemmer)
print("DONE")

# export preprocessed file
print("exporting processed set as 'preprocessed_set.txt' to '"+ppf.dir_output+"'...")
with open(ppf.dir_output+"preprocessed_set.txt", "w") as outputfile:
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
