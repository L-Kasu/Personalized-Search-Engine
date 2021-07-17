from tkinter import filedialog
import gui
from gui.builder_toolbox.tkinter_objects.radiobuttons import *
from gui.builder_toolbox.search_util import *


def default_btn(location, text, function, side=LEFT, anchor=CENTER):
    return Button(location,
                  text=text,
                  command=function,
                  font=get_config("font_header_2"),
                  bg=get_config("col_btn_idle"),
                  fg=get_config("col_acc_minor"),
                  activebackground=get_config("col_btn_active"),
                  activeforeground=get_config("col_acc_minor"),
                  relief=get_config("relief_btn"),
                  borderwidth=[0 if get_config("relief_btn") == "flat" else 2]
                  ).pack(side=side, anchor=anchor)


def btn_select_directory(self, location):
    default_btn(location, get_config("txt_selectdir"), lambda: btn_select_directory_function(self))


def btn_select_directory_function(self):
    self.dir_label['text'] = ""
    self.dir_selected = filedialog.askdirectory()
    dir_label(self, self.result_frame, self.dir_selected + "/")
    preprocess(self)


def btn_entry_search(self, location):
    default_btn(location, get_config("txt_entrysearch"), lambda: search(self, self.search_entry.get()))


def btn_entry_delete(self, location):
    default_btn(location, get_config("txt_entryclear"), lambda: btn_entry_delete_function(self))


def btn_entry_delete_function(self):
    self.search_entry.delete(0, END)
    self.result_text.delete(0, END)


def btn_preview(self, location):
    default_btn(location, get_config("txt_preview"), lambda: preview_function(self), BOTTOM)


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
    preview_window_label(self, self.preview_window, text)
    btn_preview_exit(self, self.preview_window)


def btn_preview_exit(self, location):
    default_btn(location, get_config("txt_exitpreview"), self.preview_window.destroy, BOTTOM)


def btn_settings(self, location):
    default_btn(location, get_config("txt_settingsheader"), lambda: settings_function(self))


def settings_function(self):
    col_bg = get_config("col_bg")
    col_txt = get_config("col_acc_bgcontrast")
    self.window_settings = Toplevel(bg=col_bg, bd=get_config("global_padding"))
    self.window_settings.title(get_config("txt_settingsheader"))
    label_settings(self, self.window_settings, col_bg, col_txt)
    # only works this way, no idea why...
    gui.builder_toolbox.tkinter_objects.frames.frame_stemmer(self, self.window_settings, col_bg, col_txt)
    gui.builder_toolbox.tkinter_objects.frames.frame_stopword(self, self.window_settings, col_bg, col_txt)
    gui.builder_toolbox.tkinter_objects.frames.frame_menu_lang(self, self.window_settings, col_bg, col_txt)
    gui.builder_toolbox.tkinter_objects.frames.frame_menu_colors(self, self.window_settings, col_bg, col_txt)
#     btn_exitsettings(self, self.window_settings)
#
#
# def btn_exitsettings(self, location):
#     default_btn(location, get_config("txt_okay"), lambda: btn_exitsettings_function(self), BOTTOM, S)
#
#
# def btn_exitsettings_function(self):
#     self.window_settings.destroy()
