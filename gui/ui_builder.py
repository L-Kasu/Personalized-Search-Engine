# version: alpha0.62


from gui.builder_toolbox.tkinter_objects.frames import *
from gui.builder_toolbox.tkinter_objects.buttons import *
from gui.builder_toolbox.tkinter_objects.menus import *
from gui.languagepacks.English import *
from gui.colortemplates.wip import *

master_height = 500
master_width = 800


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
        btn_select_directory(self, self.left_up_upper_frame)
        self.master_entry_frame = None
        master_entry_frame(self, self.upper_frame)
        self.result_frame = None
        result_frame(self, self.lower_frame)

        # self.menu_languages = None
        # menu_languages(self, self.right_up_upper_frame)

        self.pack()
