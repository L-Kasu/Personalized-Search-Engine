from gui.builder_toolbox.settings_util import get_configdict, write_config
from gui.builder_toolbox.settings_defaultpaths import *


def init_config(path=default_path,
                masterfile=masterconfigfile,
                langfile=languageconfigfile,
                colorsfile=colorsconfigfile):
    init_langfile(langfile, path)
    init_colorsfile(colorsfile, path)
    config = {"master_height": "500",
              "master_width": "800",
              "prev_window_size": 100,
              "preview_size": 500,
              **get_configdict(path, languageconfigfile)["English"],
              **get_configdict(path, colorsconfigfile)["wip"],
              "stemmer": "porter",
              "stop_word": True}
    write_config(config, path, masterfile)


def init_colorsfile(colorsfile=colorsconfigfile, path=default_path):
    colorsconfig = {"wip": {"ID_colors": "wip",
                            "col_bg": "#3b3b3b",
                            "col_bg_lgt": "#5f5f5f",
                            "col_btn_idle": "#940000",
                            "col_btn_active": "#d50000",
                            "col_entryfield_idle": "#bbbbbb",
                            "col_entryfield_contrast": "#3b3b3b",
                            "col_acc_major": "#b3b3b3",
                            "col_acc_minor": "#b3b3b3",
                            "font_header_1": ("Arial", 15, "bold"),
                            "font_header_2": ("Arial", 10, "bold"),
                            "font_returntext": ("Arial", 10),
                            "relief_frames": "flat",
                            "relief_btn": "flat"},
                    "teatime": {"ID_colors": "teatime",
                                "col_bg": "#386944",
                                "col_bg_lgt": "#a58850",
                                "col_btn_idle": "#bfb10b",
                                "col_btn_active": "#867c07",
                                "col_entryfield_idle": "#c2c2c2",
                                "col_entryfield_contrast": "#585858",
                                "col_acc_major": "#585858",
                                "col_acc_minor": "#585858",
                                "font_header_1": ("Old English Text MT", 20, "bold"),
                                "font_header_2": ("Goudy Old Style", 12, "bold"),
                                "font_returntext": ("Goudy Old Style", 12),
                                "relief_frames": "flat",
                                "relief_btn": "raise"},
                    "sharky": {"ID_colors": "sharky",
                               "col_bg": "#0012ae",
                               "col_bg_lgt": "#00b1ff",
                               "col_btn_idle": "#ff8e00",
                               "col_btn_active": "#ffc400",
                               "col_entryfield_idle": "#00ffd1",
                               "col_entryfield_contrast": "#474747",
                               "col_acc_major": "#272727",
                               "col_acc_minor": "#272727",
                               "font_header_1": ("Arial", 15, "bold"),
                               "font_header_2": ("Arial", 10, "bold"),
                               "font_returntext": ("Arial", 10),
                               "relief_frames": "flat",
                               "relief_btn": "raise"},
                    "redengine": {"ID_colors": "redengine",
                                  "col_bg": "#272727",
                                  "col_bg_lgt": "#373737",
                                  "col_btn_idle": "#980000",
                                  "col_btn_active": "#00b2ff",
                                  "col_entryfield_idle": "#909090",
                                  "col_entryfield_contrast": "#272727",
                                  "col_acc_major": "#f7ff00",
                                  "col_acc_minor": "#f7ff00",
                                  "font_header_1": ("Biome", 16, "bold"),
                                  "font_header_2": ("Biome", 10, "bold"),
                                  "font_returntext": ("Biome", 10),
                                  "relief_frames": "flat",
                                  "relief_btn": "flat"},
                    "cb_friendly": {"ID_colors": "cb_friendly",
                                    "col_bg": "#0072b2",
                                    "col_bg_lgt": "#cc79a7",
                                    "col_btn_idle": "#d55e00",
                                    "col_btn_active": "#009e73",
                                    "col_entryfield_idle": "#009e73",
                                    "col_entryfield_contrast": "white",
                                    "col_acc_major": "#f0e442",
                                    "col_acc_minor": "#f0e442",
                                    "font_header_1": ("Arial", 15, "bold"),
                                    "font_header_2": ("Arial", 10, "bold"),
                                    "font_returntext": ("Arial", 10),
                                    "relief_frames": "raise",
                                    "relief_btn": "raise"},
                    "monochrome": {"ID_colors": "monochrome",
                                   "col_bg": "#282828",
                                   "col_bg_lgt": "#1f1f1f",
                                   "col_btn_idle": "black",
                                   "col_btn_active": "#ffcc00",
                                   "col_entryfield_idle": "black",
                                   "col_entryfield_contrast": "#00ff00",
                                   "col_acc_major": "#ffb000",
                                   "col_acc_minor": "#ffb000",
                                   "font_header_1": ("Terminal", 15, "bold"),
                                   "font_header_2": ("Terminal", 10, "bold"),
                                   "font_returntext": ("Terminal", 10),
                                   "relief_frames": "raise",
                                   "relief_btn": "raise"},
                    "cyberpunk": {"ID_colors": "cyberpunk",
                                  "col_bg": "#272727",
                                  "col_bg_lgt": "#787878",
                                  "col_btn_idle": "#f7ff00",
                                  "col_btn_active": "#c2c800",
                                  "col_entryfield_idle": "#c9c9c9",
                                  "col_entryfield_contrast": "#272727",
                                  "col_acc_major": "#f7ff00",
                                  "col_acc_minor": "#272727",
                                  "font_header_1": ("Biome", 16, "bold"),
                                  "font_header_2": ("Biome", 10, "bold"),
                                  "font_returntext": ("Biome", 10),
                                  "relief_frames": "flat",
                                  "relief_btn": "flat"},
                    "dokidoki": {"ID_colors": "dokidoki",
                                 "col_bg": "#fbd1fd",
                                 "col_bg_lgt": "#f18bf6",
                                 "col_btn_idle": "#ec00d4",
                                 "col_btn_active": "#de2bcc",
                                 "col_entryfield_idle": "#dadada",
                                 "col_entryfield_contrast": "#de2bcc",
                                 "col_acc_major": "#fcfcfc",
                                 "col_acc_minor": "#fcfcfc",
                                 "font_header_1": ("Comic Sans MS", 18, "bold"),
                                 "font_header_2": ("Comic Sans MS", 10, "bold"),
                                 "font_returntext": ("Comic Sans MS", 10),
                                 "relief_frames": "flat",
                                 "relief_btn": "flat"},
                    }
    write_config(colorsconfig, path, colorsfile)


def init_langfile(langfile=languageconfigfile, path=default_path):
    langconfig = {"English": {"ID_lang": "English",
                              "txt_mastertitle": "Search Engine",
                              "txt_selectdir": "Select Directory",
                              "txt_settingsheader": "Settings",
                              "txt_entrysearch": "Search",
                              "txt_entryclear": "Clear",
                              "txt_resultitems": "Search result",
                              "txt_preview": "Preview",
                              "txt_page": "Page",
                              "txt_okay": "Ok",
                              "txt_exitpreview": "Exit",
                              "txt_language": "Language: ",
                              "txt_colortheme": "Theme: ",
                              "txt_selectStemmer": "Select Stemmer",
                              "txt_toggleStopword": "Stop Word Removal",
                              "txt_on": "on",
                              "txt_off": "off",
                              "ERR_noDirectorySelected": "ERROR: No directory selected",
                              "ERR_resultListEmpty": "ERROR: There are no search results"},
                  "German": {"ID_lang": "German",
                             "txt_mastertitle": "Suchmaschine",
                             "txt_selectdir": "Verzeichnis auswählen",
                             "txt_settingsheader": "Einstellungen",
                             "txt_entrysearch": "Suchen",
                             "txt_entryclear": "Löschen",
                             "txt_resultitems": "Ergebnisse",
                             "txt_preview": "Vorschau",
                             "txt_page": "Seite",
                             "txt_okay": "Ok",
                             "txt_exitpreview": "Schließen",
                             "txt_language": "Sprache: ",
                             "txt_colortheme": "Design: ",
                             "txt_selectStemmer": "Stemmerauswahl",
                             "txt_toggleStopword": "Stoppwortentfernung",
                             "txt_on": "an",
                             "txt_off": "aus",
                             "ERR_noDirectorySelected": "FEHLER: Kein Verzeichnis ausgewählt",
                             "ERR_resultListEmpty": "FEHLER: Keine Suchergebnisse vorhanden"},
                  "Spanish": {"ID_lang": "Spanish",
                              "txt_mastertitle": "Buscador",
                              "txt_selectdir": "Seleccionar Directorio",
                              "txt_settingsheader": "Ajustes",
                              "txt_entrysearch": "Buscar",
                              "txt_entryclear": "Borrar",
                              "txt_resultitems": "Buscar en resultados",
                              "txt_preview": "Vista previa",
                              "txt_page": "Pagina",
                              "txt_okay": "Okay(to be translated)",
                              "txt_exitpreview": "Exit(to be translated)",
                              "txt_language": "Language: (to be translated)",
                              "txt_colortheme": "Theme: (to be translated)",
                              "txt_selectStemmer": "Select Stemmer(to be translated)",
                              "txt_toggleStopword": "Stop Word Removal(to be translated)",
                              "txt_on": "on(to be translated)",
                              "txt_off": "off(to be translated)",
                              "ERR_noDirectorySelected": "ERROR: Ningún directorio seleccionado",
                              "ERR_resultListEmpty": "ERROR: No hay resultados de búsqueda"},
                  "Arabic": {"ID_lang": "Arabic",
                             "txt_mastertitle": "مُحَرّكُ البَحث",
                             "txt_selectdir": "اِخْتَر/ي مُجَلَّد",
                             "txt_settingsheader": "الإِعْدَادَات",
                             "txt_entrysearch": "بَحْث",
                             "txt_entryclear": "حَذْف",
                             "txt_resultitems": "نَتيجَةُ البَحْث",
                             "txt_preview": "عَيّنَة",
                             "txt_page": "الصَّفحَة",
                             "txt_okay": "حَسَنَاً",
                             "txt_exitpreview": "إِغْلاق",
                             "txt_language": "اللُّغَة",
                             "txt_colortheme": "التّصميم",
                             "txt_selectStemmer": "اخْتِيَار الStemmer",
                             "txt_toggleStopword": "إِزالَة الStop Words",
                             "txt_on": "نَعَم",
                             "txt_off": "لا",
                             "ERR_noDirectorySelected": "خَطَأ: لَمْ يَتُمَّ اِخْتِيَارُ أَيّ مُجَلَّد",
                             "ERR_resultListEmpty": "خَطَأ: لَيْسَ هُنَالِكَ نَتَائِجٌ لِلْبَحْث"},
                  }
    write_config(langconfig, path, langfile)