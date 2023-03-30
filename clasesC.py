from unicodedata import name


class Rain:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.married = False

    def parar(self):
        self.married = True
        print(self.name, self.lastname, "turn off")


nombre = Rain('cesarin', 'smith')
nombre2 = Rain('Davi', 'Luca')

print(type(nombre))
print(type(nombre2))

print(nombre.name, nombre.lastname, nombre.married)

nombre.parar()

print(nombre.name, nombre.lastname, nombre.married)
