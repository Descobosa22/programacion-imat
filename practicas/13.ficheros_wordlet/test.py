import funciones as f

COLOR_VERDE = "\033[1;32m"
COLOR_ROJO = "\033[1;31m"
COLOR_DEFECTO = "\033[0m"

OK = COLOR_VERDE + "OK" + COLOR_DEFECTO
ERROR = COLOR_ROJO + "ERROR" + COLOR_DEFECTO

print("Ejecutando tests....")

tablero = [[" "]*5]*5 

try:
    print("- Función crear_tablero(): ", end = "") 
    tablero = f.crear_tablero()
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

try:
    print("- Función letra_exacta(tablero:list, fila:int, col:int, letra:str): ", end = "") 
    f.letra_exacta(tablero, 0, 0, "A")
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print("\t\t", error)

try:
    print("- Función letra_no_exacta(tablero:list, fila:int, col:int, letra:str): ", end = "") 
    f.letra_no_exacta(tablero, 1, 1, "B")
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print("\t\t", error)

try:
    print("- Función letra_no_esta(tablero:list, fila:int, col:int, letra:str): ", end = "") 
    f.letra_no_esta(tablero, 2, 2, "C")
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print("\t\t", error)

try:
    print("- Función mostrar_tablero(list): ") 
    f.mostrar_tablero(tablero)
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

try:
    print("- Función elegir_palabra(): ", end = "") 
    f.leer_palabras()
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print(error)
    
print("Fin de los tests")