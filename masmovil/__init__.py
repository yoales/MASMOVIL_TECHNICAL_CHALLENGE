class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentation(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")

class Trabajador(Persona):
    def __init__(self, nombre, edad, departamento = 'Data', puesto = 'Analyst'):
        Persona.__init__(self, nombre, edad)

        self.departamento = departamento
        self.puesto = puesto

    def presentation(self):
        Persona.presentation(self)
        print(f"Mi departamento es {self.departamento} y mi puesto es {self.puesto}")

# self.nombre hace referencia al atributo 'nombre' de la clase 'Persona', mientras que 'nombre' es una variable creada por nosotros
nombre = 'Alberto'
persona_1 = Persona(nombre, 20)
persona_1.presentation()

nombre = 'Alejandro'
trabajador_1 = Trabajador(nombre, 30)
trabajador_1.presentation()

my_var_list = ['Andrea', '42', 'Ventas', 'Manager']
trabajador_2 = Trabajador(*my_var_list)
trabajador_2.presentation()

my_var_dict = { 'nombre': 'Andrea', 'edad': '42', 'departamento': 'Ventas', 'puesto': 'Manager'}
trabajador_3 = Trabajador(**my_var_dict)
trabajador_3.presentation()
