from gui.builder_toolbox.tkinter_objects.frames import *
from gui.builder_toolbox.tkinter_objects.buttons import *
from gui.builder_toolbox.tkinter_objects.menus import *
from gui.builder_toolbox.loading_and_saving_sessions import load_session
from gui.builder_toolbox.settings_init import init_config
from gui.restart_application import restart_application
from gui.builder_toolbox.settings_util import get_config, edit_config


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg=get_config("col_bg"))
        self.master = master
        self.ui_console = Listbox()
        self.preview_window = None
        self.tooltipflag = True
        self.master.bind('<Control-r>', lambda e: run_with_init_config(self))
        self.master.bind('<Control-p>', lambda e: draw_preview(self))
        self.master.bind('<Control-t>', lambda e: set_tooltip_flag(self, not self.tooltipflag))
        self.master.bind("<Return>", lambda e: btn_entry_search_function(self))

        def run_with_init_config(self):
            init_config()
            save_session("", None)
            restart_application(self)

        def draw_preview(self):
            if self.preview_window is None:
                preview_function(self)
            else:
                self.preview_window.destroy()
                self.preview_window = None

        def set_tooltip_flag(self, flag):
            if flag:
                print_to_ui_console(self, "tooltips enabled")
            else:
                print_to_ui_console(self, "tooltips disabled")
            self.tooltipflag = flag

        self.result = list()
        self.remove_stopwords = BooleanVar()
        self.remove_stopwords.set(get_config("stop_word"))
        path, tf_object = load_session()
        self.dir_selected = path
        self.tf_object = tf_object

        self.toggle_clustering = BooleanVar()
        self.toggle_clustering.set(get_config("clustering"))
        self.selected_stemmer = StringVar()
        self.selected_stemmer.set(get_config("stemmer"))
        self.search_mode = StringVar()
        self.search_mode.set(get_config("search_mode"))
        self.snowballstate = ACTIVE if self.selected_stemmer.get() == "snowball" else DISABLED
        self.stopwordstate = ACTIVE if get_config("stop_word") else DISABLED
        self.clusteringstate = ACTIVE if get_config("search_mode") != "logistic regression" else DISABLED
        self.master.geometry(str(get_config("master_width")) + "x" + str(get_config("master_height")))
        self.master.title(get_config("txt_mastertitle"))
        self.master.config(relief=get_config("relief_frames"),
                           bd=get_config("global_padding")+2,
                           bg=get_config("col_bg")
                           )

        self.window_settings = None  # needs to be none to prevent empty popup window at startup
        btn_settings(self, self.master)
        entry_frame(self, self.master)
        ui_console(self, self.master)
        shortcut_label(self.ui_console)
        self.preview_window = None  # needs to be none to prevent empty popup window at startup
        result_frame(self, self.master)
        dir_label(self, self.result_frame)

        self.pack()
