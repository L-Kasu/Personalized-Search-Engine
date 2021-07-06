from tkinter import *

is_off = False


def toggle(self):
    global is_off

    if is_off:
        self.btn_switch.config(image=on)
        is_off = True
    else:
        self.btn_switch.config(image=off)
        is_off = False


on = PhotoImage(file="toggle_on.png")
off = PhotoImage(file="toggle_off.png")


def switch(self, location):
    self.btn_switch = Button(location, image=off, bd=0, command=toggle)