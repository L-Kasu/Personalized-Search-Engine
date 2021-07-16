import textwrap
from tkinter import *
from tkinter import Label, TOP, X

from gui.builder_toolbox.settings_util import get_config


def result_label(self, location):
    self.result_label = Label(location,
                              text=get_config("txt_resultitems"),
                              font=get_config("font_header_1")
                              )
    self.result_label.config(bg=get_config("col_bg_lgt"),
                             fg=get_config("col_acc_major")
                             )
    self.result_label.pack(side=TOP, fill=X)


def dir_label(self, location, text):
    self.dir_label = Label(location,
                           font=get_config("font_header_2"),
                           text=text
                           )
    self.dir_label.config(bg=get_config("col_bg_lgt"),
                          fg=get_config("col_acc_minor"),
                          height=1,
                          borderwidth=0,
                          highlightthickness=0
                          )
    self.dir_label.pack(side=LEFT, fill=X)


def language_label(self, location, col_bg, col_txt):
    self.language_label = Label(location,
                                font=get_config("font_header_2"),
                                text=get_config("txt_language")
                                )
    self.language_label.config(bg=col_bg,
                               fg=col_txt,
                               height=1,
                               borderwidth=0,
                               highlightthickness=0
                               )
    self.language_label.pack(side=LEFT)


def color_label(self, location, col_bg, col_txt):
    self.language_label = Label(location,
                                font=get_config("font_header_2"),
                                text=get_config("txt_colortheme")
                                )
    self.language_label.config(bg=col_bg,
                               fg=col_txt,
                               height=1,
                               borderwidth=0,
                               highlightthickness=0
                               )
    self.language_label.pack(side=LEFT)


def preview_window_label(self, location, text):
    text = textwrap.fill(text, width=get_config("prev_window_size"))
    self.preview_window_label = Label(location,
                                      bg=get_config("col_bg_lgt"),
                                      font=get_config("font_returntext"),
                                      fg=get_config("col_acc_minor"),
                                      borderwidth=0,
                                      text=text
                                      )
    self.preview_window_label.pack(padx=10, pady=5)


def label_stemmer(self, location, col_bg, col_txt):
    self.label_stemmer = Label(location,
                               text=get_config("txt_selectStemmer"),
                               font=get_config("font_header_2"),
                               bd=get_config("global_padding"))
    self.label_stemmer.config(bg=col_bg,
                              fg=col_txt,
                              borderwidth=0,
                              highlightthickness=0
                              )
    self.label_stemmer.pack(side=TOP, fill=X, expand=True)


def label_stopword(self, location, col_bg, col_txt):
    self.label_stopword = Label(location,
                                text=get_config("txt_toggleStopword"),
                                font=get_config("font_header_2"),
                                bd=get_config("global_padding"))
    self.label_stopword.config(bg=col_bg,
                               fg=col_txt,
                               borderwidth=0,
                               highlightthickness=0
                               )
    self.label_stopword.pack(side=TOP, fill=X, expand=True)


def label_settings(self, location, col_bg, col_txt):
    self.label_settings = Label(location,
                                text=get_config("txt_settingsheader"),
                                font=get_config("font_header_1"),
                                bd=get_config("global_padding")
                                )
    self.label_settings.config(bg=col_bg,
                               fg=col_txt
                               )
    self.label_settings.pack(side=TOP, fill=X)
