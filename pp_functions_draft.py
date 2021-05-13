# draft function container for preprocessing_draft.py
# author: Niklas Munkes

import sys


dir_containers = "./PP_Containers/"
dir_archive = "./CISI_archive/"

def printLines(n):
    with open(dir_archive+'CISI.ALL') as file:
        lines = ""
        for line in file.readlines():
            lines += "\n" + line.strip() if line.startswith(".") else " " + line.strip()
        lines = lines.lstrip("\n").split("\n")

        if n == "all":
            for l in lines:
                print(l)
        else:
            for l in lines[:n]:
                print(l)


# accepts the following str
# ".T" := title
# ".A" := author
# ".I" := index
# ".W" := writing (text body)
# ".X" := ??? (some numbers)
def extractLinesByType(selector):
    with open(dir_archive+'CISI.ALL') as file:
        lines = ""
        for line in file.readlines():
            lines += "\n" + line.strip() if line.startswith(".") else " " + line.strip()
        lines = lines.lstrip("\n").split("\n")
        for line in lines:
            if selector == ".T" or ".A" or ".I" or ".W" or ".X":
                if line.startswith(selector):
                    print(line)
            else:
                tb = sys.exc_info()[2]
                raise Exception("Invalid selector").with_traceback(tb)


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
