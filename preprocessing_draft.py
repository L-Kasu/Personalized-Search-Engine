# draft file for PSE assignment 01, preprocessing
# author: Niklas Munkes

import nltk
import numpy as np
import pandas as pd
import os
import pp_functions as ppf
# from mpl_toolkits.mplot3d import Axes3D
# from sklearn.preprocessing import StandardScaler
# import matplotlib.pyplot as plt # plotting

for dirname, _, filenames in os.walk('./CISI_archive'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

        with open(os.path.join(dirname, filename)) as f:
            line_count = 0
            id_set = set()

            for l in f.readlines():
                line_count += 1
                if filename == "CISI.REL":
                    id_set.add(l.lstrip(" ").split(" ")[0])
                elif l.startswith(".I "):
                    id_set.add(l.split(" ")[1].strip())

            print(f"{filename} : {len(id_set)} items, over {line_count} lines.")

            # print("trying to load a raw document...")
            # file = open('document.txt')
            # file_raw = file.read()

            # ppf.printLines(5)
            # ppf.printLines("all")
            ppf.extractLinesByType(".A")
            # ppf.extractLinesByType("italy")
