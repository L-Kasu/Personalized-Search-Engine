from gui.builder_toolbox.tkinter_objects.frames import *
from gui.builder_toolbox.tkinter_objects.labels import *
from gui.builder_toolbox.settings_util import *


def radiobtns_stemmer(self, location):
    self.var = StringVar()

    self.radiobutton_PorterStemmer = Radiobutton(location,
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

    self.radiobutton_LancasterStemmer = Radiobutton(location,
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


def radiobtns_stopword(self, location):
    self.var = StringVar()

    self.radiobutton_on = Radiobutton(location,
                                      text=get_config("txt_on"),
                                      variable=self.var,
                                      value="on",
                                      command=set_stop_word(True)
                                      )
    self.radiobutton_on.config(bg=get_config("col_bg_lgt"),
                               fg=get_config("col_acc_major"),
                               activebackground=get_config("col_bg_lgt"),
                               selectcolor=get_config("col_bg_lgt"))
    self.radiobutton_on.pack(side=LEFT, fill=X)

    self.radiobutton_off = Radiobutton(location,
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
