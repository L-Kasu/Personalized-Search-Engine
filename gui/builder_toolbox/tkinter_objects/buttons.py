from tkinter import filedialog
from gui.builder_toolbox.search_util import *
from gui.builder_toolbox.tkinter_objects.labels import *
from gui.languagepacks.English import *
from gui.colortemplates.wip import *
from gui.ui_sizedefinitions import *


def btn_select_directory(self, location):
    self.btn_select_directory = Button(location,
                                       text=txt_selectdir,
                                       command=lambda: btn_select_directory_function(self),
                                       font=font_header_2
                                       )
    self.btn_select_directory.config(bg=col_btn_idle,
                                     fg=col_acc_minor,
                                     activebackground=col_btn_active,
                                     activeforeground=col_acc_minor,
                                     relief=relief_btn
                                     )
    if relief_btn == "flat":
        self.btn_select_directory.config(borderwidth=0)
    self.btn_select_directory.pack(side=LEFT, anchor=W)


def btn_select_directory_function(self):
    self.dir_selected = filedialog.askdirectory()
    dir_label(self, self.result_frame, self.dir_selected + "/")


def btn_entry_search(self, location, color_idle, color_active, color_text):
    self.btn_entry_search = Button(location,
                                   text=txt_entrysearch,
                                   command=lambda: search(self, self.search_entry.get())
                                   )
    self.btn_entry_search.config(bg=color_idle,
                                 fg=color_text,
                                 activebackground=color_active,
                                 activeforeground=color_text,
                                 font=font_header_2,
                                 relief=relief_btn
                                 )
    if relief_btn == "flat":
        self.btn_entry_search.config(borderwidth=0)
    self.btn_entry_search.pack(side=LEFT)


def btn_entry_delete(self, location, color_idle, color_active, color_text):
    self.btn_entry_delete = Button(location,
                                   text=txt_entryclear,
                                   command=lambda: btn_entry_delete_function(self)
                                   )
    self.btn_entry_delete.config(bg=color_idle,
                                 fg=color_text,
                                 activebackground=color_active,
                                 activeforeground=color_text,
                                 relief=relief_btn,
                                 font=font_header_2
                                 )
    if relief_btn == "flat":
        self.btn_entry_delete.config(borderwidth=0)
    self.btn_entry_delete.pack(side=LEFT)


def btn_entry_delete_function(self):
    self.search_entry.delete(0, END)
    self.result_text.delete(0, END)


def btn_preview(self, location):
    self.btn_preview = Button(location,
                              text=txt_preview,
                              command=lambda: preview_function(self, preview_size),
                              font=font_header_2
                              )
    self.btn_preview.config(bg=col_btn_idle,
                            fg=col_acc_minor,
                            activebackground=col_btn_active,
                            activeforeground=col_acc_minor,
                            relief=relief_btn
                            )
    if relief_btn == "flat":
        self.btn_preview.config(borderwidth=0)
    self.btn_preview.pack(side=BOTTOM)


def preview_function(self, n):
    selected_result_file = self.result_text.get(ANCHOR)
    if self.dir_selected == "":
        text = ERR_noDirectorySelected
    elif selected_result_file == "":
        text = ERR_resultListEmpty
    else:
        text = any_file_to_str(self.dir_selected + "/" + selected_result_file)[0:n:1] + "..."
    self.preview_window = Toplevel(bg=col_bg_lgt)
    self.preview_window.title(txt_preview + ": " + self.result_text.get(ANCHOR))
    preview_window_label(self, self.preview_window, text)
