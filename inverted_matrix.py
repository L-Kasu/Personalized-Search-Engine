import pp_file_reader as pp
import pp_main


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

    def get_matrix(self) -> dict:
        return self.matrix
    # builds the matrix with stemming and stopword removal (stemmer = lancaster)


def build_matrix_with_stemming() -> dict:
    matrix = inverted_matrix(pp_main.dir_output + "pp_output_" + pp_main.taskstring_1 + "_" + pp_main.filename + ".txt")
    return matrix


# builds the matrix without stemming and stopword removal
def build_matrix_without_stemming() -> dict:
    matrix = inverted_matrix(pp_main.dir_output + "pp_output_" + pp_main.taskstring_2 + "_" + pp_main.filename + ".txt")
    return matrix


# creates a dictionary of the mappings of each word(term) and its frequency (in how many documents it appears)
def frequency_mapping(matrix: dict) -> dict:
    mappings = {}
    for word in matrix:
        mappings[word] = len(matrix[word])
    return mappings


# gernerates an inverted matrix
# input is a collection as a txt file
# output is the matrix as a dictonary
# in the form: [[word1, [doc_id1, doc_id1, ...], [word1, [doc_id1, do_id2, ...], ...]
# matrix[i][0] is the word
# matrix[i][1] is the list of documents containing the word
def inverted_matrix(filename) -> dict:
    matrix = {}
    collection = pp.file_reader(filename)
    for x in collection:
        add_to_matrix(x['I'], x['W'], matrix)
    return matrix


# gets a list of words and the doc_id of the document containing the words and a inverted Matrix
# adds the words to the matrix
# returns the matrix
def add_to_matrix(doc_id: int, words: list, matrix: dict):
    for word in words:
        if word in matrix:
            matrix[word].append(doc_id)
        else:
            matrix[word] = [doc_id]
    return matrix


# prints matrix to a txt file
def print_matrix(matrix: dict, filename):
    file = open(filename, "w")
    for word in matrix:
        file.write(word + ": " + str(matrix[word]) + "\n")
    file.close()


print_matrix(build_matrix_with_stemming(), "matrix_output/matrix_" + pp_main.taskstring_1 + ".txt")
print_matrix(build_matrix_without_stemming(), "matrix_output/matrix_" + pp_main.taskstring_2 + ".txt")
