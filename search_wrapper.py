# simple application to run the search from preprocessing to the returned query
# author: Lars Kasüschke, Ensar Spahiu
import pp_main
import pp_preprocessing_functions
import searching_algorithm

def main():
    # preprocessing
    pp_main

    print("Enter the words you are looking for: ")
    query = input()

    # preprocess query and execute searching algorithm
    # TODO: make pipeline more flexible. e. g. flexible stemming and usable for any file, work on cross module compatibility
    documents = searching_algorithm.and_search(list(pp_preprocessing_functions.preprocessing_pipeline(query, "lancaster")))

    print("These are the documents you were looking for:")
    print(documents)

if __name__=="__main__":
    main()

