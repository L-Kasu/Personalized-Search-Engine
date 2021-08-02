from tkinter import *
from gui.builder_toolbox.settings_util import get_config


def result_text(self, location):
    self.result_text = Listbox(location)
    self.result_text.config(bg=get_config("col_bg_lgt"),
                            fg=get_config("col_acc_minor"),
                            font=get_config("font_returntext"),
                            borderwidth=0,
                            highlightthickness=0
                            )
    self.result_text.insert(0, "")
    self.result_text.pack(side=BOTTOM, fill=BOTH, expand=True)
    size = self.result_text.size()
    self.result_text.yview_scroll(size, 'units')
