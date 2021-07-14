from tkinter import *

from gui.builder_toolbox.settings_init import init_config
from gui.ui_builder import Application

if __name__ == "__main__":
    init_config()
    # set_language("German")
    # set_colors("redengine")
    root = Tk()
    app = Application(master=root)
    app.mainloop()

