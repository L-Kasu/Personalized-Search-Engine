import os
def load_all():
    name = "CISI.ALL"
    path = ""
    for root, dirs, files in os.walk(".\\CISI_archive\\"):
        if name in files:
            path = os.path.join(root, name)
    with open(path) as f:
        lines = ""
        for l in f.readlines():
            lines += "\n" + l.strip() if l.startswith(".") else " " + l.strip()
        lines = lines.lstrip("\n").split("\n")

    cisi_indecies = []
    titles = []
    corpus = []

    for l in lines:
        indicator = l[1:2]
        content = l[3:]
        if indicator == 'W':
            corpus.append(content)
        elif indicator == 'I':
            content = int(content)-1
            cisi_indecies.append(content)
        elif indicator == 'T':
            titles.append(content)
    return [cisi_indecies, titles, corpus]


def load_qry():
    name = "CISI.QRY"
    path = ""
    for root, dirs, files in os.walk("../search/CISI_archive\\"):
        if name in files:
            path = os.path.join(root, name)
    with open(path) as f:
        lines = ""
        for l in f.readlines():
            lines += "\n" + l.strip() if l.startswith(".") else " " + l.strip()
        lines = lines.lstrip("\n").split("\n")

    queries = {}
    i = 0

    for l in lines:
        indicator = l[1:2]
        content = l[3:]
        if l.startswith(".W"):
            queries[i] = content
            i += 1
    return queries

