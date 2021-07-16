from gui.builder_toolbox.tkinter_objects.labels import *
from gui.builder_toolbox.settings_util import *


def radiobtns_stemmer(self, location, col_bg, col_txt):
    self.radiobutton_PorterStemmer = Radiobutton(location,
                                                 text="Porter",
                                                 variable=self.selected_stemmer,
                                                 value="porter",
                                                 command=lambda: edit_config({"stemmer": "porter"})
                                                 )
    self.radiobutton_PorterStemmer.config(bg=col_bg,
                                          fg=col_txt,
                                          activebackground=col_bg,
                                          activeforeground=col_txt,
                                          selectcolor=col_bg,
                                          state=ACTIVE
                                          )
    self.radiobutton_PorterStemmer.pack(side=LEFT, fill=BOTH)

    self.radiobutton_LancasterStemmer = Radiobutton(location,
                                                    text="Lancaster",
                                                    variable=self.selected_stemmer,
                                                    value="lancaster",
                                                    command=lambda: edit_config({"stemmer": "lancaster"})
                                                    )
    self.radiobutton_LancasterStemmer.config(bg=col_bg,
                                             fg=col_txt,
                                             activebackground=col_bg,
                                             activeforeground=col_txt,
                                             selectcolor=col_bg,
                                             state=ACTIVE
                                             )
    self.radiobutton_LancasterStemmer.pack(side=RIGHT, fill=BOTH)


def radiobtns_stopword(self, location, col_bg, col_txt):
    self.radiobutton_on = Radiobutton(location,
                                      text=get_config("txt_on"),
                                      variable=self.remove_stopwords,
                                      value=True,
                                      command=lambda: edit_config({"stop_word": True})
                                      )
    self.radiobutton_on.config(bg=col_bg,
                               fg=col_txt,
                               activebackground=col_bg,
                               activeforeground=col_txt,
                               selectcolor=col_bg,
                               state=ACTIVE
                               )
    self.radiobutton_on.pack(side=LEFT, fill=BOTH)

    self.radiobutton_off = Radiobutton(location,
                                       text=get_config("txt_off"),
                                       variable=self.remove_stopwords,
                                       value=False,
                                       command=lambda: edit_config({"stop_word": False})
                                       )
    self.radiobutton_off.config(bg=col_bg,
                                fg=col_txt,
                                activebackground=col_bg,
                                activeforeground=col_txt,
                                selectcolor=col_bg,
                                state=ACTIVE
                                )
    self.radiobutton_off.pack(side=RIGHT, fill=BOTH)
