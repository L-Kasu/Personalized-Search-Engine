# clean function container for preprocessing_clean.py
# author: Niklas Munkes
import string

from nltk.tokenize import RegexpTokenizer
from typing import List
dir_containers = "./PP_Containers/"
dir_archive = "./CISI_archive/"


def saveTextAsTxt(filename):
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


def createTAWContainer(filename):
    taw_container = open(dir_containers+"pp_container_T-A-W_" + filename + ".txt", 'w')
    with open(dir_containers+"pp_container_" + filename + ".txt", 'r') as container:
        lines = ""
        for line in container.readlines():
            lines += "\n" + line.strip() if line.startswith(".") else " " + line.strip()
        lines = lines.lstrip("\n").split("\n")
        for line in lines:
            if line.startswith(".T")\
                or line.startswith(".A")\
                or line.startswith(".W"):
                taw_container.write(line)
                taw_container.write("\n")
        container.close()
    taw_container.close()


def __get_raw_text(filename) -> List[str]:
    raw_text= ""
    with open(dir_containers + filename, 'r') as container:
        for line in container.readlines():
            if line.startswith(".T") \
                    or line.startswith(".A") \
                    or line.startswith(".W"):
                line = line[3:]
            line = line.strip()
            raw_text += line
    return raw_text


def tokenize(filename) -> List[str]:
    raw_text = __get_raw_text(filename)
    tokenized = []
    tokenizer = RegexpTokenizer(r'((?<=[^\w\s])\w(?=[^\w\s])|(\W))+', gaps=True)
    tokenized_filtered = filter(lambda x: True if (len(x) > 1 or x.isalpha() or x.isdigit()) else False,
                            tokenizer.tokenize(raw_text))
    tokenized += tokenized_filtered
    return tokenized


# print(tokenize("pp_container_T-A-W_CISI.ALL.txt"))






