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
                  justify=None,
                  ):
    return Label(location,
                 text=text,
                 font=font,
                 bg=bg,
                 fg=fg,
                 bd=bd,
                 borderwidth=0,
                 highlightthickness=0,
                 justify=justify
                 )


def result_label(location):
    default_label(location,
                  get_config("txt_resultitems"),
                  ).pack(side=TOP,
                         fill=X,
                         expand=False)


def dir_label(self, location):
    text = "no directory selected!" \
            if self.dir_selected == "" \
            else self.dir_selected
    self.dir_label = default_label(location,
                                   text,
                                   font=get_config("font_header_2"),
                                   fg=get_config("col_acc_minor"),
                                   )
    self.dir_label.pack(side=LEFT,
                        fill=X,
                        expand=False)


def preview_window_label(location, text):
    text = textwrap.fill(text, width=get_config("prev_window_size"))
    default_label(location,
                  text,
                  font=get_config("font_returntext"),
                  bg=get_config("col_bg"),
                  fg=get_config("col_acc_bgcontrast"),
                  justify=LEFT,
                  ).pack(side=LEFT,
                         fill=None,
                         expand=False)


def label_settings(location, col_bg, col_txt):
    default_label(location,
                  get_config("txt_settingsheader"),
                  bg=col_bg,
                  fg=col_txt,
                  ).pack(side=TOP,
                         fill=X,
                         expand=True)


def label_splash(location):
    splash_label = default_label(location, "Splash Screen!")
    splash_label.pack(expand=True, fill=BOTH)
