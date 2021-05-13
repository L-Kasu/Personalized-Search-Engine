# clean function container for preprocessing_clean.py
# author: Niklas Munkes

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
