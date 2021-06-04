# preprocessing function container
# authors: Niklas Munkes, Lars Kasüschke

import sys
import time
import nltk
from preprocessing import text_processing
from preprocessing import sulyvahn
from preprocessing import pp_main as pp
from data import database
taskstring_dict = { "t" : text_processing.tokenize,
                    "n" : text_processing.normalize,
                    "w" : text_processing.remove_stop_words,
                    "p" : lambda s: text_processing.stemming(s, "porter"),
                    "l" : lambda s: text_processing.stemming(s, "lancaster"),
                    "v" : lambda s: text_processing.stemming(s, "sulyvahn")}


def is_taskstring_valid(taskstring) -> bool:
    if taskstring == "":
        return True
    else:
        return type(taskstring) == str\
               and taskstring[0] in taskstring_dict\
               and is_taskstring_valid(taskstring[1:])


def inline(container):
    result = []
    for line in container:
        if line.startswith("."):
            result.append(line.replace("\n", " "))
        else:
            if result:
                result[-1] += line.replace("\n", " ")
    return result


def inline_for_REL(container):
    result = {}
    for line in container:
        split = line.split()
        split_0 = int(split[0]) -1
        split_1 = int(split[1]) -1
        if split_0 in result:
            result[split_0].append(split_1)
        else:
            result[split_0] = [split_1]
    return result


def pre_processor(taskstring: str, filename: str) -> None:
    with open(pp.dir_archive + filename, 'r') as container:
        preprocessed_items = []
        if(filename.endswith(".REL")):
            preprocessed_items = inline_for_REL(container)
        else:
            lines_as_list = inline(container)
            for line in lines_as_list:
                if line.startswith(".I"):
                    index_string_to_integer = int(line.split()[1])
                    preprocessed_items.append({"I": index_string_to_integer})
                elif line.startswith(".W") or line.startswith(".T"):
                    reduced_line = line[3:]
                    processing_item = chain_tasks_by_taskstring(taskstring, reduced_line)
                    item_index = "W" if line.startswith(".W") else "T"
                    preprocessed_items[-1][item_index] = processing_item
                elif line.startswith(".A") or line.startswith(".X"):
                    line_without_prefix = line[3:].strip()
                    item_index = "A" if line.startswith(".A") else "X"
                    preprocessed_items[-1][item_index] = line_without_prefix
                else:
                    continue



        database.save_object(preprocessed_items, taskstring + "_pp_" + filename)


def download_NLTK_packages(packages: list) -> None:
    for package in packages:
        nltk.download(package)
        time.sleep(1)


def chain_tasks_by_taskstring(taskstring: str, processing_item) -> list:
    result = [processing_item]
    for letter in taskstring:
        result = taskstring_dict[letter](result)
    return result


