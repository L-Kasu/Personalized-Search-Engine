import json


default_path = "./config/config.json"


def write_config(config, path=default_path):
    with open(path, 'w') as file:
        json.dump(config, file)
        file.close()


def edit_config(config_dict, path=default_path):
    with open(path, 'r') as file:
        config = json.load(file)
        for key in config_dict:
            config[key] = config_dict[key]
        file.close()
    with open(path, 'w') as file:
        json.dump(config, file)
        file.close()


def get_config(key, path=default_path):
    with open(path, 'r') as file:
        config = json.load(file)
        value = config[key]
        file.close()
    return value


def init_config(path=default_path):
    config = {"master_height": "500",
              "master_width": "800",
              "prev_window_size": 100,
              "preview_size": 500,
              "txt_mastertitle": "Search Engine",
              "txt_selectdir": "Select Directory",
              "txt_settingsheader": "Settings",
              "txt_entrysearch": "Search",
              "txt_entryclear": "Clear",
              "txt_resultitems": "Search result",
              "txt_preview": "Preview",
              "txt_page": "Page",
              "ERR_noDirectorySelected": "ERROR: No directory selected",
              "ERR_resultListEmpty": "ERROR: There are no search results",
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
              "relief_btn": "flat",
              "stemmer": "porter",
              "stop_word": True}
    write_config(config, path)


def set_language(lang):
    if lang == "English":
        config = {"txt_mastertitle": "Search Engine",
                  "txt_selectdir": "Select Directory",
                  "txt_settingsheader": "Settings",
                  "txt_entrysearch": "Search",
                  "txt_entryclear": "Clear",
                  "txt_resultitems": "Search result",
                  "txt_preview": "Preview",
                  "txt_page": "Page",
                  "ERR_noDirectorySelected": "ERROR: No directory selected",
                  "ERR_resultListEmpty": "ERROR: There are no search results"}
    elif lang == "German":
        config = {"txt_mastertitle": "Suchmaschine",
                  "txt_selectdir": "Verzeichnis auswählen",
                  "txt_settingsheader": "Einstellungen",
                  "txt_entrysearch": "Suchen",
                  "txt_entryclear": "Löschen",
                  "txt_resultitems": "Ergebnisse",
                  "txt_preview": "Vorschau",
                  "txt_page": "Seite",
                  "ERR_noDirectorySelected": "FEHLER: Kein Verzeichnis ausgewählt",
                  "ERR_resultListEmpty": "FEHLER: Keine Suchergebnisse vorhanden"}
    elif lang == "Spanish":
        config = {"txt_mastertitle": "Buscador",
                  "txt_selectdir": "Seleccionar Directorio",
                  "txt_settingsheader": "Ajustes",
                  "txt_entrysearch": "Buscar",
                  "txt_entryclear": "Borrar",
                  "txt_resultitems": "Buscar en resultados",
                  "txt_preview": "Vista previa",
                  "txt_page": "Pagina",
                  "ERR_noDirectorySelected": "ERROR: Ningún directorio seleccionado",
                  "ERR_resultListEmpty": "ERROR: No hay resultados de búsqueda"}
    else:
        config = {}
    edit_config(config)


def set_colors(template):
    if template == "wip":
        config = {"col_bg": "#3b3b3b",
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
                  "relief_btn": "flat"}
    elif template == "teatime":
        config = {"col_bg": "#386944",
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
                  "relief_btn": "raise"}
    elif template == "sharky":
        config = {"col_bg": "#0012ae",
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
                  "relief_btn": "raise"}
    elif template == "redengine":
        config = {"col_bg": "#272727",
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
                  "relief_btn": "flat"}
    elif template == "cb_friendly":
        config = {"col_bg": "#0072b2",
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
                  "relief_btn": "raise"}
    elif template == "monochrome":
        config = {"col_bg": "#282828",
                  "col_bg_lgt": "#282828",
                  "col_btn_idle": "black",
                  "col_btn_active": "#ffcc00",
                  "col_entryfield_idle": "black",
                  "col_entryfield_contrast": "#00ff00",
                  "col_acc_major": "#ffb000",
                  "col_acc_minor": "#ffb000",
                  "font_header_1": ("Arial", 15, "bold"),
                  "font_header_2": ("Arial", 10, "bold"),
                  "font_returntext": ("Arial", 10),
                  "relief_frames": "raise",
                  "relief_btn": "raise"}
    elif template == "cyberpunk":
        config = {"col_bg": "#272727",
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
                  "relief_btn": "flat"}
    elif template == "dokidoki":
        config = {"col_bg": "#fbd1fd",
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
                  "relief_btn": "flat"}
    else:
        config = {}
    edit_config(config)


def set_stemmer(stem):
    if stem == "porter":
        config = {"stemmer": "porter"}
    elif stem == "lancaster":
        config = {"stemmer": "lancaster"}
    else:
        config = {}
    edit_config(config)


def set_stop_word(stpwrd):
    if stpwrd:
        config = {"stop_word": True}
    elif not stpwrd:
        config = {"stop_word": False}
    else:
        config = {}
    edit_config(config)
