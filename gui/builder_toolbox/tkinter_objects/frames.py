from gui.builder_toolbox.tkinter_objects.entries import *
from gui.builder_toolbox.tkinter_objects.listboxes import *
from gui.builder_toolbox.tkinter_objects.buttons import *
from gui.builder_toolbox.tkinter_objects.menus import *


def entry_frame(self, location):
    self.entry_frame = Frame(location,
                             bg=get_config("col_bg_lgt"),
                             relief=get_config("relief_frames"),
                             bd=get_config("global_padding")
                             )
    self.entry_frame.pack(fill=X, expand=True)
    search_entry(self, self.entry_frame)
    btn_select_directory(self, self.entry_frame)
    buttons_frame(self, self.entry_frame)
    btn_entry_delete(self, self.buttons_frame)
    btn_entry_search(self, self.buttons_frame)


def buttons_frame(self, location):
    self.buttons_frame = Frame(location, bg=get_config("col_bg_lgt"))
    self.buttons_frame.pack(side=BOTTOM, anchor=W)


def result_frame(self, location):
    self.result_frame = Frame(location, bg=get_config("col_bg_lgt"))
    self.result_frame.pack(side=BOTTOM, fill=BOTH, expand=True)

    result_label(self.result_frame)
    result_text(self, self.result_frame)
    btn_preview(self, self.result_text)


def frame_stemmer(self, location, col_bg, col_txt):
    self.frame_stemmer = Frame(location, bg=col_bg, bd=get_config("global_padding"))
    self.frame_stemmer.pack(fill=Y)
    label_stemmer(self.frame_stemmer, col_bg, col_txt)
    radiobtns_stemmer(self, self.frame_stemmer, col_bg, col_txt)


def frame_stopword(self, location, col_bg, col_txt):
    self.frame_stopword = Frame(location, bg=col_bg, bd=get_config("global_padding"))
    self.frame_stopword.pack(fill=Y)
    label_stopword(self.frame_stopword, col_bg, col_txt)
    radiobtns_stopword(self, self.frame_stopword, col_bg, col_txt)


def frame_menu_lang(self, location, col_bg, col_txt):
    self.frame_menu_lang = Frame(location,
                                 bg=col_bg,
                                 bd=get_config("global_padding"))
    self.frame_menu_lang.pack(anchor=CENTER)
    language_label(self.frame_menu_lang, col_bg, col_txt)
    menu_languages(self, self.frame_menu_lang)


def frame_menu_colors(self, location, col_bg, col_txt):
    self.frame_menu_colors = Frame(location,
                                   bg=col_bg,
                                   bd=get_config("global_padding"))
    self.frame_menu_colors.pack(anchor=CENTER)
    color_label(self.frame_menu_colors, col_bg, col_txt)
    menu_styles(self, self.frame_menu_colors)


def frame_menu_snowballstemmer_language(self, location, col_bg, col_txt):
    self.frame_menu_snowballstemmer_language = Frame(location,
                                                     bg=col_bg,
                                                     bd=get_config("global_padding"))
    self.frame_menu_snowballstemmer_language.pack(anchor=CENTER)
    label_menu_snowballstemmer_language(self.frame_menu_snowballstemmer_language, col_bg, col_txt)
    menu_snowballstemmer_language(self, self.frame_menu_snowballstemmer_language)
