from gui.builder_toolbox.tkinter_objects.entries import *
from gui.builder_toolbox.tkinter_objects.labels import *
from gui.builder_toolbox.tkinter_objects.listboxes import *
from gui.builder_toolbox.tkinter_objects.buttons import *


def lower_frame(self, location):
    self.lower_frame = Frame(location, bg=col_bg)
    self.lower_frame.pack(side=BOTTOM, fill=BOTH, expand=True)


def upper_frame(self, location):
    self.upper_frame = Frame(location, bg=col_bg)
    self.upper_frame.pack(side=TOP, fill=BOTH, expand=True)


def lo_upper_frame(self, location):
    self.lo_upper_frame = Frame(location, bg=col_bg)
    self.lo_upper_frame.pack(side=BOTTOM, fill=BOTH, expand=True)


def up_upper_frame(self, location):
    self.up_upper_frame = Frame(location, bg=col_bg)
    self.up_upper_frame.pack(side=TOP, fill=X)


def right_up_upper_frame(self, location):
    self.right_up_upper_frame = Frame(location, bg=col_bg)
    self.right_up_upper_frame.pack(side=RIGHT, fill=BOTH)


def left_up_upper_frame(self, location):
    self.left_up_upper_frame = Frame(location, bg=col_bg)
    self.left_up_upper_frame.pack(side=LEFT, fill=BOTH)


def master_entry_frame(self, location):
    self.master_entry_frame = Frame(location, bg=col_bg)
    self.master_entry_frame.pack(side=BOTTOM, fill=BOTH, expand=True)

    self.entry_frame = None
    entry_frame(self, self.master_entry_frame)

    self.search_entry = None
    search_entry(self, self.entry_frame)

    self.buttons_frame = None
    buttons_frame(self, self.entry_frame)

    self.btn_entry_search = None
    btn_entry_search(self,
                     self.buttons_frame,
                     col_btn_idle,
                     col_btn_active,
                     col_acc_minor)

    self.btn_entry_delete = None
    btn_entry_delete(self,
                     self.buttons_frame,
                     col_btn_idle,
                     col_btn_active,
                     col_acc_minor)


def entry_frame(self, location):
    self.entry_frame = Frame(location, bg=col_bg_lgt, relief=relief_frames, bd=5)
    self.entry_frame.pack(fill=X, expand=True)


def buttons_frame(self, location):
    self.buttons_frame = Frame(location)
    self.buttons_frame.pack(side=BOTTOM)


def result_frame(self, location):
    self.result_frame = Frame(location, bg=col_bg_lgt)
    self.result_frame.pack(side=LEFT, fill=BOTH, expand=True)

    self.result_label = None
    result_label(self, self.result_frame)
    self.result_text = None
    result_text(self, self.result_frame)
    self.btn_preview = None
    btn_preview(self, self.result_text)
