from tkinter import *
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

    self.checkbutton_PorterStemmer = Checkbutton(self.frame_stemmer,
                                                 text="Porter")
    # self.checkbutton_PorterStemmer.config()
    self.checkbutton_PorterStemmer.pack(side=LEFT)

    self.checkbutton_LancasterStemmer = Checkbutton(self.frame_stemmer,
                                                    text="Lancaster")
    # self.checkbutton_LancasterStemmer.config()
    self.checkbutton_LancasterStemmer.pack(side=LEFT)

