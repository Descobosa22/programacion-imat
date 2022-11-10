import errores as err

def pedir_edad():
    """"
    Args:
    Returns:
        int: 
    Raises:
        EdadError
    """
    edad_str = input("Edad: ")
    try:
        edad = int(edad_str)
    except ValueError as error:
        raise err.EdadError(f"Error en la edad {edad_str}")
    
    return edad
