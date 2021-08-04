from tkinter import Tk
from gui.builder_toolbox.settings_init import init_config
from gui.ui_builder import Application
import pyi_splash


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    pyi_splash.close()
    app.mainloop()
