from tkinter import *
from gui.builder_toolbox.settings_util import *
from gui.ui_builder import Application

if __name__ == "__main__":
    config = {"master_height": "500",
              "master_width": "800",
              "prev_window_size": 100,
              "preview_size": 500,
              "txt_mastertitle": "Search Engine",
              "txt_selectdir": "Select Directory",
              "txt_settingsheader": "Settings",
              "txt_entrysearch": "Search",
              "txt_entryclear": "Clear",
              "txt_resultitems": "Search result",
              "txt_preview": "Preview",
              "txt_page": "Page",
              "ERR_noDirectorySelected": "ERROR: No directory selected",
              "ERR_resultListEmpty": "ERROR: There are no search results",
              "col_bg": "#3b3b3b",
              "col_bg_lgt": "#5f5f5f",
              "col_btn_idle": "#940000",
              "col_btn_active": "#d50000",
              "col_entryfield_idle": "#bbbbbb",
              "col_entryfield_contrast": "#3b3b3b",
              "col_acc_major": "#b3b3b3",
              "col_acc_minor": "#b3b3b3",
              "font_header_1": ("Arial", 15, "bold"),
              "font_header_2": ("Arial", 10, "bold"),
              "font_returntext": ("Arial", 10),
              "relief_frames": "flat",
              "relief_btn": "flat"}
    write_config(config)
    root = Tk()
    app = Application(master=root)
    app.mainloop()

