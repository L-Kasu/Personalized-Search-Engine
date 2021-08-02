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
    relation = {}

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
        elif indicator == 'X':
            split = content.split()
            for i in range(0, len(split)):
                if i % 3 == 0:
                    part = split[i:i+3]
                    part = list(map(lambda x: int(x), part))
                    for item in part:
                        if item not in relation:
                            relation[item] = part
                        else:
                            for item_ in part:
                                if item_ not in relation[item]:
                                    relation[item].append(item_)


    print(relation)
    return [cisi_indecies, titles, corpus, relation]


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

