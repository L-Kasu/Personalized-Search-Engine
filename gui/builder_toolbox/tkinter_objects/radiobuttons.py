from gui.builder_toolbox.tkinter_objects.labels import *
from gui.builder_toolbox.settings_util import *


def default_radiobtn(location,
                     text,
                     variable,
                     value,
                     function,
                     col_bg,
                     col_txt,
                     state=ACTIVE,
                     side=LEFT,
                     fill=BOTH
                     ):
    Radiobutton(location,
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
                ).pack(side=side, fill=fill)


def radiobtns_stemmer(self, location, col_bg, col_txt):
    [default_radiobtn(location,
                      stemmer.upper(),
                      self.selected_stemmer,
                      stemmer,
                      lambda: edit_config({"stemmer": self.selected_stemmer.get()}),
                      col_bg,
                      col_txt)
     for stemmer in ["porter", "lancaster", "snowball"]]


def radiobtns_stopword(self, location, col_bg, col_txt):
    [default_radiobtn(location,
                      state,
                      self.remove_stopwords,
                      state == "on",
                      lambda: edit_config({"stop_word": self.remove_stopwords.get()}),
                      col_bg,
                      col_txt)
     for state in ["on", "off"]]
