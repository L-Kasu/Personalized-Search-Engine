from gui.builder_toolbox.tkinter_objects.labels import *
from gui.builder_toolbox.settings_util import *


def radiobtns_stemmer(self, location, col_bg, col_txt):
    for stemmer in ["porter", "lancaster", "snowball"]:
        Radiobutton(location,
                    text=stemmer.upper(),
                    variable=self.selected_stemmer,
                    value=stemmer,
                    command=lambda: edit_config({"stemmer": stemmer}),
                    bg=col_bg,
                    fg=col_txt,
                    activebackground=col_bg,
                    activeforeground=col_txt,
                    selectcolor=col_bg,
                    state=ACTIVE
                    ).pack(side=LEFT, fill=BOTH)


def radiobtns_stopword(self, location, col_bg, col_txt):
    for state in ["on", "off"]:
        Radiobutton(location,
                    text=state,
                    variable=self.remove_stopwords,
                    value=state,
                    command=lambda: edit_config({"stop_word": state == "on"}),
                    bg=col_bg,
                    fg=col_txt,
                    activebackground=col_bg,
                    activeforeground=col_txt,
                    selectcolor=col_bg,
                    state=ACTIVE
                    ).pack(side=LEFT, fill=BOTH)
