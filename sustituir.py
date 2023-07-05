import re


def sustituir_caracteres(archivo_origen: str, archivo_destino: str, longitud: int, columnas_irrelevantes: int,
                         posicion_por_modificar: int, primer_digito: bool, sustituto: str):
    def separar_lineas(string):
        lineas = []
        while len(string) > longitud:
            lineas.append([string[:longitud]])
            string = string[longitud:]
        return lineas

    with open(archivo_origen) as file:
        una_linea = file.readline()

        lineas_sep = separar_lineas(str(una_linea))
        lineas_post = []

        for linea in lineas_sep:
            lista_de_linea = linea[0].split()
            #
            contador = 0
            for elemento in range(columnas_irrelevantes, len(lista_de_linea) + 1):
                contador += 1
                if contador == 4:
                    contador = 0
                if contador == posicion_por_modificar:
                    if primer_digito:
                        lista_de_linea[elemento] = re.sub(r'^[\d\w]', sustituto, lista_de_linea[elemento])
                    else:
                        lista_de_linea[elemento] = re.sub(r'[\d\w]$', sustituto, lista_de_linea[elemento])
            lineas_post.append(' '.join(lista_de_linea))
            lineas_post.append(' ')

    with open(archivo_destino, mode="w") as post_file:
        post_file.writelines(lineas_post)


sustituir_caracteres(archivo_origen="Modificame_esta.txt",
                     archivo_destino="Esta_modificada.txt",
                     longitud=120,
                     columnas_irrelevantes=12,
                     posicion_por_modificar=3,
                     primer_digito=True,
                     sustituto="8"
                     )
