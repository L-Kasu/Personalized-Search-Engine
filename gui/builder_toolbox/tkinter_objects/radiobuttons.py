from gui.builder_toolbox.tkinter_objects.labels import *
from gui.builder_toolbox.settings_util import *


def choose_stemmer(self, location):
    self.frame_stemmer = Frame(location)
    self.frame_stemmer.pack()
    self.label_stemmer = Label(self.frame_stemmer,
                               text=get_config("txt_selectStemmer"),
                               font=get_config("font_header_2"))
    self.label_stemmer.config(bg=get_config("col_bg_lgt"),
                              fg=get_config("col_acc_minor"),
                              height=1,
                              borderwidth=0,
                              highlightthickness=0
                              )
    self.label_stemmer.pack(side=TOP, fill=X, expand=True)

    self.var = StringVar()

    self.radiobutton_PorterStemmer = Radiobutton(self.frame_stemmer,
                                                 text="Porter",
                                                 variable=self.var,
                                                 value="porter",
                                                 command=set_stemmer("porter")
                                                 )
    self.radiobutton_PorterStemmer.config(bg=get_config("col_bg_lgt"),
                                          fg=get_config("col_acc_major"),
                                          activebackground=get_config("col_bg_lgt"),
                                          selectcolor=get_config("col_bg_lgt")
                                          )
    self.radiobutton_PorterStemmer.pack(side=LEFT)

    self.radiobutton_LancasterStemmer = Radiobutton(self.frame_stemmer,
                                                    text="Lancaster",
                                                    variable=self.var,
                                                    value="lancaster",
                                                    command=set_stemmer("lancaster")
                                                    )
    self.radiobutton_LancasterStemmer.config(bg=get_config("col_bg_lgt"),
                                             fg=get_config("col_acc_major"),
                                             activebackground=get_config("col_bg_lgt"),
                                             selectcolor=get_config("col_bg_lgt"))
    self.radiobutton_LancasterStemmer.pack(side=LEFT)


def stopword(self, location):
    self.frame_stopword = Frame(location)
    self.frame_stopword.pack()

    self.label_stopword = Label(self.frame_stopword,
                                text=get_config("txt_toggleStopword"),
                                font=get_config("font_header_2"))
    self.label_stopword.config(bg=get_config("col_bg_lgt"),
                               fg=get_config("col_acc_minor"),
                               height=1,
                               borderwidth=0,
                               highlightthickness=0
                               )
    self.label_stopword.pack(side=TOP, fill=X, expand=True)

    self.var = StringVar()

    self.radiobutton_on = Radiobutton(self.frame_stopword,
                                      text=get_config("txt_on"),
                                      variable=self.var,
                                      value="on",
                                      command=set_stop_word(True)
                                      )
    self.radiobutton_on.config(bg=get_config("col_bg_lgt"),
                               fg=get_config("col_acc_major"),
                               activebackground=get_config("col_bg_lgt"),
                               selectcolor=get_config("col_bg_lgt"))
    self.radiobutton_on.pack(side=LEFT,fill=X)

    self.radiobutton_off = Radiobutton(self.frame_stopword,
                                       text=get_config("txt_off"),
                                       variable=self.var,
                                       value="off",
                                       command=set_stop_word(False)
                                       )
    self.radiobutton_off.config(bg=get_config("col_bg_lgt"),
                                fg=get_config("col_acc_major"),
                                activebackground=get_config("col_bg_lgt"),
                                selectcolor=get_config("col_bg_lgt"))
    self.radiobutton_off.pack(side=LEFT, fill=X)
