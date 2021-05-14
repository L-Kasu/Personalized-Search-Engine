# preprocessing function caller
# version: alpha1.24
# authors: Niklas Munkes, Lars Kasüschke

import sys
import os
import pp_functions as ppf


# init globals
req_nltk_packages = ['punkt', 'stopwords']
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
        ppf.save_text_as_txt(filename, dir_containers, dir_archive)
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
            filename = filenames[i - 1]
    if i not in range(0, file_counter):
        tb = sys.exc_info()[2]
        raise Exception("Invalid input.").with_traceback(tb)

print("downloading the necessary packages for preprocessing...", end='')
ppf.download_NLTK_packages(req_nltk_packages)
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
    raise Exception(
        "Stemmer not recognized. Supported stemming algorithms are 'porter' and 'lancaster'").with_traceback(tb)

ppf.pre_processor(taskstring_1, filename, dir_containers, dir_output)
ppf.pre_processor(taskstring_2, filename, dir_containers, dir_output)