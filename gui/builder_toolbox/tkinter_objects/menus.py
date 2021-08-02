from tkinter import *
from nltk.corpus import stopwords
from gui.builder_toolbox.settings_defaultpaths import *
from gui.builder_toolbox.settings_util import get_config, get_configdict, edit_config
from gui.builder_toolbox.settings_util import set_language
from gui.builder_toolbox.settings_util import set_colors
from gui.builder_toolbox.settings_util import set_font


def default_optionmenu(location,
                       function,
                       options=None,
                       defaultclicked=None,
                       id_key=None,
                       file=masterconfigfile,
                       path=default_path,
                       state=ACTIVE
                       ):
    clicked = StringVar()
    if options is None and defaultclicked is None:
        options = list()
        for key in get_configdict(path, file):
            options.append(key)
        clicked.set(get_config(id_key))
    else:
        options = options
        clicked.set(defaultclicked)
    optionsmenu = OptionMenu(location,
                             clicked,
                             *options,
                             command=function
                             )
    optionsmenu.config(relief=get_config("relief_btn"),
                       font=get_config("font_header_2"),
                       bg=get_config("col_btn_idle"),
                       fg=get_config("col_acc_btncontrast"),
                       activebackground=get_config("col_btn_idle"),
                       activeforeground=get_config("col_acc_btncontrast"),
                       highlightthickness=0,
                       borderwidth=[0 if get_config("relief_btn") == "flat" else 2],
                       indicatoron=0,
                       state=state
                       )
    optionsmenu.bind("<Enter>", lambda e: optionsmenu.config(activebackground=get_config("col_btn_active")))
    optionsmenu.bind("<Leave>", lambda e: optionsmenu.config(activebackground=get_config("col_btn_idle")))
    return optionsmenu


def menu_languages(self,
                   location,
                   path=default_path,
                   file=languageconfigfile):
    self.menu_languages = default_optionmenu(location,
                                             lambda x: set_language(self, x),
                                             id_key="ID_lang",
                                             file=file,
                                             path=path
                                             ).pack(side=RIGHT)


def menu_styles(self,
                location,
                path=default_path,
                file=colorsconfigfile):
    self.menu_styles = default_optionmenu(location,
                                          lambda x: set_colors(self, x),
                                          id_key="ID_colors",
                                          file=file,
                                          path=path
                                          ).pack(side=RIGHT)


def menu_fonts(self,
               location,
               path=default_path,
               file=fontconfigfile):
    self.menu_fonts = default_optionmenu(location,
                                         lambda x: set_font(self, x),
                                         id_key="ID_font",
                                         file=file,
                                         path=path
                                         ).pack(side=RIGHT)


def menu_snowballstemmer_language(self, location):
    self.menu_snowballstemmer_language = \
        default_optionmenu(location,
                           lambda x: edit_config({"snowballstemmer_language": x}),
                           options=["arabic", "danish", "dutch", "english", "finnish",
                                    "french", "german", "hungarian", "italian", "norwegian",
                                    "portuguese", "romanian", "russian", "spanish", "swedish"],
                           defaultclicked=get_config("snowballstemmer_language"),
                           state=self.snowballstate
                           )
    self.menu_snowballstemmer_language.pack(side=RIGHT)


def menu_stopword_language(self, location):
    self.menu_stopword_language = \
        default_optionmenu(location,
                           lambda x: edit_config({"stopword_language": x}),
                           options=stopwords.fileids(),
                           defaultclicked=get_config("stopword_language"),
                           state=self.stopwordstate
                           )
    self.menu_stopword_language.pack(side=RIGHT)
