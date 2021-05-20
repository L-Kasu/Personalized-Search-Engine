# preprocessing function container
# version: alpha1.4
# authors: Niklas Munkes, Lars Kasüschke

import sys
import time
import nltk
import pp_preprocessing_functions as ppf


def void(input: str) -> str:
    return input


def tprint(index: int) -> None:
    print("tokenizing paragraph " + str(index) + "...")


def nprint(index: int) -> None:
    print("normalizing paragraph " + str(index) + "...")


def wprint(index: int) -> None:
    print("removing stop words from paragraph " + str(index) + "...")


def sprint(index: int, stemmer: str) -> None:
    print("stemming paragraph " + str(index) + " with " + stemmer + " stemmer" + "...")


taskstring_dict = { "t" : ppf.tokenize,             # one input
                    "n" : ppf.normalize,            # one input
                    "w" : ppf.remove_stop_words,    # one input
                    "s" : ppf.stemming,             # two inputs !!!
                    "p" : "porter",
                    "l" : "lancaster",
                    "v" : "sulyvahn",
                    "x" : void }

taskstring_print_dict = {"tprint" : tprint,
                         "nprint" : nprint,
                         "wprint" : wprint,
                         "sprint" : sprint}


def pre_processor(taskstring: str, filename: str, dir_containers: str, dir_output: str) -> None:
    pp_container = open(dir_output + "pp_output_" + taskstring + "_" + filename + ".txt", 'w')
    with open(dir_containers + "pp_container_" + filename + ".txt", 'r') as container:
        index = "default, should not appear"
        for line in container.readlines():
            if line.startswith(".I"):
                lineindex = line[3:].rstrip("\n")
                pp_container.write(".I " + str(int(line.lstrip(".I ").rstrip("\n")) - 1))
                pp_container.write("\n")
            elif line.startswith(".W") or line.startswith(".T"):
                reduced_line = line[3:]
                line_reduction = line[:3]
                processing_item = {reduced_line}

                for i in range(0, len(taskstring)-1):
                    processing_item = read_taskstring_at_index(taskstring, i, processing_item, taskstring_dict, taskstring_print_dict, lineindex)

                print("adding preprocessed paragraph " + lineindex + " to output file...", end='')
                pp_container.write(line_reduction + str(processing_item))
                pp_container.write("\n")
                print("DONE\n")
            else:
                pp_container.write(line)
        container.close()
    pp_container.close()


def throw_exception_invalid_taskstring(taskstring: str, index: int, key: str) -> Exception:
    tb = sys.exc_info()[2]
    raise Exception("'" + taskstring + "' is not a valid taskstring. Failed to read index " + str(index) + ", key " + key).with_traceback(tb)


def save_text_as_txt(filename: str, dir_containers: str, dir_archive: str) -> None:
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


def download_NLTK_packages(packages: list) -> None:
    for package in packages:
        nltk.download(package)
        time.sleep(1)


def read_taskstring_at_index(taskstring: str, index: int,
                             processing_item: set, taskdict: dict, taskprintdict: dict, lineindex) -> any:
    key = taskstring[index]
    if key in taskdict and isinstance(taskdict[key], str):
        return taskdict[key]
    elif key in taskdict and index == 3:
        # stemming needs stemmer as additional argument!
        stemmer = read_taskstring_at_index(taskstring, 4, processing_item, taskdict, taskprintdict, lineindex)
        taskprintdict[key + "print"](lineindex, stemmer)
        return taskdict[key](processing_item, stemmer)
    elif key in taskdict:
        if key != "x":
            taskprintdict[key + "print"](lineindex)
        return taskdict[key](processing_item)
    else:
        throw_exception_invalid_taskstring(taskstring, index, key)
