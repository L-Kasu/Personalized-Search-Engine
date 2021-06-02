# simple application to run the search from preprocessing to the returned query
# author: Lars Kasüschke
import database
import tf_idf_main
from utilities import *
import evaluation.evaluation as ev

algorithm = search.searching_algorithm.and_search


def main_search(matrix: inverted_matrix.InvertedMatrix):
    # print("\nEnter the words you are looking for:")
    # print('> ', end='')
    # query = {input()}
    # taskstring = matrix.get_taskstring()
    # stemmer = pp_execution_functions.taskstring_dict[taskstring[-1]]
    # preprocessed_query = pp_preprocessing_functions.preprocessing_pipeline(query, stemmer)
    # preprocessed_query_as_list = list(preprocessed_query)
    # documents = algorithm(preprocessed_query_as_list, matrix)
    #
    # if documents == []:
    #     print("There are no documents that contain all of the words you are looking for.")
    # else:
    #     print("These are the documents you were looking for:")
    #     print(documents)
    tf_idf_main.main()


def main_evaluate(matrix: inverted_matrix.InvertedMatrix):
    taskstring = matrix.get_taskstring()
    try:
        return database.load_object(taskstring + "_evaluation")
    finally:
        query_dict = ev.query_list_to_dic(database.load_object(taskstring + "_pp" + "_CISI.QRY"))
        rel_dict = ev.rel_mapping_to_list_of_expected_results(database.load_object(taskstring + "_pp" + "_CISI.REL"))
        result = ev.evaluate(query_dict, rel_dict, matrix, algorithm)
        database.save_object(result, taskstring + "_evaluation")
        return result


def main_preprocess():
    datatuple = pp_main.preprocessing_main()
    filename = datatuple[0]
    if filename == "CISI.ALL":
        for i in range(1, 3):
            # i = 1: with stemming, i = 2: without stemming
            taskstring = datatuple[i]
            collection_of_pp_output = database.load_object(taskstring + "_pp_" + filename)
            matrix = inverted_matrix.InvertedMatrix(collection_of_pp_output, taskstring)
            database.save_object(matrix, taskstring + "_matrix")



def main():
    print("----------------------")
    print("Simple IR System Setup")
    print("----------------------\n")
    print("Do you want to preprocess (y/n)?")
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
    print("4: exit")
    i = input()
    if i == "1":
        main_search(matrix)
    elif i == "2":
        print(main_evaluate(matrix))
    elif i == "3":
        main()
    else:
        exit()


if __name__ == "__main__":
    main()
    '''
    matrix = database.load_object("tnwl_matrix").get_matrix()
    query = database.load_object("tnwp_pp_CISI.QRY")
    for item in query:
        print(item)
    print("\n")
    for item in matrix:
        print(item)
    print(matrix)
    '''
