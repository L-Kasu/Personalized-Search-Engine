# preprocessing function caller
# authors: Niklas Munkes, Lars Kasüschke

import os
from preprocessing import execution

# init globals
req_nltk_packages = ['punkt', 'stopwords']
dir_archive = "./preprocessing/CISI_archive/"
dir_output = "./preprocessing/PP_output/"


def run_preprocessing() -> tuple:

    # archive -> container
    print("Place the files you wish to search here:")
    print("endings: '.ALL' for documents, 'QRY' for querys, 'REL' for expected results.")
    print(dir_archive + "\n")
    print("press any key to continue...")
    input()
    # choose-file-to-preprocess
    print("\nplease specify the file you wish to preprocess:")
    filenames = []
    filename = None
    for dirname, _, list_of_filenames in os.walk(dir_archive):
        # remove file ending and remove duplicates
        # filter all files with correct ending
        filenames = list_of_filenames
        filenames_split_by_point = list(filter(lambda x: len(x) >= 2,[filename.split(".") for filename in filenames]))
        filenames_without_ending = list(set([split[0] for split in filenames_split_by_point]))
        file_counter = 1
        for filename in filenames_without_ending:
            print(str(file_counter) + ". " + filename)
            file_counter += 1
        print('> ', end='')
        i = int(input())
        try:
            filename = filenames_without_ending[i -1]
        except("Index Error"):
            print("seems like we don't have that many files, try again")
            return run_preprocessing()
        except():
            return run_preprocessing()

    if not(type(filename) == str and len(filename) > 0):
        print("no file in " + dir_archive + " found")
        print("try_again")
        return run_preprocessing()
    else:
        relevant_files = list(filter(lambda split: split[0] == filename, filenames_split_by_point))
        filename_endings = list(set([split[-1] for split in relevant_files]))
        filenames = [filename + "." + ending for ending in filename_endings]
        print("downloading the necessary packages for preprocessing...")
        execution.download_NLTK_packages(req_nltk_packages)
        print("DONE\n")

        taskstrings = execution.choose_stemmer_and_return_taskstrings_as_list()

        # create preprocessing files
        execution.apply_preprocessor_to_files_and_taskstrings(taskstrings, filenames)
        return (taskstrings, filenames)

    if __name__ == "__main__":
        run_preprocessing()