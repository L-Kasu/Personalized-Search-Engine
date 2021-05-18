import searching_algorithm

def evaluate():
    found_wanted_documents = 1   # number of the documents that were wanted and foud
    found_documents = 1   # number of documents that were found
    wanted_documents = 1   # number of wanted documents
    precision = found_wanted_documents/found_documents
    recall = found_wanted_documents / wanted_documents