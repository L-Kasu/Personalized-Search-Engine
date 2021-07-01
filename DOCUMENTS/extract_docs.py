import os


def extract_docs():
    with open("./CISI_ALL.txt", "r") as container:
        title = "default"
        for line in container.readlines():
            if line.startswith(".T"):
                title = line[3:].rstrip("\n")
            elif line.startswith(".W"):
                paragraph = line[3:]
                document = open("./doc_folder/" + title + ".txt", 'w')
                document.write(paragraph)
                document.close()
    container.close()

