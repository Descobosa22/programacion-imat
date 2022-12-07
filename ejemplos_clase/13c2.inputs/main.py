import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        # Tres formas de leer la marca
        marca_sys = sys.argv[1]  # Por parámetros de consola por pantalla
        marca_input = input("Marca: ")  # Por teclado de forma interactiva en el programa
        with open("marca.txt", "r") as file:  # Por fichero
            marca_file = file.readline()
            
        print(marca_sys, marca_input, marca_file)

