# clase

class boots:
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca
        self.arrancado = False


nike = boots('nike', 'mercurial')
adidas = boots('adidas', 'speedflow')

print(nike.marca, nike.modelo)
print(adidas.marca, adidas.modelo)
