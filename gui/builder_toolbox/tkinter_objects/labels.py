import textwrap
from tkinter import *
from gui.globalimports import *
from gui.ui_sizedefinitions import *


def result_label(self, location):
    self.result_label = Label(location,
                              text=txt_resultitems,
                              font=font_header_1
                              )
    self.result_label.config(bg=col_bg_lgt,
                             fg=col_acc_major
                             )
    self.result_label.pack(side=TOP, fill=X)


def dir_label(self, location, text):
    self.dir_label = Label(location,
                           font=font_header_2,
                           text=text
                           )
    self.dir_label.config(bg=col_bg_lgt,
                          fg=col_acc_minor,
                          height=1,
                          borderwidth=0,
                          highlightthickness=0
                          )
    self.dir_label.pack(side=LEFT, fill=X)


def preview_window_label(self, location, text):
    text = textwrap.fill(text, width=prev_window_size)
    self.preview_window_label = Label(location,
                                      bg=col_bg_lgt,
                                      font=font_returntext,
                                      fg=col_acc_minor,
                                      borderwidth=0,
                                      text=text
                                      )
    self.preview_window_label.pack(padx=10, pady=5)
