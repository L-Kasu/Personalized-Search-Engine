def inverted_matrix(file):

    collection = extract_words(file)
    matrix = []
    for list in collection:
        add_to_matrix(list[0], list[1], matrix)
    print(matrix)
    return matrix


# extracts the words of a preprocessed collection into a collection list, consisting of a list for every document
# the list of a document consists of the doc_id and the list of words containing it
# input file: the preprocessed collection as txt file
def extract_words(file):
    with open(file, "r") as tf:
        lines = tf.read().split('\n')

    collection = []
    wordList = []
    document = []
    for l in lines:
        if l.startswith(".I"):
            doc_id = l.split(" ")[1].strip()
            document = [doc_id]
        elif l.startswith(".X"):
            document.append(wordList)
            collection.append(document)
            wordList = []
        else:
            text = l.strip()[3:] + " "   # The first 3 characters of a line can be ignored.
            text = text.strip()[1:-1]   # {,} removed
            words = text.split(",")
            for word in words:
                word = word.strip()[1:-1]
                if word not in wordList:
                    wordList.append(word)
    return collection


# gets an list of words and the doc_id of the document containing the words and a inverted Matrix
# adds the words to the matrix
# returns the matrix
def add_to_matrix(doc_id, words, matrix):
    id = [doc_id]
    for word in words:
        entry = [word, id]
        matrix.append(entry)
    matrix = clean_matrix(matrix)
    return matrix


# sorts the words in the matrix and then checks if there are words double
def clean_matrix(matrix):
    matrix.sort()
    i = 0
    while i < len(matrix)-1:
        """merges the doc_id lists if a word is double, without any duplicates"""
        if matrix[i][0] == matrix[i+1][0]:
            for x in matrix[i+1][1]:
                if x not in matrix[i][1]:
                    matrix[i][1].append(x)
            matrix.pop(i+1)
            matrix[i][1].sort()
        else:
            i += 1
    return matrix
