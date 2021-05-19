import pp_file_reader as pp


class InvertedMatrix:

    # builds the instance of an matrix from an preprocessed file with following attributes:
    # - the matrix itself containg a pair of matrix as a dictionary { word: list_of_documents}
    # - taskstring defining how the file got preprocessed

    def __init__(self, filename):
        self.matrix = inverted_matrix(filename)

        # split string between "output_" and "_"
        self.taskstring = filename.split("output_")[1].split("_")[0]

    def get_taskstring(self):
        return self.taskstring

    def get_matrix(self):
        return self.matrix
    # builds the matrix with stemming and stopword removal (stemmer = lancaster)


def build_matrix_with_stemming():
    matrix = inverted_matrix('PP_output/pp_output_tnwsl_CISI.ALL.txt')
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
# output is the matrix as a dictonary
# in the form: [[word1, [doc_id1, doc_id1, ...], [word1, [doc_id1, do_id2, ...], ...]
# matrix[i][0] is the word
# matrix[i][1] is the list of documents containing the word
def inverted_matrix(filename):
    matrix = {}
    collection = pp.file_reader(filename)
    for x in collection:
        add_to_matrix(x['I'], x['W'], matrix)
    return matrix


# gets an dictionary of words and the doc_id of the document containing the words and a inverted Matrix
# adds the words to the matrix
#returns the matrix
def add_to_matrix(doc_id, words, matrix):
    for word in words:
        if word in matrix:
            matrix[word].append(doc_id)
        else:
            matrix[word] = [doc_id]
    return matrix