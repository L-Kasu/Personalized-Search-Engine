# utilities file for the ui builder


import io
import os
import tf
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from data import database


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    text = retstr.getvalue()
    retstr.close()
    return text


def any_file_to_str(path):
    text = ""
    if path.endswith("txt"):
        with open(path, "r") as container:
            text = container.read()
    elif path.endswith("pdf"):
        text = convert_pdf_to_txt(path)
    else:
        print("unsupported file format at:" + path)
    return text


def search(self, query):
    corpus_list = []
    for _, _, filenames in os.walk(self.dir_selected):
        titles = filenames
        dir = os.path.basename(self.dir_selected)
        for filename in filenames:
            path = self.dir_selected + "/" + filename
            text = any_file_to_str(path)
            corpus_list.append(text)

        if dir in database.list_of_files:
            self.tf_object = database.load_object(dir)
        else:
            if titles and corpus_list:
                self.tf_object = tf.tfidf(corpus_list, titles)
                database.save_object(self.tf_object, dir)
        break
    self.result_text.delete(0, self.result_text.size())
    return_docs_num = 10
    tf_obj = self.tf_object
    if tf_obj:
        self.result = tf_obj.query_k_titles(query, return_docs_num)
        for x in range(0, len(self.result)):
            self.result_text.insert(x, self.result[x])
