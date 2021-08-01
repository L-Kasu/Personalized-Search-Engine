from gui.builder_toolbox.tkinter_objects.labels import *
from gui.builder_toolbox.settings_util import *
from gui.builder_toolbox.tooltip import AddTooltip
from search import search_class


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
    self.snowballstate = [ACTIVE if self.selected_stemmer.get() == "snowball" else DISABLED]


def radiobtns_stopword(self, location, col_bg, col_txt):
    for state in ["on", "off"]:
        radiobtn = default_radiobtn(location,
                                    state,
                                    self.remove_stopwords,
                                    state == "on",
                                    lambda: stopword_function(self, self.remove_stopwords.get()),
                                    col_bg,
                                    col_txt)
        radiobtn.pack(side=LEFT, fill=BOTH)


def stopword_function(self, bool):
    self.stopwordstate = ACTIVE if bool else DISABLED


def radiobtns_clustering(self, location, col_bg, col_txt):
    for state in ["on", "off"]:
        radiobtn = default_radiobtn(location,
                                    state,
                                    self.toggle_clustering,
                                    state == "on",
                                    None,
                                    col_bg,
                                    col_txt)
        radiobtn.pack(side=LEFT, fill=BOTH)


def radiobtns_search_mode(self, location, col_bg, col_txt):
    for mode in ["GloVe", "fasttext", "tfidf", "logistic regression"]:
        radiobtn = default_radiobtn(location,
                                    mode,
                                    self.search_mode,
                                    mode,
                                    lambda: radiobtns_search_mode_function(self),
                                    col_bg,
                                    col_txt
        )
        AddTooltip(radiobtn, get_config("txt_tooltip_" + mode))
        radiobtn.pack(side=LEFT, fill=BOTH)


def radiobtns_search_mode_function(self):
    self.tf_object = search_class.Search(self.tf_object.corpus, self.tf_object.titles)
