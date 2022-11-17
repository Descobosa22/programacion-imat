class Persona:
    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Métodos
    def is_mayor_edad(self):
        """  
        if self.edad >= 18:
            return True
        else:
            return False
        """
        return self.edad >= 18

    def __str__(self):
        return f"{self.nombre} ==== {self.edad}" 

    def str_bonito(self):
        marco = "#" * 15
        return f"{marco}\n{self.nombre}: {self.edad} años\n{marco}"