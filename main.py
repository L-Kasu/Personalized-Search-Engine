# simple application to run the search from preprocessing to the returned query
# author: Lars Kasüschke
import evaluation
import pp_main
import pp_preprocessing_functions
import searching_algorithm
import inverted_matrix
import pp_execution_functions


def main():
    # preprocessing
    pp_main

    print("\nEnter the words you are looking for:")
    print('> ', end='')
    query = {input()}

    # create the inverted matrix
    print("with stemming (y/n)?")
    stemming = input()
    if stemming == "y":
        taskstring = pp_main.taskstring_1
    else:
        taskstring = pp_main.taskstring_2

    file = pp_main.dir_output + "pp_output_" + taskstring + "_" + pp_main.filename + ".txt"
    matrix = inverted_matrix.InvertedMatrix(file)

    stemmer = pp_execution_functions.taskstring_dict[matrix.get_taskstring()[-1]]

    # preprocess query and execute searching algorithm
    preprocessed_query = pp_preprocessing_functions.preprocessing_pipeline(query, stemmer)
    as_list = list(preprocessed_query)
    documents = searching_algorithm.and_search(as_list, matrix)

    if documents == []:
        print("There are no documents that contain all of the words you are looking for.")
    else:
        print("These are the documents you were looking for:")
        print(documents)

    # print("\nDo you want to evaluate your search (y/n)?")
    # print('> ', end='')
    # if input() == "y":
    #     evaluation
    #     print("The evaluation results con be found at ./eval_output/evaluation.txt")
    #     exit()
    # else:
    #     exit()


if __name__=="__main__":
    main()

