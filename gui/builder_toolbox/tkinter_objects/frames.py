from tkinter import Frame

from gui.builder_toolbox.tkinter_objects.entries import *
from gui.builder_toolbox.tkinter_objects.listboxes import *
from gui.builder_toolbox.tkinter_objects.buttons import *


def lower_frame(self, location):
    self.lower_frame = Frame(location, bg=get_config("col_bg"))
    self.lower_frame.pack(side=BOTTOM, fill=BOTH, expand=True)


def upper_frame(self, location):
    self.upper_frame = Frame(location, bg=get_config("col_bg"))
    self.upper_frame.pack(side=TOP, fill=BOTH, expand=True)


def lo_upper_frame(self, location):
    self.lo_upper_frame = Frame(location, bg=get_config("col_bg"))
    self.lo_upper_frame.pack(side=BOTTOM, fill=BOTH, expand=True)


def up_upper_frame(self, location):
    self.up_upper_frame = Frame(location, bg=get_config("col_bg"))
    self.up_upper_frame.pack(side=TOP, fill=X)


def right_up_upper_frame(self, location):
    self.right_up_upper_frame = Frame(location, bg=get_config("col_bg"))
    self.right_up_upper_frame.pack(side=RIGHT, fill=BOTH)


def left_up_upper_frame(self, location):
    self.left_up_upper_frame = Frame(location, bg=get_config("col_bg"))
    self.left_up_upper_frame.pack(side=LEFT, fill=BOTH)


def master_entry_frame(self, location):
    self.master_entry_frame = Frame(location, bg=get_config("col_bg"))
    self.master_entry_frame.pack(side=BOTTOM, fill=BOTH, expand=True)

    entry_frame(self, self.master_entry_frame)
    search_entry(self, self.entry_frame)
    buttons_frame(self, self.entry_frame)
    btn_entry_search(self,
                     self.buttons_frame,
                     get_config("col_btn_idle"),
                     get_config("col_btn_active"),
                     get_config("col_acc_minor"))
    btn_entry_delete(self,
                     self.buttons_frame,
                     get_config("col_btn_idle"),
                     get_config("col_btn_active"),
                     get_config("col_acc_minor"))


def entry_frame(self, location):
    self.entry_frame = Frame(location, bg=get_config("col_bg_lgt"), relief=get_config("relief_frames"), bd=5)
    self.entry_frame.pack(fill=X, expand=True)


def buttons_frame(self, location):
    self.buttons_frame = Frame(location)
    self.buttons_frame.pack(side=BOTTOM)


def result_frame(self, location):
    self.result_frame = Frame(location, bg=get_config("col_bg_lgt"))
    self.result_frame.pack(side=LEFT, fill=BOTH, expand=True)

    result_label(self, self.result_frame)
    result_text(self, self.result_frame)
    btn_preview(self, self.result_text)


def frame_stemmer(self, location):
    self.frame_stemmer = Frame(location, bg=get_config("col_bg_lgt"))
    self.frame_stemmer.pack()
    label_stemmer(self, self.frame_stemmer)
    radiobtns_stemmer(self, self.frame_stemmer)


def frame_stopword(self, location):
    self.frame_stopword = Frame(location, bg=get_config("col_bg_lgt"))
    self.frame_stopword.pack()
    label_stopword(self, self.frame_stopword)
    radiobtns_stopword(self, self.frame_stopword)
