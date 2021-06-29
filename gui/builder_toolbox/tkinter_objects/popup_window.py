from tkinter import *


def popup_window(self):
    self.win = Toplevel()
    self.win.wm_title("Preview")

    self.prev_label = Label(self.win, text="here will the preview appear")
    self.prev_label.pack(TOP)

    self.exit_btn = Button(self.win, text="Okay", command=self.win.destroy())
    self.exit_btn.pack(BOTTOM)
