# version: alpha0.63


from gui.builder_toolbox.tkinter_objects.frames import *
from gui.builder_toolbox.tkinter_objects.buttons import *
from gui.builder_toolbox.tkinter_objects.radiobuttons import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master_height = get_config("master_height")
        self.dir_selected = ""
        self.result = list()
        self.tf_object = clustering.Clustering(["dummyDoc"], ["dummyTitle"])
        self.master.geometry(get_config("master_width") + "x" + self.master_height)
        self.master.title(get_config("txt_mastertitle"))
        self.master.config(relief=get_config("relief_frames"), bd=7, bg=get_config("col_bg"))

        self.lower_frame = Frame()
        lower_frame(self, self.master)
        self.upper_frame = Frame()
        upper_frame(self, self.master)
        self.lo_upper_frame = Frame()
        lo_upper_frame(self, self.upper_frame)
        self.up_upper_frame = Frame()
        up_upper_frame(self, self.upper_frame)
        self.right_up_upper_frame = Frame()
        right_up_upper_frame(self, self.up_upper_frame)
        self.left_up_upper_frame = Frame()
        left_up_upper_frame(self, self.up_upper_frame)

        self.btn_select_directory = Button()
        # self.switch = None

        self.dir_label = Label()
        btn_select_directory(self, self.left_up_upper_frame)
        btn_settings(self, self.left_up_upper_frame)
        self.master_entry_frame = Frame()
        self.entry_frame = Frame()
        self.search_entry = Entry()
        self.buttons_frame = Frame()
        self.btn_entry_search = Button()
        self.btn_entry_delete = Button()
        master_entry_frame(self, self.upper_frame)
        self.result_frame = Frame()
        self.result_label = Label()
        self.result_text = Listbox()
        self.btn_preview = Button()
        self.preview_window = None # needs to be none to prevent empty popup window at startup
        self.preview_window_label = Label()
        result_frame(self, self.lower_frame)

        # self.menu_languages = None
        # menu_languages(self, self.right_up_upper_frame)

        self.pack()
