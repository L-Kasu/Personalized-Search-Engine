import pickle
import os

# usage: sve obejects as .pickle file
# input: name (just the name it will be saved it the data folder) as "./data/" + name + ".pickle"
# can only be called from the same folder as the data folder is in
def save_object(obj, name):
    filename = "./data/" + name + ".pickle"
    try:
        with open(filename, "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)


# usage: load object from .pickle file
# input: name (just the name .pickle will be added for ex load_object("tnwp_pp_CISI.ALL")
# can only be called from the same parent folder as data folder
def load_object(filename="data"):
    try:
        with open("./data/" + filename + ".pickle", "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)

def list_files_in_database() -> list:
    list_of_folders = os.listdir('./data/')
    result = filter(lambda file: file.endswith(".pickle"), list_of_folders)
    result = [filename.rstrip(".pickle") for filename in list(result)]
    return result


# list of saved files in this directory
list_of_files = list_files_in_database()