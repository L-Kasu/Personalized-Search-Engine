from tkinter import *
from gui.builder_toolbox.settings_util import get_config


class WindowCleaner(object):
    def __init__(self, widget):
        self.widget = widget
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.widget.wm_overrideredirect(True)
        self.widget.wm_geometry("+%d+%d" % (x, y))
        default_btn(self.widget,
                    "X",  # TODO proper exit img
                    lambda: self.widget.destroy()
                    ).pack(side=RIGHT, anchor=N)


def default_btn(location, text, function):
    return Button(location,
                  text=text,
                  command=function,
                  font=get_config("font_header_2"),
                  bg=get_config("col_btn_idle"),
                  fg=get_config("col_acc_btncontrast"),
                  activebackground=get_config("col_btn_active"),
                  activeforeground=get_config("col_acc_btncontrast"),
                  relief=get_config("relief_btn"),
                  borderwidth=[0 if get_config("relief_btn") == "flat" else 2]
                  )
