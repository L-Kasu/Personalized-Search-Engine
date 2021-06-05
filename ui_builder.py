# script for a simple ui
# version: alpha0.1
# author: Niklas Munkes, Haitham Samaan

from tkinter import *


# Selects the directory the user wants to search in
def select_dir():
    pass


# Returns the file size the user chose
def get_file_size():
    file_size_scale.get()


# Preprocesses based on the search settings
def preprocess():
    pass


# Filters the search based on the user's choice of file types
def file_type():
    if pdf.get() == 1:
        pass
    elif txt.get() == 1:
        pass
    elif docx.get() == 1:
        pass
    pass


# instantiating a Window:
window = Tk()
window.geometry("600x400")
window.title("Search Engine")

# Allows the user to select the directory they want to search in
select_directory = Button(window,
                          text="Select Directory",
                          command=select_dir)
select_directory.pack(side=TOP, anchor=NW)

# Used many frames here to organize the different widgets better
# a settings frame including: options for selecting file size and type
settings_frame = Frame(window)
settings_frame.pack(side=TOP)

settings_label = Label(settings_frame, text="Settings")
settings_label.pack()

file_size_frame = Frame(settings_frame)
file_size_frame.pack()

file_size_label = Label(file_size_frame, text="Pick file size (in MB)")
file_size_label.pack()

file_size_scale = Scale(settings_frame,
                        from_=0,
                        to=200,
                        length=150,
                        orient=HORIZONTAL)
file_size_scale.pack()

file_type_frame = Frame(settings_frame)
file_type_frame.pack()

file_type_label = Label(file_type_frame, text="Select file type:")
file_type_label.pack()

pdf = IntVar()
file_type_pdf = Checkbutton(file_type_frame, text="PDF", variable=pdf)
file_type_pdf.pack()

txt = IntVar()
file_type_txt = Checkbutton(file_type_frame, text="TXT", variable=txt)
file_type_txt.pack()

docx = IntVar()
file_type_docx = Checkbutton(file_type_frame, text="DOCX", variable=docx)
file_type_docx.pack()

preprocess_button = Button(settings_frame, text="preprocess", command=preprocess)
preprocess_button.pack(side=BOTTOM)

# Entry frame
entry_frame = Frame(window)
entry_frame.pack(side=TOP, anchor=NE)

search_entry = Entry(entry_frame)
search_entry.pack(side=TOP)

search_button = Button(entry_frame, text="Search")
search_button.pack(side=BOTTOM)


window.mainloop()
