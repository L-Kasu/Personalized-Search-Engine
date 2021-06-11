# script for a simple ui
# version: alpha0.24
# author: Haitham Samaan, Niklas Munkes

#TODO: code cleanup

from tkinter import *
from tkinter import filedialog
import ui_builder_search_util as s_util


# style definitions
col_bg = "#3b3b3b"
col_bg_lgt = "#5f5f5f"
col_btn_idle = "#940000"
col_btn_active = "#d50000"
col_checkbtn_idle = "#bbbbbb"
col_checkbtn_active = "#ffff00"
# col_checkbtn_mark = "#"
col_scale_idle = "#bbbbbb"
col_acc = "#b3b3b3"
col_acc_lgt = "#b3b3b3"
col_mark = "#ffb200"

font_header_1 = ("Arial", 15, "bold")
font_header_2 = ("Arial", 10, "bold")
font_returntext = ("Arial", 10)

master_height = 400
master_width = 600
filesearchspan_min = 0
filesearchspan_max = 200


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_window()
        self.create_grids()
        self.pack()
        self.btn_select_dir(self.grid_00)
        self.frame_settings(self.grid_01, filesearchspan_min, filesearchspan_max)
        self.frame_entry(self.grid_02)
        self.frame_path(self.grid_10)
        self.frame_result(self.grid_11)


    def create_window(self):
        # instantiating a window
        self.master.geometry(str(master_width)+"x"+str(master_height))
        self.master.title("Search Engine")
        self.master.config(relief=FLAT, bd=7, bg=col_bg)

    def create_grids(self):
        self.grid_00 = self.create_grid(0, 0, master_height/2, master_width/3, 2, col_bg)
        self.grid_01 = self.create_grid(0, 2, master_height/2, master_width/3, 2, col_bg)
        self.grid_02 = self.create_grid(0, 4, master_height/2, master_width/3, 2, col_bg)
        self.grid_10 = self.create_grid(1, 0, master_height/2, master_width/2, 3, col_bg)
        self.grid_11 = self.create_grid(1, 3, master_height/2, master_width/2, 3, col_bg)

    def create_grid(self, m, n, h, w, n_span, col_bg):
        grid = Frame(self, height=h, width=w)
        grid.config(bg=col_bg)
        grid.grid(row=m,
                  column=n,
                  columnspan=n_span
                  )
        # grid.pack(expand=True, fill=BOTH)
        return grid

    def btn_select_dir(self, location):
        self.select_directory = Button(location,
                                        relief=FLAT,
                                        text="Select Directory",
                                        command=filedialog.askdirectory
                                       )
        self.select_directory.config(bg=col_btn_idle,
                                        fg=col_acc_lgt,
                                        activebackground=col_btn_active,
                                        activeforeground=col_acc_lgt,
                                        borderwidth=0
                                     )
        self.select_directory.grid(row=0, column=0)

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

        # File type
        self.file_type_frame = Frame(self.settings_frame)
        self.file_type_frame.config(bg=col_bg_lgt)
        self.file_type_frame.grid(row=4, column=1)

        self.file_type_label = Label(self.file_type_frame,
                                        text="Select file type:",
                                        font=font_header_2)
        self.file_type_label.config(bg=col_bg_lgt, fg=col_acc_lgt)
        self.file_type_label.grid(row=5, column=1)
        self.checkbtn_pdf(self.file_type_frame, col_bg_lgt, col_acc_lgt)
        self.checkbtn_txt(self.file_type_frame, col_bg_lgt, col_acc_lgt)
        self.checkbtn_docx(self.file_type_frame, col_bg_lgt, col_acc_lgt)
        self.btn_preprocessing(self.settings_frame, col_btn_idle, col_btn_active, col_acc_lgt)

    def btn_preprocessing(self, location, color_idle, color_active, color_text):
        self.preprocess_button = Button(location,
                                        text="preprocess",
                                        command=s_util.preprocess)
        self.preprocess_button.config(bg=color_idle,
                                      fg=color_text,
                                      activebackground=color_active,
                                      activeforeground=color_text,
                                      borderwidth=0)
        self.preprocess_button.grid(row=7, column=1)

    def checkbtn_docx(self, location, color_bg, color_text):
        self.docx = IntVar()
        self.file_type_docx = Checkbutton(location, text="DOCX", variable=self.docx)
        self.file_type_docx.config(bg=color_bg,
                                    fg=color_text,
                                    selectcolor=color_bg,
                                    activebackground=color_bg,
                                    activeforeground=color_text,
                                    highlightbackground=color_bg)
        self.file_type_docx.grid(row=6, column=2)

    def checkbtn_txt(self, location, color_bg, color_text):
        self.txt = IntVar()
        self.file_type_txt = Checkbutton(location, text="TXT", variable=self.txt)
        self.file_type_txt.config(bg=color_bg,
                                  fg=color_text,
                                  selectcolor=color_bg,
                                  activebackground=color_bg,
                                  activeforeground=color_text,
                                  highlightbackground=color_bg)
        self.file_type_txt.grid(row=6, column=1)

    def checkbtn_pdf(self, location, color_bg, color_text):
        self.pdf = IntVar()
        self.file_type_pdf = Checkbutton(location, text="PDF", variable=self.pdf)
        self.file_type_pdf.config(bg=color_bg,
                                  fg=color_text,
                                  selectcolor=color_bg,
                                  activebackground=color_bg,
                                  activeforeground=color_text,
                                  highlightbackground=color_bg)
        self.file_type_pdf.grid(row=6, column=0)

    def scale_filesize(self, location, min, max):
        self.file_size_scale = Scale(location,
                                     from_=min,
                                     to=max,
                                     length=150,
                                     orient=HORIZONTAL)
        self.file_size_scale.config(bg=col_bg_lgt, fg=col_acc_lgt,
                                    activebackground=col_bg_lgt,
                                    troughcolor=col_scale_idle,
                                    highlightbackground=col_bg_lgt)
        self.file_size_scale.grid(row=3, column=1)

    def frame_entry(self, location):
        # Entry frame
        self.entry_frame = Frame(location)
        self.entry_frame.config(bg=col_bg_lgt)
        self.entry_frame.grid(row=0,
                              column=0,
                              rowspan=2,
                              columnspan=3,
                              # sticky=EW
                              )

        # self.logo_label = Label(self.entry_frame, image=PhotoImage(file="./search_logo3.png"))
        # self.logo_label.config(bg=col_bg)
        # self.logo_label.grid(row=0, column=3)
        # search_logo = Label(entry_frame, text="tf_idf")
        # search_logo.config(font=("Arial", 40, "bold"),
        #                    fg="#a30bba",
        #                    bg=col_bg_lgt)
        # search_logo.grid(row=0, column=3)
        self.search_entry = Entry(self.entry_frame)
        self.search_entry.config(bg=col_bg, fg=col_acc_lgt)
        self.search_entry.grid(row=0,
                               column=0,
                               columnspan=3
                               )

        # Buttons frame
        self.buttons_frame = Frame(self.entry_frame)
        self.buttons_frame.grid(row=1,
                                column=0,
                                columnspan=2
                                )
        self.btn_entry_search(self.buttons_frame, col_btn_idle, col_btn_active, col_acc_lgt)
        self.btn_entry_delete(self.buttons_frame, col_btn_idle, col_btn_active, col_acc_lgt)

    def btn_entry_search(self, location, color_idle, color_active, color_text):
        self.search_button = Button(location,
                                    text="Search"
                                    )
        self.search_button.config(bg=color_idle,
                                  fg=color_text,
                                  activebackground=color_active,
                                  activeforeground=color_text,
                                  borderwidth=0
                                  )
        self.search_button.grid(row=2,
                                column=0
                                )

    def btn_entry_delete(self, location, color_idle, color_active, color_text):
        self.delete_button = Button(location,
                                    text="Clear",
                                    command=self.search_entry.delete(0, END))
        self.delete_button.config(bg=color_idle,
                                  fg=color_text,
                                  activebackground=color_active,
                                  activeforeground=color_text,
                                  borderwidth=0
                                  )
        self.delete_button.grid(row=2,
                                column=1
                                )

    def frame_path(self, location):
        self.path_label = Label(location,
                                text="Path to result",
                                font=font_header_2
                                )
        self.path_label.config(bg=col_bg_lgt,
                               fg=col_acc_lgt
                               )
        self.path_label.grid(row=0,
                             sticky=EW
                             )

        self.path_text = Listbox(location)
        self.path_text.config(bg=col_bg,
                              fg=col_bg_lgt,
                              font=font_returntext,
                              height=0,
                              width=0
                              )
        self.path_text.grid(row=1,
                            sticky=EW
                            )

    def frame_result(self, location):
        self.result_label = Label(location,
                                    text="Search result",
                                    font=font_header_2
                                    )
        self.result_label.config(bg=col_bg_lgt,
                                fg=col_acc_lgt
                                )
        self.result_label.grid(row=0,
                                sticky=EW
                                )

        self.result_text = Listbox(location)
        self.result_text.config(bg=col_bg,
                                fg=col_bg_lgt,
                                font=font_returntext,
                                height=0,
                                width=0
                                )
        self.result_text.grid(row=1,
                                sticky=EW
                                )


def main():
    root = Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
