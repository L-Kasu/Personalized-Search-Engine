import os
def load_all():
    name = "CISI.ALL"
    path = ""
    for root, dirs, files in os.walk(os.sep.join([".", "evaluation/CISI_archive"])):
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
                    part = (split[0], split[-1])
                    a = int(part[0]) - 1
                    b = int(part[-1]) - 1
                    if a not in relation:
                        relation[a] = [b]
                    else:
                        relation[a].append(b)


    return [cisi_indecies, titles, corpus, relation]


def load_qry():
    name = "CISI.QRY"
    path = ""
    for root, dirs, files in os.walk(os.sep.join([".", "evaluation/CISI_archive"])):
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

def load_rel():
    name = "CISI.REL"
    path = ""
    relation = {}
    for root, dirs, files in os.walk(os.sep.join([".", "evaluation/CISI_archive"])):
        if name in files:
            path = os.path.join(root, name)
    with open(path) as f:
        for l in f.readlines():
            split = l.split()
            a = int(split[0]) - 1
            b = int(split[1]) - 1
            if a not in relation:
                relation[a] = [b]
            else:
                relation[a].append(b)
    return relation

