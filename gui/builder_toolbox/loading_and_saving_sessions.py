import pickle
import os.path

previous_session_path = "data/previous_session.pickle"


def load_session(path=previous_session_path):
    directory_path = ""
    search_class_instance = None
    if os.path.isfile(path):
        directory_path, search_class_instance = pickle.load(open(path, "rb"))
    return directory_path, search_class_instance


def save_session(directory_path, search_class_instance, path=previous_session_path):
    pickle.dump((directory_path, search_class_instance), open(path, "wb"))
    pass
