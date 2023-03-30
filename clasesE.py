class Suma:
    def __init__(self, n1, n2):
        self.numero1 = n1
        self.numero2 = n2

    def print_suma(self):
        print(self.numero1 + self.numero2)


class Resta:
    def __init__(self, n1, n2):
        self.numero1 = n1
        self.numero2 = n2

    def print_resta(self):
        print(self.numero1 - self.numero2)


# instancia
res_suma = Suma(5, 3)
res_resta = Resta(6, 3)

res_suma.print_suma()
res_resta.print_resta()
