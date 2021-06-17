# preprocessing function container
# authors: Niklas Munkes, Lars Kasüschke

import re
import time
import nltk
from preprocessing import text_processing
from preprocessing import pp_main as pp
from data import database

taskstring_dict = {"t": text_processing.tokenize,
                   "n": text_processing.normalize,
                   "w": text_processing.remove_stop_words,
                   "p": lambda s: text_processing.stemming(s, "porter"),
                   "l": lambda s: text_processing.stemming(s, "lancaster"),
                   "v": lambda s: text_processing.stemming(s, "sulyvahn")}


def download_NLTK_packages(packages: list) -> None:
    for package in packages:
        nltk.download(package)
        time.sleep(1)


def apply_tasks_by_taskstring(taskstring: str, processing_item: str) -> list:
    result = [processing_item]
    for letter in taskstring:
        result = taskstring_dict[letter](result)
    return result


def is_taskstring_valid(taskstring) -> bool:
    if taskstring == "":
        return True
    else:
        return type(taskstring) == str \
               and taskstring[0] in taskstring_dict \
               and is_taskstring_valid(taskstring[1:])


# for REL files
def __transform_rel_to_query_to_expected_documents_dictionary(filename):
    with open(pp.dir_archive + filename, 'r') as container:
        result = {}
        for line in container:
            split = line.split()
            if len(split) > 1:
                doc_id = int(split[0]) - 1
                res_id = int(split[1]) - 1
                result[doc_id] = [split[1]] \
                    if doc_id not in result.keys() else result[doc_id] + [res_id]
        return result


# for indexed files
def __transform_indexed_file_to_dictionary_of_indexed_parts(taskstring, filename):
    index_letters, content = [], []
    with open(pp.dir_archive + filename, 'r') as container:

        for line in container:
            match_on_index_letter = re.fullmatch('(?s:(\\.)([A-Z])( |\n)(.*))', line)

            if match_on_index_letter:
                index_letter = match_on_index_letter.__getitem__(2)
                rest = match_on_index_letter.__getitem__(4)

                if index_letter.strip() == 'I':
                    rest = int(rest) - 1
                    index_letters.append([index_letter])
                    content.append([str(rest)])
                else:
                    index_letters[-1].append(index_letter)
                    content[-1].append(rest)

            elif content:
                content[-1][-1] += line
    # map indeces to content and turn into dictionary for every pair of indeces, content lists
    # returns a list of dictionary
    result = []
    for i, r in zip(index_letters, content):
        r = [apply_tasks_by_taskstring(taskstring, item) for item in r]
        result.append(dict(zip(i, r)))
    return result


# for any text file
def __simple_preprocess(taskstring, filename):
    with open(pp.dir_archive + filename, 'r') as container:
        big_string = " ".join(container.readlines())
    return apply_tasks_by_taskstring(taskstring, big_string)


# the mighty preprocessor
def pre_processor(taskstring: str, filename: str) -> list:
    # for relation files
    if filename.endswith(".REL"):
        preprocessed_items = __transform_rel_to_query_to_expected_documents_dictionary(filename)
    # for indexed files
    elif filename.endswith(".ALL") or filename.endswith(".QRY"):
        preprocessed_items = __transform_indexed_file_to_dictionary_of_indexed_parts(taskstring, filename)
    else:
        preprocessed_items = __simple_preprocess(taskstring, filename)
    database.save_object(preprocessed_items, taskstring + "_pp_" + filename)
    return list(map(lambda x: x["T"], preprocessed_items))
