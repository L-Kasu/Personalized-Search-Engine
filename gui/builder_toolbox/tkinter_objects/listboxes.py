from tkinter import *
from gui.colortemplates.wip import *


def listbox_dir(self, location):
    self.select_dir_path_listbox = Listbox(location,
                                           font=font_header_2
                                           )
    self.select_dir_path_listbox.config(bg=col_bg_lgt,
                                        fg=col_acc_minor,
                                        height=1,
                                        borderwidth=0,
                                        highlightthickness=0
                                        )
    self.select_dir_path_listbox.pack(side=TOP, fill=X)


def result_text(self, location):
    self.result_text = Listbox(location)
    self.result_text.config(bg=col_bg_lgt,
                            fg=col_acc_minor,
                            font=font_returntext,
                            height=10,
                            width=0,
                            borderwidth=0,
                            highlightthickness=0
                            )
    self.result_text.pack(side=BOTTOM, fill=BOTH, expand=True)
