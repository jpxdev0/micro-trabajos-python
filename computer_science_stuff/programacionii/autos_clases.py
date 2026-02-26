class Auto:
    def __init__(self,marca,modelo,anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"
    
def obtener_anio(auto):
    return auto.anio
auto1 = Auto("Toyota", "Hilux", 2017)

auto2 = Auto("Toyota", "Corolla", 2015)
auto3 = Auto("Ford", "Mustang", 2025)
auto4 = Auto("Dodge", "Challenger", 2015)

lista_autos = [auto1, auto2, auto3, auto4]

lista_ordenada = sorted(lista_autos, key=obtener_anio)

for auto in lista_ordenada:
    print(auto)