file = open("Cambiar sensor.txt", mode="r")
lineas = file.readlines()

superlista = []
for linea in lineas:
    lista = list(linea)
    if lista[75] == "E":
        lista[75] = "F"
    elif lista[75] == "D":
        lista[75] = "F"
    elif lista[75] == "C":
        lista[75] = "F"
    elif lista[75] == "B":
        lista[75] = "E"
    elif lista[75] == "A":
        lista[75] = "D"
    elif lista[75] == "9":
        lista[75] = "C"
    elif lista[75] == "8":
        lista[75] = "B"
    elif lista[75] == "7":
        lista[75] = "A"
    elif lista[75] == "6":
        lista[75] = "9"
    elif lista[75] == "5":
        lista[75] = "8"
    elif lista[75] == "4":
        lista[75] = "7"
    elif lista[75] == "3":
        lista[75] = "6"
    elif lista[75] == "2":
        lista[75] = "5"
    elif lista[75] == "1":
        lista[75] = "4"
    elif lista[75] == "0":
        lista[75] = "3"
    if lista[99] == "1":
        lista[99] = "0"
    elif lista[99] == "2":
        lista[99] = "0"
    elif lista[99] == "3":
        lista[99] = "0"
    elif lista[99] == "4":
        lista[99] = "1"
    elif lista[99] == "5":
        lista[99] = "2"
    elif lista[99] == "6":
        lista[99] = "3"
    elif lista[99] == "7":
        lista[99] = "4"
    elif lista[99] == "8":
        lista[99] = "5"
    elif lista[99] == "9":
        lista[99] = "6"
    elif lista[99] == "A":
        lista[99] = "7"
    elif lista[99] == "B":
        lista[99] = "8"
    elif lista[99] == "C":
        lista[99] = "9"
    elif lista[99] == "D":
        lista[99] = "A"
    elif lista[99] == "E":
        lista[99] = "B"
    elif lista[99] == "F":
        lista[99] = "C"
    superlista.append(str("".join(lista)))

new_file = open("Nuevoarchivo.txt", "w")
new_file.writelines(superlista)
