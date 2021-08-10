from tkinter import *
from gui.builder_toolbox.settings_init import init_config
from gui.ui_builder import Application
from gui.builder_toolbox.tkinter_objects.splash import *

splash_function()


def main():
    if __name__ == "__main__":
        splash_root.destroy()
        root = Tk()
        Application(master=root)


splash_root.after(1000, main)
mainloop()
