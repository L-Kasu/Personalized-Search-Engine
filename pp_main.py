# draft file for PSE assignment 01, preprocessing
# author: Niklas Munkes

import os
import pp_functions as ppf

####################
# Menu definitions #
####################

print("----------------------")
print("Simple IR System Setup")
print("----------------------\n")
print("place the files you wish to search here:")
print(ppf.dir_archive+"\n")


for dirname, _, filenames in os.walk(ppf.dir_archive):
    for filename in filenames:
        print("saving data as pp_container_"+filename+".txt...")
        ppf.saveTextAsTxt(filename)
        print("DONE")

filename = "CISI.ALL"
print("masterfully preprocessing " + filename)
ppf.masterProcessor(filename)
print("DONE")
