from tkinter import Tk

from gui.builder_toolbox.settings_init import init_config
init_config()
from gui.ui_builder import Application


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
