from tkinter import Tk
from gui.builder_toolbox.settings_init import init_config
from gui.ui_builder import Application


if __name__ == "__main__":
    init_config()
    root = Tk()
    app = Application(master=root)
    app.mainloop()
