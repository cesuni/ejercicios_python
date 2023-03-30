# clase

class SportCar:
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca
        self.arrancado = False

    def arrancar(self):
        self.arrancado = True
        print(self.marca, self.modelo, "turn on")

    def parar(self):
        self.arrancado = False
        print(self.marca, self.modelo, "turn off")


laguna = SportCar('Turbo S', 'Porche')
tesla = SportCar('volt', 'tesla')


# print tipo de dato
print(type(laguna))
print(type(tesla))

print(laguna.marca, laguna.modelo)
print(tesla.marca, tesla.modelo)

laguna.arrancar()
tesla.arrancar()

print(laguna.arrancado)
print(tesla.arrancado)

laguna.parar()
tesla.parar()

print(laguna.arrancado)
print(tesla.arrancado)
