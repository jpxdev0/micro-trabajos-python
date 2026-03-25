class Mueble:
    def __init__(self,year,cost):
        self.year = year
        self.cost = cost
    def __str__(self):
        return f"Soy un mueble del año {self.year} y costo {self.cost}"
    def imprimir_datos(self):
        print(f"soy un mueble del año {self.year} y costo {self.cost}")
