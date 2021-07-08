from gui.builder_toolbox.tkinter_objects.labels import *


def choose_stemmer(self, location):
    self.frame_stemmer = Frame(location)
    self.frame_stemmer.pack()
    self.label_stemmer = Label(self.frame_stemmer,
                               text="Select Stemmer:",
                               font=font_header_2)
    self.label_stemmer.config(bg=col_bg_lgt,
                              fg=col_acc_minor,
                              height=1,
                              borderwidth=0,
                              highlightthickness=0
                              )
    self.label_stemmer.pack(side=TOP, fill=X, expand=True)

    self.var = IntVar()

    self.radiobutton_PorterStemmer = Radiobutton(self.frame_stemmer,
                                                 text="Porter",
                                                 variable=self.var,
                                                 value=1)
    self.radiobutton_PorterStemmer.pack(side=LEFT)

    self.radiobutton_LancasterStemmer = Radiobutton(self.frame_stemmer,
                                                    text="Lancaster",
                                                    variable=self.var,
                                                    value=2)
    self.radiobutton_LancasterStemmer.pack(side=LEFT)


def stopword(self, location):
    self.frame_stopword = Frame(location)
    self.frame_stopword.pack()

    self.label_stopword = Label(self.frame_stopword,
                                text="Stop Word:",
                                font=font_header_2)
    self.label_stopword.config(bg=col_bg_lgt,
                               fg=col_acc_minor,
                               height=1,
                               borderwidth=0,
                               highlightthickness=0
                               )
    self.label_stopword.pack(side=TOP, fill=X, expand=True)

    self.var = IntVar()

    self.radiobutton_on = Radiobutton(self.frame_stopword,
                                      text="on",
                                      variable=self.var,
                                      value=1)
    self.radiobutton_on.pack(side=LEFT)

    self.radiobutton_off = Radiobutton(self.frame_stopword,
                                       text="off",
                                       variable=self.var,
                                       value=2)
    self.radiobutton_off.pack(side=LEFT)
