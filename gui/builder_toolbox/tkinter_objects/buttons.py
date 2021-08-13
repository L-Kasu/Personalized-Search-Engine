from tkinter import filedialog
import gui
from search import clustering
from gui.builder_toolbox.tkinter_objects.radiobuttons import *
from gui.builder_toolbox.search_util import *

btn_padding = get_config("btn_padding")


def default_btn(location, text, function):
    button = Button(location,
                    text=text,
                    command=function,
                    font=get_config("font_header_2"),
                    bg=get_config("col_btn_idle"),
                    fg=get_config("col_acc_btncontrast"),
                    bd=get_config("global_padding"),
                    activebackground=get_config("col_btn_active"),
                    activeforeground=get_config("col_acc_btncontrast"),
                    relief=get_config("relief_btn"),
                    borderwidth=[0 if get_config("relief_btn") == "flat" else 2]
                    )
    button.bind("<Enter>", lambda e: button.config(bg=get_config("col_btn_active")))
    button.bind("<Leave>", lambda e: button.config(bg=get_config("col_btn_idle")))
    return button


def btn_select_directory(self, location):
    default_btn(location,
                get_config("txt_selectdir"),
                lambda: btn_select_directory_function(self)
                ).pack(side=LEFT,
                       pady=btn_padding
                       )


def btn_select_directory_function(self):
    print_to_ui_console(self, "preprocessing in progress...")
    new_dir = filedialog.askdirectory()
    if new_dir != "":
        self.dir_selected = new_dir
        preprocess(self)
        self.dir_label.config(text=self.dir_selected)
        print_to_ui_console(self, "preprocessing successful")
    else:
        print_to_ui_console(self, "preprocessing aborted")


def btn_entry_search(self, location):
    default_btn(location,
                get_config("txt_entrysearch"),
                lambda: btn_entry_search_function(self)
                ).pack(side=LEFT,
                       anchor=CENTER,
                       padx=btn_padding,
                       pady=btn_padding)


def btn_entry_search_function(self):
    if self.tf_object is None:
        print_to_ui_console(self, "you need to select a directory before you can search for documents!")
    else:
        search(self, self.search_entry.get() if self.search_entry.get() else print_to_ui_console(self,
                                                                                                 "search entry field is empty!"))


def btn_entry_delete(self, location):
    default_btn(location,
                get_config("txt_entryclear"),
                lambda: btn_entry_delete_function(self)
                ).pack(side=RIGHT,
                       anchor=CENTER,
                       pady=btn_padding)


def btn_entry_delete_function(self):
    self.search_entry.delete(0, END)
    self.result_text.delete(0, END)


def preview_function(self):
    selected_result_file = self.result_text.get(ANCHOR)
    if self.dir_selected == "":
        text = get_config("ERR_noDirectorySelected")
    elif selected_result_file == "":
        text = get_config("ERR_resultListEmpty")
    else:
        text = get_page_text(self, selected_result_file)
    self.preview_window.destroy() if self.preview_window is not None else print()
    self.preview_window = Toplevel(bg=get_config("col_bg"), bd=get_config("global_padding"))
    self.preview_window.title(get_config("txt_preview") + ": " + self.result_text.get(ANCHOR))
    preview_window_label(self.preview_window, text)
    x = y = 0
    x, y, cx, cy = self.master.bbox("insert")
    x += self.result_text.winfo_rootx() + (get_config("master_width") / 4)
    y += self.result_text.winfo_rooty()
    self.preview_window.wm_geometry("+%d+%d" % (x, y))


def btn_settings(self, location):
    self.btn_settings = default_btn(location,
                                    get_config("txt_settingsheader"),
                                    lambda: settings_function(self)
                                    )
    self.btn_settings.pack(side=TOP,
                           anchor=NE)


def settings_function(self):
    col_bg = get_config("col_bg")
    col_txt = get_config("col_acc_bgcontrast")
    self.window_settings.destroy() if self.window_settings is not None else print()
    self.window_settings = Toplevel(bg=col_bg,
                                    bd=get_config("global_padding"),
                                    relief=get_config("relief_frames")
                                    )
    self.window_settings.title(get_config("txt_settingsheader"))
    self.window_settings.geometry(str(get_config("settings_width")) + "x" + str(get_config("settings_height")))
    x = y = 0
    x, y, cx, cy = self.master.bbox("insert")
    x += self.btn_settings.winfo_rootx() \
         - get_config("settings_width") \
         - get_config("global_padding") \
         - 2
    y += self.btn_settings.winfo_rooty() - 1
    self.window_settings.wm_geometry("+%d+%d" % (x, y))
    label_settings(self.window_settings, col_bg, col_txt)
    # only works this way, no idea why...
    gui.builder_toolbox.tkinter_objects.frames.frame_stemmer(self, self.window_settings, col_bg, col_txt).pack(fill=X)
    gui.builder_toolbox.tkinter_objects.frames.frame_stopword(self, self.window_settings, col_bg, col_txt).pack(fill=X)
    gui.builder_toolbox.tkinter_objects.frames.frame_searchmode(self, self.window_settings, col_bg, col_txt).pack(
        fill=X)
    gui.builder_toolbox.tkinter_objects.frames.frame_clustering(self, self.window_settings, col_bg, col_txt).pack(
        fill=X)
    gui.builder_toolbox.tkinter_objects.frames.frame_menu_lang(self, self.window_settings, col_bg, col_txt).pack(fill=X)
    gui.builder_toolbox.tkinter_objects.frames.frame_menu_colors(self, self.window_settings, col_bg, col_txt).pack(
        fill=X)
    gui.builder_toolbox.tkinter_objects.frames.frame_menu_fonts(self, self.window_settings, col_bg, col_txt).pack(
        fill=X)
    gui.builder_toolbox.tkinter_objects.frames.frame_menu_snowballstemmer_language(self, self.window_settings, col_bg,
                                                                                   col_txt).pack(fill=X)
    gui.builder_toolbox.tkinter_objects.frames.frame_menu_stopword_language(self, self.window_settings, col_bg,
                                                                            col_txt).pack(fill=X)
    gui.builder_toolbox.tkinter_objects.frames.frame_menu_docs_to_return(self, self.window_settings, col_bg,
                                                                         col_txt).pack(fill=X)
    default_btn(self.window_settings,
                get_config("txt_confirm"),
                lambda: settings_confirm_function(self,
                                                  self.selected_stemmer.get(),
                                                  self.remove_stopwords.get(),
                                                  self.search_mode.get(),
                                                  self.toggle_clustering.get()
                                                  )
                ).pack(side=LEFT,
                       pady=btn_padding)
    default_btn(self.window_settings,
                get_config("txt_cancel"),
                lambda: self.window_settings.destroy()
                ).pack(anchor=W,
                       padx=btn_padding,
                       pady=btn_padding)


def settings_confirm_function(self,
                              stemmer,
                              stopword,
                              search_mode,
                              toggle_clustering
                              ):
    edit_config({"stemmer": stemmer})
    edit_config({"stop_word": stopword})
    old_clustering = get_config("clustering")
    edit_config({"clustering": toggle_clustering})
    if get_config("search_mode") != search_mode:
        edit_config({"search_mode": search_mode})
        self.tf_object = search_class.Search(self.tf_object.corpus, self.tf_object.titles, self)
        save_session(self.dir_selected, self.tf_object)
    if get_config("clustering") != old_clustering:
        self.tf_object.set_clustering(clustering.Clustering(self.tf_object.search_method.get_matrix(), app=self))
        save_session(self.dir_selected, self.tf_object)
    self.window_settings.destroy()
