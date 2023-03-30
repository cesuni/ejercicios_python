class Person:
    # declaraciones o statements
    # pass esta sentencia no hace nada pero se utiliza cuando es necesaria en la sintaxis

    # -> Atributos o propiedades
    # __init__ es el inicializador de los atributos de la instancia, es un metodo especial
    def __init__(self, n, s):  # self es un atributo para diferenciar los atributos de las variables
        self.name = n
        self.school = s

    # metodo || funcion
    def print_name(self):
        print(self.name)

    def print_school(self):
        print(self.school)

# Podemos identificar de qué clase es jorge, y qué espacio ocupa en la memoria
# print(jorge)


jorge = Person('Jorge', 'Unipoli')

jorge.print_name()
jorge.print_school()

print(jorge.name, jorge.school)
