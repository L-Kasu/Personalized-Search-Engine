from tkinter import *
from gui.builder_toolbox.settings_util import get_config
from gui.builder_toolbox.settings_util import set_language
from gui.builder_toolbox.settings_util import set_colors


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
    self.menu_styles = OptionMenu(location,
                                  clicked,
                                  *options,
                                  command=set_colors)
    self.menu_styles.config(relief=get_config("relief_btn"),
                            font=get_config("font_header_2"),
                            bg=get_config("col_btn_idle"),
                            fg=get_config("col_acc_minor"),
                            activebackground=get_config("col_btn_active"),
                            activeforeground=get_config("col_acc_minor"),
                            highlightthickness=0
                            )
    if get_config("relief_btn") == "flat":
        self.menu_styles.config(borderwidth=0)
    self.menu_styles.pack(side=LEFT, anchor=NE)

