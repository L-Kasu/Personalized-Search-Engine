# clean function container for preprocessing_clean.py
# author: Niklas Munkes


def saveTextAsTxt(filename):
    container = open("pp_container_"+filename+".txt", 'w')
    with open('./CISI_archive/'+filename) as file:
        lines = ""
        for line in file.readlines():
            lines += "\n" + line.strip() if line.startswith(".") else " " + line.strip()
        lines = lines.lstrip("\n").split("\n")
        for line in lines:
            container.write(line)
            container.write("\n")
        container.close()

