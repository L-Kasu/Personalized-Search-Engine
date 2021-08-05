import pickle
import os.path

previous_session_path = "config/session/previous_session.pickle"


def load_session(path=previous_session_path):
    directory_path = ""
    search_class_instance = None

    with open(path, "rb") as file:
        try:
            directory_path, search_class_instance = pickle.load(file)
        except EOFError:
            pass
    return directory_path, search_class_instance


def save_session(directory_path, search_class_instance, path=previous_session_path):
    with open(path, "wb") as file:
        pickle.dump((directory_path, search_class_instance), file)
    pass
