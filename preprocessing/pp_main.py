# preprocessing function caller
# authors: Niklas Munkes, Lars Kasüschke

import os
from preprocessing import execution
from data import database
# init globals
req_nltk_packages = ['punkt', 'stopwords']
dir_archive = "./preprocessing/CISI_archive/"
dir_output = "./preprocessing/PP_output/"


# run preprocessing applying preprocessing_functions for a specified taskstring default: "tnwl"
# taskstrings: tasks you want to perfom
# filenames: attach filenames of file you want to preprocess, even if it was preprocessed already
# all files not preprocessed already (with current taskstring), will be preprocessed by default
def run_preprocessing(taskstring="tnwl", filenames=[]) -> tuple:
    if not execution.is_taskstring_valid(taskstring):
        print("you need to put in a valid taskstring, one more try, or we go with 'tnwl'")
        i = input()
        taskstring = i if execution.is_taskstring_valid(i) else "tnwl"
    print("Place the files you wish to preprocess: " + dir_archive)
    print("endings: '.ALL' for documents, 'QRY' for querys, 'REL' for expected results.")
    print("press any key when you are finished")
    input()
    # get all files in dir_archive not preprocessed and ppend tofilenames
    files_in_dir_archive = []
    for _, _, files in os.walk(dir_archive):
        files_in_dir_archive = files
        filenames += list(filter(lambda file: taskstring + "_pp_" + file not in database.list_of_files ,files))
        break
    # remove duplicates and filenames not in archive:
    filenames = list(set(filenames).union(set(files_in_dir_archive)))
    for filename in filenames:
        execution.pre_processor(taskstring, filename)
    print("we have successfully preprocessed: " + str(filenames) + " with tasksstring: " + taskstring + "\n")
    return taskstring, filenames

