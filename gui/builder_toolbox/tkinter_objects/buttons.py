from tkinter import filedialog
import gui
from gui.builder_toolbox.tkinter_objects.radiobuttons import *
from gui.builder_toolbox.search_util import *
from gui.builder_toolbox.windowcleaner import WindowCleaner


def default_btn(location, text, function):
    button = Button(location,
                    text=text,
                    command=function,
                    font=get_config("font_header_2"),
                    bg=get_config("col_btn_idle"),
                    fg=get_config("col_acc_btncontrast"),
                    bd=get_config("global_padding"),
                    activebackground=get_config("col_btn_active"),
                    activeforeground=get_config("col_acc_btncontrast"),
                    relief=get_config("relief_btn"),
                    borderwidth=[0 if get_config("relief_btn") == "flat" else 2]
                    )
    button.bind("<Enter>", lambda e: button.config(bg=get_config("col_btn_active")))
    button.bind("<Leave>", lambda e: button.config(bg=get_config("col_btn_idle")))
    return button


def btn_select_directory(self, location):
    default_btn(location,
                get_config("txt_selectdir"),
                lambda: btn_select_directory_function(self)
                ).pack(side=LEFT)


def btn_select_directory_function(self):
    self.dir_label['text'] = ""
    self.dir_selected = filedialog.askdirectory()
    dir_label(self.result_frame, self.dir_selected + "/")
    preprocess(self)


def btn_entry_search(self, location):
    default_btn(location,
                get_config("txt_entrysearch"),
                lambda: search(self, self.search_entry.get())
                ).pack(side=LEFT, anchor=CENTER)


def btn_entry_delete(self, location):
    default_btn(location,
                get_config("txt_entryclear"),
                lambda: btn_entry_delete_function(self)
                ).pack(side=RIGHT, anchor=CENTER)


def btn_entry_delete_function(self):
    self.search_entry.delete(0, END)
    self.result_text.delete(0, END)


def btn_preview(self, location):
    default_btn(location, get_config("txt_preview"), lambda: preview_function(self)).pack(side=BOTTOM, anchor=CENTER)


def preview_function(self):
    selected_result_file = self.result_text.get(ANCHOR)
    if self.dir_selected == "":
        text = get_config("ERR_noDirectorySelected")
    elif selected_result_file == "":
        text = get_config("ERR_resultListEmpty")
    else:
        text = get_page_text(self, selected_result_file)
    self.preview_window = Toplevel(bg=get_config("col_bg_lgt"), bd=get_config("global_padding"))
    self.preview_window.title(get_config("txt_preview") + ": " + self.result_text.get(ANCHOR))
    # WindowCleaner(self.preview_window)
    preview_window_label(self.preview_window, text)


def btn_settings(self, location):
    default_btn(location, get_config("txt_settingsheader"), lambda: settings_function(self)).pack(side=TOP, anchor=NW)


def settings_function(self):
    col_bg = get_config("col_bg")
    col_txt = get_config("col_acc_bgcontrast")
    self.window_settings = Toplevel(bg=col_bg, bd=get_config("global_padding"), relief=get_config("relief_frames"))
    self.window_settings.title(get_config("txt_settingsheader"))
    # WindowCleaner(self.window_settings)
    label_settings(self.window_settings, col_bg, col_txt)
    # only works this way, no idea why...
    gui.builder_toolbox.tkinter_objects.frames.frame_stemmer(self, self.window_settings, col_bg, col_txt).pack(fill=X)
    gui.builder_toolbox.tkinter_objects.frames.frame_stopword(self, self.window_settings, col_bg, col_txt).pack(fill=X)
    gui.builder_toolbox.tkinter_objects.frames.frame_embedding(self, self.window_settings, col_bg, col_txt).pack(fill=X)
    gui.builder_toolbox.tkinter_objects.frames.frame_clustering(self, self.window_settings, col_bg, col_txt).pack(fill=X)
    gui.builder_toolbox.tkinter_objects.frames.frame_menu_lang(self, self.window_settings, col_bg, col_txt).pack(fill=X)
    gui.builder_toolbox.tkinter_objects.frames.frame_menu_colors(self, self.window_settings, col_bg, col_txt).pack(fill=X)
    gui.builder_toolbox.tkinter_objects.frames.frame_menu_fonts(self, self.window_settings, col_bg, col_txt).pack(fill=X)
    gui.builder_toolbox.tkinter_objects.frames.frame_menu_snowballstemmer_language(self, self.window_settings, col_bg,
                                                                                   col_txt).pack(fill=X)
    gui.builder_toolbox.tkinter_objects.frames.frame_menu_stopword_language(self, self.window_settings, col_bg,
                                                                                   col_txt).pack(fill=X)
