# tf-idf algorithm function caller
# version: alpha1.0
# author: Niklas Munkes


import sys
import tf_idf.tf_idf_functions as func


def main(doc_dicts: list, qry_dicts: list) -> None:
    print("\nDo you also want to retrieve documents using the tf-idf algorithm (y/n)?")
    print('> ', end='')
    if input() == "y":
        want_tf_idf(doc_dicts, qry_dicts)
    else:
        exit()


def want_tf_idf(doc_dicts: list, qry_dicts: list) -> None:
    print("\nDo you want to retrieve documents for a predefined query or for your own query?")
    print("1. predefined query")
    print("2. custom query")
    print('> ', end='')
    i = input()
    if i == "1":
        want_predef_qry(doc_dicts, qry_dicts)
    elif i == "2":
        want_custom_qry(doc_dicts)
    else:
        tb = sys.exc_info()[2]
        raise Exception("Invalid input.").with_traceback(tb)


def want_predef_qry(doc_dicts: list, qry_dicts: list) -> None:
    print("\nPlease specify the index of the query (0-"+str(len(qry_dicts)-1)+")")
    print('> ', end='')
    index = int(input())
    if index in range(0, len(qry_dicts)):
        want_predef_qry_i(index, doc_dicts, qry_dicts)
    else:
        tb = sys.exc_info()[2]
        raise Exception("Invalid input.").with_traceback(tb)


def want_predef_qry_i(index: int, doc_dicts: list, qry_dicts: list) -> None:
    print("\nPlease specify how many documents you want to retrieve (1-" + str(len(doc_dicts)) + ")")
    print('> ', end='')
    doc_count = int(input())
    if doc_count in range(1, len(doc_dicts)+1):
        print("\nretrieving documents...", end='')
        result = func.get_k_documents_for_query_i(doc_dicts, qry_dicts, doc_count, index)
        print("DONE")
        print("\nHere is your result:")
        print(result)
        exit()
    else:
        tb = sys.exc_info()[2]
        raise Exception("Invalid input.").with_traceback(tb)


def want_custom_qry(doc_dicts: list) -> None:
    print("\nPlease enter the words you are looking for (term1, term2, ...)")
    print('> ', end='')
    query = input().split(", ")
    custom_qry_dict = [{"I": 0, "W": query}, {"I": 1, "W": ["dummy1", "dummy2"]}]
    print("\nPlease specify how many documents you want to retrieve (1-" + str(len(doc_dicts)) + ")")
    print('> ', end='')
    doc_count = int(input())
    if doc_count in range(1, len(doc_dicts) + 1):
        print("\nretrieving documents...", end='')
        result = func.get_k_documents_for_query_i(doc_dicts, custom_qry_dict, doc_count, 0)
        print("DONE")
        print("\nHere is your result:")
        print(result)
        exit()
    else:
        tb = sys.exc_info()[2]
        raise Exception("Invalid input.").with_traceback(tb)
