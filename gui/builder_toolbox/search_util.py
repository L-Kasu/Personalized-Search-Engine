# utilities file for the ui builder


import os
# need pdfminer.six (diffrent from pdfminer)
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
from gui.builder_toolbox.settings_util import get_config
from search import clustering

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
    text = ""
    if path.endswith("txt"):
        with open(path, "r") as container:
            text = container.read()
    elif path.endswith("pdf"):
        text = convert_pdf_to_txt(path)
    else:
        print("unsupported file format at: " + path)
    return text


def search(self, query):
    self.result_text.delete(0, self.result_text.size())
    tf_obj = self.tf_object
    result = []
    doc_indices = tf_obj.search_in_cluster(query)
    docs_to_return = 10
    for index in doc_indices:
        result.append(tf_obj.titles[index])
    if result:
        result = result[:docs_to_return]
        for x in range(0, len(result)):
            self.result_text.insert(x, result[x])


def preprocess(self):
    corpus_list = []
    titles = []
    page_list = []
    for _, _, filenames in os.walk(self.dir_selected):
        dir = os.path.basename(self.dir_selected)
        for filename in filenames:
            path = self.dir_selected + "/" + filename
            page_list.append(file_to_list_of_string(path))
            for i in range(0, len(page_list)):
                page = page_list[i]
                if page:
                    titles.append(filename + ", " + get_config("txt_page") + " " + str(i + 1))
                    corpus_list.append(page)
        # TODO: implement saving to databases
        if titles and corpus_list:
            self.tf_object = clustering.Clustering(corpus_list, titles)
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


