from tkinter import *
from gui.languagepacks.english import *
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
