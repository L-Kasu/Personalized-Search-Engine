from gui.builder_toolbox.tkinter_objects.labels import *
from gui.builder_toolbox.settings_util import *
from gui.builder_toolbox.tooltip import AddTooltip


def default_radiobtn(location,
                     text,
                     variable,
                     value,
                     function,
                     col_bg,
                     col_txt,
                     state=ACTIVE
                     ):
    return Radiobutton(location,
                       text=text,
                       variable=variable,
                       value=value,
                       command=function,
                       bg=col_bg,
                       fg=col_txt,
                       activebackground=col_bg,
                       activeforeground=col_txt,
                       selectcolor=col_bg,
                       state=state
                       )


def radiobtns_stemmer(self, location, col_bg, col_txt):
    for stemmer in ["porter", "lancaster", "snowball"]:
        radiobtn = default_radiobtn(location,
                                    stemmer.upper(),
                                    self.selected_stemmer,
                                    stemmer,
                                    lambda: stemmer_function(self),
                                    col_bg,
                                    col_txt)
        AddTooltip(radiobtn, get_config("txt_tooltip_"+stemmer))
        radiobtn.pack(side=LEFT, fill=BOTH)


def stemmer_function(self):
    edit_config({"stemmer": self.selected_stemmer.get()})
    isstemmer = "is" + self.selected_stemmer.get()
    try:
        edit_config({isstemmer: not get_config(isstemmer)})
        self.snowballstate = ACTIVE
    except KeyError:
        edit_config({"issnowball": not get_config("issnowball")})
        self.snowballstate = DISABLED


def radiobtns_stopword(self, location, col_bg, col_txt):
    for state in ["on", "off"]:
        radiobtn = default_radiobtn(location,
                      state,
                      self.remove_stopwords,
                      state == "on",
                      lambda: edit_config({"stop_word": self.remove_stopwords.get()}),
                      col_bg,
                      col_txt)
        radiobtn.pack(side=LEFT, fill=BOTH)


def radiobtns_embedding(self, location, col_bg, col_txt):
    for mode in ["GloVe", "fasttext"]:
        radiobtn = default_radiobtn(location,
                                    mode,
                                    self.embedding_mode,
                                    mode,
                                    lambda: edit_config({"embedding": self.embedding_mode.get()}),
                                    col_bg,
                                    col_txt)
        radiobtn.pack(side=LEFT, fill=BOTH)
