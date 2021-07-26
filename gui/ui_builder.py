from gui.builder_toolbox.tkinter_objects.frames import *
from gui.builder_toolbox.tkinter_objects.buttons import *
from gui.builder_toolbox.tkinter_objects.menus import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # WindowCleaner(self.master)
        self.dir_selected = ""
        self.dir_label = Label()
        self.result = list()
        self.remove_stopwords = BooleanVar()
        self.remove_stopwords.set(get_config("stop_word"))
        self.toggle_clustering = BooleanVar()
        self.toggle_clustering.set(get_config("clustering"))
        self.selected_stemmer = StringVar()
        self.selected_stemmer.set(get_config("stemmer"))
        self.search_mode = StringVar()
        self.search_mode.set(get_config("search_mode"))
        self.snowballstate = [ACTIVE if get_config("issnowball") else DISABLED]
        self.stopwordstate = [ACTIVE if get_config("stop_word") else DISABLED]
        self.master.geometry(str(get_config("master_width")) + "x" + str(get_config("master_height")))
        self.master.title(get_config("txt_mastertitle"))
        self.master.config(relief=get_config("relief_frames"),
                           bd=get_config("global_padding")+2,
                           bg=get_config("col_bg"))

        btn_settings(self, self.master)

        self.entry_frame = Frame()
        self.search_entry = Entry()
        self.buttons_frame = Frame()
        entry_frame(self, self.master)

        self.result_frame = Frame()
        self.result_text = Listbox()
        self.preview_window = None  # needs to be none to prevent empty popup window at startup
        result_frame(self, self.master)

        self.pack()
