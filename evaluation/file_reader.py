def load_all():
    with open('evaluation/CISI_archive/CISI.ALL') as f:
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
    with open('evaluation/CISI_archive/CISI.QRY') as f:
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

