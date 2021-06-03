# simple application to run the search from preprocessing to the returned query
# author: Lars Kasüschke

from utilities import *
algorithm = search.searching_algorithm.and_search


def main_search(taskstring):
    qry_dicts = database.load_object(taskstring + "_pp_" + "CISI.QRY")
    doc_dicts = database.load_object(taskstring + "_pp_" + "CISI.ALL")
    tf_idf_main.main(doc_dicts, qry_dicts)



def main_evaluate(taskstring):
    try:
        return database.load_object(taskstring + "_evaluation")
    finally:
        query_dict = database.load_object(taskstring + "_pp_" + "CISI.QRY")
        doc_dict = database.load_object(taskstring + "_pp_" + "CISI.ALL")
        rel_dict = ev.rel_mapping_to_list_of_expected_results(database.load_object(taskstring + "_pp" + "_CISI.REL"))
        result = ev.evaluate_tf_idf(query_dict, doc_dict, rel_dict)
        ev.save_eval_tf_idf(result, taskstring)
        database.save_object(result, taskstring + "_evaluation")
        return result
    pass


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
    print("enter taskstring you want to work with: ")
    taskstring = input()
    print("\nDo you want to:")
    print("1: enter a search query")
    print("2: evaluate the current searching_algorithm")
    print("3: rerun")
    print("4: exit")
    i = input()
    if i == "1":
        main_search(taskstring)
    elif i == "2":
        main_evaluate(taskstring)
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
