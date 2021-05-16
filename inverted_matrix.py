import pp_file_reader as pp


# builds the matrix with stemming and stopword removal
def build_matrix_with_stemming():
    matrix = inverted_matrix('PP_output/pp_output_tnwsl_CISI.ALL.txt')
    return matrix


# builds the matrix without stemming and stopword removal
def build_matrix_without_stemming():
    matrix = inverted_matrix('PP_output/pp_output_tnxx_CISI.ALL.txt')
    return matrix


def frequenzy_mapping(matrix):
    # TODO implement function
    None


# gernerates an inverted matrix
# input is a collection as a txt file
# output is the matrix as a list
# in the form: [[word1, [doc_id1, doc_id1, ...], [word1, [doc_id1, do_id2, ...], ...]
# matrix[i][0] is the word
# matrix[i][1] is the list of documents containing the word
def inverted_matrix(file):
    matrix = []
    collection = pp.file_reader(file)
    for x in collection:
        add_to_matrix(x['I'], x['W'], matrix)
    return matrix


# gets an list of words and the doc_id of the document containing the words and a inverted Matrix
# adds the words to the matrix
# returns the matrix
def add_to_matrix(doc_id, words, matrix):
    document_id = [doc_id]
    for word in words:
        entry = [word, document_id]
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