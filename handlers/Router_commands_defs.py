import os

date0 = os.getcwd()

with open('default_settings.txt', "r") as text_file:
            lines0 = text_file.readlines()

def commP(date, comm, lin):      
    res0 = comm
    with open(date, "r") as text_file:
        lines = text_file.readlines()
    if res0 == 'd':
        lines[lin] = lines0[lin]
    else:
        lines[lin] = res0 + '\n'
    with open(date, "w") as text_file:
        text_file.writelines(lines)



def commO(date, lin):
    with open(date, "r") as text_file:
        lines = text_file.readlines()
    if int(lines[lin]) == 0:
        lines[lin] = '1' + '\n'
    else:
        lines[lin] = '0' + '\n'
    with open(date, "w") as text_file:
        text_file.writelines(lines)
    return lines[lin]