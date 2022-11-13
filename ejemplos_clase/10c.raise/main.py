import funciones as func

a = 3
b = 0
try:
    resultado = func.dividir(a, b)
    print(f"{a} / {b} = {resultado}")
except ZeroDivisionError as error:
    print(error)

try:
    resultado = func.dividir2(a, b)
    print(f"{a} / {b} = {resultado}")
except ZeroDivisionError as error:
    print(error)