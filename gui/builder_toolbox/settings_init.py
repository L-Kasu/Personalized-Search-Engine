from gui.builder_toolbox.settings_util import get_configdict, write_config
from gui.builder_toolbox.settings_defaultpaths import *


def init_config(path=default_path,
                masterfile=masterconfigfile,
                langfile=languageconfigfile,
                colorsfile=colorsconfigfile,
                fontfile=fontconfigfile):
    init_langfile(langfile, path)
    init_colorsfile(colorsfile, path)
    init_fontfile(fontfile, path)
    config = {"master_height": 500,
              "master_width": 800,
              "prev_window_size": 100,
              "preview_size": 500,
              "tooltip_window_size": 50,
              "global_padding": 5,
              **get_configdict(path, languageconfigfile)["english"],
              **get_configdict(path, colorsconfigfile)["wip"],
              **get_configdict(path, fontconfigfile)["Arial"],
              "stemmer": "porter",
              "snowballstemmer_language": "english",
              "stop_word": True,
              "stopword_language": "english",
              "clustering": False,
              "search_mode": "tfidf"}
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
                            "col_acc_bgcontrast": "#b3b3b3",
                            "col_acc_btncontrast": "#b3b3b3",
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
                                "col_acc_major": "#232323",
                                "col_acc_minor": "#232323",
                                "col_acc_bgcontrast": "#232323",
                                "col_acc_btncontrast": "#232323",
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
                               "col_acc_bgcontrast": "#00b1ff",
                               "col_acc_btncontrast": "#272727",
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
                                  "col_acc_bgcontrast": "#f7ff00",
                                  "col_acc_btncontrast": "#f7ff00",
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
                                    "col_acc_bgcontrast": "#f0e442",
                                    "col_acc_btncontrast": "#f0e442",
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
                                   "col_acc_bgcontrast": "#ffb000",
                                   "col_acc_btncontrast": "#ffb000",
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
                                  "col_acc_bgcontrast": "#f7ff00",
                                  "col_acc_btncontrast": "#272727",
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
                                 "col_acc_major": "#ff004b",
                                 "col_acc_minor": "#ff004b",
                                 "col_acc_bgcontrast": "#ff004b",
                                 "col_acc_btncontrast": "#ffdff3",
                                 "font_header_1": ("Comic Sans MS", 18, "bold"),
                                 "font_header_2": ("Comic Sans MS", 10, "bold"),
                                 "font_returntext": ("Comic Sans MS", 10),
                                 "relief_frames": "flat",
                                 "relief_btn": "flat"},
                    }
    write_config(colorsconfig, path, colorsfile)


def init_langfile(langfile=languageconfigfile, path=default_path):
    langconfig = {"english": {"ID_lang": "english",
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
                              "txt_language": "Language",
                              "txt_colortheme": "Theme",
                              "txt_font": "Font",
                              "txt_selectStemmer": "Select Stemmer",
                              "txt_toggleStopword": "Stop Word Removal",
                              "txt_toggleClustering": "Clustering",
                              "txt_selectsearchmode": "Search Mode",
                              "txt_selectsnowballlang": "Language (Snowball Stemmer)",
                              "txt_selectstopwordlang": "Language (Stop Words)",
                              "txt_on": "on",
                              "txt_off": "off",
                              "txt_confirm": "Confirm",
                              "txt_cancel": "Cancel",
                              "txt_tooltip_porter": "This is the Porter stemming algorithm. It follows the algorithm presented in Porter, M. 'An algorithm for suffix stripping.' Program 14.3 (1980): 130-137.",
                              "txt_tooltip_lancaster": "A word stemmer based on the Lancaster (Paice/Husk) stemming algorithm. It follows the algorithm presented in Paice, Chris D. “Another Stemmer.” ACM SIGIR Forum 24.3 (1990): 56-61.",
                              "txt_tooltip_snowball": "This is an Implementation of the 'Snowball' stemmers created by Martin Porter. Select this option if you want to stem documents in Arabic, Danish, Dutch, English, Finnish, French, German, Hungarian, Italian, Norwegian, Portuguese, Romanian, Russian, Spanish or Swedish. The english algorithm was presented in Porter, M. 'An algorithm for suffix stripping.' Program 14.3 (1980): 130-137.",
                              "txt_tooltip_stemmer": "A Stemmer is an algorithm, that reduces given inflected/derived words to their word stem (the part of the word responsible for its lexical meaning). For example the stem of the words 'cats', 'catlike' and 'catty' would be 'cat'",
                              "txt_tooltip_stopwords": "Stop words are words which are filtered out before processing a dataset (because they do not contain information relevant for the search) to speed up the processing step. Such words could be 'the', 'is', 'at', 'which' or 'on'.",
                              "txt_tooltip_clustering": "Clustering is the process of grouping objects of a given dataset by a certain trait (some sort of similarity, in this case words are grouped by the similarity of the context they appear in). Here this is done to speed up the search",
                              "txt_tooltip_tfidf": "Term Frequency–Inverse Document Frequency is a numerical statistic that is intended to reflect how important a word is to single document in a collection of documents.  Here it is used as a weighting factor for the search. The tf–idf value increases proportionally to the number of times a word appears in the document and is offset by the number of documents in the collection that contain the word, which helps to adjust for the fact that some words appear more frequently in general.",
                              "txt_tooltip_GloVe": "GloVe is an unsupervised learning algorithm for obtaining vector representations for words. Training is performed on aggregated global word-word co-occurrence statistics from a corpus. It is used for word embedding (word embedding is a term used for the representation of words for text analysis, typically in the form of a real-valued vector that encodes the meaning of the word such that the words that are closer in the vector space are expected to be similar in meaning (word embedding is much faster than using tf-idf)). GloVe was presented in Jeffrey Pennington, Richard Socher, and Christopher D. Manning. 2014. GloVe: Global Vectors for Word Representation.",
                              "txt_tooltip_fasttext": "FastText is a free, open-source algorithm for obtaining vector representations for words, which is trained on English webcrawl and Wikipedia. It is used for word embedding (word embedding is a term used for the representation of words for text analysis, typically in the form of a real-valued vector that encodes the meaning of the word such that the words that are closer in the vector space are expected to be similar in meaning (word embedding is much faster than using tf-idf))",
                              "txt_tooltip_logistic regression": "TODO logreg tooltip",
                              "ERR_noDirectorySelected": "ERROR: No directory selected",
                              "ERR_resultListEmpty": "ERROR: There are no search results"},
                  "german": {"ID_lang": "german",
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
                             "txt_language": "Sprache",
                             "txt_colortheme": "Design",
                             "txt_font": "Schriftart",
                             "txt_selectStemmer": "Stemmerauswahl",
                             "txt_toggleStopword": "Stoppwortentfernung",
                             "txt_toggleClustering": "Clustering",
                             "txt_selectsearchmode": "Suchverfahren",
                             "txt_selectsnowballlang": "Sprache (Snowball Stemmer)",
                             "txt_selectstopwordlang": "Sprache (Stopwörter)",
                             "txt_on": "an",
                             "txt_off": "aus",
                             "txt_confirm": "Bestätigen",
                             "txt_cancel": "Verwerfen",
                             "txt_tooltip_porter": "Dies ist der Porter Stemming Algorithmus. Er basiert auf dem Algorithmus vorgestellt in Porter, M. 'An algorithm for suffix stripping.' Program 14.3 (1980): 130-137.",
                             "txt_tooltip_lancaster": "Dies ist der Lancaster (Paice/Husk) Stemming Algorithmus. Er basiert auf dem Algorithmus vorgestellt in Paice, Chris D. “Another Stemmer.” ACM SIGIR Forum 24.3 (1990): 56-61.",
                             "txt_tooltip_snowball": "Dies ist eine Implementierung der 'Snowball' Stemmer nach Martin Porter. Wählen Sie diese Option wenn Sie Dokumente in Arabisch, Dänisch, Deutsch, Englisch, Finnisch, Französisch, Italienisch, Niederländisch, Norwegisch, Portugiesisch, Rumänisch, Russisch, Schwedisch, Spanisch oder Ungarisch verarbeiten wollen. Der englische Stemmer basiert auf dem Algorithmus vorgestellt in Porter, M. 'An algorithm for suffix stripping.' Program 14.3 (1980): 130-137.",
                             "txt_tooltip_stemmer": "Ein Stemmer ist ein Algorithmus, der gegebene Wörter auf ihren Wortstamm reduziert (den Teil des Wortes, der für seine lexikalische Bedeutung verantwortlich ist). Der Wortstamm der Wörter 'cats', 'catlike' und 'catty' wäre zum Beispiel 'cat'.",
                              "txt_tooltip_stopwords": "Stoppwörter sind Wörter, die vor der Verarbeitung eines Datensatzes herausgefiltert werden (weil sie keine für die Suche relevanten Informationen enthalten), um den Verarbeitungsschritt zu beschleunigen. Solche Wörter könnten 'der', 'ist', 'bei', 'welcher' oder 'am' sein.",
                              "txt_tooltip_clustering": "Beim Clustering werden Objekte eines bestimmten Datensatzes nach einer bestimmten Eigenschaft gruppiert (nach einer Art von Ähnlichkeit, in diesem Fall werden Wörter nach der Ähnlichkeit des Kontexts gruppiert, in dem sie vorkommen). Clustering kann angewendet werden, um die Suche zu beschleunigen.",
                              "txt_tooltip_tfidf": "Term Frequency-Inverse Document Frequency ist ein numerischer Wert, der wiedergeben soll, wie wichtig ein Wort für ein einzelnes Dokument in einer Sammlung von Dokumenten ist. Hier wird er als Gewichtungsfaktor für die Suche verwendet. Der tf-idf-Wert steigt proportional zur Häufigkeit, mit der ein Wort im Dokument vorkommt, und wird durch die Anzahl der Dokumente in der Sammlung, die das Wort enthalten, ausgeglichen, was dazu beiträgt, die Tatsache auszugleichen, dass einige Wörter generell häufiger vorkommen.",
                              "txt_tooltip_GloVe": "GloVe ist ein unsupervised learning Algorithmus zur Erstellung von Vektordarstellungen für Wörter. Das Training wird auf der Grundlage aggregierter globaler Statistiken aus einem Korpus durchgeführt. Er wird für word embedding verwendet (word embedding ist ein Begriff, der für die Darstellung von Wörtern für die Textanalyse verwendet wird, typischerweise in Form eines Vektors, der die Bedeutung des Wortes kodiert, sodass die Wörter, die im Vektorraum näher beieinander liegen, in ihrer Bedeutung ähnlich sind (word embedding ist viel schneller als die Verwendung von tf-idf)). GloVe wurde vorgestellt in Jeffrey Pennington, Richard Socher, and Christopher D. Manning. 2014. GloVe: Global Vectors for Word Representation.",
                              "txt_tooltip_fasttext": "FastText ist ein freier, open-source Algorithmus zur Ermittlung von Vektordarstellungen für Wörter, der auf Webcrawl und Wikipedia trainiert ist. Er wird für word embedding verwendet (word embedding ist ein Begriff, der für die Darstellung von Wörtern für die Textanalyse verwendet wird, typischerweise in Form eines reellwertigen Vektors, der die Bedeutung des Wortes kodiert, so dass die Wörter, die im Vektorraum näher beieinander liegen, in ihrer Bedeutung voraussichtlich ähnlich sind (word embedding ist viel schneller als die Verwendung von tf-idf)).",
                             "txt_tooltip_logistic regression": "TODO logreg tooltip",
                             "ERR_noDirectorySelected": "FEHLER: Kein Verzeichnis ausgewählt",
                             "ERR_resultListEmpty": "FEHLER: Keine Suchergebnisse vorhanden"},
                  "spanish": {"ID_lang": "spanish",
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
                              "txt_font": "Font (to be translated)",
                              "txt_selectStemmer": "Select Stemmer(to be translated)",
                              "txt_toggleStopword": "Stop Word Removal(to be translated)",
                              "txt_toggleClustering": "TODO Clustering",
                              "txt_selectsearchmode": "TODO select search label",
                              "txt_selectsnowballlang": "TODO txt_selectsnowballlang",
                              "txt_selectstopwordlang": "TODO Language (Stop Words)",
                              "txt_on": "on(to be translated)",
                              "txt_off": "off(to be translated)",
                              "txt_confirm": "TODO: Confirm",
                              "txt_cancel": "TODO: Cancel",
                              "txt_tooltip_porter": "TODO: portertooltip",
                              "txt_tooltip_lancaster": "TODO: lancastertooltip",
                              "txt_tooltip_snowball": "TODO: snowballtooltip",
                              "txt_tooltip_stemmer": "TODO",
                              "txt_tooltip_stopwords": "TODO",
                              "txt_tooltip_clustering": "TODO",
                              "txt_tooltip_tfidf": "TODO",
                              "txt_tooltip_GloVe": "TODO",
                              "txt_tooltip_fasttext": "TODO",
                              "txt_tooltip_logistic regression": "TODO logreg tooltip",
                              "ERR_noDirectorySelected": "ERROR: Ningún directorio seleccionado",
                              "ERR_resultListEmpty": "ERROR: No hay resultados de búsqueda"},
                  "arabic": {"ID_lang": "arabic",
                             "txt_mastertitle": "مُحَرّكُ البَحث",
                             "txt_selectdir": "اِخْتَيار مُجَلَّد",
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
                             "txt_font": "الخَط",
                             "txt_selectStemmer": "اخْتِيَار الStemmer",
                             "txt_toggleStopword": "إِزالَة الStop Words",
                             "txt_toggleClustering": "التَّجميع (Clustering)",
                             "txt_selectsearchmode": "اختِيار صَنف البَحث",
                             "txt_selectsnowballlang": "لغة snowball stemmer",
                             "txt_selectstopwordlang": "كلمات التوقّف (Stop Words)",
                             "txt_on": "نَعَم",
                             "txt_off": "لا",
                             "txt_confirm": "TODO: Confirm",
                             "txt_cancel": "TODO: Cancel",
                             "txt_tooltip_porter": "مجذّع الكلمات Porter, يتبّع الخوارزميّة المقدّمة في Porter, M 'An algorithm for suffix stripping.' Program 14.3 (1980): 130-137",
                             "txt_tooltip_lancaster": "مجذّع كلمات مرتكز على خوارزميّة Lancaster (Paice/Husk). يتبّع الخوارزميّة المقدّمة في Paice, Chris D. “Another Stemmer.” ACM SIGIR Forum 24.3 (1990): 56-61.",
                             "txt_tooltip_snowball": "تطبيق لمجذّع الكلمات 'Snowball' المُنشأ من قِبَل مارتين بورتر. هذا الخيار مناسب للتجذيع باللّغات: العربيّة, الدنماركيّة, الهولنديّة, الإنجليزيّة, الفنلنديّة, الفرنسيّة, الألمانيّة, الهنغاريّة, الإيطاليّة, النرويجيّة, البرتغاليّة, الرومانيّة, الروسيّة, الإسبانيّة, السويديّة. الخوارزميّة الإنكليزيّة قُدِّمَت في Porter, M. 'An algorithm for suffix stripping.' Program 14.3 (1980): 130-137.",
                             "txt_tooltip_stemmer": "المُجّذّع هو خوارزميّة تقوم بتخفيف الكلمات المشتقّة إلى جذرها أو جذعها (جزئيّة الكلمة المسؤلة عن المعنى اللغوي للكلمة), على سبيل المثال جذع الكلمات 'كاتب' 'كتاب' 'مكتوب' هو 'كتب'.",
                             "txt_tooltip_stopwords": "مستبعدات الفهرسة هنّ كلمات تتمّ تصفيتهم قبل معالجة مجموعة البيانات (لعدم احتوائهم على معلومات ذات صلة بالبحث) لتسريع المعالجة.بعض الأمثلة الممكنة لمستبعدات الفهرسة: 'يا' 'هي' 'هو' 'و' 'أو' 'أنّ' 'إنّ'",
                             "txt_tooltip_clustering": "التصنيف (بالإنجليزيّة Clustering) هو عمليّة تجميع محتويّات مجموعة البيانات المعطاة بواسطة سمة معيّنة (نوع من التشابه, في هذه الحالة يتم تجميع الكلمات حسب تشابه السّياقات التي تظهر فيها), يتمّ هذا لتسريع عمليّة البحث.",
                             "txt_tooltip_tfidf": "تردد المصطلح-معكوس تردد الوثيقة(TF-IDF) هو عبارة عن إحصاء رقمي يهدف إلى إظهار مدى أهمية كلمة ما لمستند واحد في مجموعة من المستندات. هنا يتم استخدامه كعامل ترجيح للبحث. تزداد قيمة الTF-IDF بشكل متناسب مع عدد المرّات التي تظهر فيها الكلمة في المستند ويتم موازنتها بعدد المستندات المحتوية على الكلمة في المجموعة.",
                             "txt_tooltip_GloVe": "هي خوارزميّة تعلّم غير مراقب أو تعلم استنتاجي (بالإنجليزية: Unsupervised learning) للحصول على تمثيلات شعاعيّة للكلمات. يجري التدريب على التواجد المُشترك لثنائي من الكلمات. يتم استخدامها لتضمين الكلمات (تضمين الكلمات هو تمثيل المفردات والمركبات بصورة أشعة رياضية وأعداد حقيقية وهي من طرائق نمذجة اللغات الطبيعية(يعتبر تضمين الكلمات أسرع بكثير من TF-IDF)) تم تقديم GloVe في Jeffrey Pennington, Richard Socher, and Christopher D. Manning. 2014. GloVe: Global Vectors for Word Representation.",
                             "txt_tooltip_fasttext": "هي خوارزميّة حرّة ومفتوحة المصدر لتحصيل تمثيلات شعاعيّة للكلمات, يتمّ تدريبها على زاحف شبكة إنجليزي (بالإنجليزيّة Web Crawler). يتم استخدامها لتضمين الكلمات (تضمين الكلمات هو تمثيل المفردات والمركبات بصورة أشعة رياضية وأعداد حقيقية وهي من طرائق نمذجة اللغات الطبيعية(يعتبر تضمين الكلمات أسرع بكثير من TF-IDF))",
                             "txt_tooltip_logistic regression": "الانحدار اللوجستي (بالإنجليزية Logistic regression) هو نموذج إحصائي ينتمي لنماذج الانحدار الخطي يمكن من نمذجة متغير ثنائي الحد بدلالة مجموعة من المتغيرات العشوائية المتوقعة، رقمية كانت أو فئوية. يستخدم الانحدار اللوجستي للتنبؤ باحتمالية وقوع حدث ما بمعرفة إضافية لقيم متغيرات يمكن أن تكون مفسرة أو مرتبطة بهذا الحدث. يستخدم الانحدارُ اللوجستي عدة متغيرات مُتوقَّعة والتي يمكن أن تكون رقمية أو فئوية.",
                             "ERR_noDirectorySelected": "خَطَأ: لَمْ يَتُمَّ اِخْتِيَارُ أَيّ مُجَلَّد",
                             "ERR_resultListEmpty": "خَطَأ: لَيْسَ هُنَالِكَ نَتَائِجٌ لِلْبَحْث"},
                  }
    write_config(langconfig, path, langfile)


def init_fontfile(fontfile=fontconfigfile, path=default_path):
    fontconfig = {"Arial":
                      {"ID_font": "Arial",
                       "font_header_1": ["Arial", 15, "bold"],
                       "font_header_2": ["Arial", 10, "bold"],
                       "font_returntext": ["Arial", 10]},
                  "Old Goudy/English Text MT":
                      {"ID_font": "Old Goudy/English Text MT",
                       "font_header_1": ["Old English Text MT", 20, "bold"],
                       "font_header_2": ["Goudy Old Style", 12, "bold"],
                       "font_returntext": ["Goudy Old Style", 12]},
                  "Biome":
                      {"ID_font": "Biome",
                       "font_header_1": ["Biome", 16, "bold"],
                       "font_header_2": ["Biome", 10, "bold"],
                       "font_returntext": ["Biome", 10]},
                  "Terminal":
                      {"ID_font": "Terminal",
                       "font_header_1": ["Terminal", 15, "bold"],
                       "font_header_2": ["Terminal", 10, "bold"],
                       "font_returntext": ["Terminal", 10]},
                  "Comic Sans MS":
                      {"ID_font": "Comic Sans MS",
                       "font_header_1": ["Comic Sans MS", 18, "bold"],
                       "font_header_2": ["Comic Sans MS", 10, "bold"],
                       "font_returntext": ["Comic Sans MS", 10]},
                  "SimSun":
                      {"ID_font": "SimSun",
                       "font_header_1": ["SimSun", 15, "bold"],
                       "font_header_2": ["SimSun", 10, "bold"],
                       "font_returntext": ["SimSun", 10]},
                  "Agency FB":
                      {"ID_font": "Agency FB",
                       "font_header_1": ["Agency FB", 15, "bold"],
                       "font_header_2": ["Agency FB", 10, "bold"],
                       "font_returntext": ["Agency FB", 10]},
                  "Andalus":
                      {"ID_font": "Andalus",
                       "font_header_1": ["Andalus", 15, "bold"],
                       "font_header_2": ["Andalus", 10, "bold"],
                       "font_returntext": ["Andalus", 10]},
                  "Bahnschrift":
                      {"ID_font": "Bahnschrift",
                       "font_header_1": ["Bahnschrift", 15, "bold"],
                       "font_header_2": ["Bahnschrift", 10, "bold"],
                       "font_returntext": ["Bahnschrift", 10]},
                  "Book Antiqua":
                      {"ID_font": "Book Antiqua",
                       "font_header_1": ["Book Antiqua", 15, "bold"],
                       "font_header_2": ["Book Antiqua", 10, "bold"],
                       "font_returntext": ["Book Antiqua", 10]},
                  "Copperplate Gothic Bold":
                      {"ID_font": "Copperplate Gothic Bold",
                       "font_header_1": ["Copperplate Gothic Bold", 15, "bold"],
                       "font_header_2": ["Copperplate Gothic Bold", 10, "bold"],
                       "font_returntext": ["Copperplate Gothic Bold", 10]},
                  "Ink Free":
                      {"ID_font": "Ink Free",
                       "font_header_1": ["Ink Free", 15, "bold"],
                       "font_header_2": ["Ink Free", 10, "bold"],
                       "font_returntext": ["Ink Free", 10]},
                  "Monotype Corsiva":
                      {"ID_font": "Monotype Corsiva",
                       "font_header_1": ["Monotype Corsiva", 15, "bold"],
                       "font_header_2": ["Monotype Corsiva", 10, "bold"],
                       "font_returntext": ["Monotype Corsiva", 10]},
                  "OCR A Extended":
                      {"ID_font": "OCR A Extended",
                       "font_header_1": ["OCR A Extended", 15, "bold"],
                       "font_header_2": ["OCR A Extended", 10, "bold"],
                       "font_returntext": ["OCR A Extended", 10]},
                  "PERPETUA TITLING MT":
                      {"ID_font": "PERPETUA TITLING MT",
                       "font_header_1": ["PERPETUA TITLING MT", 15, "bold"],
                       "font_header_2": ["PERPETUA TITLING MT", 10, "bold"],
                       "font_returntext": ["PERPETUA TITLING MT", 10]},
                  "Segoe Script":
                      {"ID_font": "Segoe Script",
                       "font_header_1": ["Segoe Script", 15, "bold"],
                       "font_header_2": ["Segoe Script", 10, "bold"],
                       "font_returntext": ["Segoe Script", 10]},
                  "Simplified Arabic":
                      {"ID_font": "Simplified Arabic",
                       "font_header_1": ["Simplified Arabic", 16, "bold"],
                       "font_header_2": ["Simplified Arabic", 10, "bold"],
                       "font_returntext": ["Simplified Arabic", 10]},
                  "Small Fonts":
                      {"ID_font": "Small Fonts",
                       "font_header_1": ["Smal Fonts", 16, "bold"],
                       "font_header_2": ["Smal Fonts", 10, "bold"],
                       "font_returntext": ["Smal Fonts", 10]},
                  "Source Code Pro Semibold":
                      {"ID_font": "Source Code Pro Semibold",
                       "font_header_1": ["Source Code Pro Semibold", 16, "bold"],
                       "font_header_2": ["Source Code Pro Semibold", 10, "bold"],
                       "font_returntext": ["Source Code Pro Semibold", 10]},
                  "System":
                      {"ID_font": "System",
                       "font_header_1": ["System", 16, "bold"],
                       "font_header_2": ["System", 10, "bold"],
                       "font_returntext": ["System", 10]},
                  "Tw Cen MT":
                      {"ID_font": "Tw Cen MT",
                       "font_header_1": ["Tw Cen MT", 16, "bold"],
                       "font_header_2": ["Tw Cen MT", 10, "bold"],
                       "font_returntext": ["Tw Cen MT", 10]},
                  }
    write_config(fontconfig, path, fontfile)

