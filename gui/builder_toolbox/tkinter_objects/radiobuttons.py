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
    self.radiobtns_stemmer = []
    for stemmer in ["porter", "lancaster", "snowball"]:
        state = ACTIVE if get_config("search_mode") is not ("GloVe" or "fasttext") else DISABLED
        radiobtn = default_radiobtn(location,
                                    stemmer.upper(),
                                    self.selected_stemmer,
                                    stemmer,
                                    lambda: stemmer_function(self),
                                    col_bg,
                                    col_txt,
                                    state=state
                                    )
        AddTooltip(radiobtn, get_config("txt_tooltip_"+stemmer))
        radiobtn.pack(side=LEFT, fill=BOTH)
        self.radiobtns_stemmer.append(radiobtn)


def stemmer_function(self):
    state = ACTIVE if self.selected_stemmer.get() == "snowball" else DISABLED
    self.snowballstate = state
    self.menu_snowballstemmer_language.config(state=state)


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
    state = ACTIVE if bool else DISABLED
    self.stopwordstate = state
    self.menu_stopword_language.config(state=state)


def radiobtns_clustering(self, location, col_bg, col_txt):
    self.radiobtns_clustering = []
    for state in ["on", "off"]:
        activestate = self.clusteringstate
        radiobtn = default_radiobtn(location,
                                    state,
                                    self.toggle_clustering,
                                    state == "on",
                                    None,
                                    col_bg,
                                    col_txt,
                                    state=activestate)
        radiobtn.pack(side=LEFT, fill=BOTH)
        self.radiobtns_clustering.append(radiobtn)


def radiobtns_search_mode(self, location, col_bg, col_txt):
    for mode in ["GloVe", "fasttext", "tfidf", "logistic regression"]:
        radiobtn = default_radiobtn(location,
                                    mode,
                                    self.search_mode,
                                    mode,
                                    lambda: radiobtns_search_mode_function(self, self.search_mode.get()),
                                    col_bg,
                                    col_txt
        )
        AddTooltip(radiobtn, get_config("txt_tooltip_" + mode))
        radiobtn.pack(side=LEFT, fill=BOTH)


def radiobtns_search_mode_function(self, mode):
    state = ACTIVE if mode == "tfidf" or mode == "logistic regression" else DISABLED
    for radiobtn in self.radiobtns_stemmer:
        radiobtn.config(state=state)

    if mode == "logistic regression":
        self.toggle_clustering.set(False)
        self.clusteringstate = DISABLED

    cstate = ACTIVE if mode != "logistic regression" else DISABLED
    for radiobtn in self.radiobtns_clustering:
        radiobtn.config(state=cstate)
