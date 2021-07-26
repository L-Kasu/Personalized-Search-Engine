# utilities file for the ui builder


import os
# need pdfminer.six (diffrent from pdfminer)
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
from gui.builder_toolbox.settings_util import get_config
from search import *
import timeit

from search import search_class

'''    for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                                         password=password,
                                                         caching=caching,
                                                         check_extractable=True)):'''


def convert_pdf_to_txt(path) -> list:
    path_to_pdf = path
    pages = []
    for page_layout in extract_pages(path_to_pdf):
        page_str = ""
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                # print(element.get_text())
                page_str += element.get_text()
        pages.append(page_str.replace("\n", " "))
    return pages


def file_to_list_of_string(path):
    text = []
    if path.endswith("txt"):
        with open(path, "r") as container:
            try:
                text = container.read()
                text = [text]
            except:
                return []

    elif path.endswith("pdf"):
        text = convert_pdf_to_txt(path)
    else:
        print("unsupported file format at: " + path)

    return text


def search(self, query):
    self.result_text.delete(0, self.result_text.size())
    tf_obj = self.tf_object
    result = []
    start = timeit.default_timer()
    doc_indices = tf_obj.search_indicies(query)
    stop = timeit.default_timer()
    print("search took:", stop - start)
    docs_to_return = 10
    for index in doc_indices:
        result.append(tf_obj.titles[index])
    if result:
        result = result[:docs_to_return]
        for x in range(0, len(result)):
            self.result_text.insert(x, result[x])


def preprocess(self):
    start = timeit.default_timer()
    corpus_list = []
    titles = []
    # reading in the files
    for _, _, filenames in os.walk(self.dir_selected):
        dir = os.path.basename(self.dir_selected)
        for filename in filenames:
            path = self.dir_selected + "/" + filename
            pages = file_to_list_of_string(path)
            page_titles = [filename + ", " + get_config("txt_page") + " " + str(i + 1) for i in range(0, len(pages))]
            for i in range(0, len(pages)):
                page = pages[i]
                page_title = page_titles[i]
                if page:
                    titles.append(page_title)
                    corpus_list.append(page)
        stop = timeit.default_timer()
        print("reading in files took: ", str(stop - start), " for ", len(titles), " pages ")
        # TODO: implement saving to databases
        # create search object
        if titles and corpus_list:
            start = timeit.default_timer()
            self.tf_object = search_class.Search(corpus_list, titles)
            stop = timeit.default_timer()
            print("creating the search object took:", str(stop - start))
            '''
            start = timeit.default_timer()
            tf.tfidf(corpus_list, titles)
            stop = timeit.default_timer()
            print("For comparison: creating normal tf_obj only took: ", str(stop - start))
            '''

        break


def get_page_text(self, filename):
    tf_object = self.tf_object
    try:
        index = tf_object.titles.index(filename)
        return tf_object.corpus[index]
    except ValueError:
        return "File not Found"
    else:
        return "File not Found"
