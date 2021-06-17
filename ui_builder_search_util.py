# utilities file for the ui builder 3.5
# version: alpha0.23
# author: Haitham Samaan, Niklas Munkes

#TODO: code cleanup


from tkinter import filedialog
from preprocessing import pp_main as pm
from data import database
import tf
import io

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


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


# initiates the searching algorithm



# # Returns the file size the user chose
# def get_file_size():
#     return file_size_scale.get()


def any_file_to_str(path):
    text = ""
    if path.endswith("txt"):
        with open(path, "r") as container:
            text = container.read()
    elif path.endswith("pdf"):
        text = convert_pdf_to_txt(path)
    else:
        text = ""
        print("unsupported file format at:" + path)
    return text


# # Filters the search based on the user's choice of file types
# def file_type():
#     if pdf.get() == 1:
#         pass
#     elif txt.get() == 1:
#         pass
#     elif docx.get() == 1:
#         pass
#     pass
#
#
# # Gets user input
# def user_entry():
#     search_entry.get()
#
#
# # clears the entry box
# def delete():
#     search_entry.delete(0, END)