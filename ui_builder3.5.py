# script for a simple ui
# version: alpha0.22
# author: Haitham Samaan, Niklas Munkes

#TODO: code cleanup

from tkinter import *
from tkinter import filedialog
import ui_builder_util as util


# style definitions
col_bg = "#3b3b3b"
col_bg_lgt = "#5f5f5f"
col_btn_idle = "#940000"
col_btn_active = "#d50000"
col_acc = "#2c24a0"
col_acc_lgt = "#00f707"
former_black = "#2c24a0"
former_white = "#2c24a0"

col_mark = "#ffb200"

font_header_1 = ("Arial", 15, "bold")
font_header_2 = ("Arial", 10, "bold")

master_height = 400
master_width = 600
filesearchspan_min = 0
filesearchspan_max = 200


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_window()
        self.create_grids()
        self.btn_select_dir(self.grid_00)
        self.frame_settings(self.grid_01, filesearchspan_min, filesearchspan_max)
        # self.frame_entry()


    def create_window(self):
        # instantiating a window
        self.master.geometry(str(master_height)+"x"+str(master_width))
        self.master.title("Search Engine")
        self.master.config(relief=FLAT, bd=7, bg=col_bg)


    def create_grids(self):
        self.grid_00 = self.create_grid(0, 0, master_height/2, master_width/3, 2, col_bg)
        self.grid_01 = self.create_grid(0, 2, master_height/2, master_width/3, 2, col_bg)
        self.grid_02 = self.create_grid(0, 4, master_height/2, master_width/3, 2, col_bg)
        self.grid_10 = self.create_grid(1, 0, master_height/2, master_width/2, 3, col_bg)
        self.grid_11 = self.create_grid(1, 3, master_height/2, master_width/2, 3, col_bg)


    def create_grid(self, m, n, h, w, n_span, col_bg):
        grid = Frame(self, height=str(h), width=str(w))
        grid.config(bg=col_bg)
        grid.grid(row=m, column=n, columnspan=n_span)
        return grid


    def btn_select_dir(self, location):
        self.select_directory = Button(location,
                                        relief=FLAT,
                                        text="Select Directory",
                                        command=util.select_dir
                                       )
        self.select_directory.config(bg=col_btn_idle,
                                        fg=col_acc_lgt,
                                        relief=FLAT,
                                        activebackground=col_btn_active,
                                        activeforeground=col_acc_lgt
                                     )
        self.select_directory.pack(side=RIGHT)


    def frame_settings(self, location, scale_min, scale_max):
        # Used many frames here to organize the different widgets better
        # a settings frame including: options for selecting file size and type
        self.settings_frame = Frame(location, relief=FLAT, bd=5)
        self.settings_frame.config(bg=col_bg_lgt)
        self.settings_frame.pack(side=TOP)

        self.settings_label = Label(self.settings_frame,
                                    text="Settings",
                                    font=font_header_1)
        self.settings_label.config(bg=col_bg_lgt, fg=col_acc)
        self.settings_label.grid(row=1, column=1)

        # File size
        self.file_size_frame = Frame(self.settings_frame)
        self.file_size_frame.config(bg=col_bg_lgt)
        self.file_size_frame.grid(row=2, column=1)

        self.file_size_label = Label(self.file_size_frame,
                                        text="Select file size (in MB)",
                                        font=font_header_2)
        self.file_size_label.config(bg=col_bg_lgt, fg=col_acc_lgt)
        self.file_size_label.grid(row=1, column=0)
        self.scale_filesize(self.settings_frame, scale_min, scale_max)

        #TODO: refactoring from here to end

        # File type
        self.file_type_frame = Frame(self.settings_frame)
        self.file_type_frame.config(bg=col_bg_lgt)
        self.file_type_frame.grid(row=4, column=1)

        self.file_type_label = Label(self.file_type_frame,
                                        text="Select file type:",
                                        font=font_header_2)
        self.file_type_label.config(bg=col_bg_lgt, fg=col_acc_lgt)
        self.file_type_label.grid(row=5, column=1)
        self.checkbtn_pdf()
        self.checkbtn_txt()
        self.checkbtn_docx()
        self.btn_preprocessing()

    def btn_preprocessing(self):
        self.preprocess_button = Button(self.settings_frame, text="preprocess", command=util.preprocess)
        self.preprocess_button.config(bg=col_bg,
                                      fg=col_acc_lgt,
                                      activebackground=col_bg_lgt,
                                      activeforeground=col_acc_lgt)
        self.preprocess_button.grid(row=7, column=1)

    def checkbtn_docx(self):
        self.docx = IntVar()
        self.file_type_docx = Checkbutton(self.file_type_frame, text="DOCX", variable=self.docx)
        self.file_type_docx.config(bg=col_bg_lgt,
                                   fg=col_acc_lgt,
                                   selectcolor=former_black,
                                   activebackground=col_bg_lgt,
                                   activeforeground=col_acc_lgt,
                                   highlightbackground=col_bg_lgt)
        self.file_type_docx.grid(row=6, column=2)

    def checkbtn_txt(self):
        self.txt = IntVar()
        self.file_type_txt = Checkbutton(self.file_type_frame, text="TXT", variable=self.txt)
        self.file_type_txt.config(bg=col_bg_lgt,
                                  fg=col_acc_lgt,
                                  selectcolor=former_black,
                                  activebackground=col_bg_lgt,
                                  activeforeground=col_acc_lgt,
                                  highlightbackground=col_bg_lgt)
        self.file_type_txt.grid(row=6, column=1)

    def checkbtn_pdf(self):
        self.pdf = IntVar()
        self.file_type_pdf = Checkbutton(self.file_type_frame, text="PDF", variable=self.pdf)
        self.file_type_pdf.config(bg=col_bg_lgt,
                                  fg=col_acc_lgt,
                                  selectcolor=former_black,
                                  activebackground=col_bg_lgt,
                                  activeforeground=col_acc_lgt,
                                  highlightbackground=col_bg_lgt)
        self.file_type_pdf.grid(row=6, column=0)

    def scale_filesize(self, location, min, max):
        self.file_size_scale = Scale(location,
                                     from_=min,
                                     to=max,
                                     length=150,
                                     orient=HORIZONTAL)
        self.file_size_scale.config(bg=col_bg_lgt, fg=col_acc_lgt,
                                    activebackground=col_bg_lgt,
                                    troughcolor=col_bg,
                                    highlightbackground=col_bg_lgt)
        self.file_size_scale.grid(row=3, column=1)

    def frame_entry(self):
        # Entry frame
        self.entry_frame = Frame(self)
        self.entry_frame.config(bg=col_bg)
        # entry_frame.config(relief=FLAT, bd=0.5)
        self.entry_frame.grid(row=1, column=2)

        # self.logo_label = Label(self.entry_frame, image=PhotoImage(file="./search_logo3.png"))
        # self.logo_label.config(bg=col_bg)
        # self.logo_label.grid(row=0, column=3)
        # search_logo = Label(entry_frame, text="tf_idf")
        # search_logo.config(font=("Arial", 40, "bold"),
        #                    fg="#a30bba",
        #                    bg=col_bg_lgt)
        # search_logo.grid(row=0, column=3)
        self.search_entry = Entry(self.entry_frame)
        self.search_entry.config(bg=former_black, fg=col_acc_lgt)
        self.search_entry.grid(row=1, column=3, ipadx=120, ipady=10)

        # Buttons frame
        self.buttons_frame = Frame(self.entry_frame)
        self.buttons_frame.grid(row=2, column=3)

        self.search_button = Button(self.buttons_frame, text="Search")
        self.search_button.config(bg=col_bg,
                                  fg=col_acc_lgt,
                                  activebackground=col_bg_lgt,
                                  activeforeground=col_acc_lgt)
        self.search_button.grid(row=2, column=3)
        self.delete_button = Button(self.buttons_frame, text="Clear", command=self.search_entry.delete(0, END))
        self.delete_button.config(bg=col_bg,
                                  fg=col_acc_lgt,
                                  activebackground=col_bg_lgt,
                                  activeforeground=col_acc_lgt)
        self.delete_button.grid(row=2, column=4)


    def frame_path(self):
        # Path frame
        self.path_frame = Frame(self.master)
        self.path_frame.config(bg=col_bg_lgt, relief=FLAT, bd=0.5)
        self.path_frame.grid(row=4, column=0)
        self.path_label = Label(self.path_frame,
                                text="Path to result:",
                                font=font_header_2)
        self.path_label.config(bg=col_bg_lgt, fg=col_acc_lgt)
        self.path_label.grid(row=5, column=0)
        self.path_text = Text(self.path_frame)
        self.path_text.config(bg=col_bg, fg=former_white)
        self.path_text.config(width=30, height=9)
        self.path_text.grid(row=6, column=0, ipadx=42, ipady=30)


    def frame_result(self):
        # Result frame
        self.result_frame = Frame(self.master)
        self.result_frame.grid(row=4, column=2)
        self.result_frame.config(bg=col_bg_lgt, relief=FLAT, bd=0.5)
        self.result_label = Label(self.result_frame,
                                    text="Search result:",
                                    font=font_header_2)
        self.result_label.config(bg=col_bg_lgt, fg=col_acc_lgt)
        self.result_label.grid(row=5, column=1)
        self.result_text = Text(self.result_frame)
        self.result_text.config(bg=col_bg, fg=former_white)
        self.result_text.config(width=30, height=9)
        self.result_text.grid(row=6, column=1, ipadx=81, ipady=30)


root = Tk()
app = Application(master=root)
app.mainloop()