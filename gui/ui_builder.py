# version: alpha0.52


from gui.builder_toolbox.tkinter_objects.frames import *
from gui.builder_toolbox.tkinter_objects.buttons import *
from gui.languagepacks.english import *
from gui.colortemplates.wip import *

master_height = 500
master_width = 800
filesearchspan_min = 0
filesearchspan_max = 2000

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.dir_selected = ""
        self.result_text = ""
        self.tf_object = None
        self.create_window()
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
        # self.menu_languages()
        # self.change_language()
        self.master_entry_frame = None
        master_entry_frame(self, self.upper_frame)
        self.result_frame = None
        result_frame(self, self.lower_frame)
        self.pack()

    def create_window(self):
        self.master.geometry(str(master_width) + "x" + str(master_height))
        self.master.title(txt_mastertitle)
        self.master.config(relief=relief_frames, bd=7, bg=col_bg)

    def menu_languages(self):
        clicked = StringVar()
        options = [
            "English",
            "Deutsch",
            "Español"
        ]
        clicked.set(options[0])
        self.lst_languages = OptionMenu(self.right_up_upper_frame, clicked, *options)
        self.lst_languages.config(relief=relief_btn,
                                  font=font_header_2,
                                  bg=col_btn_idle,
                                  fg=col_acc_minor,
                                  activebackground=col_btn_active,
                                  activeforeground=col_acc_minor,
                                  highlightthickness=0)
        self.lst_languages.pack(side=LEFT, anchor=NE)

    # def change_language(self, *args):
    #     if self.lst_languages.getvar() == "English":
    #         pass
    #     elif self.lst_languages.getvar() == "Deutsch":
    #         pass
    #     elif self.lst_languages.getvar == "Español":
    #         pass
