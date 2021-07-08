from tkinter import *


def popup_window(self):
    self.win = Toplevel()
    self.win.wm_title("Preview")

    self.prev_label = Label(self.win, text="Here will the preview appear")
    self.prev_label.grid(row=0, column=0)

    self.exit_btn = Button(self.win, text="Okay", command=self.win.destroy)
    self.exit_btn.grid(row=1, column=0)
