from search import searching_algorithm as search


# evaluates the search, that uses the preprocessing with stemming
# returns a dictionary that associates the query index with the precision and recall
def evaluate_with_stemming() -> dict:
    qry = read_qry_list('./preprocessing/PP_output/pp_output_tnwsl_CISI.QRY.txt')
    rel = read_related_documents('./preprocessing/PP_output/pp_output_tnwsp_CISI.REL.txt')
    evaluation = {}
    for i in rel:
        searched = search.and_search(qry[i])
        found_wanted_documents = len(search.intersect(searched, rel[i]))  # number of the documents that were wanted and foud
        found_documents = len(searched)   # number of documents that were found
        wanted_documents = len(rel[i])  # number of wanted documents
        precision = get_precision(found_wanted_documents, found_documents)
        recall = get_recall(found_wanted_documents, wanted_documents)
        evaluation[i] = [precision, recall]
    return evaluation


def evaluate_without_stemming() -> dict:
    qry = read_qry_list('./preprocessing/PP_output/pp_output_tnxx_CISI.QRY.txt')
    rel = read_related_documents('./preprocessing/PP_output/pp_output_tnxx_CISI.REL.txt')
    evaluation = {}
    for i in rel:
        searched = search.and_search_without_stemming(qry[i])
        found_wanted_documents = len(search.intersect(searched, rel[i])) # number of the documents that were wanted and foud
        found_documents = len(searched)   # number of documents that were found
        wanted_documents =  len(rel[i])  # number of wanted documents
        precision = get_precision(found_wanted_documents, found_documents)
        recall = get_recall(found_wanted_documents, wanted_documents)
        evaluation[i] = [precision, recall]
    return evaluation


def get_precision(found_wanted_documents: int, found_documents: int) -> float:
    if found_documents == 0 :
        return 0
    return found_wanted_documents/found_documents


def get_recall(found_wanted_documents: int, wanted_documents: int) -> float:
    if wanted_documents == 0:
        return 0
    return found_wanted_documents/wanted_documents


# maps the querrys to an index
def read_qry_list(filename: str) -> dict:
    qry_list = {}
    file = open(filename, "r")
    i = 1
    for line in file:
        if line.startswith('.W {'):
            line_without_prefix = line[3:].strip()
            content = set()
            for element in line_without_prefix[1:-1].split(","):
                content.add(element[2:-1])
            qry_list[i] = list(content)
            i = i +1
    file.close()
    return qry_list


# maps the related documents to a querry index
def read_related_documents(filename: str) -> dict:
    relation = {}
    file = open(filename, "r")
    for line in file:
        i = 1
        for element in line.split():
            if i == 1:
                key = int(element)
                i = 2
            elif i == 2:
                value = int(element)
                i = 3
            elif i == 3:
                if key in relation:
                    relation[key].append(value)
                else :
                    relation[key] = [value]
                i = 4
            else:
                i = 1
    file.close()
    return relation


# saves the evaluation in txt file
def save_eval() -> None:
    evaluation_with_stemming = evaluate_with_stemming()
    file = open('eval_output/evaluation.txt', "w")
    file.write("with stemminng: \n")
    for i in evaluation_with_stemming:
        file.write("Querry " + str(i) + ":")
        file.write("\t\tprecission: "+ str(evaluation_with_stemming[i][0]))
        file.write("\t\trecall: " + str(evaluation_with_stemming[i][1]) + "\n")
    file.write("\n\n\nwithout stemming: \n")
    evaluation_without_stemming = evaluate_without_stemming()
    for i in evaluation_without_stemming:
        file.write("Querry " + str(i) + ":")
        file.write("\t\tprecission: "+ str(evaluation_without_stemming[i][0]))
        file.write("\t\trecall: " + str(evaluation_without_stemming[i][1]) + "\n")
    file.close()


save_eval()