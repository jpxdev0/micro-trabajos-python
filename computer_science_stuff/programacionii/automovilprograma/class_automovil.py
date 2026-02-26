import random
class Automovil:
    marca = ['Toyota','Ford','Dodge','Chevrolet','mazda','Ferrari','Subaru']
    #modelo pendiente
    #anio = [2020,2021,2026]
    anio = range(2020,2027)
    def __init__(self,marca = 'honda', anio = '2021'):
        random.seed()
        self.marca = random.choice(Automovil.marca)
        self.anio = random.choice(Automovil.anio)
    def __str__(self):
        return f"Soy un {self.marca} del anio {self.anio}"