import funciones as f

COLOR_VERDE = "\033[1;32m"
COLOR_ROJO = "\033[1;31m"
COLOR_DEFECTO = "\033[0m"

OK = COLOR_VERDE + "OK" + COLOR_DEFECTO
ERROR = COLOR_ROJO + "ERROR" + COLOR_DEFECTO

print("Ejecutando tests....")

try:
    print("- Función inicializar_datos(): ", end = "") 
    f.inicializar_datos()
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

try:
    print("- Función limpiar_datos(ordenador:str): ", end = "") 
    print(f.limpiar_datos("HC, Intel+ i7,16, HD1: 512Gb1"), end = " - ")
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print("\t\t", error)

try:
    print("- Función normalizar_marcas(marca_entrada:str): ", end = "") 
    print(f.normalizar_marcas("levo"), end = " - ")
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

try:
    print("- Función normalizar_cpu(cpu_entrada:str): ", end = "") 
    print(f.normalizar_cpu("Intel PRO+ i5"), end = " - ")
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

try:
    print("- Función normalizar_hd(hd_entrada:str): ", end = "") 
    print(f.normalizar_hd("HD1: 512Gb1"), end = " - ")
    print(f.normalizar_hd("ssd6"), end = " - ")
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print("\t\t", error)


    
print("Fin de los tests")