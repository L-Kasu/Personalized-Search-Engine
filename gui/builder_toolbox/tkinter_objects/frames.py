from gui.builder_toolbox.tkinter_objects.entries import *
from gui.builder_toolbox.tkinter_objects.listboxes import *
from gui.builder_toolbox.tkinter_objects.buttons import *
from gui.builder_toolbox.tkinter_objects.menus import *


def get_setting_frame(self,
                      location,
                      name,
                      selector,
                      col_bg,
                      col_txt):
    frame = Frame(location,
                  bg=col_bg,
                  bd=get_config("global_padding")
                  )
    default_label(frame,
                  name,
                  bg=col_bg,
                  fg=col_txt,
                  font=get_config("font_header_2"),
                  justify=LEFT
                  ).pack(side=LEFT,
                         anchor=W,
                         expand=True
                         )
    selector(self,
             frame,
             col_bg,
             col_txt
             )
    return frame



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
    return get_setting_frame(self,
                      location,
                      get_config("txt_selectStemmer"),
                      (lambda s, f, b, t: radiobtns_stemmer(s, f, b, t)),
                      col_bg,
                      col_txt
                      )


def frame_stopword(self, location, col_bg, col_txt):
    return get_setting_frame(self,
                      location,
                      get_config("txt_toggleStopword"),
                      (lambda s, f, b, t: radiobtns_stopword(s, f, b, t)),
                      col_bg,
                      col_txt
                      )


def frame_embedding(self, location, col_bg, col_txt):
    return get_setting_frame(self,
                      location,
                      get_config("txt_selectsearchmode"),
                      (lambda s, f, b, t: radiobtns_search_mode(s, f, b, t)),
                      col_bg,
                      col_txt
                      )


def frame_clustering(self, location, col_bg, col_txt):
    return get_setting_frame(self,
                      location,
                      get_config("txt_toggleClustering"),
                      (lambda s, f, b, t: radiobtns_clustering(s, f, b, t)),
                      col_bg,
                      col_txt
                      )


def frame_menu_lang(self, location, col_bg, col_txt):
    return get_setting_frame(self,
                             location,
                             get_config("txt_language"),
                             (lambda s, f, b, t: menu_languages(s, f)),
                             col_bg,
                             col_txt
                             )


def frame_menu_colors(self, location, col_bg, col_txt):
    return get_setting_frame(self,
                             location,
                             get_config("txt_colortheme"),
                             (lambda s, f, b, t: menu_styles(s, f)),
                             col_bg,
                             col_txt
                             )


def frame_menu_snowballstemmer_language(self, location, col_bg, col_txt):
    return get_setting_frame(self,
                             location,
                             get_config("txt_selectsnowballlang"),
                             (lambda s, f, b, t: menu_snowballstemmer_language(s, f)),
                             col_bg,
                             col_txt
                             )


def frame_menu_stopword_language(self, location, col_bg, col_txt):
    return get_setting_frame(self,
                             location,
                             get_config("txt_selectstopwordlang"),
                             (lambda s, f, b, t: menu_stopword_language(s, f)),
                             col_bg,
                             col_txt
                             )