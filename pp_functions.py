# function container for preprocessing_draft.py
# author: Niklas Munkes

import sys


def printLines(n):
    with open('./CISI_archive/CISI.ALL') as file:
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
    with open('./CISI_archive/CISI.ALL') as file:
        lines = ""
        for line in file.readlines():
            lines += "\n" + line.strip() if line.startswith(".") else " " + line.strip()
        lines = lines.lstrip("\n").split("\n")
        for line in lines:
            if selector == ".T":
                if line.startswith(selector):
                    print(line)
            elif selector == ".A":
                if line.startswith(selector):
                    print(line)
            elif selector == ".I":
                if line.startswith(selector):
                    print(line)
            elif selector == ".W":
                if line.startswith(selector):
                    print(line)
            elif selector == ".X":
                if line.startswith(selector):
                    print(line)
            else:
                tb = sys.exc_info()[2]
                raise Exception("Invalid selector").with_traceback(tb)

