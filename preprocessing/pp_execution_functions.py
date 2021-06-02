# preprocessing function container
# authors: Niklas Munkes, Lars Kasüschke

import sys
import time
import nltk

import database
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
        pp_item = []
        for line in container.readlines():
            if line.startswith(".I"):
                index_adjustment = int(line.lstrip(".I ").rstrip("\n")) - 1
                pp_container.write(".I " + str(index_adjustment))
                pp_item.append({"I": index_adjustment})
                pp_container.write("\n")
            elif line.startswith(".W") or line.startswith(".T"):
                reduced_line = line[3:]
                line_reduction = line[:3]
                processing_item = {reduced_line}

                for i in range(0, len(taskstring)):
                    processing_item = read_taskstring_at_index(taskstring, i, processing_item, taskstring_dict)

                pp_container.write(line_reduction + str(processing_item))
                item_index = "W" if line.startswith(".W") else "T"
                pp_item[-1][item_index] = processing_item
                pp_container.write("\n")
            elif line.startswith(".A") or line.startswith(".X"):
                pp_container.write(line)
                line_without_prefix = line[3:].strip()
                item_index = "A" if line.startswith(".A") else "X"
                pp_item[-1][item_index] = line_without_prefix
            else:
                if filename == "CISI.REL":
                    split_line = line.split()
                    # adjust index for rel file
                    for i in range(0, 2):
                        try:
                            split_line[i] = int(split_line[i]) - 1
                        finally:
                            continue
                    pp_item.append(split_line)


        database.save_object(pp_item, taskstring + "_pp_" + filename)
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
