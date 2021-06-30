from tkinter import *
from gui.languagepacks.English import *
from gui.colortemplates.wip import *


def result_label(self, location):
    self.result_label = Label(location,
                              text=txt_resultitems,
                              font=font_header_1
                              )
    self.result_label.config(bg=col_bg_lgt,
                             fg=col_acc_major
                             )
    self.result_label.pack(side=TOP, fill=X)


def preview_window_label(self, location, text):
    self.preview_window_label = Label(location,
                                      bg=col_bg_lgt,
                                      text=text,
                                      font=font_returntext,
                                      fg=col_acc_minor
                                      )
    self.preview_window_label.pack(padx=10, pady=5)
