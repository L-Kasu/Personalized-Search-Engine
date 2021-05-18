import pp_file_reader as pp


# builds the matrix with stemming and stopword removal
def build_matrix_with_stemming():
    matrix = inverted_matrix('PP_output/pp_output_tnwsp_CISI.ALL.txt')
    return matrix


# builds the matrix without stemming and stopword removal
def build_matrix_without_stemming():
    matrix = inverted_matrix('PP_output/pp_output_tnxx_CISI.ALL.txt')
    return matrix

# creates a dictionary of the mappings of each word(term) and its frequency (in how many documents it appears)
def frequency_mapping(matrix):
    mappings = {}
    for word in matrix:
        mappings[word]=len(matrix[word])
    return mappings


# gernerates an inverted matrix
# input is a collection as a txt file
# output is the matrix as a list
# in the form: [[word1, [doc_id1, doc_id1, ...], [word1, [doc_id1, do_id2, ...], ...]
# matrix[i][0] is the word
# matrix[i][1] is the list of documents containing the word
def inverted_matrix(file):
    matrix = {}
    collection = pp.file_reader(file)
    for x in collection:
        add_to_matrix(x['I'], x['W'], matrix)
    return matrix


# gets an list of words and the doc_id of the document containing the words and a inverted Matrix
# adds the words to the matrix
# returns the matrix
def add_to_matrix(doc_id, words, matrix):
    for word in words:
        if(word in matrix):
            matrix[word].append(doc_id)
        else:
            matrix[word] = [doc_id]
    return matrix

def print_matrix(matrix, filename):
    file = open(filename, "w")
    for word in matrix:
        file.write(word + ": " + str(matrix[word]) + "\n")
    file.close()


print_matrix(build_matrix_with_stemming(), "matrix_output/matrix_with_stemming.txt")
print_matrix(build_matrix_without_stemming(), "matrix_output/matrix_without_stemming.txt")
