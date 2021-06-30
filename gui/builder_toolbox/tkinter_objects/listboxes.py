from tkinter import *
from gui.builder_toolbox.tkinter_objects.buttons import btn_preview
from gui.colortemplates.wip import *


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

    self.btn_preview = None
    btn_preview(self, self.result_text)
