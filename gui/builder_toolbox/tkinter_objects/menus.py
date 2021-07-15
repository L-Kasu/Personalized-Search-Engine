from tkinter import *
from gui.builder_toolbox.settings_defaultpaths import *
from gui.builder_toolbox.settings_util import get_config, get_configdict
from gui.builder_toolbox.settings_util import set_language
from gui.builder_toolbox.settings_util import set_colors


def menu_languages(self,
                   location,
                   path=default_path,
                   file=languageconfigfile):
    clicked = StringVar()
    options = list()
    for key in get_configdict(path, file):
        options.append(key)
    clicked.set(get_config("ID_lang"))
    self.menu_languages = OptionMenu(location,
                                     clicked,
                                     *options,
                                     command=lambda x: set_language(self, x))
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


def menu_styles(self,
                location,
                path=default_path,
                file=colorsconfigfile):
    clicked = StringVar()
    options = list()
    for key in get_configdict(path, file):
        options.append(key)
    clicked.set(get_config("ID_colors"))
    self.menu_styles = OptionMenu(location,
                                  clicked,
                                  *options,
                                  command=lambda x: set_colors(self, x))
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

