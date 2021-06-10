# utilities file for the ui builder 3.5
# version: alpha0.2
# author: Haitham Samaan, Niklas Munkes

#TODO: code cleanup


from tkinter import filedialog


# Selects the directory the user wants to search in
def select_dir():
    dir_selected = filedialog.askdirectory()
    return dir_selected


# # Returns the file size the user chose
# def get_file_size():
#     return file_size_scale.get()


# Preprocesses based on the search settings
def preprocess():
    pass


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