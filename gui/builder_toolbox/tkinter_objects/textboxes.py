from tkinter import *
from gui.colortemplates.wip import *


def preview_window_text(self, location, text):
    self.preview_window_text = Text(location,
                                    bg=col_bg_lgt,
                                    font=font_returntext,
                                    fg=col_acc_minor,
                                    borderwidth=0
                                    )
    self.preview_window_text.insert(END, text)
    self.preview_window_text.pack(padx=10, pady=5, fill=BOTH)
