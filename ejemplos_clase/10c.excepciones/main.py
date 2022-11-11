import funciones as func
import errores as err

if __name__ == "__main__":
    try:
        edad = func.pedir_edad()
        print(edad)
    except err.EdadError as error:
        print(error)

"""nombre = func.pedir_nombre()
persona = crear_persona(nombre, edad)
fichero.guardar(persona)"""


