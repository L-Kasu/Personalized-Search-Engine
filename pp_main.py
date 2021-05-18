# preprocessing function caller
# version: alpha1.4
# authors: Niklas Munkes, Lars Kasüschke

import sys
import os
import pp_sulyvahn as pps
import pp_execution_functions as execution_function


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
        execution_function.save_text_as_txt(filename, dir_containers, dir_archive)
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

print("downloading the necessary packages for preprocessing...")
execution_function.download_NLTK_packages(req_nltk_packages)
print("DONE\n")

print("please chose a stemming algorithm:")
print("1. PorterStemmer")
print("2. LancasterStemmer")
print('> ', end='')
i = input()
if i == "1":
    stemmer = "porter"
elif i == "2":
    stemmer = "lancaster"
elif i == "273": # base damage of the Pontiff Knight Curved Sword
    stemmer = "sulyvahn"
    print("Thank you for choosing the Sulyvahn Stemmer. Please stand by while the Outrider Knights are dispatched.")
    print("If you like the Sulyvahn Stemmer, please consider leaving a positive review.\nIf you write it now, I'll make sure it is featured in the next issue of the Irithyll Morning Post.\nDo you want to write a review now (y/n)?")
    print('> ', end='')
    j = input()
    if j == "y":
        print('Your review:\n> ', end='')
        usr_review = input()
        pps.save_sulyvahn_review(usr_review, dir_output)
        print("Thank you!\n")
    elif j == "n":
        print(":(\n")
    elif j != "n":
        tb = sys.exc_info()[2]
        raise Exception("Stop wasting my time, you impudent fool! Type either 'y' or 'n'").with_traceback(tb)
    print("Should you stumble upon any bugs, something is not working or you just want to say hi, hit me up at freshpontiffsulyvahn89[at]profaned-flame-online.gov")
    print("Have a nice day :)")
    print("Cheers,")
    print("Pontiff Sulyvahn")
    print("\nContinue with the preprocessing (y/n)?\n> ", end='')
    k = input()
    if k == "y":
        pass
    else:
        exit()
else:
    tb = sys.exc_info()[2]
    raise Exception("Invalid input. Type either '1' or '2'").with_traceback(tb)

print("preprocessing...")

# see pp_execution_functions.py for taskstring structure

taskstring_1 = "tnws"
taskstring_2 = "tnxx"
if stemmer == "porter":
    taskstring_1 = taskstring_1 + "p"
elif stemmer == "lancaster":
    taskstring_1 = taskstring_1 + "l"
elif stemmer == "sulyvahn":
    taskstring_1 = taskstring_1 + "v"
else:
    tb = sys.exc_info()[2]
    raise Exception(
        "Stemmer not recognized. Supported stemming algorithms are 'porter' and 'lancaster'").with_traceback(tb)

execution_function.pre_processor(taskstring_1, filename, dir_containers, dir_output)
execution_function.pre_processor(taskstring_2, filename, dir_containers, dir_output)