"""
Programa creado únicamente para generar el fichero de palabras de 5 letras
"""

if __name__ == "__main__":
    fichero = open("palabras.txt", "r", encoding = "utf-8")
    fichero_wordlet = open("palabras_wordlet.txt", "w", encoding = "utf-8")
    linea = fichero.readline()[:-1]
    while linea:
        if len(linea) == 5:
            acentos = False
            for letra in linea:
                if letra in ["á", "é", "í", "ó", "ú", "\\"]:
                    acentos = True
            if not acentos:
                fichero_wordlet.write(linea + "\n")
        linea = fichero.readline()[:-1]
    fichero.close()
    fichero_wordlet.close()