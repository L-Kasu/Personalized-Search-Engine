from gui.builder_toolbox.tkinter_objects.frames import *
from gui.builder_toolbox.tkinter_objects.buttons import *
from gui.builder_toolbox.tkinter_objects.menus import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.dir_selected = ""
        self.result = list()
        self.tf_object = clustering.Clustering(["dummyDoc"], ["dummyTitle"])
        self.remove_stopwords = BooleanVar()
        self.remove_stopwords.set(get_config("stop_word"))
        self.selected_stemmer = StringVar()
        self.selected_stemmer.set(get_config("stemmer"))
        self.master.geometry(get_config("master_width") + "x" + get_config("master_height"))
        self.master.title(get_config("txt_mastertitle"))
        self.master.config(relief=get_config("relief_frames"),
                           bd=get_config("global_padding")+2,
                           bg=get_config("col_bg"))

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

        btn_select_directory(self, self.left_up_upper_frame)

        self.frame_stemmer = Frame()
        self.frame_stopword = Frame()
        self.frame_menu_lang = Frame()
        self.frame_menu_colors = Frame()
        self.menu_languages = None
        self.menu_styles = None
        btn_settings(self, self.left_up_upper_frame)

        self.master_entry_frame = Frame()
        self.entry_frame = Frame()
        self.search_entry = Entry()
        self.buttons_frame = Frame()
        master_entry_frame(self, self.upper_frame)

        self.result_frame = Frame()
        self.result_text = Listbox()
        self.preview_window = None  # needs to be none to prevent empty popup window at startup
        result_frame(self, self.lower_frame)

        self.pack()
