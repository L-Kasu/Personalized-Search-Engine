import numpy as np
import io
import pickle


# for loading the original files
def load_glove_model(File):
    print("Loading Glove Model")
    f = open(File,'r',encoding="utf-8")
    gloveModel = {}
    for line in f:
        splitLines = line.split()
        word = splitLines[0]
        wordEmbedding = np.array([float(value) for value in splitLines[1:]])
        gloveModel[word] = wordEmbedding
    print(len(gloveModel)," words loaded!")
    return gloveModel

# for loading the original files
def load_fasttext_model(fname):
    print("Loading fastText Model")
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    data = {}
    
    lenght = n
    count = 0
    
    for line in fin:
        if count % round(lenght/100) == 0:
            print(round(count/lenght * 100), "%")
        
        tokens = line.rstrip().split(' ')
        data[tokens[0]] = list(map(float, tokens[1:]))
        
        count += 1
    print(len(data)," words loaded!")
    return data


# copies and saves as pickle file (name is the same, with p as file type)
# e.g.: bla.txt -> bla.p
def save_emedding_as_pickle(embedding_loader, fname):
    embedding = embedding_loader(fname)
    
    split_path = embedding_path.split(".")
    pickle_split_path = split_path[:-1]
    pickle_split_path.append("p")
    
    pickle_embedding_path = ".".join(pickle_split_path)
    
    pickle.dump(embedding, open(pickle_embedding_path, "wb"))