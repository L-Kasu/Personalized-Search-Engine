# version: alpha0.63


from gui.builder_toolbox.tkinter_objects.frames import *
from gui.builder_toolbox.tkinter_objects.buttons import *
from gui.builder_toolbox.tkinter_objects.menus import *
from gui.globalimports import *
from gui.ui_sizedefinitions import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.dir_selected = ""
        self.result = list()
        self.tf_object = None
        self.master.geometry(str(master_width) + "x" + str(master_height))
        self.master.title(txt_mastertitle)
        self.master.config(relief=relief_frames, bd=7, bg=col_bg)

        self.lower_frame = None
        lower_frame(self, self.master)
        self.upper_frame = None
        upper_frame(self, self.master)
        self.lo_upper_frame = None
        lo_upper_frame(self, self.upper_frame)
        self.up_upper_frame = None
        up_upper_frame(self, self.upper_frame)
        self.right_up_upper_frame = None
        right_up_upper_frame(self, self.up_upper_frame)
        self.left_up_upper_frame = None
        left_up_upper_frame(self, self.up_upper_frame)

        self.btn_select_directory = None
        self.switch = None

        self.dir_label = None
        btn_select_directory(self, self.left_up_upper_frame)
        btn_settings(self, self.left_up_upper_frame)
        self.master_entry_frame = None
        self.entry_frame = None
        self.search_entry = None
        self.buttons_frame = None
        self.btn_entry_search = None
        self.btn_entry_delete = None
        master_entry_frame(self, self.upper_frame)
        self.result_frame = None
        self.result_label = None
        self.result_text = None
        self.btn_preview = None
        self.preview_window = None
        self.preview_window_label = None
        result_frame(self, self.lower_frame)

        # self.menu_languages = None
        # menu_languages(self, self.right_up_upper_frame)

        self.pack()
