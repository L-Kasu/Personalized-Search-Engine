from tkinter import filedialog
from gui.builder_toolbox.search_util import *
from gui.builder_toolbox.settings_util import get_config
from gui.builder_toolbox.tkinter_objects.radiobuttons import *


def btn_select_directory(self, location):
    self.btn_select_directory = Button(location,
                                       text=get_config("txt_selectdir"),
                                       command=lambda: btn_select_directory_function(self),
                                       font=get_config("font_header_2")
                                       )
    self.btn_select_directory.config(bg=get_config("col_btn_idle"),
                                     fg=get_config("col_acc_minor"),
                                     activebackground=get_config("col_btn_active"),
                                     activeforeground=get_config("col_acc_minor"),
                                     relief=get_config("relief_btn")
                                     )
    if get_config("relief_btn") == "flat":
        self.btn_select_directory.config(borderwidth=0)
    self.btn_select_directory.pack(side=LEFT, anchor=W)


def btn_select_directory_function(self):
    self.dir_label['text'] = ""
    self.dir_selected = filedialog.askdirectory()
    dir_label(self, self.result_frame, self.dir_selected + "/")
    preprocess(self)


def btn_entry_search(self, location, color_idle, color_active, color_text):
    self.btn_entry_search = Button(location,
                                   text=get_config("txt_entrysearch"),
                                   command=lambda: search(self, self.search_entry.get())
                                   )
    self.btn_entry_search.config(bg=color_idle,
                                 fg=color_text,
                                 activebackground=color_active,
                                 activeforeground=color_text,
                                 font=get_config("font_header_2"),
                                 relief=get_config("relief_btn")
                                 )
    if get_config("relief_btn") == "flat":
        self.btn_entry_search.config(borderwidth=0)
    self.btn_entry_search.pack(side=LEFT)


def btn_entry_delete(self, location, color_idle, color_active, color_text):
    self.btn_entry_delete = Button(location,
                                   text=get_config("txt_entryclear"),
                                   command=lambda: btn_entry_delete_function(self)
                                   )
    self.btn_entry_delete.config(bg=color_idle,
                                 fg=color_text,
                                 activebackground=color_active,
                                 activeforeground=color_text,
                                 relief=get_config("relief_btn"),
                                 font=get_config("font_header_2")
                                 )
    if get_config("relief_btn") == "flat":
        self.btn_entry_delete.config(borderwidth=0)
    self.btn_entry_delete.pack(side=LEFT)


def btn_entry_delete_function(self):
    self.search_entry.delete(0, END)
    self.result_text.delete(0, END)


def btn_preview(self, location):
    self.btn_preview = Button(location,
                              text=get_config("txt_preview"),
                              command=lambda: preview_function(self),
                              font=get_config("font_header_2")
                              )
    self.btn_preview.config(bg=get_config("col_btn_idle"),
                            fg=get_config("col_acc_minor"),
                            activebackground=get_config("col_btn_active"),
                            activeforeground=get_config("col_acc_minor"),
                            relief=get_config("relief_btn")
                            )
    if get_config("relief_btn") == "flat":
        self.btn_preview.config(borderwidth=0)
    self.btn_preview.pack(side=BOTTOM)


def preview_function(self):
    selected_result_file = self.result_text.get(ANCHOR)
    if self.dir_selected == "":
        text = get_config("ERR_noDirectorySelected")
    elif selected_result_file == "":
        text = get_config("ERR_resultListEmpty")
    else:
        text = get_page_text(self, selected_result_file)
    self.preview_window = Toplevel(bg=get_config("col_bg_lgt"))
    self.preview_window.title(get_config("txt_preview") + ": " + self.result_text.get(ANCHOR))
    preview_window_label(self, self.preview_window, text)
    self.btn_exit = Button(self.preview_window, text=get_config("txt_exitpreview"), command=self.preview_window.destroy)
    self.btn_exit.config(bg=get_config("col_btn_idle"),
                         fg=get_config("col_acc_minor"),
                         activebackground=get_config("col_btn_active"),
                         activeforeground=get_config("col_acc_minor"),
                         relief=get_config("relief_btn")
                         )
    self.btn_exit.pack(side=BOTTOM)


# Settings button
def btn_settings(self, location):
    self.btn_settings = Button(location,
                               text=get_config("txt_settingsheader"),
                               command=lambda: settings_function(self),
                               font=get_config("font_header_2")
                               )
    self.btn_settings.config(bg=get_config("col_btn_idle"),
                             fg=get_config("col_acc_minor"),
                             activebackground=get_config("col_btn_active"),
                             activeforeground=get_config("col_acc_minor"),
                             relief=get_config("relief_btn")
                             )
    if get_config("relief_btn") == "flat":
        self.btn_settings.config(borderwidth=0)
    self.btn_settings.pack(side=LEFT)


def settings_function(self):
    self.window_settings = Toplevel(bg=get_config("col_bg"))
    self.window_settings.title("Settings")
    self.label_settings = Label(self.window_settings,
                                text="Settings",
                                font=get_config("font_header_1")
                                )
    self.label_settings.config(bg=get_config("col_bg"),
                               fg=get_config("col_acc_major")
                               )
    self.label_settings.pack(side=TOP, fill=X)
    choose_stemmer(self, self.window_settings)
    stopword(self, self.window_settings)
    self.btn_exit = Button(self.window_settings,
                           text=get_config("txt_okay"),
                           command=self.window_settings.destroy
                           )
    self.btn_exit.config(bg=get_config("col_btn_idle"),
                         fg=get_config("col_acc_minor"),
                         activebackground=get_config("col_btn_active"),
                         activeforeground=get_config("col_acc_minor"),
                         relief=get_config("relief_btn")
                         )
    self.btn_exit.pack(side=BOTTOM)

