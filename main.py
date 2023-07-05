file = open("Modifícame esta.txt", mode="r")
lines = file.readlines()

for i, line in enumerate(lines):
    line = line[5:]
    line = f"{hex(i)[2:].zfill(4)[2:]} {hex(i)[2:].zfill(4)[:2]}{line}"

modified_file = open("Esta modificada.txt", "w")
modified_file.writelines(lines)
