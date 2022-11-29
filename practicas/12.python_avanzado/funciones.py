import objetos as obj

def inicializar_datos() -> list:
    ordenadores = []
    ordenadores.append("DEL  ,i5,8,256GB")
    ordenadores.append("H, Intel i7,8,HD: 128")
    ordenadores.append("Lenvo  ,Intel i5,8,  200")
    ordenadores.append("DLL,  Inteli5,8,ssd256")
    ordenadores.append("Lnovo, i7,  8,512gb")
    ordenadores.append("HC, Intel+ i7,16, HD1: 512Gb1")
    ordenadores.append("DLL,  Inteli5,8,ssd6")
    return ordenadores

def limpiar_datos(ordenador:str) -> obj.Ordenador:
    try:
        ordenador = ordenador.replace(" ", "")
        valores = ordenador.split(",")
        marca = normalizar_marcas(valores[0])
        cpu = normalizar_cpu(valores[1])
        ram = int(valores[2])
        hd = int(normalizar_hd(valores[3]))

        ordenador = obj.Ordenador(marca, cpu, ram, hd)
        return ordenador
    except Exception as error:
        raise error


def normalizar_marcas(marca_entrada:str) -> str:
    """
    Returns:
            marca_normalizada (str): "DELL", "HP", "Lenovo"
    """
    marcas_estandarizadas = ["DELL", "HP", "Lenovo"]
    marca_normalizada = ""

    if marca_entrada not in marcas_estandarizadas:
        coincidencias_lista = [] 
        for i in range(len(marcas_estandarizadas)):
            marca_estandarizada = marcas_estandarizadas[i]
            coincidencias = 0
            for letra in marca_entrada:
                coincidencias += marca_estandarizada.count(letra)
            coincidencias_lista.append(coincidencias)

        posicion = coincidencias_lista.index(max(coincidencias_lista))
    
        marca_normalizada = marcas_estandarizadas[posicion]
    else:
        marca_normalizada = marca_entrada

    return marca_normalizada

def normalizar_cpu(cpu_entrada:str) -> str:
    """
    Returns:
        cpu_normalizada  (str): i3, i5, i7
    """
    cpu_normalizada = ""
    for i in range(len(cpu_entrada)-1):
        if cpu_entrada[i] == "i" and cpu_entrada[i+1].isdecimal():
            cpu_normalizada = cpu_entrada[i:i+2]
    
    if len(cpu_normalizada) != 2:
        raise ValueError

    return cpu_normalizada

def normalizar_hd(hd_entrada:str) -> str:
    """
    Returns:
        hd_str  (int): 64, 128, 515...
    """
    hd_str = ""
    i = 0
    while i in range(len(hd_entrada)):
        if hd_entrada[i].isdecimal():
            hd_str += hd_entrada[i]
        else:
            if len(hd_str) < 3:
                hd_str = ""
            else:
                i = len(hd_entrada)
        i += 1
    
    if len(hd_str) < 2:
        raise ValueError

    return hd_str