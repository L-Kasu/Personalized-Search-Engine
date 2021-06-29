from tkinter import *


def popup_window(self):
    self.win = Toplevel(self)
    self.win.wm_title("Preview")

    self.label_prev = Label(self.win, text="here will the preview appear")
    self.label_prev.pack(TOP)

    self.exit_btn = Button(self.win, text="Okay", command=self.win.destroy())
    self.exit_btn.pack(BOTTOM)
