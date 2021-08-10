from tkinter import Tk
from gui.builder_toolbox.settings_util import get_config
from gui.builder_toolbox.tkinter_objects.labels import label_splash

splash_root = Tk()
splash_root.geometry(str(get_config("master_width")) + "x" + str(get_config("master_height")))


def splash_function():
    label_splash(splash_root)