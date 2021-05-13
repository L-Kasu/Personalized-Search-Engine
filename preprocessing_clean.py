# clean file for PSE assignment 01, preprocessing
# author: Niklas Munkes

import os
import pp_functions_clean as ppf


for dirname, _, filenames in os.walk(ppf.dir_archive):
    for filename in filenames:
        print("saving data as pp_container_"+filename+".txt...")
        ppf.saveTextAsTxt(filename)
        print("DONE")

filename = "CISI.ALL"
print("creating TAW container of " + filename)
ppf.createTAWContainer(filename)
print("DONE")