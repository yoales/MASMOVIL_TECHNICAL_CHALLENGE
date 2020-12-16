class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentation(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")

class Trabajador(Persona):
    def __init__(self, nombre, edad, departamento, puesto):
        Persona.__init__(self, nombre, edad)

        self.departamento = departamento
        self.puesto = puesto

    def presentation(self):
        Persona.presentation(self)
        print(f"Mi departamento es {self.departamento} y mi puesto es {self.puesto}")

nombre = 'Alberto'
persona_1 = Persona(nombre, 20)
persona_1.presentation()

nombre = 'Alejandro'
trabajador_1 = Trabajador(nombre, 30, 'Data', 'Analyst')
trabajador_1.presentation()
