import os
from tkinter import *
from gui.builder_toolbox.settings_util import get_config
from gui.builder_toolbox.settings_util import set_language
from gui.builder_toolbox.settings_util import set_colors

dir_languages = "./gui/languagepacks"


def menu_languages(self, location):
    clicked = StringVar()
    options = ("English", "German", "Spanish", "Arabic")
    clicked.set(options[0])
    self.menu_languages = OptionMenu(location,
                                     clicked,
                                     *options,
                                     command=set_language)
    self.menu_languages.config(relief=get_config("relief_btn"),
                               font=get_config("font_header_2"),
                               bg=get_config("col_btn_idle"),
                               fg=get_config("col_acc_minor"),
                               activebackground=get_config("col_btn_active"),
                               activeforeground=get_config("col_acc_minor"),
                               highlightthickness=0
                               )
    if get_config("relief_btn") == "flat":
        self.menu_languages.config(borderwidth=0)
    self.menu_languages.pack(side=LEFT, anchor=NE)


def menu_styles(self, location):
    clicked = StringVar()
    options = ("wip", "teatime", "sharky", "redengine", "cb_friendly", "monochrome", "cyberpunk", "dokidokiwip")
    clicked.set(options[0])
    self.menu_languages = OptionMenu(location,
                                     clicked,
                                     *options,
                                     command=set_colors)
    self.menu_languages.config(relief=get_config("relief_btn"),
                               font=get_config("font_header_2"),
                               bg=get_config("col_btn_idle"),
                               fg=get_config("col_acc_minor"),
                               activebackground=get_config("col_btn_active"),
                               activeforeground=get_config("col_acc_minor"),
                               highlightthickness=0
                               )
    if get_config("relief_btn") == "flat":
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

