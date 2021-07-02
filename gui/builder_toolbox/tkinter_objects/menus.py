import os
from tkinter import *
from gui.globalimports import *


dir_languages = "./gui/languagepacks"


def menu_languages(self, location):
    clicked = StringVar()
    options = get_options()
    clicked.set(options[0])
    self.menu_languages = OptionMenu(location,
                                     clicked,
                                     *options)
    self.menu_languages.config(relief=relief_btn,
                               font=font_header_2,
                               bg=col_btn_idle,
                               fg=col_acc_minor,
                               activebackground=col_btn_active,
                               activeforeground=col_acc_minor,
                               highlightthickness=0
                               )
    if relief_btn == "flat":
        self.menu_languages.config(borderwidth=0)
    self.menu_languages.pack(side=LEFT, anchor=NE)


def get_options():
    options = []
    for dirname, _, filenames in os.walk(dir_languages):
        filenames_split_by_point = list(filter(
            lambda x:
            len(x) >= 2,
            [filename.split(".") for filename in filenames]))
        filenames_without_ending = list([split[0] for split in filenames_split_by_point])
        endings = list([split[1] for split in filenames_split_by_point])
        for i in range(0, len(filenames_without_ending)-1):
            if endings[i] == "py":
                options.append(filenames_without_ending[i])
    return options


# def change_language(self):
#     selected_language = self.menu_languages.getvar()
#     print(selected_language)
#
#     if selected_language == "English":
#         pass
#     elif selected_language == "Deutsch":
#         pass
#     elif selected_language == "Español":
#         pass
