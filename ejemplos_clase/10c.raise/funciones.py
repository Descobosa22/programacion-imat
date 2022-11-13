def dividir(a, b):
    if b != 0:
        resultado = a / b    
    else:
        raise ZeroDivisionError(f"{b} no es un divisor válido")
    
    return resultado


def dividir2(a, b):
    try:
        resultado = a / b    
    except:
        raise ZeroDivisionError(f"{b} no es un divisor válido")
    
    return resultado