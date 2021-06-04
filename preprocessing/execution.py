# preprocessing function container
# authors: Niklas Munkes, Lars Kasüschke

import sys
import time
import nltk
from preprocessing import text_processing
from preprocessing import sulyvahn
from preprocessing import main as pp
from data import database
taskstring_dict = { "t" : text_processing.tokenize,
                    "n" : text_processing.normalize,
                    "w" : text_processing.remove_stop_words,
                    "p" : lambda s: text_processing.stemming(s, "porter"),
                    "l" : lambda s: text_processing.stemming(s, "lancaster"),
                    "v" : lambda s: text_processing.stemming(s, "sulyvahn")}


def inline(container):
    result = []
    for line in container:
        if line.startswith("."):
            result.append(line.strip())
        else:
            if result:
                result[-1] += line.strip()
    return result



def choose_stemmer_and_return_taskstrings_as_list() -> list:
    print("please choose a stemming algorithm:")
    print("1. PorterStemmer")
    print("2. LancasterStemmer")
    print('> ', end='')
    i = input()
    if i == "1":
        stemmer = "porter"
    elif i == "2":
        stemmer = "lancaster"
    elif i == "273":  # base damage of the Pontiff Knight Curved Sword
        stemmer = "sulyvahn"
        sulyvahn.form_follows_function()
    else:
        print("nope, try aain")

    # see execution_functions.py for taskstring structure
    taskstring_1 = "tnw"
    taskstring_2 = "tn"

    if stemmer == "porter":
        taskstring_1 = taskstring_1 + "p"
    elif stemmer == "lancaster":
        taskstring_1 = taskstring_1 + "l"
    elif stemmer == "sulyvahn":
        taskstring_1 = taskstring_1 + "v"
    else:
        print("you can't fool me! Try again. And this time a valid input!")
        return choose_stemmer_and_return_taskstrings_as_list()

    return [taskstring_1, taskstring_2]


def pre_processor(taskstring: str, filename: str) -> None:
    with open(pp.dir_archive + filename, 'r') as container:
        preprocessed_items = []
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
                print("line without index")
                continue

        database.save_object(preprocessed_items, taskstring + "_pp_" + filename)


def throw_exception_invalid_taskstring(taskstring: str, index: int, key: str) -> Exception:
    tb = sys.exc_info()[2]
    raise Exception("'" + taskstring + "' is not a valid taskstring. Failed to read index " + str(index) + ", key " + key).with_traceback(tb)


def save_text_as_txt(filename: str, dir_containers: str, dir_archive: str) -> None:
    container = open(dir_containers+"pp_container_"+ filename+".txt", 'w')
    with open(dir_archive+filename) as file:
            lines = ""
            i = 0
            for line in file.readlines():
                if filename.endswith(".REL"):
                    lines += ".I " + str(i) + line.rstrip()
                    i += 1
                else:
                    lines = ""
                    for line in file.readlines():
                        lines += "\n" + line.strip() if (line.startswith(".")) else " " + line.strip()
                    lines = lines.lstrip("\n").split("\n")
            for line in lines:
                container.write(line)
                container.write("\n")
    container.close()



def download_NLTK_packages(packages: list) -> None:
    for package in packages:
        nltk.download(package)
        time.sleep(1)


def chain_tasks_by_taskstring(taskstring: str, processing_item) -> list:
    result = [processing_item]
    for letter in taskstring:
        result = taskstring_dict[letter](result)
    return result


def apply_preprocessor_to_files_and_taskstrings(taskstrings= str, filenames = list):
    for filename in filenames:
        for taskstring in taskstrings:
            pre_processor(taskstring, filename)

