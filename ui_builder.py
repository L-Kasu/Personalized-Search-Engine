# script for a simple ui
# version: alpha0.44
# author: Haitham Samaan, Niklas Munkes

# TODO: code cleanup

from tkinter import *
from tkinter import filedialog
import ui_builder_search_util as s_util
from ui_colortemplates.wip import *
from ui_languagepacks.english import *
import os
import tf
from data import database
import copy
import clustering

master_height = 500
master_width = 800
filesearchspan_min = 0
filesearchspan_max = 2000


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.dir_selected = ""
        self.tf_object = None
        self.create_window()
        self.split_window()
        self.pack()
        self.frame_select_dir()
        self.frame_settings(filesearchspan_min, filesearchspan_max)
        # self.frame_path()
        self.frame_result()
        self.frame_entry()

    def create_window(self):
        # instantiating a window
        self.master.geometry(str(master_width) + "x" + str(master_height))
        self.master.title(txt_mastertitle)
        self.master.config(relief=relief_frames, bd=7, bg=col_bg)

    def split_window(self):
        self.upper_frame = tkinter.Frame(self.master, bg=col_bg)
        self.upper_frame.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        self.lower_frame = tkinter.Frame(self.master, bg=col_bg)
        self.lower_frame.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)

    def frame_select_dir(self):
        self.select_dir_frame = tkinter.Frame(self.upper_frame, bg=col_bg)
        self.select_dir_frame.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, ipadx=5, ipady=5)
        self.btn_select_directory()

    def btn_select_directory(self):
        self.select_directory = tkinter.Button(self.select_dir_frame,
                                               relief=relief_frames,
                                               text=txt_selectdir,
                                               command=self.btn_select_directory_function,
                                               font=font_header_2
                                               )
        self.select_directory.config(bg=col_btn_idle,
                                     fg=col_acc_minor,
                                     activebackground=col_btn_active,
                                     activeforeground=col_acc_minor,
                                     relief=relief_btn
                                     )
        if relief_btn == "flat":
            self.select_directory.config(borderwidth=0)
        self.select_directory.pack(expand=True)

    def btn_select_directory_function(self):
        self.select_dir()
        self.select_dir_path_listbox.insert(1, self.dir_selected+"/")


    def frame_settings(self, scale_min, scale_max):
        # Used many frames here to organize the different widgets better
        # a settings frame including: options for selecting file size and type
        self.all_settings_frame = tkinter.Frame(self.upper_frame, bg=col_bg)
        self.all_settings_frame.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, ipadx=5, ipady=5)
        self.settings_frame = tkinter.Frame(self.all_settings_frame, relief=relief_frames, bd=5)
        self.settings_frame.config(bg=col_bg_lgt)
        self.settings_frame.pack(fill=tkinter.BOTH, expand=True)

        self.settings_label = tkinter.Label(self.settings_frame,
                                            text=txt_settingsheader,
                                            font=font_header_1)
        self.settings_label.config(bg=col_bg_lgt, fg=col_acc_major)
        self.settings_label.pack(side=tkinter.TOP, fill=tkinter.BOTH)

        # # File size
        # self.file_size_frame = Frame(self.settings_frame)
        # self.file_size_frame.config(bg=col_bg_lgt)
        # self.file_size_frame.pack(side=TOP, fill=X, expand=True)
        #
        # self.file_size_label = Label(self.file_size_frame,
        #                              text=txt_settingsfilesize,
        #                              font=font_header_2)
        # self.file_size_label.config(bg=col_bg_lgt, fg=col_acc_minor)
        # self.file_size_label.pack(side=TOP)
        # self.scale_filesize(self.file_size_frame, scale_min, scale_max)
        #
        # # File type
        # self.file_type_frame = Frame(self.settings_frame)
        # self.file_type_frame.config(bg=col_bg_lgt)
        # self.file_type_frame.pack(side=TOP, fill=X, expand=True)
        #
        # self.file_type_label = Label(self.file_type_frame,
        #                              text=txt_settingsfiletype,
        #                              font=font_header_2)
        # self.file_type_label.config(bg=col_bg_lgt, fg=col_acc_minor)
        # self.file_type_label.pack(side=TOP, fill=X)
        # self.checkbtn_pdf(self.file_type_frame, col_bg_lgt, col_acc_minor)
        # self.checkbtn_txt(self.file_type_frame, col_bg_lgt, col_acc_minor)
        # self.checkbtn_docx(self.file_type_frame, col_bg_lgt, col_acc_minor)
        self.btn_preprocessing(self.settings_frame, col_btn_idle, col_btn_active, col_acc_minor)

    def btn_preprocessing(self, location, color_idle, color_active, color_text):
        self.preprocess_button = tkinter.Button(location,
                                                text=txt_preprocess,
                                                command=lambda: self.preprocess())
        self.preprocess_button.config(bg=color_idle,
                                      fg=color_text,
                                      activebackground=color_active,
                                      activeforeground=color_text,
                                      relief=relief_btn,
                                      font=font_header_2)
        if relief_btn == "flat":
            self.preprocess_button.config(borderwidth=0)
        self.preprocess_button.pack(side=tkinter.BOTTOM)

    def checkbtn_docx(self, location, color_bg, color_text):
        self.docx = tkinter.IntVar()
        self.file_type_docx = tkinter.Checkbutton(location, text="DOCX", variable=self.docx)
        self.file_type_docx.config(bg=color_bg,
                                   fg=color_text,
                                   selectcolor=color_bg,
                                   activebackground=color_bg,
                                   activeforeground=color_text,
                                   font=font_header_2)
        self.file_type_docx.pack(expand=True, side=tkinter.LEFT)

    def checkbtn_txt(self, location, color_bg, color_text):
        self.txt = tkinter.IntVar()
        self.file_type_txt = tkinter.Checkbutton(location, text="TXT", variable=self.txt)
        self.file_type_txt.config(bg=color_bg,
                                  fg=color_text,
                                  selectcolor=color_bg,
                                  activebackground=color_bg,
                                  activeforeground=color_text,
                                  font=font_header_2)
        self.file_type_txt.pack(side=tkinter.LEFT, expand=True)

    def checkbtn_pdf(self, location, color_bg, color_text):
        self.pdf = tkinter.IntVar()
        self.file_type_pdf = tkinter.Checkbutton(location, text="PDF", variable=self.pdf)
        self.file_type_pdf.config(bg=color_bg,
                                  fg=color_text,
                                  selectcolor=color_bg,
                                  activebackground=color_bg,
                                  activeforeground=color_text,
                                  font=font_header_2)
        self.file_type_pdf.pack(side=tkinter.LEFT, expand=True)

    def scale_filesize(self, location, min, max):
        self.file_size_scale = tkinter.Scale(location,
                                             from_=min,
                                             to=max,
                                             length=150,
                                             orient=tkinter.HORIZONTAL)
        self.file_size_scale.config(bg=col_bg_lgt, fg=col_acc_minor,
                                    activebackground=col_interactionpoint_contrast,
                                    troughcolor=col_interactionpoint_idle,
                                    highlightbackground=col_bg_lgt,
                                    font=font_header_2
                                    )
        self.file_size_scale.pack(side=tkinter.TOP, fill=tkinter.X)

    def frame_entry(self):
        # Entry frame
        self.all_entry_frame = tkinter.Frame(self.upper_frame, bg=col_bg)
        self.all_entry_frame.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        self.entry_frame = tkinter.Frame(self.all_entry_frame, bg=col_bg_lgt, relief=relief_frames, bd=5)
        self.entry_frame.pack(fill=tkinter.X, expand=True)

        # self.logo_label = Label(self.entry_frame, image=PhotoImage(file="./search_logo3.png"))
        # self.logo_label.config(bg=col_bg)
        # self.logo_label.grid(row=0, column=3)
        # search_logo = Label(entry_frame, text="tf_idf")
        # search_logo.config(font=("Arial", 40, "bold"),
        #                    fg="#a30bba",
        #                    bg=col_bg_lgt)
        # search_logo.grid(row=0, column=3)
        self.search_entry = tkinter.Entry(self.entry_frame)
        self.search_entry.config(bg=col_entryfield_idle, fg=col_entryfield_contrast, font=font_header_2)
        self.search_entry.pack(side=tkinter.TOP, fill=tkinter.X, expand=True, ipadx=50)

        # Buttons frame
        self.buttons_frame = tkinter.Frame(self.entry_frame)
        self.buttons_frame.pack(side=tkinter.BOTTOM)
        self.btn_entry_search(self.buttons_frame, col_btn_idle, col_btn_active, col_acc_minor)
        self.btn_entry_delete(self.buttons_frame, col_btn_idle, col_btn_active, col_acc_minor)

    def btn_entry_search(self, location, color_idle, color_active, color_text):
        self.search_button = tkinter.Button(location,
                                            text=txt_entrysearch,
                                            command=lambda: self.search(self.search_entry.get())
                                            )
        self.search_button.config(bg=color_idle,
                                  fg=color_text,
                                  activebackground=color_active,
                                  activeforeground=color_text,
                                  font=font_header_2,
                                  relief=relief_btn
                                  )
        if relief_btn == "flat":
            self.search_button.config(borderwidth=0)
        self.search_button.pack(side=tkinter.LEFT)

    def btn_entry_delete(self, location, color_idle, color_active, color_text):
        self.delete_button = tkinter.Button(location,
                                            text=txt_entryclear,
                                            command=self.btn_entry_delete_function
                                            )
        self.delete_button.config(bg=color_idle,
                                  fg=color_text,
                                  activebackground=color_active,
                                  activeforeground=color_text,
                                  relief=relief_btn,
                                  font=font_header_2
                                  )
        if relief_btn == "flat":
            self.delete_button.config(borderwidth=0)
        self.delete_button.pack(side=tkinter.LEFT)

    def btn_entry_delete_function(self):
        self.search_entry.delete(0, tkinter.END)
        # self.path_text.delete(0, END)
        self.result_text.delete(0, tkinter.END)
        self.select_dir_path_listbox.delete(0, tkinter.END)

    def frame_path(self):
        self.path_frame = tkinter.Frame(self.lower_frame, bg=col_bg)
        self.path_frame.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        self.path_label = tkinter.Label(self.path_frame,
                                        text=txt_resultpath,
                                        font=font_header_2
                                        )
        self.path_label.config(bg=col_bg_lgt,
                               fg=col_acc_major
                               )
        self.path_label.pack(side=tkinter.TOP, fill=tkinter.X)

        self.path_text = tkinter.Listbox(self.path_frame)
        self.path_text.config(bg=col_bg_lgt,
                              fg=col_acc_minor,
                              font=font_returntext,
                              height=0,
                              width=0,
                              borderwidth=0,
                              highlightthickness=0
                              )
        self.path_text.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)

    def frame_result(self):
        self.result_frame = tkinter.Frame(self.lower_frame, bg=col_bg)
        self.result_frame.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        self.result_label = tkinter.Label(self.result_frame,
                                          text=txt_resultitems,
                                          font=font_header_1
                                          )
        self.result_label.config(bg=col_bg_lgt,
                                 fg=col_acc_major
                                 )
        self.result_label.pack(side=tkinter.TOP, fill=tkinter.X)
        self.listbox_dir(self.result_frame)
        self.result_text = tkinter.Listbox(self.result_frame)
        self.result_text.config(bg=col_bg_lgt,
                                fg=col_acc_minor,
                                font=font_returntext,
                                height=10,
                                width=0,
                                borderwidth=0,
                                highlightthickness=0
                                )
        self.result_text.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)

    def listbox_dir(self, location):
        self.select_dir_path_listbox = tkinter.Listbox(location,
                                                       font=font_header_2
                                                       )
        self.select_dir_path_listbox.config(bg=col_bg_lgt,
                                            fg=col_acc_minor,
                                            height=1,
                                            borderwidth=0,
                                            highlightthickness=0
                                            )
        self.select_dir_path_listbox.pack(side=tkinter.TOP, fill=tkinter.X)

    def search(self, query):
        self.result_text.delete(0, self.result_text.size())
        tf_obj = self.tf_object
        query_vec = tf_obj.tfidfVectorizer.transform([query])
        cluster_index = tf_obj.clustering.get_cluster_of_vector(query_vec)
        target_cluster = tf_obj.get_cluster_of_index(cluster_index)
        tf_copy = copy.deepcopy(tf_obj)
        tf_copy.tfidf_mat = target_cluster
        return_docs_num = 10

        if tf_copy:
            result = tf_copy.query_k_titles(query, return_docs_num)
            for x in range(0, len(result)):
                self.result_text.insert(x, result[x])

    # Selects the directory the user wants to search in
    def select_dir(self):
        self.dir_selected = filedialog.askdirectory()

    def preprocess(self):
        corpus_list = []
        titles = []
        for _, _, filenames in os.walk(self.dir_selected):
            titles = filenames
            dir = os.path.basename(self.dir_selected)
            for filename in filenames:
                path = self.dir_selected + "/" + filename
                text = s_util.any_file_to_str(path)
                corpus_list.append(text)

            if dir in database.list_of_files:
                self.tf_object = database.load_object(dir)
            else:
                if titles and corpus_list:
                    self.tf_object = clustering.Clustering(corpus_list, titles)
                    database.save_object(self.tf_object, dir)
            break


def main():
    root = tkinter.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
