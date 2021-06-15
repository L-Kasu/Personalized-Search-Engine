# preprocessing function caller
# authors: Niklas Munkes, Lars Kasüschke

import os
from preprocessing import execution
from data import database
# init globals
req_nltk_packages = ['punkt', 'stopwords']
dir_archive = "./preprocessing/CISI_archive/"


# run preprocessing applying preprocessing_functions for a specified taskstring default: "tnwl"
# taskstrings: tasks you want to perfom
# filenames: attach filenames of file you want to preprocess, even if it was preprocessed already
# all files not preprocessed already (with current taskstring), will be preprocessed by default

def run_preprocessing(taskstring="tnwl", filenames=[]) -> tuple:

    if not (execution.is_taskstring_valid(taskstring) or len(taskstring == 0)):
        print("you need to put in a valid taskstring, one more try, or we go with 'tnwl'")
        i = input()
        taskstring = i if execution.is_taskstring_valid(i) else "tnwl"

    # get all files in dir_archive not preprocessed and append to filenames
    files_in_dir_archive = []
    for _, _, files in os.walk(dir_archive):
        files_in_dir_archive = files
        already_preprocessed_files = database.list_of_files
        filenames += list(filter(lambda file: taskstring + "_pp_" + file not in already_preprocessed_files, files))
        break

    # remove duplicates and filenames not in archive:
    filenames = list(set(filenames) & (set(files_in_dir_archive)))

    # preprocess all files in filenames
    for filename in files_in_dir_archive:
        if filename in filenames:
            execution.pre_processor(taskstring, filename)
            print("we have successfully preprocessed: " + filename + " with tasksstring: " + taskstring + "")
        else:
            print("we got " + filename + " already with: " + taskstring)

    print("\n")

    return taskstring, filenames
