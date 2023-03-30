class Producto:
    def __init__(self, codigo, nombre, precio):
        # atributos privados
        # creacion de variable
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def precio(self):
        return self.__precio

    @codigo.setter
    def precio(self, valor):
        self.__precio = valor

    def __str__(self) -> str:
        return 'codigo: ' + str(self.__codigo) + ', nombre: ' + str(self.__nombre) + ', precio: ' + str(self.__precio)


p1 = Producto(1, 'xbox', 6999)
p2 = Producto(2, 'xbox360', 7000)
p3 = Producto(3, 'xboxone', 8799)
p4 = Producto(4, 'xboxoneX', 9999)

print(p1)
print(p2)
print(p3)
print(p4)
