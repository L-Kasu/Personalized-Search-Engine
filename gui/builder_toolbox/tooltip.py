import textwrap
from tkinter import *
from gui.builder_toolbox.settings_util import get_config


class AddTooltip(object):
    def __init__(self, widget, text='default widget info'):
        self.widget = widget
        self.text = textwrap.fill(text, width=get_config("tooltip_window_size"))
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)
        self.tooltipwindow = None

    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tooltipwindow = Toplevel(self.widget)
        self.tooltipwindow.wm_overrideredirect(True)
        self.tooltipwindow.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tooltipwindow,
                      text=self.text,
                      bg=get_config("col_bg_lgt"),
                      fg=get_config("col_acc_minor"),
                      bd=get_config("global_padding"),
                      relief=get_config("relief_frames"),
                      borderwidth=0,
                      font=get_config("font_returntext")
                      )
        label.pack(ipadx=1)

    def close(self, event=None):
        if self.tooltipwindow:
            self.tooltipwindow.destroy()
