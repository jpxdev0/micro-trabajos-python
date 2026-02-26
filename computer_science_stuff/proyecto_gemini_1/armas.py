# Archivo: armas.py

class Arma:
    def __init__(self,nombre,dano):
        self.nombre = nombre
        self.dano = dano
    def mostrar_detalles(self):
        print(f"Arma|{self.nombre},| danio|{self.dano}")