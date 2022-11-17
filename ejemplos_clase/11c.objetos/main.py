from objetos import Persona

if __name__ == "__main__":
    persona1 = Persona("Luis", 22)
    nombre = "Ana"
    edad = 17
    persona2 = Persona(nombre, edad)

    print(persona1.edad)
    print(persona2.nombre)

    personas_tupla = [("Luis", 22), ("Ana", 19)] 
    personas = [persona1, persona2, Persona("Ramón", 33)]

    for persona in personas:
        print(f"{persona.nombre} es mayor edad: {persona.is_mayor_edad()}")

    for persona in personas_tupla:
        print(persona)

    for persona in personas:
        print(persona)  # La salida por defecto se consigue con __str__()

    for persona in personas:
        print(persona.str_bonito())  # Siempre podemos tener otras funcionalidades con nuevos métodos

