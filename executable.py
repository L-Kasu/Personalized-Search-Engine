from tkinter import *
from gui.builder_toolbox.settings_util import *
from gui.ui_builder import Application

if __name__ == "__main__":
    init_config()
    root = Tk()
    app = Application(master=root)
    app.mainloop()

