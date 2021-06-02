# preprocessing function container
# authors: Niklas Munkes, Lars Kasüschke

import sys
import time
import nltk
import preprocessing.pp_preprocessing_functions as ppf


taskstring_dict = { "t" : ppf.tokenize,
                    "n" : ppf.normalize,
                    "w" : ppf.remove_stop_words,
                    "p" : lambda s: ppf.stemming(s, "porter"),
                    "l" : lambda s: ppf.stemming(s, "lancaster"),
                    "v" : lambda s: ppf.stemming(s, "sulyvahn")}


def pre_processor(taskstring: str, filename: str, dir_containers: str, dir_output: str) -> None:
    pp_container = open(dir_output + "pp_output_" + taskstring + "_" + filename + ".txt", 'w')
    with open(dir_containers + "pp_container_" + filename + ".txt", 'r') as container:
        for line in container.readlines():
            if line.startswith(".I"):
                pp_container.write(".I " + str(int(line.lstrip(".I ").rstrip("\n")) - 1))
                pp_container.write("\n")
            elif line.startswith(".W") or line.startswith(".T"):
                reduced_line = line[3:]
                line_reduction = line[:3]
                processing_item = {reduced_line}

                for i in range(0, len(taskstring)-1):
                    processing_item = read_taskstring_at_index(taskstring, i, processing_item, taskstring_dict)

                pp_container.write(line_reduction + str(processing_item))
                pp_container.write("\n")
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
            lines += "\n" + line.strip() if (line.startswith(".") or filename == "CISI.REL") else " " + line.strip()
        lines = lines.lstrip("\n").split("\n")
        for line in lines:
            container.write(line)
            container.write("\n")
        container.close()


def download_NLTK_packages(packages: list) -> None:
    for package in packages:
        nltk.download(package)
        time.sleep(1)


def read_taskstring_at_index(taskstring: str, index: int, processing_item: set, taskdict: dict) -> set:
    key = taskstring[index]
    if key in taskdict:
        return taskdict[key](processing_item)
    else:
        throw_exception_invalid_taskstring(taskstring, index, key)
