# preprocessing text file reader
# version: alpha1.24
# author: Lars Kasüschke


# format: list of dictionaries, accessed via the index of a text
# regarding indexes: see in the output files, decrement the index from the input files by 1,
# if you want to access the right part of the list.

# Each dictionary contains:
# 'I' : index
# 'T' : Title
# 'A' : Author
# 'W' : either the text for the input files or the set of words for the ouput files
# 'X' : ???

def file_reader(filename):

    text_list = []
    file = open(filename, "r")

    for line in file:

        if line.startswith('.I'):
            text_dictonary = {'I': int(line[2:].strip())}
            text_list.append(text_dictonary)

        else:
            line_without_prefix = line[3:].strip()
            content = line_without_prefix

            if line.startswith('.W {'):
                content = set()

                for element in line_without_prefix[1:-1].split(","):
                    content.add(element[2:-1])

            text_list[-1][line[1]] = content

    return text_list
    file.close()
