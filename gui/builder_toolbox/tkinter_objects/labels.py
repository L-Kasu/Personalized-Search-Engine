import textwrap
from tkinter import *
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
