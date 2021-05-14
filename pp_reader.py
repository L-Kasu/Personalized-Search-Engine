
def pp_output_reader(filelocation):
    with open(filelocation, 'r') as container:
        paras_list = []
        counter = 1
        for line in container.readlines():
            if line.startswith(".I")\
                and counter == 1:
                reduced_line = line[3:]
                line_reduction = line[:3]
                para_dict = {line_reduction:reduced_line}
            elif counter == 6:
                paras_list.append(para_dict)
                counter = 1
                reduced_line = line[3:]
                line_reduction = line[:3]
                para_dict = {line_reduction: reduced_line}
            else:
                reduced_line = line[3:]
                line_reduction = line[:3]
                para_dict.update({line_reduction: reduced_line})
                counter += 1
    container.close()
    return paras_list

print(pp_output_reader("./PP_output/pp_output_tnwsl_CISI.ALL.txt"))