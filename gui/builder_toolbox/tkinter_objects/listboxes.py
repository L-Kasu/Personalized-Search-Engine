from tkinter import *
from gui.builder_toolbox.settings_util import get_config


def result_text(self, location):
    self.result_text = Listbox(location)
    self.result_text.config(bg=get_config("col_bg_lgt"),
                            fg=get_config("col_acc_minor"),
                            font=get_config("font_returntext"),
                            bd=get_config("global_padding"),
                            borderwidth=0,
                            highlightthickness=0,
                            exportselection=0,
                            activestyle=NONE,
                            selectbackground=get_config("col_bg"),
                            selectforeground=get_config("col_acc_bgcontrast")
                            )
    self.result_text.insert(0, "")
    self.result_text.pack(side=BOTTOM, fill=BOTH, expand=True)
    size = self.result_text.size()
    self.result_text.yview_scroll(size, 'units')


def ui_console(self, location):
    self.ui_console = Listbox(location)
    self.ui_console.config(bg=get_config("col_bg"),
                           fg=get_config("col_acc_bgcontrast"),
                           font=get_config("font_returntext"),
                           bd=get_config("global_padding"),
                           height=6,
                           borderwidth=0,
                           highlightthickness=0,
                           exportselection=0,
                           activestyle=NONE,
                           selectbackground=get_config("col_bg"),
                           selectforeground=get_config("col_acc_bgcontrast")
                           )
    self.ui_console.insert(0, "")
    self.ui_console.pack(side=TOP, fill=X)
    size = self.ui_console.size()
    self.ui_console.yview_scroll(size, 'units')


def print_to_ui_console(self, string):
    self.ui_console.insert(0, string)
