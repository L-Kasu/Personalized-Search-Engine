from tkinter import *

from nltk.corpus import stopwords

from gui.builder_toolbox.settings_defaultpaths import *
from gui.builder_toolbox.settings_util import get_config, get_configdict, edit_config
from gui.builder_toolbox.settings_util import set_language
from gui.builder_toolbox.settings_util import set_colors
from gui.builder_toolbox.settings_util import set_font


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
                                             ).pack(side=RIGHT)


def menu_styles(self,
                location,
                path=default_path,
                file=colorsconfigfile):
    self.menu_styles = default_optionmenu(location,
                                          "ID_colors",
                                          lambda x: set_colors(self, x),
                                          file,
                                          path
                                          ).pack(side=RIGHT)


def menu_fonts(self,
               location,
               path=default_path,
               file=fontconfigfile):
    self.menu_fonts = default_optionmenu(location,
                                         "ID_font",
                                         lambda x: set_font(self, x),
                                         file,
                                         path
                                         ).pack(side=RIGHT)


def menu_snowballstemmer_language(self, location):
    clicked = StringVar()
    options = ["arabic", "danish", "dutch", "english", "finnish", "french", "german", "hungarian", "italian", "norwegian", "portuguese", "romanian", "russian", "spanish", "swedish"]
    clicked.set(get_config("snowballstemmer_language"))
    self.menu_snowballstemmer_language = OptionMenu(location,
                                                    clicked,
                                                    *options,
                                                    command=lambda x: edit_config({"snowballstemmer_language": x})
                                                    )
    self.menu_snowballstemmer_language.config(relief=get_config("relief_btn"),
                                              font=get_config("font_header_2"),
                                              bg=get_config("col_btn_idle"),
                                              fg=get_config("col_acc_btncontrast"),
                                              activebackground=get_config("col_btn_active"),
                                              activeforeground=get_config("col_acc_btncontrast"),
                                              highlightthickness=0,
                                              borderwidth=[0 if get_config("relief_btn") == "flat" else 2],
                                              indicatoron=0,
                                              state=self.snowballstate
                                              )
    self.menu_snowballstemmer_language.pack(side=RIGHT)


def menu_stopword_language(self, location):
    clicked = StringVar()
    options = stopwords.fileids()
    clicked.set(get_config("stopword_language"))
    self.menu_stopword_language = OptionMenu(location,
                                             clicked,
                                             *options,
                                             command=lambda x: edit_config({"stopword_language": x})
                                             )
    self.menu_stopword_language.config(relief=get_config("relief_btn"),
                                       font=get_config("font_header_2"),
                                       bg=get_config("col_btn_idle"),
                                       fg=get_config("col_acc_btncontrast"),
                                       activebackground=get_config("col_btn_active"),
                                       activeforeground=get_config("col_acc_btncontrast"),
                                       highlightthickness=0,
                                       borderwidth=[0 if get_config("relief_btn") == "flat" else 2],
                                       indicatoron=0,
                                       state=self.stopwordstate
                                       )
    self.menu_stopword_language.pack(side=RIGHT)
