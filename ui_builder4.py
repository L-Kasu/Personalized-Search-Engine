from tkinter import *
from tkinter import filedialog
import ui_builder_search_util as s_util
from ui_colortemplates.wip import *
from ui_languagepacks.english import *
import os
import tf
from data import database

master_height = 500
master_width = 800
filesearchspan_min = 0
filesearchspan_max = 2000

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.dir_selected = ""
        self.tf_object = None
        self.create_window()
        self.split_window()
        self.split_upper_frame()
        self.split_up_upper_frame()
        self.pack()
        self.btn_select_directory()
        self.menu_language()
        # self.frame_settings(filesearchspan_min, filesearchspan_max)
        # # self.frame_path()
        # self.frame_result()
        self.frame_entry()

    def create_window(self):
        # instantiating a window
        self.master.geometry(str(master_width) + "x" + str(master_height))
        self.master.title(txt_mastertitle)
        self.master.config(relief=relief_frames, bd=7, bg=col_bg)

    def split_window(self):
        self.upper_frame = Frame(self.master, bg=col_bg)
        self.upper_frame.pack(side=TOP, fill=BOTH, expand=True)
        self.lower_frame = Frame(self.master, bg=col_bg)
        self.lower_frame.pack(side=BOTTOM, fill=BOTH, expand=True)

    def split_upper_frame(self):
        self.up_upper_frame = Frame(self.upper_frame, bg=col_bg)
        self.up_upper_frame.pack(side=TOP, fill=X)
        self.lo_upper_frame = Frame(self.upper_frame, bg=col_bg)
        self.lo_upper_frame.pack(side=BOTTOM, fill=BOTH, expand=True)

    def split_up_upper_frame(self):
        self.left_up_upper_frame = Frame(self.up_upper_frame, bg=col_bg)
        self.left_up_upper_frame.pack(side=LEFT, fill=BOTH)
        self.right_up_upper_frame = Frame(self.up_upper_frame, bg=col_bg)
        self.right_up_upper_frame.pack(side=RIGHT, fill=BOTH)

    def btn_select_directory(self):
        self.select_directory = Button(self.left_up_upper_frame,
                                       relief=relief_frames,
                                       text=txt_selectdir,
                                       # command=self.btn_select_directory_function,
                                       font=font_header_2
                                       )
        self.select_directory.config(bg=col_btn_idle,
                                     fg=col_acc_minor,
                                     activebackground=col_btn_active,
                                     activeforeground=col_acc_minor,
                                     relief=relief_btn
                                     )
        self.select_directory.pack(side=LEFT, anchor=W)

        # if relief_btn == "flat":
        #     self.select_directory.config(borderwidth=0)
        # self.select_directory.pack(expand=True)

    # def btn_select_directory_function(self):
    #     self.select_dir()
    #     self.select_dir_path_listbox.insert(1, self.dir_selected+"/")

    def menu_language(self):
        clicked = StringVar()
        clicked.set("English")
        self.language = OptionMenu(self.right_up_upper_frame, clicked, "English", "Deutsch", "Español")
        self.language.config(relief=relief_btn,
                             font=font_header_2,
                             bg=col_btn_idle,
                             fg=col_acc_minor,
                             activebackground=col_btn_active,
                             activeforeground=col_acc_minor
                             )
        self.language.pack(side=LEFT, anchor=NE)

    def frame_entry(self):
        # Entry frame
        self.all_entry_frame = Frame(self.upper_frame, bg=col_bg)
        self.all_entry_frame.pack(side=BOTTOM, fill=BOTH, expand=True)
        self.entry_frame = Frame(self.all_entry_frame, bg=col_bg_lgt, relief=relief_frames, bd=5)
        self.entry_frame.pack(fill=X, expand=True)

        self.search_entry = Entry(self.entry_frame)
        self.search_entry.config(bg=col_entryfield_idle, fg=col_entryfield_contrast, font=font_header_2)
        self.search_entry.pack(side=TOP, fill=X, expand=True, ipadx=50)

        # Buttons frame
        self.buttons_frame = Frame(self.entry_frame)
        self.buttons_frame.pack(side=BOTTOM)
        self.btn_entry_search(self.buttons_frame, col_btn_idle, col_btn_active, col_acc_minor)
        self.btn_entry_delete(self.buttons_frame, col_btn_idle, col_btn_active, col_acc_minor)

    def btn_entry_search(self, location, color_idle, color_active, color_text):
        self.search_button = Button(location,
                                    text=txt_entrysearch,
                                    # command=lambda: self.search(self.search_entry.get())
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
        self.search_button.pack(side=LEFT)

    def btn_entry_delete(self, location, color_idle, color_active, color_text):
        self.delete_button = Button(location,
                                    text=txt_entryclear,
                                    # command=self.btn_entry_delete_function
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
        self.delete_button.pack(side=LEFT)

    # def btn_entry_delete_function(self):
    #     self.search_entry.delete(0, END)
    #     # self.path_text.delete(0, END)
    #     self.result_text.delete(0, END)
    #     self.select_dir_path_listbox.delete(0, END)



def main():
    root = Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()