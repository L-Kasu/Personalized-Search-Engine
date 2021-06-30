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
