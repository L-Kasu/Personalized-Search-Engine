# script for a simple ui
# version: alpha0.1
# author: Haitham Samaan

from tkinter import *


# Selects the directory the user wants to search in
def select_dir():
    pass


# Returns the file size the user chose
def get_file_size():
    return file_size_scale.get()


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


# Gets user input
def user_entry():
    return search_entry.get()


# clears the entry box
def delete():
    search_entry.delete(0, END)


# instantiating a Window:
window = Tk()
window.geometry("810x480")
window.title("Search Engine")
window.config(relief=RAISED, bd=7)
# Upper empty label
empty_up = Label(window, text=" ")
empty_up.grid(row=0, column=0)
# Allows the user to select the directory they want to search in
upleft_frame = Frame(window)
upleft_frame.grid(row=1, column=0)
# empty space
empty_0 = Label(upleft_frame, text="   ")
empty_0.grid(row=1, column=0)

select_directory = Button(upleft_frame,
                          text="Select Directory",
                          command=select_dir)
select_directory.grid(row=1, column=1)

# empty space
empty_1 = Label(upleft_frame, text="     ")
empty_1.grid(row=1, column=2)

# Used many frames here to organize the different widgets better
# a settings frame including: options for selecting file size and type
settings_frame = Frame(upleft_frame, relief=RAISED, bd=5)
settings_frame.grid(row=1, column=3)

settings_label = Label(settings_frame,
                       text="Settings",
                       font=("Arial", 15, "bold"))
settings_label.grid(row=1, column=1)

# File size
file_size_frame = Frame(settings_frame)
file_size_frame.grid(row=2, column=1)

file_size_label = Label(file_size_frame,
                        text="Select file size (in MB)",
                        font=("Arial", 10, "bold"))
file_size_label.grid(row=1, column=0)

file_size_scale = Scale(settings_frame,
                        from_=0,
                        to=200,
                        length=150,
                        orient=HORIZONTAL)
file_size_scale.grid(row=3, column=1)

# File type
file_type_frame = Frame(settings_frame)
file_type_frame.grid(row=4, column=1)

file_type_label = Label(file_type_frame,
                        text="Select file type:",
                        font=("Arial", 10, "bold"))
file_type_label.grid(row=5, column=1)

pdf = IntVar()
file_type_pdf = Checkbutton(file_type_frame, text="PDF", variable=pdf)
file_type_pdf.grid(row=6, column=0)

txt = IntVar()
file_type_txt = Checkbutton(file_type_frame, text="TXT", variable=txt)
file_type_txt.grid(row=6, column=1)

docx = IntVar()
file_type_docx = Checkbutton(file_type_frame, text="DOCX", variable=docx)
file_type_docx.grid(row=6, column=2)

preprocess_button = Button(settings_frame, text="preprocess", command=preprocess)
preprocess_button.grid(row=7, column=1)

# empty space
empty_2 = Label(window, text="     ")
empty_2.grid(row=1, column=1)

# Entry frame
entry_frame = Frame(window)
entry_frame.config(relief=RAISED, bd=5)
entry_frame.grid(row=1, column=2)

search_entry = Entry(entry_frame)
search_entry.grid(row=1, column=3, ipadx=120, ipady=10)

# Buttons frame
buttons_frame = Frame(entry_frame)
buttons_frame.grid(row=2, column=3)

search_button = Button(buttons_frame, text="Search")
search_button.grid(row=2, column=3)
delete_button = Button(buttons_frame, text="Clear", command=delete)
delete_button.grid(row=2, column=4)

# empty space
empty_3 = Label(window, text=" ")
empty_3.grid(row=3, column=0)

# Path frame
path_frame = Frame(window)
path_frame.grid(row=4, column=0)
path_label = Label(path_frame,
                   text="Path to result:",
                   font=("Arial", 10, "bold"))
path_label.grid(row=5, column=0)
path_text = Text(path_frame)
path_text.config(width=30, height=9)
path_text.grid(row=6, column=0, ipadx=43, ipady=30)

# Result frame
result_frame = Frame(window)
result_frame.grid(row=4, column=2)
result_label = Label(result_frame,
                     text="Search result:",
                     font=("Arial", 10, "bold"))
result_label.grid(row=5, column=1)
result_text = Text(result_frame)
result_text.config(width=30, height=9)
result_text.grid(row=6, column=1, ipadx=81, ipady=30)
window.mainloop()
