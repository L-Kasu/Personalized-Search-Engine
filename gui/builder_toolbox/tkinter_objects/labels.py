import textwrap
from tkinter import *
from tkinter import Label, TOP, X
from gui.builder_toolbox.settings_util import get_config


def default_label(location,
                  text,
                  font=get_config("font_header_1"),
                  bg=get_config("col_bg_lgt"),
                  fg=get_config("col_acc_major"),
                  bd=get_config("global_padding"),
                  side=LEFT,
                  fill=X,
                  expand=True):
    Label(location,
          text=text,
          font=font,
          bg=bg,
          fg=fg,
          bd=bd,
          borderwidth=0,
          highlightthickness=0
          ).pack(side=side,
                 fill=fill,
                 expand=expand)


def result_label(location):
    default_label(location,
                  get_config("txt_resultitems"),
                  side=TOP,
                  expand=False)


def dir_label(location, text):
    default_label(location,
                  text,
                  font=get_config("font_header_2"),
                  fg=get_config("col_acc_minor"),
                  expand=False)


def language_label(location, col_bg, col_txt):
    default_label(location,
                  get_config("txt_language"),
                  font=get_config("font_header_2"),
                  bg=col_bg,
                  fg=col_txt,
                  fill=None,
                  expand=False)


def color_label(location, col_bg, col_txt):
    default_label(location,
                  get_config("txt_colortheme"),
                  font=get_config("font_header_2"),
                  bg=col_bg,
                  fg=col_txt,
                  fill=None,
                  expand=False)


def preview_window_label(location, text):
    text = textwrap.fill(text, width=get_config("prev_window_size"))
    default_label(location,
                  text,
                  font=get_config("font_returntext"),
                  fg=get_config("col_acc_minor"),
                  fill=None,
                  expand=False)


def label_stemmer(location, col_bg, col_txt):
    default_label(location,
                  get_config("txt_selectStemmer"),
                  font=get_config("font_header_2"),
                  bg=col_bg,
                  fg=col_txt,
                  side=TOP)


def label_stopword(location, col_bg, col_txt):
    default_label(location,
                  get_config("txt_toggleStopword"),
                  font=get_config("font_header_2"),
                  bg=col_bg,
                  fg=col_txt,
                  side=TOP)


def label_settings(location, col_bg, col_txt):
    default_label(location,
                  get_config("txt_settingsheader"),
                  bg=col_bg,
                  fg=col_txt,
                  side=TOP)
