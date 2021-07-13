from gui.builder_toolbox.tkinter_objects.buttons import *


def search_entry(self, location):
    self.search_entry = Entry(location)
    self.search_entry.config(bg=get_config("col_entryfield_idle"),
                             fg=get_config("col_entryfield_contrast"),
                             font=get_config("font_header_2"))
    self.search_entry.pack(side=TOP, fill=X, expand=True, ipadx=50)
