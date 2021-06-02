# simple application to run the search from preprocessing to the returned query
# author: Lars Kasüschke

from utilities import *
import evaluation.evaluation as ev

algorithm = search.searching_algorithm.and_search


def main_search(matrix: inverted_matrix.InvertedMatrix):
    print("\nEnter the words you are looking for:")
    print('> ', end='')
    query = {input()}
    taskstring = matrix.get_taskstring()
    stemmer = pp_execution_functions.taskstring_dict[taskstring[-1]]
    preprocessed_query = pp_preprocessing_functions.preprocessing_pipeline(query, stemmer)
    preprocessed_query_as_list = list(preprocessed_query)
    documents = algorithm(preprocessed_query_as_list, matrix)

    if documents == []:
        print("There are no documents that contain all of the words you are looking for.")
    else:
        print("These are the documents you were looking for:")
        print(documents)


def main_evaluate(matrix: inverted_matrix.InvertedMatrix):
    taskstring = matrix.get_taskstring()
    try:
        return database.load_object(taskstring + "_evaluation")
    finally:
        query_dict = ev.read_qry_list("./preprocessing/PP_output/pp_output_" + taskstring + "_CISI.QRY.txt")
        rel_dict = ev.read_related_documents("./preprocessing/PP_output/pp_output_" + taskstring + "_CISI.REL.txt")
        result = ev.evaluate(query_dict, rel_dict, matrix, algorithm)
        database.save_object(result, taskstring + "_evaluation")
        print(result)


def main_preprocess():
    datatuple = pp_main.preprocessing_main()
    filename = datatuple[0]
    if filename == "CISI.ALL":
        for i in range(1, 3):
            # i = 1: with stemming, i = 2: without stemming
            taskstring = datatuple[i]
            file = pp_main.dir_output + "pp_output_" + taskstring + "_" + filename + ".txt"
            matrix = inverted_matrix.InvertedMatrix(file)
            database.save_object(matrix, taskstring + "_matrix")



def main():
    print("do you want to preprocess? (type 'y', otherwise 'n'")
    i = input()
    if i == "y":
        main_preprocess()
    print("enter taskstring of matrix you want to work with: ")
    taskstring = input()
    matrix = database.load_object(taskstring + "_matrix")
    print("do you want to:")
    print("1: enter a search query")
    print("2: evaluate the current searching_algorithm")
    print("3: rerun")
    i = input()
    if i == "1":
        main_search(matrix)
    elif i == "2":
        main_evaluate(matrix)
    elif i == "3":
        main()
    else:
        exit()


if __name__ == "__main__":
    main()
