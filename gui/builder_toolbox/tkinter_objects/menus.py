from tkinter import *
from gui.builder_toolbox.settings_defaultpaths import *
from gui.builder_toolbox.settings_util import get_config, get_configdict
from gui.builder_toolbox.settings_util import set_language
from gui.builder_toolbox.settings_util import set_colors


def default_optionmenu(location,
                       id_key,
                       function,
                       file,
                       path=default_path,
                       ):
    clicked = StringVar()
    options = list()
    for key in get_configdict(path, file):
        options.append(key)
    clicked.set(get_config(id_key))
    optionsmenu = OptionMenu(location,
                             clicked,
                             *options,
                             command=function
                             )
    optionsmenu.config(relief=get_config("relief_btn"),
                       font=get_config("font_header_2"),
                       bg=get_config("col_btn_idle"),
                       fg=get_config("col_acc_btncontrast"),
                       activebackground=get_config("col_btn_active"),
                       activeforeground=get_config("col_acc_btncontrast"),
                       highlightthickness=0,
                       borderwidth=[0 if get_config("relief_btn") == "flat" else 2],
                       indicatoron=0
                       )
    return optionsmenu


def menu_languages(self,
                   location,
                   path=default_path,
                   file=languageconfigfile):
    self.menu_languages = default_optionmenu(location,
                                             "ID_lang",
                                             lambda x: set_language(self, x),
                                             file,
                                             path
                                             ).pack(side=LEFT, anchor=NE)


def menu_styles(self,
                location,
                path=default_path,
                file=colorsconfigfile):
    self.menu_styles = default_optionmenu(location,
                                          "ID_colors",
                                          lambda x: set_colors(self, x),
                                          file,
                                          path
                                          ).pack(side=LEFT, anchor=NE)
